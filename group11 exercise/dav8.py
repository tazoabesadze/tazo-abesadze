age = int(input("enter your age:  "))

if age <= 12:
    print("You are little")
elif age >= 13 and age <=18:
    print("You are a teenager")
elif age >= 19 and age <= 30:
    print("You are a free person")
elif age >= 31 and age <= 45:
    print("You are working on a serious business")
elif age >= 46 and age <= 60:
    print("Your hair is turning gray")
else:
    print("You are old")