#!/bin/bash
# I will add more logic and make the script nicer but for now
# run this from your tmux directory
# create a backup directory first IE: mkdir backup
#
# create patch 
diff -u config.sh.git config.sh > changes.patch
# backup current defaults.sh
cp -p defaults.sh backup/defaults.sh.`date +"%Y.%m.%d-%H.%M.%S"`
# apply patch
patch defaults.sh < changes.patch
# backup old config.sh.git
cp -p config.sh.git backup/config.sh.git.`date +"%Y.%m.%d-%H.%M.%S"`
# create new config.sh.git
cp -p config.sh config.sh.git
