# set 
# {}
# set()
# *********************************************************

set_1 = {"red", "blue", "pink", "red"}
colors = "red", "blue", "pink", "red"
set_2 = set(colors)
print(set_1)
print(set_2)
print(type(set_1))
print(type(colors))
print(type(set_2))

# *********************************************************
print()
# *********************************************************

# {} bu set boş küme değil. Dict. dir
# set te boş küme yapmak için set() kullanılır.

flower_list = ["rose", "violet", "carnation", "rose", "orchid", "rose", "orchid"]
flowerset = set(flower_list)
flowerlist = list(flowerset)

print(flowerset)
print(flowerlist)

# *********************************************************
print()
# *********************************************************

set3 = {"apple", "banana", "cherry"}

for x in set3:
    print(x)


# *********************************************************
print()
# *********************************************************

set3 = {"apple", "banana", "cherry"}

print("cherry" in set3)
print("appple" in set3)

# *********************************************************
print()
# *********************************************************

set4 = {"apple", "banana", "cherry"}

set4.add("orange")
set4.add("FG")

print(set4)

# *********************************************************
print()
# *********************************************************

set5 = {"apple", "banana", "cherry"}

set5.update(["orange", "mango", "grapes"])

print(set5)
print(len(set5))

set5.remove("banana") # remove() kaldırlıcak öge yoksa hata verir.
print(len(set5))

set5.discard("banana") # .discard() kaldırılacak öge yoksa sorun yapmaz.
print(len(set5))

set5.discard("mango")
print(len(set5))

# *********************************************************
print()
# *********************************************************

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()   # Note: Sets are unordered, 
                    # so when using the pop() method, 
                    # you will not know which item that gets removed.

print(x) #removed item

print(thisset) #the set after removal

# You can also use the pop(), method to remove an item, 
# but this method will remove the last item. 
# Remember that sets are unordered, 
# so you will not know what item that gets removed.

# The return value of the pop() method is the removed item.

# *********************************************************
print()
# *********************************************************

thisset = {"apple", "banana", "cherry"}

thisset.clear()  # The clear() method empties the set:

print(thisset)

# *********************************************************
print()
# *********************************************************

# thisset1 = {"apple", "banana", "cherry"}

# del thisset1  # The del keyword will delete the set completely:

# print(thisset1)


# *********************************************************
print()
# *********************************************************

set1 = {"a", "b","c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
set4 = set1.update(set2)
print(set3)
print(set4)

# Note: Both union() and update() will exclude any duplicate items.

# *********************************************************
print()
# *********************************************************

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# *********************************************************
print()
# *********************************************************

# line = 10
# print()
# for i in range(line):
#     print(' '*16+' '*19+'*'*12+' '*7+'*'*12+' '*7+'*'*(line-1-i)+'*'*(3*i+1))
# for i in range(line*2-7):
#     print(' '*(line+5-i)+'*'*(i+1)+'*'*12+' '*7+'*'*12+' '*7+'*'*12+' '*7+'*'*12)
# for i in range(5):
#     print(' '*16+'*'*19+'*'*19+'*'*12+' '*7+'*'*12)


# *********************************************************
print()
# *********************************************************




