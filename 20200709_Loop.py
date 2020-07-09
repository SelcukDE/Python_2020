names = ["susan", "tom", "edward"]
mood = ["happy", "sad"]

if i in names:
    if ii in mood:
        print(i + "is" + ii)



print()
# ****************************************************

evens = []     # evens  
odds =  []  # odds 

for i in range(11):
    if i % 2 == 0:
        evens.append(i)
    else:
        odds.append(i)

print("evens :", evens)
print("odds :", evens)


# ****************************************************
print()


text = ['one', 'two', 'three','four', 'five']
numbers = [1, 2, 3, 4, 5, 6, 7]
# numbers = [range(7)] ---çalışmadı

for x, y in zip(text, numbers):
    print(x, ":", y)

# ****************************************************
print()
print()

print(*("separete"))

print(*range(10,0,-2))
print(*range(10,1,-2))
print(*range(3,0,-2))
print(*range(8,0,-2))

print(*range(5, 25, 2))

# ****************************************************
print()
# print()
    

# number = int(input("enter a number between 1-10: "))


# for i in range(11):
#     print("{}x{} = ".format(number, i), number * i)

# ****************************************************
print()
print()

print()

print()
print()
print()
# ****************************************************

listem = (11, 2, 24, 61, 48, 33, 3)

odds = 0
evens = 0

if i in listem:
    if not i % 2:
        evens+=1
    else:
        odds+=1

print("The number of even (çift) numbers: ", evens)
print("The number of odd (tek) numbers: ", odds)

# ****************************************************
print()
print()
# ****************************************************

for i in range(1, 10):
    print(str(i) * i)

# ****************************************************
print()

# names = ["susan", "tom", "edward"]
# mood = ["happy", "sad"]

# if i in names:
#     if ii in mood:
#         print(i + "is" + ii)



# ****************************************************



