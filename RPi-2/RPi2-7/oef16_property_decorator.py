class Boss:

    def __init__(self, salaris):
        if isinstance(salaris, int) and salaris <= 100000:
                self._salaris = salaris
        else:
            print("Gelieve een salaris tussen 0 - 100000  in te geven.")

    @property
    def salaris(self):
        return self._salaris

    @salaris.setter
    def salaris(self, salaris):
        if isinstance(salaris, int) and salaris <= 100000:
                self._salaris = salaris
        else:
            print("Gelieve een salaris tussen 0 - 100000  in te geven.")



diederik_steinway = Boss(100000)
print(diederik_steinway.salaris)

diederik_steinway.salaris = 85000  # salaris wordt terug toegekend alsof salaris een gewone instance variabele is
print(diederik_steinway.salaris)   # salaris wordt terug opgevraagd alsof een instance variabele is

diederik_steinway.salaris = 110000
print(diederik_steinway.salaris)