#!/usr/bin/env python
# coding: utf-8

# In[1]:


import socket
import os


# In[2]:


ip_address="127.0.0.1"
port_number = 3000


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


# In[8]:


filename = "C:/Users/Public/myTest.txt"
suffix = (filename.split("."))[-1]


# In[9]:


print("waiting for client connection... ")
client, client_address = myServer.accept()  # blocks til receives a connection from client

if not os.path.isfile(filename):
    print("File not found")
elif suffix != "txt":
    print("Invalid file type: ", suffix)    
else:
        print("Connection established...")
        try: 
           # Reading file and sending data to server 
            myFile = open(filename, "r") 

            data = myFile.read() 
            print( "Reading file 'myTest.txt': \n\n",data) # prints file 

            while data: 
                myServer.send(str(data).encode()) 
                data = myFile.read() 
            myFile.close()
        except:
            print("Client closed...")
            client.close()
    


# In[ ]:




