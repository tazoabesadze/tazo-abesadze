# upper - ადიდებს სტრინგს(ასოს)


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



# გავაკეთოთ პროგრამა. მომხმარებელს სჰემოატანინეტ პაროლი იქამდე,
#  სანამ არ დაემთხვევა რეგისტრირებულ პაროლს, while და if else 
#   გამოყენებით


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




# word = [2,5,15]
# print(min(word))

# def numbers(nums):
#     result = 0

#     for i in nums:
#         result = result + i
#     return result

# print(numbers([1,2,3]))


# რომელი სიტყვაც მეტია 5-ზე დავმატოთ სიაში

# def str_list(string):
#     string_word = []

#     for i in string:
#         if len(i) > 5:
#             string_word.append(i)

#     return string_word

# names = ["giorgi", "tazo", "temo", "nika", "luka", "sopiko", "ramazi"]
# print(str_list(names))


 
# def even_nambers(number):
#     filter_nambers = []

#     for i in number:
#         if i % 2 == 0:
#             filter_nambers.append(i)

#     return filter_nambers

# filter_even_numbers = [1,2,3,4,5,6,7,8,9,10]
# print(even_nambers(filter_even_numbers))


# max(max_number)

# def number(num):
#     return max(num)

# num_list = [1,2,3,4,5,6,7,8,9,10]
# print(number(num_list))



# def number(num):
#     max_number = num[0]

#     for i in num:
#         if max_number < i:
#             max_number = i

#     return max_number

# num_list = [1,2,3,4,5,6,7,8,9,10]
# print(number(num_list))



# სტრინგების სია. გამოიტანოს სიიდან ისეთი სიტყვა რომელიც იწყება "ე"-ზე

# def str_list(string):
#     filter_string = []

#     for i in string:
#         if i[0] == "e":
#             filter_string.append(i)
#     return filter_string

# str = ["nika", "elene", "luka", "elisabedi", "temo"]
# print(str_list(str))




# გვექნება რიცხვების სია. გამოვიტანთ ახალ სიაში ამ რიცხვების კვადრატს

# def num_list(numbers):
#     x2_num_list = []

#     for i in numbers:
#         x2_num_list.append(i ** 2)
    
#     return x2_num_list
    
# list = [1,2,3,4,5]
# print(num_list(list))


# რიცხვების სია. და გამოვიტანთ იმ რიცხვების ჯამს, რომლებიც არიან 
# 10-ზე მეტი

# def num_list(number):
#     numbers_jami = 0

#     for i in number:
#         if i > 10:
#             numbers_jami = numbers_jami + i

#     return numbers_jami

# num = [1,2,3,14,9,16,15,7]
# print(num_list(num))


# შექმენით პროგრამა სადაც მომხმარებელს შემოატანინებთ თუ რამდენ 
#  რიცხვს შემოიტანენ სიაში. შემდეგ შექმენით სია, for ციკლში input-ით
#   შეეკითხეთ რიცხვი და შეიტანე სიაში. ბოლოს დააბრუნეთ სიის ჯამი

# def filter_evens(numbers):
#     filtered_list = []

#     for num in numbers:
#         if num > 10 and num % 2 == 0:
#             filtered_list.append(num)

#     return filtered_list

# def sum_of_numbers(numbers):
#     sum = 0

#     for i in numbers:
#         sum = sum + i

#     return sum

# count = int(input("how many numbers do you want to input: "))

# numbers = []

# for i in range(count):
#     number = int(input("enter number: "))
#     numbers.append(number)

# print(sum_of_numbers(numbers))
# print(filter_evens(numbers))


#  -    -   -   -   -   >

# anbani = ["d", "a", "e", "g", "b", "f", "c"]

# anbani_sort = sorted(anbani)

# print(anbani_sort)


# number = [4,2,7,9,4,78,3,5,1,8,9,22343,5]

# number_srt = sorted(number)

# print(number_srt)


# a = ("h", "b", "a", "c", "f", "d", "e", "g")

# x = sorted(a, reverse=True)

# print(x)

# -   -   -   -   -   -   ->


# def user_name(name):
#     for i in range(name):
#         print("tazo")

# user_name(3)
# user_name(2)
# user_name(7)



# def numbers(num1, num2):
#     return num1 * num2

# print(numbers(5, 10))


# x = [1,2,3,4,5]
# x.append(7)
# print(x)




# my = ("my", "you", "then")

# x = " ".join(my)

# print(x)

# მომხმარებელს შეეკითხეთ საწყისი და საბოლოო რიცხვები. ეს რიცხვები
# გადაეცით ფუნქციას, for ციკლით სიაში შეინახეთ მათ შორის არსებული
# რიცხვები. შემდეგ მოახდინეთ გაფილტვრა, ისევ for ციკლით განიხილეთ
# თითოეული რიცხვი - თუ რიცხვი ლუწი იქნება, ახალ სიაში დაამატეთ
# მისი მეორე ხარისხი, ხოლო თუ კენტი იქნება სიაში დაამატეთ მისი
# კვადრატული ფესვი (0.5 ხარისხი).



# def numbers(num1, num2):
#     number_list = []
#     filtered_nums = []
    
#     for i in range(num1, num2):
#             number_list.append(i)

#     print(number_list)

#     for i in number_list:
#         if i % 2 == 0:
#                 filtered_nums.append(i ** 2)

#         else:
#               filtered_nums.append(i ** 0.5)

#     return filtered_nums

# num1 = int(input("enter a number 1:  "))
# num2 = int(input("enter a number 2:  "))

# result_list = numbers(num1, num2)
# print(result_list)



# number = [1,2,3,4,5,6,7]
# print(range(len(number)))

# შექმენით ფუნქცია, რომელსაც გადასცემთ მომხმარებლისგან მიღებულ
# სახელსა და გვარს. შემდეგ ისინი დაამატეთ სიაში და დააბრუნეთ სია.

#       <    - ?  - ?  - ?  -   >

# შექმენით ფუნქცია, რომელსაც გადაეცემა 1-იდან 20-ის ჩათვლით 
# რიცხვების სია. თქვენ უნდა დააბრუნოთ გაფილტრული სია, სადაც 
# უკვე მარტო 4-ის ჯერადები იქნება.

# def Multiples_of_4(namber):
#     filtered_list = []

#     for i in namber:
#         if i % 4 == 0:
#             filtered_list.append(i)

#     return filtered_list

# num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(Multiples_of_4(num))


# შექმენით ფუნქცია, რომელსაც გადასცემთ მომხმარებლის გვარს. გვარის 
# თითოეული ასო გადაიტანეთ ახალ სიაში. შემდეგ for ციკლის გამოყენებით
# იმუშავეთ ამ სიაზე - მარტო ლუწ ინდექსებზე მყოფი ასოები დაამატეთ 
# ახალ სიაში. საბოლოოდ დააბრუნეთ ეს სია. Bonus (არაა სავალდებულო):
# ეს სია გარდაქმენით სთრინგად და ამ სახით დააბრუნეთ.

# def person_surname(surname):
#     even_index_char = []

#     for i in range(len(surname)):
#         if i % 2 == 0:
#             even_index_char.append(surname[i])
    
#     return " ".join(even_index_char)

# surname = input("enter your surname: ")
# print(person_surname(surname))

# შექმენით ფუნქცია, რომელსაც გადაეცემა რიცხვების სია. თქვენ უნდა
# დააბრუნოთ ამ სიის საშუალო არითმეტიკული ( ჯამი / სიგრძე )



# def opposite(number):
#     return -1 * number

# print(opposite(4))



# b = "tazo, nika!"
# print(b[0:2])

# a = "tazo!"
# print(a[0:2])

# b = "nika!"
# print(b[0:2])

# print(a[0:2] + b[0:2])

# b = "Hello, World!"
# print(b[-4:-2])

# a = "tazo abesadze."

# print(a[-5:-1])


# მოვძებნოთ ყველაზე პატარა ინტეჯერი სიაში

# 1 ხერხი

# def int_word(integer):
#     word_list = integer[0]

#     for i in integer:
#         if word_list > i:
#             word_list = i

#     return word_list

# num_list = [7,4,33,89,34,99,105,2668]
# print(int_word(num_list))


# 2 ხერხი

# def int_word(integer):
#     return min(integer)

# int_list = [8,44,33,7,9,789]
# print(int_word(int_list))



# def no_space(x):
#     return x.replace(" ","")

# print(no_space("tazo abesaze"))


# მოვაშოროთ სტრინგიდან სფეისები

# def no_space(str):
#     str_list = ""

#     for i in str:
#         if i != " ":
#             str_list += i

#     return str_list

# list = "me var tazo abesadze"
# print(no_space(list))



# print(bool(5 == 5))



# ფუნქცია რომელიც მიიღებს რიცხვების სიას და დააბრუნებს ამ რიცხვების
# ჯამს

# def number_list(number):
#     sum_of_numbers = 0

#     for i in number:
#         sum_of_numbers += i 

#     return sum_of_numbers

# n_list = [1,2,3]
# print(number_list(n_list))



# print("a". upper())

# name = "tazo"
# print(name.upper())


# upper - ადიდებს სტრინგს(ასოს)
# name = "tazo"
# print(name.upper())


# split - გახლეჩვა
# print("tazo abesadze".split(" "))





# def start_end_numbers(start_num, end_num):
#     filtered_num = []
    
#     for i in range(start_num, end_num):
#         if i % 2 == 0:
#             filtered_num.append(i ** 2)
#         else:
#             filtered_num.append(i ** 0.5)

#     return filtered_num

# start_num = int(input("enter first number: "))
# end_num = int(input("enter end number: "))

# result_list = start_end_numbers(start_num, end_num)
# print(result_list)



# num = [1,2,3]
# i = int(input("enter a number: "))
# num.append(i)
# print(num[-2])




# x = []

# for i in range(20, 40):
#     x.append(i)
#     print(i)




# num1 = int(input("enter num 1:  "))
# num2 = int(input("enter num 2:  "))

# for i in range(num1, num2):
#     if i % 5 == 0:
#         print(i)



# a = [1,2,3,4,5]
# print(a[::-1])




