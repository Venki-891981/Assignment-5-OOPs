#!/usr/bin/env python
# coding: utf-8

# # Assignment-5: OOPs
# 
# # Challenge 3: Implement the Complete Student Class

# In[1]:


class Student:

    def setName(self):
        print("The name of the student is set")
    def getName(self, name):
        self.__name = name
        print("The name of the student is : {}".format(self.__name))
    def setRollNumber(self):
        print("The roll number is set")
    def getRollNumber(self, RollNumber):
        self.__RollNumber = RollNumber
        print("The roll number of the student is : {}".format(self.__RollNumber))


# In[2]:


student_class = Student()


# In[3]:


student_class.setName()


# In[4]:


student_class.getName("Ed")


# In[5]:


student_class.setRollNumber()


# In[7]:


student_class.getRollNumber(123456)


# In[ ]:




