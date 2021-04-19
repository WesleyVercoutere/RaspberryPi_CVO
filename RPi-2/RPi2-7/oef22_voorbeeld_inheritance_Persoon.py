class Persoon():

    aantal_personen = 0

    def __init__(self, leeftijd= None, lengte = None, gewicht= None , naam = None, voornaam = None):
        self.leeftijd = leeftijd
        self.lengte = lengte
        self.gewicht = gewicht
        self.naam = naam
        self.voornaam = voornaam

class Leraar(Persoon):
    pass

class Leerling(Persoon):
    pass

wim = Leraar()

koen = Leerling()

print(wim.__dict__)

# method look up by python!