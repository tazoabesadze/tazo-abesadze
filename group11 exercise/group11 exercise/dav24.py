# input-ით შეეკითხეთ მომხმარებელს რაიმე რიცხვი 
# 1-იდან 100-ის ჩათვლით, და შემდეგ for ციკლის
# გამოყენებით გამოიტანეთ 100-იდან მაგ რიცხვამდე 
# ლუწი რიცხვები (თუ მომხმარებელმა შეიყვანა 1-ზე 
# ნაკლები ან 100-ზე მეტი რიცხვი if elif else-ის 
# გამოყენებით უთხარით რომ 1-100-ამდე უნდა 
# ჩაწეროს რიცხვი)

input_number = int(input("chawere ricxvi 1-dan 100-is chatvlit:  "))

if input_number > 100:
    print("error")
elif input_number < 1:
    print("error")
else:
    for i in range(100, input_number, -1):
        if i % 2 == 0:
            print(i)