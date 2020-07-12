# Assignment - 3 (Is it Armstrong Number?)

while True:
    number = int("enter a positiv number: ")
    digits = len(number)

    if not number.isdigit() :
        print(number, "It is an invalid entry. Do not use non-numeric, float, or negative values!")
    elif int(number) >= 0 :
        for i in range (digits):
            summ += int(number [i]) ** digits
        if summ == int(number):
            print(number, "is an Armstrong number.")
            break
        else:
            print(number, "is not an Armstrong number.")
            break



# Assignment (Prime Number) Asal Sayılar

n = int(input("enter : "))

count = 0

for i in range(1, n+1) :
    if not (n % i) : count += 1

if (n == 0) or (n == 1) or (count >=3) : print(n, "is not a prime number.")
else : print(n, "is a prime number")


# Assignment - 5 (Fibonacci Numbers)

fibo = []

for i in range(-2, 8) :
    if i < 0 : fibo.append(1)
    else : fibo.append(fibo[i] + fibo[i+1])

print(fibo)

# Kalfalık Soruları....

# A sample of filter() funtion


# Ternary conditionals

# list comprehension


[i for i in "clarusway"]