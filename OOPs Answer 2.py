#!/usr/bin/env python
# coding: utf-8

# # Assignment-5: OOPs
#     
# # Challenge 2: Implement a Calculator Class    

# In[1]:


class Calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        print("Numbers initiated : {}, {}".format(self.num1, self.num2))
        
    def add(self):
        self.addition = self.num1+self.num2
        print("The sum after addition is : {} + {} : {}".format(self.num1,self.num2,self.addition))
    def subtract(self):
        self.subtraction = self.num1-self.num2
        print("The sum after addition is : {} - {} : {}".format(self.num1,self.num2,self.subtraction))
    def multiply(self):
        self.multiplication = self.num1*self.num2
        print("The sum after addition is : {} * {} : {}".format(self.num1,self.num2,self.multiplication))
    def divide(self):
        self.division = self.num1/self.num2
        print("The sum after addition is : {} / {} : {}".format(self.num1,self.num2,self.division))


# In[2]:


calci = Calculator(10, 94)


# In[3]:


calci.add()


# In[4]:


calci.subtract()


# In[5]:


calci.multiply()


# In[6]:


calci.divide()


# In[ ]:




