'''
• Een variabele naam mag slechts bestaan uit letters, cijfers, en “underscores” (_)
• A variabele naam moet beginnen met een letter of een underscore.
• A variabele naam mag geen gereserveerd woord zijn

• Programmeurs kiezen nooit een variabele naam die ook de naam is van een functie
(of het nu een standaard Python functie betreft of een functie die ze zelf hebben
geschreven). Als je dat doet, loop je de kans dat de functie niet langer door de code
gebruikt kan worden, wat kan leiden tot uitermate vreemde fouten.

• Programmeurs proberen variabele namen zo te kiezen dat ze betekenisvol zijn in
de context van het programma. Bijvoorbeeld, een variabele die het aantal seconden
in een week bijhoudt, zou de naam secs_per_week kunnen hebben, maar niet
ik_haat_mijn_baan. Het zou nog erger zijn om het aantal seconden in een week op
te slaan in een variabele secs_per_maand.

• Een uitzondering op het kiezen van betekenisvolle variabele namen is het kiezen
van namen voor “wegwerp variabelen,” dat wil zeggen, variabelen die slechts in een
klein deel van de code gebruikt worden, naderhand niet meer gebruikt worden, en
die van zichzelf eigenlijk geen betekenis hebben. Programmeurs kiezen vaak éénletter
namen voor dit soort variabelen, zoals i of j.

• Om verwarring tussen hoofd- en kleine letters te vermijden, gebruiken programmeurs
meestal alleen kleine letters in variabele namen.

• Als een variabele naam uit meerdere woorden bestaat, zetten programmeurs underscores
tussen die woorden.

• Programmeurs kiezen nooit variabele namen die beginnen met een underscore. Het
gebruik van dat soort namen is voorbehouden aan de auteurs van Python.

'''
pi = 3.14159265
straal = 7.5
hoogte = 8.25
volume_van_kegel = pi * straal * straal * hoogte / 3
print( volume_van_kegel )