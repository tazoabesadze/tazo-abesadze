# დაწერეთ პროგრამა, რომელიც ბეჭდავს კვირის დღეს მომხმარებლის 
# მიერ შეყვანილი რიცხვის საფუძველზე (1 ორშაბათისთვის, 2 
# სამშაბათისთვის და ა.შ.) if, elif და სხვა გამოყენებით.

print("Monday", "Tuesday", "Wednesday", "Thursday", 
"Friday", "Saturday", "Sunday")

person_choice = int(input("Choose a weekday: "))

if person_choice == 1:
    print("Monday")

elif person_choice == 2:
    print("Tuesday")

elif person_choice == 3:
    print("Wednesday")

elif person_choice == 4:
    print("Thursday")

elif person_choice == 5:
    print("Friday")

elif person_choice == 6:
    print("Saturday")

elif person_choice == 7:
    print("Sunday")
else:
    print("Its a wrong choice")