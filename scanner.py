#!/bin/python3

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")

#Add a pretty banner

print('''
 ________  ________  ________  ________  ________  ___    ___               
|\   ____\|\   __  \|\   __  \|\   __  \|\   __  \|\  \  /  /|              
\ \  \___|\ \  \|\  \ \  \|\  \ \  \|\  \ \  \|\  \ \  \/  / /              
 \ \  \    \ \   _  _\ \   __  \ \   ____\ \   ____\ \    / /               
  \ \  \____\ \  \\  \\ \  \ \  \ \  \___|\ \  \___|\/  /  /                
   \ \_______\ \__\\ _\\ \__\ \__\ \__\    \ \__\ __/  / /                  
    \|_______|\|__|\|__|\|__|\|__|\|__|     \|__||\___/ /                   
                                                 \|___|/                    
                                                                     
                                                                            
 ________  ________  ________  ________   ________   _______   ________     
|\   ____\|\   ____\|\   __  \|\   ___  \|\   ___  \|\  ___ \ |\   __  \    
\ \  \___|\ \  \___|\ \  \|\  \ \  \\ \  \ \  \\ \  \ \   __/|\ \  \|\  \   
 \ \_____  \ \  \    \ \   __  \ \  \\ \  \ \  \\ \  \ \  \_|/_\ \   _  _\  
  \|____|\  \ \  \____\ \  \ \  \ \  \\ \  \ \  \\ \  \ \  \_|\ \ \  \\  \| 
    ____\_\  \ \_______\ \__\ \__\ \__\\ \__\ \__\\ \__\ \_______\ \__\\ _\ 
   |\_________\|_______|\|__|\|__|\|__| \|__|\|__| \|__|\|_______|\|__|\|__|
   \|_________|                                                             
                                                                            
                                                                            
''')

print("-" * 50)
print("Scanning target: "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result == 0:
			print(f"Port {port} is open")
		s.close()
except KeyboardInterrupt:
	print("\nExiting Program.")
	sys.exit()
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()
except socket.error:
	print("Could not connect to server.")
	sys.exit()
