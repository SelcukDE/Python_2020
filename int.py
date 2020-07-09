number = int(input("Enter an integer value: "))

if number %7 == 0 and number %3 == 0:
    print("Yes, this number satisfies the rules. ")

elif number %7 == 0 and number %3 != 0:
    print("Tis number can be divided to 7.")

else:
    print("No, this number does not satisfies the rules.")