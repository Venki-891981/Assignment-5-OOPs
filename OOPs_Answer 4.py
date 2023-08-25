#!/usr/bin/env python
# coding: utf-8

# # OOP Assignment
# 
# # Challenge 4: Implement a Banking Account

# In[25]:


## Task 1

class Account:
    
    balance_cnt = 0
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance
        print("title : {}, balance : {}".format(self.title,self.balance))


class SavingsAccount(Account):

    def __init__(self, title, balance, interestRate):
        
        super().__init__(title, balance)
        self.interestRate = interestRate
       


# In[26]:


## Task 2

credentials = Account("Ashish", 5000)


# In[29]:


## Task 3


credentials_1 = SavingsAccount("Ashish", 5000, 5)


# In[30]:


credentials_1.interestRate


# In[ ]:




