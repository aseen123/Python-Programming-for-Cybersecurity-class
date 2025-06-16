#!/usr/bin/env python
# coding: utf-8

# In[1]:


from scapy.all import *


# In[2]:


def scanRemoteHostPorts(ip_address, port_number):
    
    ## assembling layers: TCP, IP
    ip_layer=IP(dst=ip_address)
    tcp_layer=TCP(dport=port_number, flags='S')
    myPacket = ip_layer/tcp_layer
    
    ## send a response, with no verbose, timeout
    response= sr1( myPacket, verbose=0, timeout=1 )
    
    if response is None:
        return False
    
    if response.haslayer(TCP):
        if response[TCP].flags=='SA':
            return True  ## port is Open
        else:
            return False ## Port is not Open
    else:
        return False
            
    print( response.show())


# In[3]:


remoteHostIP= input("Enter a host name: ")   ## "52.53.232.80"- www.usman.cloud


# In[ ]:


## scan ports for the remote host 
portRange = range(20,120)
for port in portRange:
    if scanRemoteHostPorts(remoteHostIP, port):
        print("Port ", port, "   is Open!!")
    

