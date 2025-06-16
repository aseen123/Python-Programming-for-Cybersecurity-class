#!/usr/bin/env python
# coding: utf-8

# In[1]:


import socket


# In[2]:


ip_address = '127.0.0.1'
port_number=3000


# In[3]:


client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip_address,port_number))


# #### Making DNS request and connecting to server

# In[4]:


while True:
    request= input("Enter your message: ")  
    request+= "\r\n"

    if not request:           
        break
    if request[:4] =='quit':
        break
    client.sendall(request.encode('utf-8'))
    request = (client.recv(1024)).decode()

## client.close()


# In[5]:


print(request)


# In[ ]:




