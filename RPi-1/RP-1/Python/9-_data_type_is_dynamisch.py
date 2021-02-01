# In tegenstelling tot C/ C++ waar je moet kiezen welk datatype je variabele heeft is dit in python dynamisch

# test met run/debug faster / step into

a= 10
print(type(a))

a= 50.48
print(type(a))

a= "CVO"
print(type(a))

a= True
print(type(a))

#  opnieuw maar nu printen van de geheugenlocatie van a

a= 10
print("1>",id(a))   # print( , , , , )  Je kan meerdere constanten of variabelen  tusen de haakjes plaatsen, wel scheiden door comma's

a= 50.48
print("2>",id(a))

a= "CVO"
print("3>",id(a))

a= True
print("4>",id(a))


# Wat besluit je uit de 4 print resultaten?  Wat gebeurt er precies wanneer je een variabele wijzigt?  Immutable betekent?

# Zijn deze basic data types onveranderbaar (immutable)?