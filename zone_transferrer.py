!/usr/bin/python
# A script that performs zone transfer
# Pay attention: it requires dnspython
# To install it: pip install dnspython

import dns.resolver
import dns.query
import dns.inet
import dns.zone
import sys

if(len(sys.argv) < 2):
   print("[*] Zone transfer script")
   print("[*] Usage:", sys.argv[0], "<domain name>")
else:
   domain = sys.argv[1]
   answer = dns.resolver.query(domain, 'NS')
   for ns in answer:
      try:
         zone_file = dns.zone.from_xfr(dns.query.xfr(str(ns), domain))
         print("Zone file for",ns)
         print(zone_file.to_text().decode("utf-8"))        
      except:
         print("Zone Transfer not available for",ns)
