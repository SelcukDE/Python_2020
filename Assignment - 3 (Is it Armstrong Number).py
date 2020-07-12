# takes a positive integer number from the user,
# checks the entered number if it is Armstrong,
# consider the negative, float and any entries 
# other than numeric values then display a warning message to the user.

# 371 = 3**3 + 7**3 + 1**3;
# 9474 = 9**4 + 4**4 + 7**4 + 4**4;
# 93084 = 9**5 + 3**5 + 0**5 + 8**5 + 4**5;

sayı = int(input('To find out if a number is "Armstrong Number" enter a number: '))

toplam = 0

x = sayı

while x > 0 :
    rakam = x % 10
    toplam += rakam **3
    x //= 10

if sayı == toplam:
    print(sayı, "is an Armstrong number")
else:
    print(sayı, "is not an Armstrong number")