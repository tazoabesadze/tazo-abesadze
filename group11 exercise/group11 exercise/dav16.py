# დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს რიცხვს და 
# ბეჭდავს არის თუ არა ეს რიცხვი დადებითი, უარყოფითი ან ნულოვანი.

input_num = int(input("enter a number:  "))

if input_num < 0:
    print("is less than zero")

elif input_num == 0:
    print("is equal to zero")

else:
    print("is greater than zero")