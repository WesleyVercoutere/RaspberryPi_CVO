# oefeningen if else elif OPGELET geen loops gebruiken als je die reeds kent...
"""
# oef1 ) vraag de gebruiker 2 getallen en zeg hem daarna of het eerste of tweede getal het grootste was of zeg hem dat ze gelijk waren.
getal1=int(input('geef  getal1 in>='))
getal2=int(input('geef getal2 in>='))
if getal1>=getal2:
    print('getal1 is groter dan getal2')
elif getal1<getal2:
    print('getal2 is groter dan getal1')    
else:
    print('de getallen zijn gelijk')

"""
# oef2 ) vraag de gebruiker zijn punten op 100 voor wiskunde, nederlands en geschiedenis. Bereken en geef het gemiddelde aan de verbuiker en zeg de gebruiker of hij
# onvoldoende ( <60) , voldoende ( >==60) , onderscheiding ( >==70) , grote onderscheiding ( >==80) of grootste onderscheiding ( >==90) behaalde
"""
wiskunde=int(input("Geef uw punten voor wiskunde aub>="))
nederlands=int(input("Geef uw punten voor nederlands aub>="))
geschiedenis=int(input("Geef uw punten voor geschiedenis aub>="))
gemiddelde = (wiskunde + nederlands +geschiedenis)/3

if gemiddelde >== 90 :
    resultaat="Grootste onderscheiding"
elif gemiddelde >== 80 :
    resultaat="Grote onderscheiding"
elif gemiddelde >== 70 :
    resultaat="Onderscheiding"
elif gemiddelde >== 60 :
    resultaat="Voldoende"
else:
    resultaat="Onvoldoende"

print("Uw gemiddelde is", round(gemiddelde,1))
print("Uw resultaat is",resultaat)

"""
"""
#oef3 vraag de gebruiker om een geheel getal in te vullen en zeg hem dan of dit getal even of oneven was.
getal=int(input('Geef een geheel getal aub>='))
if getal%2==0:
    print('even')
else:
    print('oneven')
    

    
"""

"""
#oef4 vraag de gebruiker om een geheel getal in te geven van 3 cijfers, zeg de gebruiker dat het te groot of te klein is indien hij minder of meer dan 3 cijfers ingeeft.
# check of het getal dat ingegeven is cijfers heeft die van klein naar groot staan,  print "Ja, kleine naar grote cijfers" of "Nee, geen kleine naar grote cijfers"
# vb 189 Ja, 198 Nee,  891 nee...
getal=int(input("Geef een getal van 3 cijfers aub>="))

if getal >= 999 :
    print=('getal is te groot')
elif getal < 100 :
    print=('getal is te klein')
else:
    cijfer1= getal // 100
    cijfer2= (getal - cijfer1 * 100) //10 
    cijfer3= getal - cijfer1 * 100 - cijfer2 * 10
    if cijfer1 < cijfer2 and cijfer2 < cijfer3:
        print ("Ja, kleine naar grote cijfers")
    else:
        print("Nee, geen kleine naar grote cijfers")      

 """



#oef5 vraag de gebruiker zijn punten op 100 voor wiskunde, nederlands en geschiedenis. Bereken en geef het gemiddelde aan de verbuiker en zeg de gebruiker of hij
# onvoldoende ( <60) , voldoende ( >==60) , onderscheiding ( >==70) , grote onderscheiding ( >==80) of grootste onderscheiding ( >==90) behaalde.
# indien max 1 onvoldoende en niet lager dan 40 % wordt de student gedelibereerd
# indien meer dan 1 onvoldoende of een onvoldoende lager dan 40 % dan jaar over doen. Print de juiste beslissing naar de gebruiker

"""
wiskunde=int(input("Geef uw punten voor wiskunde aub>="))
nederlands=int(input("Geef uw punten voor nederlands aub>="))
geschiedenis=int(input("Geef uw punten voor geschiedenis aub>="))
gemiddelde = (wiskunde + nederlands +geschiedenis)/3

if gemiddelde >== 90 :
    resultaat="Grootste onderscheiding"
elif gemiddelde >== 80 :
    resultaat="Grote onderscheiding"
elif gemiddelde >== 70 :
    resultaat="Onderscheiding"
elif gemiddelde >== 60 :
    resultaat="Voldoende"
else:
    resultaat="Onvoldoende"
    
teller_onvoldoende_60=0
if wiskunde < 60: teller_onvoldoende_60+=1
if nederlands < 60: teller_onvoldoende_60+=1
if geschiedenis < 60: teller_onvoldoende_60+=1


teller_onvoldoende_40=0
if wiskunde < 40: teller_onvoldoende_40+=1
if nederlands < 40: teller_onvoldoende_40+=1
if geschiedenis < 40: teller_onvoldoende_40+=1




if teller_onvoldoende_60 >= 1 or teller_onvoldoende_40 >=0:
    print('Jaar overdoen!')
else:
    print('Wordt gedelibereerd!')    

"""
"""
#oef6 Je programma krijgt als input een jaartal. Als dat jaar een schrikkeljaar is print het programma "SCHRIKKELJAAR" anders print het  "GEEN SCHRIKKELJAAR".
#De regels hiervoor zijn als volgt:
#een jaar is een schrikkeljaar als dit getal exact deelbaar is door vier, maar niet deelbaar door 100,
#een jaar is altijd een schrikkeljaar als het exact deelbaar is door 400.
jaartal = int(input('Geef een jaartal op'))

if (jaartal % 4 == 0 and jaartal % 100 !=0 ) or jaartal % 400 ==0:
    print('SCHRIKKELJAAR')
else :
    print('GEEN SCHRIKKELJAAR')
 """
"""
#oef7 vraag de gebruiker 3 gehele getallen en print ze in dalende volgorde.
getal1=int(input('Geef een geheel getal op'))
getal2=int(input('Geef een geheel getal op'))
getal3=int(input('Geef een geheel getal op'))

if getal1 >= getal2 >= getal3 :
    print(getal1,getal2,getal3)
elif getal1 >= getal3 >= getal2 :
    print(getal1,getal3,getal2)
elif getal2 >= getal1 >= getal3 :
    print(getal2,getal1,getal3)
elif getal2 >= getal3 >= getal1 :
    print(getal2,getal3,getal1)
elif getal3 >= getal2 >= getal1 :
    print(getal3,getal2,getal1)
#elif getal3 >= getal1 >= getal2 :
else:
    print(getal3,getal1,getal2)
"""
"""
#oef8 vraag de gebruiker een maand in 2019 in te geven bv januari, print dan "het aantal dagen in januari is 31."
maand = input('Geef een maand op aub>= ')

if maand == "januari" or maand == "maart" or maand == "mei" or maand == "juli" or maand == "augustus" or maand == "oktober" or maand == "december" :
    print(maand,'heeft 31 dagen')
elif maand == "februari" :
    print( maand, 'heeft 28 dagen')
elif maand == "april" or maand == "juni" or maand == "september" or maand == "november":
    print(maand,'heeft 30 dagen')
else:
    print('Uw invor werd niet herkend')   

 """   

"""
#oef9 vraag de gebruiker 3 gehele getallen, print daarna hoeveel getallen er gelijk zijn aan elkaar. ( 0,2 of 3 )
getal1 = int(input('geef een geheel getal op'))
getal2 = int(input('geef een geheel getal op'))
getal3 = int(input('geef een geheel getal op'))

if getal1 == getal2 == getal3 :
    print('De getallen zijn alle drie gelijk aan elkaar')
elif getal1 == getal2 or getal1 == getal3 or getal2 == getal3 :
    print('Er zijn twee getallen gelijk aan elkaar')
else :
    print('Er zijn geen getallen gelijk aan elkaar')
"""  

#oef 10 vraag de gebruiker een karakter in te typen, print daarna of dit een kleine letter, hoofdletter, cijfer of ander karakter is.
# Gebruik hiervoor de asci tabel en de methode ord()  vb ord("a")=97  ord("A")=65  ord("0")=48
"""

ascii_waarde = ord(input('geef een karakter op aub >= '))

print("ascii waarde = ", ascii_waarde)

if ascii_waarde>= 48 and ascii_waarde <=57 :
    print('Dit is een cijfer')
elif ascii_waarde>= 97 and ascii_waarde <=122 :
    print('Dit is een kleine letter')
elif ascii_waarde>= 65 and ascii_waarde <=90:
    print('Dit is een hoofdletter')
else:
    print('Dit is een teken')
    
"""
    

#oef 11 vraag de gebruiker een letter uit het alfabet in te typen, print daarna of dit een klinker of medeklinker is.
letter = input('Geef een letter in aub >= ')
 
if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" :
     print('Deze letter is een klinker')
else:
#elif letter == [b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, z] :
    print('Deze letter is een medeklinker')






