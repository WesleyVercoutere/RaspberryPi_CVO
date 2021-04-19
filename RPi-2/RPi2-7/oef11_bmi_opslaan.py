class Persoon:

    def __init__(self, gewicht , lengte , leeftijd):
        self.gewicht = gewicht
        self.lengte = lengte
        self.leeftijd = leeftijd
        self.bmi = gewicht / (lengte/100 * lengte/100)


wim = Persoon(80, 180, 18)

jef = Persoon(75, 182, 19)

print("1", dir(wim))
print("2", dir(jef))

print("3", wim.__dict__)
print("4", jef.__dict__)

print("5", dir())