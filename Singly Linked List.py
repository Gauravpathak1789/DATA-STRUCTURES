#!/usr/bin/env python
# coding: utf-8

# In[23]:


class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL:
    def __init__(self,start=None):
        self.start=start
        
    def is_empty(self):
        return self.start==None
    
    def insert_at_start(self,data):
        N=Node(data,self.start)
        self.start=N
        
    def insert_at_last(self,data):
        N=Node(data)
        if self.is_empty():
            self.start=N
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=N
    
    def Serach(self,data):
        if not self.is_empty():
            temp=self.start
            while temp is not None:
                if temp.item==data:
                    return temp
                temp=temp.next
                
    def insert_after(self,temp,data):
        N=Node(data,temp.next)
        temp.next=N
    
    def print_element(self):
        if not self.is_empty():
            temp=self.start
            while temp is not None:
                print(temp.item,end=" ")
                temp=temp.next
    
    def delete_first(self):
        if self.is_empty():
            pass
        else:
            self.start=self.start.next
    
    def delete_last(self):
        if self.is_empty():
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
    
    def delete_item(self,data):
        if self.is_empty():
            pass
        elif self.start.next==None:
            if self.start.item==data:
                self.start=None
        else:
            temp=self.start
            while temp.next is not None:
                if temp.next.item==data:
                    temp.next=temp.next.next
                    break
                temp=temp.next
                    


# In[24]:


s1=SLL()


# In[25]:


s1.insert_at_start(5)
s1.insert_at_start(4)
s1.insert_at_start(3)
s1.insert_at_start(2)


# In[26]:


s1.print_element()


# In[27]:


s1.insert_at_last(90)


# In[28]:


s1.delete_first()


# In[29]:


s1.delete_item(5)


# In[30]:


s1.delete_last()


# In[31]:


s1.is_empty()


# In[32]:


s1.Serach(4)


# In[ ]:




