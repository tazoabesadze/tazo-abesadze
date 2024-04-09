# for i in range(1, 100):
#     if i % 2 == 0:
#         print(str(i) + " luwia")
#     else:
#         print(str(i) + " kentia")


#   gavaketot kalkulatori -->

# def edition(x, y):
#     return x + y

# print(edition(6, 3))

# def edition(x, y):
#     return x - y

# print(edition(6, 3))

# def edition(x, y):
#     return x * y

# print(edition(6, 3))

# def edition(x, y):
#     return x / y

# print(edition(6, 3))



#   გავაკეთოთ პროგრამა. მომხმარებელს სჰემოატანინეტ პაროლი იქამდე, სანამ არ დაემთხვევა რეგისტრირებულ პაროლს, while და if else გამოყენებით


# password = "tazo123"

# while True:
#     input_password = input("enter your password: ")

#     if password == input_password:
#         print("successfuly logged in")
#         break
#     else:
#         print("incorrect password ")
#         try_again = input("try_agein? (yes or no): ")
#         if try_again == "no":
#           break
#         print("invalid input")



#    araperi  -->

# password = "tazo123"

# while True:
#     passwordinput = input("enter password: ")

#     if passwordinput == password:
#         print("the password is correct")
#         break

#     else:
#         print("the password is incorrect, try again")




#   დაწერე პროგრამა რომელიც გამოიტანს რიცხვებს 1იდან 10ამდე while ციკლის გამოყენებით


# num = 0
# while num <= 10:
#     print(num)
#     num += 1

#  while ციკლის მეშვეობით შეამოწმე რიცხვები 1 დან 20 ჩათვლით. რიცხვი თუ იყოფა 3 და 5 ზე მაშინ დაპრინტე ეგ რიცხვი 

# i = 1
# while i <= 20:
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)
#     i += 1


#    --->


# შექმენით ფუნქცია, რომელიც მიიღებს მომხმარებლისგან სიტყვას. შემდეგ თქვენ უნდა მოახდინოთ ამ სიტყვის შებრუნება, 
# მაგ: word - drow. საბოლოდ კი დააბრუნეთ შედეგი.

# def word(name):
#     return name[::-1]

# print(word("tazo"))



# def numbesr(number):
#     return number ** 3

# print(numbesr(5))



# def numbesr(number):
#     return number * 2

# print(numbesr(5))



# def num(number):
#     if number % 2 == 0:
#         print("tazo")
#     else:
#         print(number)

# print(num(int(input("enter a number:  "))))

# --------->>>>-------->>>>>>>>>

# დაპრინტეთ გოას ფასები:
# კვირაში 1-ხელ 190 ლარი
# კვირაში 2-ჯერ 290 ლარი
# კვირაში 3-ჯერ 390 ლარი
# და გამოთვალეთ მაგაზე 20% ფასდაკლება. და ლამაზად დაპრინტეთ


# tax1 = 190
# discount = 30
# tax1_discount1 = tax1 - tax1 * discount / 100

# tax2 = 290
# discount = 30
# tax2_discount2 = tax2 - tax2 * discount / 100

# tax3 = 390
# discount = 30
# tax3_discount3 = tax3 - tax3 * discount / 100

# print(tax1)
# print(tax2)
# print(tax3)

# print(tax1_discount1)
# print(tax2_discount2)
# print(tax3_discount3)


# შექმენით ფუნქცია, რომელიც მომხმარებელს შეეკითხება რიცხვს,
#ხოლო დაუპრინტავს ამ რიცხვზე 3-ჯერ დიდ რიცხვს.

# num = int(input("enter a number: "))
# num = num * 3

# print(num)



# def say_hi(user_name):
#     print("gamarjoba " + user_name)

# say_hi(input("enter your name: "))




# num1 = int(input("plearse enter start value: "))
# num2 = int(input("plearse enter end value: "))

# result = 0

# for num in range(num1, num2 + 1):
#     result =  result + num
#     print(num)

# print(result)


# -------->>>>>>>>>>>------------>>>>>>


# შექმრნით სარეგიატრაციო ფორმა. რეგისტრაცია და ლოგინი!   -->
# მოვთხოვოთ: სახელი, გვარი, მეილი და პაროლი.

# while True:

#     print("1. sign up")
#     print("2. login up")
#     print("3. exit")

#     person_choice = int(input("please enter your choise:  "))

#     if person_choice == 1:
#         print("sing up page")
#         enter_name = input("enter your name:  ")
#         enter_surname = input("enter your surname:  ")
#         enter_gmail =  input("enter your gmail:  ")
#         enter_password = input("enter your password:  ")
#         enter_password2 = input("enter your password egain:  ")

#         if enter_password == enter_password2:
#             print("You are logged in to the account")
#         else:
#             print("You could not log in to your account")

#     if person_choice == 2:
#         print("login up")

#         input_name = input("enter your name:  ")
#         input_gmail = input("enter your gmil:  ")
#         input_password = input("enter your password:  ")

#         if input_name == enter_name and input_password == enter_password and input_gmail == enter_gmail:
#             print("You have registered")
#         else:
#             print("You failed to register")

#     if person_choice == 3:
#         print("EXIT. Thank you for using our service")
#     else:
#         print("Invalid digit")
#     break


#   - - - - - - - -> 

# for i in range(0, 20, 2):
#     print(i)


# sum = 0

# for i in range(11):
#     sum += i

# print(sum)




# for i in "hallo world":
#     print(i)


# for i in "hallo world":
#     print(i, end="")


#     წ ლ ო ვ ა ნ ე ბ ე ბ ი  --=>

# age = int(input("please enter your age: "))

# if age < 0:
#     print("this age doesn't exist")
# elif age <= 10:
#     print("you are a child")
# elif age < 20:
#     print("you are a teen")
# elif age >= 20 and age < 35:
#     print("You are a fully formed person")
# elif age >= 36 and age <= 60:
#     print("Your hair is turning gray")
# else:
#     print("You are old")


# ----->>>>>>>>>>>>>>>

# def hi(name):
#     print("gamaarjoba " + name)

# hi(input("enter name:  "))



# def num(number):
#     print(number * 3)

# num(6)
# num(7)
# num(2)



# print("Please select which action you want")
# print("addition, subtraction, multiplication, division")

# user = input("Enter your chosen action: ")

# print("You have selected the action Add")

# num = int(input(" please enter number : "))
# num1 = int(input(" plese enter second number : "))

# print("You have selected to add a behavior")

# if user == "addition":
#     print(num + num1)
# elif user == "subtraction":
#     print(num - num1)
# elif user == "multiplication":
#     print(num * num1)
# elif user == "division":
#     print(num / num1)
# else:
#     print("is wrong")



# def luwi_ricxvi(number_list):
#     for i in range(len(number_list) -1, -1, -1):
#         if number_list[i] % 2 == 0:
#             return number_list[i]
        
# print(luwi_ricxvi([1,2,3,4,5]))


# 1) შექმენით პროგრამა, სადაც ბოლოდან პირველ 2-ის 
# ჯერად რიცხვს გამოიტანთ სიიდან. მაგ სიაში კი 
# 0-დან 10-ის ჩათვლით უნდა იყოს რიცხვები.

# numbers = []

# for i in range(10, 50 + 1):
#     numbers.append(i)


# def oris_jeradebi(numbers):
#     for index in range(len(numbers) - 1, -1, -1):
#         if numbers[index] % 4 == 0:
#             return numbers[index]
        
# print(oris_jeradebi(numbers))



# nums = []

# for i in range(21):
#     nums.append(i)

# print(nums)




# word = [2,5,15]
# print(min(word))



