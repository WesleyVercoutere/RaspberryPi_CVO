#  UTF-8 is a variable-width character encoding used for electronic communication

# zie bv https://www.css-voorbeelden.nl/artikelen/lijsten/artikelen-063.html

print("\u2706")

print("\u20ac")

print("\u0030")

####################################

a= b"test"

print("a is een byte string >",a)


byte_string = b"\x43\x56\x4f"  # zie ascii table > https://simple.wikipedia.org/wiki/ASCII

print("byte_string=",byte_string)

#######################################

dec_a= a.decode('utf8')

print("na decoderen krijgen we een gewone utf8 string>",dec_a)

######################################

byte_str= dec_a.encode('utf8')

print("na encoderen hebben we terug een byte string > ",byte_str)

# zenden via UART of SOCKET in byte formaat, dus strings eerst encoderen met encode functie

# na ontvangen via UART of SOCKET omzetten in gewone utf-8 string via decode functie




