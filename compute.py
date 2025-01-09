#!/usr/bin/env python
# coding: utf-8

# In[38]:


def mean_value(*n):
    sum = 0
    counter = 0
    for x in n:
        counter = counter +1
        sum += x
        mean = sum / counter
        return mean


# In[39]:


mean_value(99,57,38,62,10,79,110,5605,11200,8900)


# In[33]:


def median_value(*n):
    num_list = list(n)
    num_list.sort()
    l = len(num_list)
    
    if l%2 == 0:
        median = (num_list[int(l/2)] + num_list[int(l/2)-1])/2
    else:
        median = num_list[int(l/2)]
    return median
    


# In[31]:


mean_value(99,57,38,62,10,79,110,605,1200,8500)


# In[25]:


median_value(99,57,38,62,10,79,110,404,100,800)


# In[ ]:




