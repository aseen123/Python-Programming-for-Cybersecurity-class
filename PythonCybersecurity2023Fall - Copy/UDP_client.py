#!/usr/bin/env python
# coding: utf-8

# In[1]:


import socket


# In[2]:


destination_host=input("Enter IP address: ")   ##ip_address="127.0.0.1"
destination_port=int(input("Enter port number: ")) ##port_number = 3000


# In[3]:


client= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# In[4]:


socket_address=(destination_host, destination_port)


# In[5]:


while True:
    request= input("Enter your message: ")  ## client.recv(1024)
    request+= "\r\n"
    client.sendto( request.encode(), socket_address)
    response,server_address= client.recvfrom(1024)
    print("\r\n"+response.decode("utf-8"))
    if request.strip()== 'quit':
        break
print("Conversation ended...")


# ### 
