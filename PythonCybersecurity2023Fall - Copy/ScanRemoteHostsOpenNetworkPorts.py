#!/usr/bin/env python
# coding: utf-8

# In[1]:


import socket
import sys
from datetime import datetime


# In[2]:


remoteServer= input("Enter a host name: ")   ## "34.160.164.47", "192.168.1.138", "8.8.8.8", "8.8.4.4"
remoteServerIP= socket.gethostbyname( remoteServer )


# In[3]:


print( " Please wait while scanning remote host server: ", remoteServerIP)

## test the time spent doing the scan - just a bit of extra besides the requierement
t1 = datetime.now()


# In[ ]:


#use a range of ports between 0, 65535)
try: 
    for port in range(0, 65535):
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        result = mySocket.connect_ex(( remoteServerIP, port ))
        
        ## if result==0, automatically  will be sent an SYN request, and receive a SYN/ACK response.
        ## If that happens, that means the port is open to the public.
        
        if result == 0:  ## returns 0 if succesful, socket errors: 10060- timeout connection failed
            print("Port {}    Open").format(port)
        mySocket.close()
        
except KeyboardInterrupt:
        print("You pressed ^C")
        sys.exit()
        
except socket.gaierror:
        print("Host name could not be resolved, Exiting")
        sys.exit()


    
t2 = datetime.now()   



# In[ ]:


total = t2 - t1
print(" Scanning completed in: ", total)


# In[ ]:




