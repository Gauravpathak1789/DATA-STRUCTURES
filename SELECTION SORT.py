#!/usr/bin/env python
# coding: utf-8

# In[24]:


def selection_sort(array):
    n=len(array)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if (array[min_index]>array[j]):
                min_index=j
        arr=array[i]    
        array[i]=array[min_index]
        array[min_index]=arr
    return array
        
        
        


# In[25]:


selection_sort([40,30,10])


# In[ ]:




