' This simple VB script can be used to set the speed of your SQRL Device
' Examples below add more for however many devices you have. 
' To increase speed use {+} for each increase and - for each decrease.
' Use the number to select each device and 9 and then n to select devices above 9
' Make sure to add "TITLE SQRLMiner" after the echo off of your batch file. 
' To get this to automatically run when you batch file restarts run call it from your batch file
' Like: start "" cmd /c cscript changespeed.vbs right after the :loop command. 
' 
Set WshShell = WScript.CreateObject("WScript.Shell")
Wscript.Sleep 10000
WshShell.AppActivate "SQRLMiner"
'Choose device 1 and decrease speed by 6
WshShell.SendKeys "1{+}{+}{+}{+}{+}{+}"
Wscript.Sleep 1000
'Choose device 2 and decrease speed by 1
'WshShell.SendKeys "2-"
'Wscript.Sleep 1500
'Choose device 12 and increase speed by 3
'WshShell.SendKeys "9nnn{+}{+}{+}"
