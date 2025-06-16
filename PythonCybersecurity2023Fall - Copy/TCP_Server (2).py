#!/usr/bin/env python
# coding: utf-8

# In[1]:


import socket
import time


# In[2]:


ip_address="127.0.0.1"
port_number = 4000


# In[3]:


myServer= socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# In[4]:


server_address=(ip_address, port_number)


# In[5]:


myServer.bind(server_address)


# In[6]:


myServer.listen(1) # only one client accepted


# In[7]:


print("Listening...")


# In[ ]:


while True:
    print("waiting for client connection... ")
    client, client_address = myServer.accept()  # blocks til receives a connection from client
    print("Client type: ", type(client))
    
    try:
        print("Connection established...")
        
        while True:
            if client != 0:
                data = client.recv(1024)
                text_data = data.decode("utf-8")
                data = ('You sent >>'+text_data).encode()
                print("Data received...", text_data)
                if text_data.strip() != 'quit':
                    print("Sending Echo back to client", data)
                    client.sendall(data)
                else:
                    print("Quiting... ")
                    break
    finally:
        client.close()


# ### 
