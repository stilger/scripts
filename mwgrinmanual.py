#!/usr/bin/python3
  
# Copyright 2018 Blade M. Doyle
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#	 http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import os
import requests
import json
import subprocess
import argparse
import getpass
from datetime import datetime
	
def print_banner():
	print(" ")
	print("############# MWGrinPool Manual Payout Request Script Started #############")
	print("## Started: {} ".format(datetime.now()))
	print("## ")

def print_footer():
	print("## ")
	print("## Complete: {} ".format(datetime.now()))
	print("############# MWGrinPool Manual Payout Request Completed      #############")
	print(" ")

##
# Get configuration - either from commandline or by prompting the user
parser = argparse.ArgumentParser()
parser.add_argument("--pool_user", help="Username on MWGrinPool")
parser.add_argument("--pool_pass", help="Password on MWGrinPool")
parser.add_argument("--file_name", help="File Name")
parser.add_argument("--get_unsigned", help="Get MWGrinPool Unsigned Slate", action="store_true")
parser.add_argument("--send_signed", help="Send MWGrinPool Signed Slate", action="store_true")
args = parser.parse_args()

prompted = False
print_banner()
if args.get_unsigned is True and args.send_signed is True:
	print("   ... You can not specify --get_unsigned and --send_signed on the same command line")
	print("   ... Exiting")
	print_footer()
	sys.exit(0)
	
if args.pool_user is None:
	username = raw_input("   MWGrinPool Username: ")
	prompted = True
else:
	username = args.pool_user

if args.pool_pass is None:
	password = getpass.getpass("   MWGrinPool Password: ")
	prompted = True
else:
	password = args.pool_pass

if args.get_unsigned is True or args.send_signed is True:
	if args.file_name is None:
		filename = raw_input("   File Name: ")
		prompted = True
	else:
		filename = args.file_name
	if args.get_unsigned is True:
		if os.path.exists(filename):
			# An unsigned slate file exists
			# XXX TODO: check if the response exists and if not offer to try to process it?
			print("   ... "+filename+" already exists. To not lose data we will not overwrite a file that exists.")
			print("   ... Please choose a new name.")
			print("   ... Exiting")
			print_footer()
			sys.exit(0)

if prompted:
	print(" ")

## --------------------------------
# End of User Configuration section
## --------------------------------

mwURL = "https://api.mwgrinpool.com"
POOL_MINIMUM_PAYOUT = 0.25

dont_clean = False



def get_pool_user():
	##
	# Get my pool user_id
	get_user_id = mwURL + "/pool/users"
	r = requests.get(
			url = get_user_id,
			auth = (username, password),
	)
	if r.status_code != 200:
		print("   *** Failed")
		print(" ")
		print(" ")
		print("   *** Failed to get your account information from MWGrinPool: {}".format(r.text))
		print_footer()
		sys.exit(1)
	user_id = str(r.json()["id"])
	return user_id

def get_pool_balance():
	##
	# Get the users balance
	sys.stdout.write('   ... Getting miner balance: ')
	sys.stdout.flush()
	get_user_balance = mwURL + "/worker/utxo/"+user_id
	r = requests.get(
			url = get_user_balance,
			auth = (username, password),
	)
	if r.status_code != 200:
		print("Failed")
		print(" ")
		print(" ")
		print("   *** Failed to get your account balance: {}".format(r.text))
		print_footer()
		sys.exit(1)
	if r.json() is None:
		balance_nanogrin = 0
	else:
		balance_nanogrin = r.json()["amount"]
	balance = balance_nanogrin / 1000000000.0
	print("{} Grin".format(balance))


	##
	# Only continue if there are funds available
	if args.get_unsigned is True:
		if balance <= POOL_MINIMUM_PAYOUT:
			print(" ")
			print("   *** Not enough funds available to request a payment.")
			print(" ")
			print("	   Note: If you have recently attempted a payment request that did not complete, the pool will return your funds within 30 minutes.")
			print("	   Please try again later.")
			sys.exit(0)

def get_unsigned_file():
	##
	# Get the initial tx slate and write it to a file
	sys.stdout.write('   ... Getting payment slate: ')
	sys.stdout.flush()
	get_tx_slate_url = mwURL + "/pool/payment/get_tx_slate/"+user_id
	r = requests.post(
			url = get_tx_slate_url,
			auth = (username, password),
	)
	if r.status_code != 200:
		print("   *** Failed")
		print(" ")
		print(" ")
		print("   *** Failed to get a payment slate.")
		print_footer()
		sys.exit(1)
	f = open(filename, "w")
	f.write(r.text)
	f.flush()
	f.close()
	print("   ... Unsigned Slate file:"+filename+" downloaded")
	print("   ... Please sign this file with your wallet on your exchange")
	print("   ... Once complete run this script with --send_signed argument using the signed file")

def send_signed_file():
	# Submit the signed slate back to MWGrinPool to be finalized and posted to the network
	sys.stdout.write("   ... Submitting the signed slate back to GrinPool: ")
	sys.stdout.flush()
	submit_tx_slate_url = mwURL + "/pool/payment/submit_tx_slate/"+user_id
	r = requests.post(
			url = submit_tx_slate_url,
			data = open(filename, "r"),
			auth = (username, password),
	)
	if r.status_code != 200:
		print("   *** Failed")
		print(" ")
		print(" ")
		print("   *** Failed to submit signed slate - {}".format(r.text))
		print_footer()
		print(responsefile.read())
		sys.exit(1)
	print("Ok.")

get_pool_user()
user_id=get_pool_user()

# if args.get_balance is True or args.get_unsigned is True:
if args.send_signed is not True:
	get_pool_balance()

if args.get_unsigned is True:
	get_unsigned_file()

if args.send_signed is True:
	send_signed_file()

print_footer()