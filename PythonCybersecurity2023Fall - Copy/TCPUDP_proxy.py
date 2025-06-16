#!/usr/bin/env python
# coding: utf-8

# In[1]:


import socket


# In[2]:


proxy_address= ("127.0.0.1",3000)
forwarding_address = ("127.0.0.1", 4000)


# In[3]:


proxy= socket.socket(socket.AF_INET, socket.SOCK_STREAM)    ## TCP


# In[4]:


proxy.bind(proxy_address)


# In[5]:


proxy.listen(1) # only one client accepted
print("Listening...")


# In[6]:


while True:
    print("waiting for client connection... ")
    client, client_address = proxy.accept()  # blocks til receives a connection from client
    
    try:
        print("Connection established...")
        while True:

            ## start sending data between client and proxy    - TCP         
            client_data = client.recv(1024)
            if not client_data:
                break
            print("CLIENT_REQUEST: "+client_data.decode("utf-8") )
            
            ## open socket between proxy and server           
            proxy_serverside= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  ## UDP
            proxy_serverside.sendto(client_data,forwarding_address)
            
            response_data, server_address= proxy_serverside.recvfrom(1024)
            print("SERVER_RESPONSE: "+response_data.decode("utf-8") )
            
            ## send data to the client - TCP
            client.sendall( response_data)
    finally:
        break
client.close()


# In[ ]:




