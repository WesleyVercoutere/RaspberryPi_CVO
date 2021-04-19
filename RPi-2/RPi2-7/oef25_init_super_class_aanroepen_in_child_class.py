class Persoon():

    aantal_personen = 0

    def __init__(self, voornaam, achternaam):
        self.voornaam = voornaam
        self.achternaam = achternaam
        Persoon.aantal_personen +=1


    def bezig_zijn(self):
        print("ik werk")


class Leraar(Persoon):

    def __init__(self,voornaam, achternaam, salaris):
        super().__init__(voornaam, achternaam)
        self.salaris = salaris

    def bezig_zijn(self):
        print("ik geef les")


class Leerling(Persoon):

    def __init__(self,voornaam, achternaam, inschrijvingsgeld):
        super().__init__(voornaam, achternaam)
        self.inschrijvingsgeld = inschrijvingsgeld

    def bezig_zijn(self):
        print("ik studeer")


wv = Leraar('wim','verlinden',1000)
kdd = Leerling('koen','dedecker',560)

print('1', wv.__dict__)
print('2', kdd.__dict__)

print('3', wv.__dict__)
print('4', kdd.__dict__)

print('5', Persoon.aantal_personen)
print('6', wv.aantal_personen)
print('7', kdd.aantal_personen)


