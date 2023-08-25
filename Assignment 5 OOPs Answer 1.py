#!/usr/bin/env python
# coding: utf-8

# # OOP Assignment
# 
# # Challenge 1: Square Numbers and Return Their Sum
#     
# 

# In[14]:


class Point:

    def __init__(self, x, y, z):
        print("Accessing x, y, z directly from class :", x, y, z)
        self.x = x
        self.y = y
        self.z = z
        

    def sqSum(self):
        self.x = self.x*self.x
        self.y = self.y*self.y
        self.z = self.z*self.z
        print("sqSum : x^2: {} + y^2 : {} + z^2 : {}".format(self.x, self.y, self.z))
        
    def print_sum(self):
        sqSum = self.x + self.y + self.z
        print("sqSum : x : {} + y : {} + z : {} : ".format(self.x, self.y, self.z), sqSum)
        
   


# In[16]:


answer = Point(1,3,5)


# In[17]:


answer.sqSum()


# In[18]:


answer.print_sum()

