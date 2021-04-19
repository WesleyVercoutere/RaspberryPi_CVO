class Persoon():

    aantal_personen = 0

    def __init__(self, leeftijd= None, lengte = None, gewicht= None , naam = None, voornaam = None):
        self.leeftijd = leeftijd
        self.lengte = lengte
        self.gewicht = gewicht
        self.naam = naam
        self.voornaam = voornaam

    def bezig_zijn(self):
        print("ik werk")


class Leraar(Persoon):

    def bezig_zijn(self):
        print("ik geef les")


class Leerling(Persoon):

    def bezig_zijn(self):
        print("ik studeer")


wim = Leraar()
koen = Leerling()

print(wim.__dict__)

# method overriding!

wim.bezig_zijn()
koen.bezig_zijn()