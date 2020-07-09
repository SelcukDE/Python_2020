#!/usr/bin/env python
# coding: utf-8

# In[3]:


empty_list_1= []

empty_list_2 = list()


# In[4]:


empty_list_1 = []
empty_list_1.append('114')
empty_list_1.append('plastic-free sea')

print(empty_list_1) 


# In[5]:


city = ['New York', 'London', 'Istanbul', 'Seoul', 'Sydney']
city.append('Addis Ababa')

print(city) 


# In[6]:


colors = ['red', 'purple', 'blue', 'yellow', 'green']
print(colors[2])  # If we start at zero, 
# the second element will be 'blue'.


# In[7]:


city = ['New York', 'London', 'Istanbul', 'Seoul', 'Sydney']

city_list = []
city_list.append(city) # we have created a nested list

print(city_list)


# In[8]:


city_list = [['New York', 'London', 'Istanbul', 'Seoul', 'Sydney']]
print(city_list[0]) # access to first and only element


# In[9]:


city_list = [['New York', 'London', 'Istanbul', 'Seoul', 'Sydney']]
print(city_list[0][2])


# In[10]:


city_list = [['New York', 'London', 'Istanbul', 'Seoul', 'Sydney']]
print(city_list[0][2][3])


# In[11]:


odd_numbers = [[11, 13, 15], 17, 19, 21, 23, 25, 27, 29]

print(odd_numbers[6])


# In[12]:


fruits = ['apple', 'banana', 'watermelon', 'orange', 'mango', 'avocado']

fruit_list = []
fruit_list.insert(0, fruits)
print(fruit_list[0][2][7])


# In[13]:


numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17]
print(numbers[2:5])  # we get the elements from index=2 to index=5(5 is not included)


# In[14]:


count = list(range(11))
print(count)

print(count[0:11:2])


# In[15]:


animals = ['elephant', 'bear', 'fox', 'wolf', 'rabbit', 'deer', 'giraffe']

print(animals[:])  # all elements of the list


# In[16]:


animals = ['elephant', 'bear', 'fox', 'wolf', 'rabbit', 'deer', 'giraffe']
print(animals[3:])


# In[17]:


animals = ['elephant', 'bear', 'fox', 'wolf', 'rabbit', 'deer', 'giraffe']
print(animals[:5])


# In[18]:


animals = ['elephant', 'bear', 'fox', 'wolf', 'rabbit', 'deer', 'giraffe']
print(animals[::2])


# In[19]:


even_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

print(even_numbers[4:9])


# In[21]:


print(len([[12, 34, 56]]))


# In[22]:


print(len([[12, 34, 56]][0]))


# In[ ]:


aa = [1,2,3,4,5]


# In[25]:


x = "2020's hard"


print([x])
print(list(x))


# In[33]:


a = list(range(:5))

print()

print(a.insert(4, 5))


# In[34]:


a = range(0,11)

print(a)


# In[41]:


mix_list = [1, [1, "one", 2, "two", 3, "three"], 4]
print(mix_list[1][1:6:2])


# In[49]:


print(not 0 and "write me")


# In[46]:


print(False or {})


# In[8]:


#ÖDEV
#leap_year = input("Bir yıl giriniz: ")

#year = int(year)

#a = "year/4" = True
#b = "year/400" = True
#c = "year/100" = False

sayi = int(input("Bir yıl giriniz: "))

sayi = (sayi % 4 == 0) and (sayi % 400 ==0)

print(sayi)


sayi2 = int(input("Bir yıl giriniz: "))
sayi2 = (sayi % 100 != 0)

print(sayi2)

# a = True
#b = True
#c = False

#print(a and b or c) 



#print("Leap year : {} ".format(year))


# ## name = input("Please enter your name:")
# last_name = input("and enter your last name:")
# age = int(input("Please enter your name:"))
# 
# print("Name = {}\nLast Name = {} \nAge = {}".format(name, last_name, age))

# In[19]:


even_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

print(even_numbers[4:9])


# In[16]:


kk = [3, 4, 5, 6, 7]

kk[3] = "x"
kk[4:] = "istanbul"

print (kk[2:])


# In[19]:


my_list = ['joseph', 'Clarusway', 2020]

new_list1 = list(my_list)
new_list2 = [my_list]

print(new_list1)
print(len(new_list1))

print(new_list2)
print(len(new_list2))


# In[20]:


a = "2020's hard"

print(list(a))

print([a])


# In[21]:


numbers = [1, 4, 7]

numbers.append(9)
numbers.append('9')

print(numbers)


# In[24]:


empty_list = []
empty_list.append(666)
empty_list.append('Multiverse')
empty_list.append([0])

print(empty_list)


# In[25]:


numbers =[1,4,7]

numbers.insert(2, 9)
print(numbers)

numbers.insert(2, 6)
print(numbers)


# In[27]:


numbers = [1, 4, 7, '9']
numbers.remove(7)
numbers.remove('9')
print(numbers)


# In[28]:


numbers = [4, 1, 9, 7]
numbers.sort()

print(numbers)


# In[ ]:


mix = ['d', 1, 'a', 7]
mix.sort() 

print(mix)


# In[1]:


city_list = [['New York', 'London', 'Istanbul', 'Seoul', 'Sydney']]
print(city_list[0]) # access to first and only element


# In[2]:


city_list = [['New York', 'London', 'Istanbul', 'Seoul', 'Sydney']]
print(city_list[0][2])


# In[3]:


fruits = ['apple', 'banana', 'watermelon', 'orange', 'mango', 'avocado']

fruit_list = []
fruit_list.insert(0, fruits)

print(fruit_list[0][2][7])


# In[4]:


numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17]

print(numbers[2:5])  # we get the elements from index=2 to index=5(5 is not included)


# In[5]:


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist[:4])


# In[6]:


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])


# In[8]:


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist[-4:-1])
print(thislist[-3:-1])
print(thislist[-2:-1])
print(thislist[-1:-1])
print(thislist[4:-1])


# In[9]:


thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


# In[10]:


thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


# In[11]:


thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


# In[12]:


thislist = ["apple", "banana", "cherry"]
print(len(thislist))


# In[13]:


thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


# In[14]:


thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


# In[15]:


thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


# In[16]:


thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)  # The pop() method removes the specified index, (or the last item if index is not specified)


# In[17]:


thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)  # The del keyword removes the specified index


# In[19]:


thislist = ["apple", "banana", "cherry"]
del thislist  # The del keyword can also delete the list completely


# In[20]:


thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)  # The clear() method empties the list


# In[21]:


thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist) 

# Make a copy of a list with the copy() method


# In[22]:


thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Another way to make a copy is to use the built-in method list().


# In[23]:


numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17]
print(numbers[2:5])  

# we get the elements from index=2 to index=5(5 is not included)


# In[ ]:


count = list(range(11))
print(count)

print(count[0:11:2])


# In[1]:


count = list(range(11))
print(count)

print(count[0:11:2])


# In[2]:


animals = ['elephant', 'bear', 'fox', 'wolf', 'rabbit', 'deer', 'giraffe']

print(animals[:])  # all elements of the list


# In[6]:


print(len([[12, 34, 56]][0]))

print(len([[34, 56]][0]))

print(len([[0]][0]))

print(len([[]][0]))

print(len([0][[0]][0]))


# In[7]:


print(len([[12, 34, 56]]))

print(len([[34, 56]]))

print(len([[56]]))

print(len([[]]))

print(len([[0]]))


# In[8]:


odd_no = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(odd_no[7:3:-1])
print(odd_no[2:6:-1])


# In[9]:


thistuple = ("apple", "banana", "cherry")
print(thistuple)


# In[10]:


thistuple = ("apple", "banana", "cherry")
print(thistuple[1])


# In[11]:


thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])


# In[12]:


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])


# In[13]:


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])


# In[ ]:


family = { 'name1 :'Joseph',
           'name2': 'Bella',
           'name3': 'Ayse'   
   
}


# In[15]:


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict["brand"]
y = thisdict["model"]
z = thisdict["year"]

print(x)
print(y)
print(z)

print(x, y, z, sep=',')


# In[11]:


grocer = ["banana", ["orange", ["apple", "eggplant", "melon", "spinach", "cheese", "leek" ], "water"], "mandarin"]

print(grocer[1][1][1:2], grocer[1][1][3:4], grocer[1][1][5:6])


# In[12]:


# A dictionary is a collection which is unordered, changeable and indexed. 
# In Python dictionaries are written with curly brackets, and they have keys and values.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


# In[13]:


state_capitals = {'Arkansas': 'Little Rock',
                  'Colorado': 'Denver',
                  'California': 'Sacramento',
                  'Georgia': 'Atlanta' 
                 }

print(state_capitals['Colorado']) # accessing method


# In[14]:


state_capitals = {'Arkansas': 'Little Rock',
                  'Colorado': 'Denver',
                  'California': 'Sacramento',
                  'Georgia': 'Atlanta' 
                 }

state_capitals['Virginia'] = 'Richmond' # adding a new item

print(state_capitals)


# In[15]:


mix_dict = {'animal': ('dog', 'cat'),  # tuple type
            'planet': ['Neptun', 'Saturn', 'Jupiter'],  # list type
            'number': 40,  # int type
            'pi': 3.14,  # float type
            'is_good': True}  # bool type

print(mix_dict)


# In[16]:


dict_by_dict = dict(animal='dog', planet='neptun', number=40, pi=3.14, is_good=True)

print(dict_by_dict)


# In[17]:


dict_by_dict = {'animal': 'dog',
                'planet': 'neptun',
                'number': 40,
                'pi': 3.14,
                'is_good': True}

print(dict_by_dict.items(), '\n')
print(dict_by_dict.keys(), '\n')
print(dict_by_dict.values())


# In[18]:


dict_by_dict = {'animal': 'dog',
                'planet': 'neptun',
                'number': 40,
                'pi': 3.14,
                'is_good': True}

dict_by_dict.update({'is_bad': False})

print(dict_by_dict)


# In[19]:


dict_by_dict = {'animal': 'dog',
               'planet': 'neptun',
               'number': 40,
               'pi': 3.14,
               'is_good': True,
               'is_bad': False}

del dict_by_dict['animal']

print(dict_by_dict) 


# In[20]:


dict_by_dict = {'planet': 'neptun',
               'number': 40,
               'pi': 3.14,
               'is_good': True,
               'is_bad': False}

print('pi' in dict_by_dict) 
print('animal' not in dict_by_dict)  # remember, we have deleted 'animal'


# In[24]:


student_ages = {"Harry": 29,
                "Clark": 32,
                "Peter": 22,
                "Bruce": 36
                }

print(student_ages['Clark'])


# In[ ]:


school_records={
    "personal_info":
        {"kid":{"tom": {"class": "intermediate", "age": 10},
                "sue": {"class": "elementary", "age": 8}
               },
         "teen":{"joseph":{"class": "college", "age": 19},
                 "marry":{"class": "high school", "age": 16}
               },               
        },
        
    "grades_info":
        {"kid":{"tom": {"math": 88, "speech": 69},
                "sue": {"math": 90, "speech": 81}
               },
         "teen":{"joseph":{"coding": 80, "math": 89},
                 "marry":{"coding": 70, "math": 96}
               },               
        },        
}


# In[25]:


school_records={
    "personal_info":
        {"kid":{"tom": {"class":"intermediate", "age":10},
                "sue": {"class":"elementary", "age":8}
               },
         "teen":{"joseph":{"class":"college", "age":19},
                 "marry":{"class":"high school", "age":16}
               },               
        },
}

print(school_records['personal_info']['teen']['marry']['age'])


# In[ ]:


customers = { 
'bank': 
{1: {'name': 'James', 'age': '27', 'sex': 'Male'}, 
 2: {'name': 'Nicole', 'age': '25', 'sex': 'Female'},  
 3: {'name': 'Andy', 'age': '38', 'sex': 'Male'}, 
 4: {'name': 'Alex', 'age': '19', 'sex': 'Male'}, 
 5: {'name': 'Linda', 'age': '33', 'sex': 'Female'}, 
},
'insurance':
{1: {'name': 'Jashua', 'age': '33', 'sex': 'Male'}, 
 2: {'name': 'Marry', 'age': '66', 'sex': 'Female'},  
 3: {'name': 'Adam', 'age': '56', 'sex': 'Male'}, 
 4: {'name': 'Samuel', 'age': '54', 'sex': 'Male'}, 
 5: {'name': 'Lisa', 'age': '22', 'sex': 'Female'},
},
}

print(customers['insurance'][5]['age'])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




