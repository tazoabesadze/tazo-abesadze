# გააკეთეთ კალკულატორი, მომხმარებელმა უნდა აირჩიოს რომელი მოქმედება უნდა: 
# მიმატება, გამოკლება, გამრავლება, გაყოფა

# multiplication, division, addition, deduction

num = int(input("please enter first number:  "))
num1 = int(input("please enter second number:  "))

print("please enter one")
print("multiplication")
print("division")
print("addition")
print("deduction")

while True:

    choise = input("Please choose one: ")

    if choise == "1":
        print(num * num1)
        break
    elif choise == "2":
        print(num / num1)
        break
    elif choise == "3":
        print(num + num1)
        break
    elif choise == "4":
        print(num - num1)
        break
    else:
        print("It's a wrong choice")
