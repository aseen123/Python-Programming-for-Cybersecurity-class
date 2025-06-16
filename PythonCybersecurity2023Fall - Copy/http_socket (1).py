#!/usr/bin/env python
# coding: utf-8

# In[1]:


import socket


# In[2]:


web_address= input("Please input a web address: ")
protocol, x = web_address.split("/", 1)
host_name, resource = x[1:].split("/")  ##host_name= 'www.google.com'

##print( "Protocol: "+ protocol[:-1]+ ", Host_name: "+ host_name+ ", Resource: /"+ resource, "\n")
port_number=80


# In[3]:


myHTTPClient=socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# #### Making DNS request and connecting to server

# In[4]:


ip_address=socket.gethostbyname(host_name)


# In[5]:


print(ip_address)


# In[6]:


request= 'GET /' + resource + '\r\n'   ##'GET helloworld.html\r\n'


# In[7]:


myHTTPClient.connect((ip_address,port_number))


# In[8]:


myHTTPClient.sendall(request.encode())


# In[9]:


response=b''
buffer_size=1024

while True:
    cup_of_data=myHTTPClient.recv(buffer_size)
    if not cup_of_data:
        break
    response=response+cup_of_data
    


# In[10]:


print(response.decode('utf-8'))

