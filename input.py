from konversi import fahrenheit,kelvin

userinput = float(input("masukan suhu dalam fahrenheit : "))
result = fahrenheit(userinput)
print(f"suhu dalam kelvin adalah : {result}")

userinput = float(input("masukan suhu dalam kelvin : "))
hasil= kelvin(userinput)
print(f"suhu dalam fahrenheit adalah : {hasil}")