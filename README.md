# MattermostPrinterBot

The project was created during a 2 week internship at bytemine GmbH.
The bot is able to provide information about the ink level of an MFC-9332CDW printer via Mattermost.

# Installation
To get the bot up and running, simply create a configuration file and start the main.py file with python 3.

# Configuration
The configuration file consists of the following parameters:

host -> Enter the host name (e.g. mattermost.example.net)  
user -> Enter the username of the bot. The user must be created before!  
pass -> Enter the password of the username  
team -> Enter the team where the bot is located  
channel -> Enter the channel name where the bot should be active  
access_token -> Enter the access token of the bot. Check out (Check https://docs.mattermost.com/developer/personal-access-tokens.html)  
source -> Here you can add additional config sources. (At the moment only printer is available)

# Example of a configuration file:
```
host:         mattermost.example.net
user:         john
pass:         dohn
team:         company
channel:      printer_info
access_token: xxxxxxxxxxxxxxxxxxxxxxxxxxx
source:       printer.txt
```

# Printer configuration
Currently only the MFC-9332CDW printer is supported.

plugin -> this should be set to "printer"  
host -> host of the printer (e.g. printer.company.net)  

# Example of printer configuration file
```
plugin: printer
host:   printer.company.net
```

# Commands
Commands can't be configured yet.
There is only one available command.
```
!printer <Color>
```
If you want to output all colors, then don't specify any parameters.
The bot supports all native colors.

