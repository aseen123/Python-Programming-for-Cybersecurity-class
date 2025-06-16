#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket


# In[ ]:


ip_address = '127.0.0.1'
port_number=3000


# In[ ]:


client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip_address,port_number))


# #### Making DNS request and connecting to server

# In[ ]:


while True:
    request= input("Enter your message: ")  
    request+= "\r\n"

    if not request:           
        break
    if request[:4] =='quit':
        break
    client.sendall(request.encode('utf-8'))
    request = (client.recv(1024)).decode()


# In[ ]:


print(request)


# In[ ]:




