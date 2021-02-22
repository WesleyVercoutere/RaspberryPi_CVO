print(dir())  # __builtins__  maar print functie niet in de namespace?

# pyton  checkt local scope, enclosing scope, global scope en tenslotte de builtins daarna een error indien niet gevonden!


#print()

print(dir(__builtins__))