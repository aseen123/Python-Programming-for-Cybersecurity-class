#!/usr/bin/env python
# coding: utf-8

# In[1]:


from scapy.all import *


# In[2]:


def scanAHostPorts(ip_address, port_number):
    
    ## assemble layer TCP
    ip_layer=IP(dst=ip_address)
    
    ##assemle layer IP
    tcp_layer=TCP(dport=port_number, flags='S')
    
    ## build packet of TCP and IP layers
    myPacket = ip_layer/tcp_layer
    
    ## send a packet and listen for an answer
    response= sr1( myPacket, verbose=0, timeout=1 )
    
    if response is None:
        return False
    
    ## if packet has a TCP, and an SA- SYN/ACK flag, return true
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


# In[4]:


## scan ports for the remote host in a given range: 20, 120
portRange = range(20,120)
for port in portRange:
    if scanAHostPorts(remoteHostIP, port):
        print("Port ", port, "   is Open!!")
    

