#!/usr/bin/env python
# coding: utf-8

# In[1]:


#operators:

x=30
y=10

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x**y)
print(x//y)
print(x%y)


# In[15]:


#data types:

x=55
y=5.5
z=5+5j

print (type(x))
print (type("x"))
print (type(y))
print (type(z))
print (type(True))


# In[16]:


x=10
y=20
if x>=y:
    print(True)
    
else:
    print(False)


# In[4]:


x=10
y=10
#x and y gets multiplies
z=(x*y)
z=(x+y)
z=(x-y)
z=(x/y)
z=(x//y)
z=(x**y)
print("the output is : " + str (z))


# In[71]:


#case sensitive

x = 4
X = "Sally"

print(x)
print(X)


# In[ ]:


get_ipython().set_next_input('Absolute equal');get_ipython().run_line_magic('pinfo', 'equal')

