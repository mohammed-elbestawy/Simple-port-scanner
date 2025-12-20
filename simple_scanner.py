#!/bin/python3
import sys          #control in arguments & operaing commands
import socket       #communicate with NIC & open connection with TCP & UDP
from datetime import datetime

#define our target
if len(sys.argv) == 2:
     #sys.argv (the sentence the user write in terminal)
     #sys.argv[0] = scanner.py   sys.argv[1] = the sentence
     target = socket.gethostbyname(sys.argv[1]) 
     #translate hostname to ipv4
     #socket only understand IPs otherwise get gaierror
else:
     print("invalid amount of arguments")
     print("syntax: python3 scanner.py <ip>")

#add a pretty panner
print("-" * 50)
print("scanning target: "+target)
print("time started: "+str(datetime.now()))
print("-" * 50)

try:   
        for port in range(50,85):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)    
            #if the server didn't respond in 1 second consider it close 
            result = s.connect_ex((target, port))
            if result ==0:
                 print(f"port {port} is open")
            s.close()
 
except KeyboardInterrupt:    
               print("\nExsiting program")
               sys.exit()

except socket.gaierror:       
               print("hostname can not be resolved")
               sys.exit()
               
except socket.error:
               print("couldn't connect to server")
               sys.exit()
