#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket


# In[ ]:


proxy_address= ("127.0.0.1",3000)
forwarding_address = ("127.0.0.1", 4000)


# In[ ]:


proxy= socket.socket(socket.AF_INET, socket.SOCK_STREAM)    ## TCP


# In[ ]:


proxy.bind(proxy_address)


# In[ ]:


proxy.listen(1) # only one client accepted
print("Listening...")


# In[ ]:


while True:
    print("Waiting for client connection... ")
    client, client_address = proxy.accept()  # blocks til receives a connection from client
    
    # creating connection with server
    forward_server = socket.create_connection( forwarding_address)
    
    try:
        print("Connection done...")
        while True:

            ## start sending data between client and forward_server
            
            client_data = client.recv(1024)
            if not client_data:
                break
            print("CLIENT_REQUEST: "+client_data.decode("utf-8") )
            forward_server.sendall(client_data)
           
            response_data = forward_server.recv(1024)
            if not response_data:
                break
            print("SERVER_RESPONSE: "+response_data.decode("utf-8") )
            client.sendall( response_data)
    finally:
        client.close()
        forward_server.close()
        break


# In[ ]:




