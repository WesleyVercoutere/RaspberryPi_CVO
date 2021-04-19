class Persoon:

    def __init__(self, gewicht , lengte , leeftijd):
        self.gewicht = gewicht
        self.lengte = lengte
        self.leeftijd = leeftijd
        self.bmi = gewicht / (lengte/100 * lengte/100)

    def bmi_rapport(self):
        if self.bmi < 18.5:
            print("ondergewicht")
        elif self.bmi < 25:
            print("gezond gewicht")
        elif self.bmi < 30:
            print("overgewicht")
        else:
            print("ernstig overgewicht(obesitas)")


wim = Persoon(80, 180, 18)
jef = Persoon(75, 182, 19)
mr_heavy = Persoon(200, 160, 23)
mr_light = Persoon(45, 175, 20)


wim.bmi_rapport()
jef.bmi_rapport()
mr_heavy.bmi_rapport()
mr_light.bmi_rapport()