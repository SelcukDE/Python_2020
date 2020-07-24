#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#micro-learning
#daily-python-challenge
QUESTION:
Write a Python code to sort the list at below without using .sort() method of list.
elements of list = [999, 333, 2, 8982, 12, 45, 77, 99, 11]
Expected output:
[2, 11, 12, 45, 77, 99, 333, 999, 8982]
ANSWER:
mylist = [999, 333, 2, 8982, 12, 45, 77, 99, 11]
for i in range(len(mylist)):
   for j in range(i+1,len(mylist)):
       if mylist[i] > mylist[j]:
           temp = mylist[i]
           mylist[i] = mylist[j]
           mylist[j] = temp
print(mylist)


# In[ ]:


#micro-learning
#daily-python-challenge
QUESTION:
Write a Python code to sort the list at below without using .sort() method of list.
elements of list = [999, 333, 2, 8982, 12, 45, 77, 99, 11]
Expected output:
[2, 11, 12, 45, 77, 99, 333, 999, 8982]


# In[ ]:


#micro-learning
#daily-python-challenge
QUESTION:
Write a Python code that calculates the average of scores that students took in a math class at below.
scores = {"Mary" : 85, "Susan": 75, "Barry" : 65, "Alexis" : 88, "Jane" : 45, "Tina" : 100, "Tom" : 90, "Tim": 60}
ANSWER:
scores = {"Mary" : 85, "Susan": 75, "Barry" : 65, "Alexis" : 88, "Jane" : 45, "Tina" : 100, "Tom" : 90, "Tim": 60}
average = sum(scores.values()) / len(scores)
print(average)


# In[ ]:


#micro-learning
#daily-python-challenge
QUESTION:
Write a Python code that calculates the average of scores that students took in a math class at below.
scores = {"Mary" : 85, "Susan": 75, "Barry" : 65, "Alexis" : 88, "Jane" : 45, "Tina" : 100, "Tom" : 90, "Tim": 60}


# In[ ]:


#micro-learning
#daily-python-challenge
QUESTION:
Please reverse the text below without using text index methods. Please use a loop.
text = “Clarusway”
ANSWER:
text = "Clarusway"
newtext = ""
for i in range(len(text)-1, -1, -1):
   newtext += text[i]
print(newtext)


# In[ ]:





# In[ ]:




