class Persoon:

    def __init__(self,gewicht,lengte,leeftijd):
        if lengte > 50 and lengte < 250:
            self.lengte = lengte
        else:
            raise Exception("Je lengte in cm moet een integer getal zijn tussen 50 en 250cm!")
            return
        self.gewicht = gewicht
        self.leeftijd = leeftijd
        self.bmi = gewicht / (lengte / 100 * lengte / 100)

    def bmi_rapport(self):
        if self.bmi < 18.5:
            print("ondergewicht")
        elif self.bmi < 25:
            print("gezond gewicht")
        elif self.bmi < 30:
            print("overgewicht")
        else:
            print("ernstig overgewicht(obesitas)")

    def set_lengte(self, lengte):
        if isinstance(lengte, int):
            if lengte > 50 and lengte < 250:
                self.lengte = lengte
                return
        else:
            raise Exception("Je lengte in cm moet een integer getal zijn tussen 50 en 250cm!")


wim = Persoon(80, 180, 18)
jef = Persoon(75, 182, 19)
mr_heavy = Persoon(200, 160, 23)
mr_light = Persoon(45, 175, 20)


wim.bmi_rapport()
jef.bmi_rapport()
mr_heavy.bmi_rapport()
mr_light.bmi_rapport()

wim.set_lengte(150)
print("1", wim.__dict__)

wim.set_lengte(1.8)
print("2", wim.__dict__)

