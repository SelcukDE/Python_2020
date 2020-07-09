#!/usr/bin/env python
# coding: utf-8

# <img src="https://docs.google.com/uc?id=14xeXxFrVRjvOoUYWn_GuyE-v84wVzrqr" class="img-fluid" alt="CLRWY">

# # Python Lab Session-1 (22 June 2020)

# ### [Assignment - 1 (Weekly Profit)](https://lms.clarusway.com/mod/assign/view.php?id=3880&forceview=1)

# In[1]:


deposit = 1000 # ilk gün yatırdığımız para - pazartesi
deposit = deposit * 7/100 + deposit # ilk günün parası - salı
deposit = deposit * 7/100 + deposit # ikinci günün parası - çarşamba
deposit = deposit * 7/100 + deposit # üçüncü günün parası - perşembe
deposit = deposit * 7/100 + deposit # dördüncü günün parası - cuma
deposit = deposit * 7/100 + deposit # beşinci günün parası - cumartesi
deposit = deposit * 7/100 + deposit # altıncı günün parası - pazar
deposit = deposit * 7/100 + deposit # yedinci günün parası - pazartesi
deposit


# In[2]:


deposit = 1000
deposit = deposit * 1.07 ** 7
deposit


# ### [Assignment - 2 (Covid - 19 Possibility)](https://lms.clarusway.com/mod/assign/view.php?id=4400)

# In[3]:


#not
#and
#or


# In[4]:


bool(1)


# In[5]:


bool(-1)


# In[6]:


bool(None)


# In[7]:


bool(0)


# In[8]:


bool([])


# In[9]:


bool({})


# In[10]:


bool(0.0)


# In[11]:


age = False
chronic = True
immune = False

risk = age or chronic or immune
risk


# In[12]:


ısı = True
madde = False
oksijen = True


# In[13]:


yangın = ısı and madde and oksijen

yangın


# ### Mini Quiz (Boolean Operators)

# In[14]:


not ("dolu_string" and "" or 0 and False and "False")


# ### [Assignment - 3 (Measure Converter)](https://lms.clarusway.com/mod/assign/view.php?id=4401&forceview=1)

# In[20]:


first = int(input("bir rakam gir:"))
second = int(input("başka bir rakam daha gir:"))

print(first + second)


# In[17]:


print("5" + "3")


# In[19]:


"a" + "a"


# In[23]:


celsius = float(input("celsius ısı degeri girelim:"))

fahreinheit = (celsius * 1.8) + 32

output = f"Celsius derece olarak {celsius} degeri, {fahreinheit} fahreinheit eder"

print(output)


# In[24]:


kilometre = float(input("kilometre değeri giriniz:"))

miles = kilometre * 0.6213

output1 = f"{kilometre} km degeri, {miles} mil eder"

print(output1)


# In[ ]:




