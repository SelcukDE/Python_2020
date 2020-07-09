name = input("What is your name?: ").title().strip()

if name == "Joseph":
    # message = "Hello, {name1}! The password is: W@12".format(name1 = name)
    print("Hello, {name1}! The password is: W@12".format(name1 = name))

elif name == "Mark":
    print("Hello, {name1}! The password is: fg2023".format(name1 = name))
  
else:
    print("Hello! {name1}! See you later.".format(name1 = name))