#!/usr/bin/python
import sys
from scapy.all import *

if (len(sys.argv) < 2 or len(sys.argv) > 2):
    print("Usage: sudo python3 pyngsweeper.py 192.168.1.0/24")
else:
   ip_string_base = sys.argv[1][:-4]
   for i in range(1, 255):
       ip = ip_string_base + str(i)
       answer = sr1((IP(dst=ip)/ICMP()),timeout=0.3, verbose=0)
       if (answer != None):
           print(ip,"is up") 
