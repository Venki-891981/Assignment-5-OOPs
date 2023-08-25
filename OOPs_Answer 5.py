#!/usr/bin/env python
# coding: utf-8

# # OOP Assignment
# 
# # Challenge 5: Handling a Bank Account

# In[40]:


class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def withdrawal(self, balance = 2000, withdrawal = 500):
        self.balance = 2000
        self.withdrawal = 500
        
    def getBalance_withdrawal(self, balance = 2000, withdrawal = 500):
        self.balance = 2000
        self.withdrawal = 500
        self.getbalance_withdrawal = self.balance - self.withdrawal
        return self.getbalance_withdrawal
        
        
        
    def deposit(self, balance = 5000, deposit = 500):
        self.balance = 2000
        self.deposit = 500
        
    def getBalance_deposit(self, balance = 2000, deposit = 500):
        self.balance = 2000
        self.deposit = 500
        self.getbalance_deposit = self.balance + self.deposit
        return self.getbalance_deposit
        
        
        
class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
            super().__init__(title, balance = 2000)
            self.interestRate = interestRate
    
    def interestAmount(self, balance = 2000, interestRate = 5):
        self.balance = 2000
        self.interestRate = 5
        self.interestAmount = (self.interestRate*self.balance)/100
        print("(interestAmount : (interestRate : {} * balance :{}) / 100 : {}".format
              (self.interestRate, self.balance, self.interestAmount))

#code to test - do not edit this

demo1 = SavingsAccount("Ashish", 2000, 5)   # initializing a SavingsAccount object


# In[41]:


bank = Account()


# In[42]:


bank.getBalance_withdrawal()


# In[43]:


bank.getBalance_deposit()


# In[44]:


bank_1 = SavingsAccount("Ashish", 2000, 5)


# In[45]:


bank_1.title


# In[46]:


bank_1.balance


# In[47]:


bank_1.interestRate


# In[48]:


bank_1.interestAmount()


# In[ ]:




