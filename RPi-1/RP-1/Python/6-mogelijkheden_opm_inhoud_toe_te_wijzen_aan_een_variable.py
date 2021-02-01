# een constante toe wijzen

a= 3.14

# een andere variable toewijzen

b=a

# een expressie toewijzen

c=9*a+3

# je mag de variabele zelf opnieuw gebruiken

d=2

d=d+5 # wat geeft print(d)  

# de input methode gebruiken

d=input("Hoe oud ben je? >")

print("Je bent", d, "jaar oud")

# Wat wordt er geprint?
x = 2
y = 3
print( "x =", x )
print( "y =", y )
print( "x * y =", x * y )
print( "x + y =", x + y )

# Wat wordt er geprint?
y = 5
print( y )
y = 7 * 9 + 13 # overschrijft de vorige waarde van x
print( y )
y = "En nu iets heel anders..."
print( y )
y = int( 15 / 4 ) - 27
print( y )

# verwissel inhoud van variabelen
x = 2
y = 3
print( "x =", x, "en y =", y )
# Verwissel de waardes van x en y via z
z = x
x = y
y = z
print( "x =", x, "en y =", y )

# wat doet
x,y = y,x