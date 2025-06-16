#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket


# In[ ]:


ip_address = "127.0.0.1"
port_number=4000


# In[ ]:


myServer= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# In[ ]:


server_address =(ip_address, port_number) 


# In[ ]:


myServer.bind(server_address)


# In[ ]:


while True:
    data,client_address= myServer.recvfrom(1024)
    text_data = data.decode("utf-8")
    data = ('You sent >>'+text_data).encode()
    print("Data received...", text_data)
    myServer.sendto(data,client_address)
    print("Response sent...")


# In[ ]:





# In[ ]:




