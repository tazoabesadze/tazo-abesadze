# while loopis meshveobit gamoitane ricxvebi 1-dan 20-is chatvlit
# აქიდან ამოიგებ ისეთ რიცხვს რომელიც ჯერ იყოფა 3ზე 5 ერთიანად 
# მერე ამოიგებ ისეთ რიცხვებს რომელიც იყოფა 9ზე

number = 1

while number < 21:
    if number %3 == 0 or number %5 == 0 or number %9 == 0:
        print(number)
    number += 1