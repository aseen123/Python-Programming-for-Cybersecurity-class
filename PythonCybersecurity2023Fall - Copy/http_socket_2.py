#!/usr/bin/env python
# coding: utf-8

# In[1]:


import socket


# In[2]:


web_address= input("Please input a web address: ")   ## http://www.google.com/helloworld.html
protocol, x = web_address.split("/", 1)
host_name, resource = x[1:].split("/")  

## print( "Protocol: "+ protocol[:-1]+ ", Host_name: "+ host_name+ ", Resource: /"+ resource, "\n")
port_number=80


# In[3]:


myHTTPClient=socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# ##Making DNS request and connecting to server

# In[4]:


ip_address=socket.gethostbyname(host_name)


# In[5]:


print(ip_address)


# In[6]:


request= 'GET /' + resource + '\r\n'   ##'GET /helloworld.html\r\n'


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


# In[11]:


# HTTP Response Codes
http_codes = [200, 301, 302, 400, 403, 404, 500, 503]
description = ""
http_error_first_line = response.decode('utf-8').split('\n', 1)[0]
http_code = [int(co) for co in http_error_first_line.split() if co.isdigit()]

##print("\n\nhttp_error_first_line: " + http_error_first_line+ "\n\nCode: "+ str(http_code[0]))



# In[12]:


code = http_code[0]
if code in http_codes:    
  if code == 200:
    description = "" ## "OK"
  elif code == 301:
    description = "moved permanently"
  elif code == 302:
    description = "moved temporarily"
  elif code == 400:
    description = "bad request"
  elif code == 403:
    description = "forbiden"
  elif code == 404:
    description = "not found"
  elif code == 500:
    description = "internal server error"
  elif code == 503:
    description = "service unavailable"
else:
    description = "not possible"

if code != 200:
  print("HTTP code " + str(code) + ": Sorry, "+ description )


# In[ ]:




