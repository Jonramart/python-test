temperatura = float(input("ingrese temperatura a convertir:"))
#print(temperatura)
#floatTemp = float(temperatura)
conversion = input("Es Fahrenheit(F) o Celsius (C):").upper()
if conversion == "F":
    #print((temperatura - 32) * 5/9 ," ", "Grados Celsius")
    celsius = (temperatura-32) *5/9
    print(celsius," ", "Grados Celsius")
elif conversion == "C":
    #fahrenheit = temperatura * 1.8 + 32
    #print(fahrenheit, " ", "Grados Farentheit" )
    print(temperatura +1.8 + 32, " ", "Grados Fahrentheit" )
else:
    print(temperatura," ", "Son grados Kelvin")
