lenguajes =["Python","Ruby","PHP","Javascript", "Java"]
lenguajes.insert(3,"Go")
lenguajes.insert(0,"C")
lenguajes.remove("Ruby")
#Validar si un valor existe en la lista
print("PHP" in lenguajes)#Manda True
print("Kotlin" in lenguajes)#Manda False
#lenguajes.clear() #limpia los valores de una lista y regresa []
print(len(lenguajes))

print(lenguajes)