# age =  can be assigned only True/False
# chronic =  can be assigned only True/False
# immune =  can be assigned only True/False
# risk = ?

age = str(input("Are you a cigarette addict older than 75 years old?: (Yes/No)")).title().strip()
chronic = str(input("Do you have a severe chronic disease? (Yes/No)")).title().strip()
immune = str(input("Is your immune system too weak?? (Yes/No)")).title().strip()

risk = age or chronic or immune

if risk == "Yes":
    print("there is a risk of death.")
else:
    print("there is not a risk of death")