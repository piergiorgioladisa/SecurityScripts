#!/usr/bin/python

import socket
import sys

if len(sys.argv) !=3:
        print("[*] Usage:sudo python3 smtp-users-checker.py <ip address> <user-list>")
        sys.exit(0)

# Create a Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the Server
connect = s.connect((sys.argv[1],25))

# Receive the banner
banner = s.recv(1024)
print("[*] Banner received from",sys.argv[1],":",banner)

# VRFY the list of users
try:
   f = open(sys.argv[2],"r")
   print("[*] Verifying the list of users ...")
   for user in f:
      print(user)
      s.send(('VRFY '+ user + '\r\n').encode())
      result = s.recv(1024)
      print("[*] Answer for",user, ":", result)
   s.close()   


except:
   print("Error: File does not exist. Try to provide the correct file name or path")
