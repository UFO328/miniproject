from function import penjumlahan,perkalian,pengurangan,pembagian

while True:
    print("pilih operator aritmatika")
    print("+")
    print("*")
    print("-")
    print("/")
    
    user = input("masukan operator +,*,-,/. :")
    num1 = int(input("masukan angka : "))
    num2 = int(input("masukan angka : "))

    if user == "+":
        hasil = penjumlahan(num1,num2)
        print(f"hasil {num1} + {num2} = {hasil}")
    elif user == "*":
        hasil = perkalian(num1,num2)
        print(f"hasil {num1} * {num2} = {hasil}")
    elif user == "-":
        hasil = pengurangan(num1,num2)
        print(f"hasil {num1} - {num2} = {hasil}")
    elif user == "/":
        hasil  = pembagian(num1,num2)
        print(f"hasil {num1} / {num2} = {hasil}")


    
    

