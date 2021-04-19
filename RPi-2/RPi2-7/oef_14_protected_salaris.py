class Boss:

    def __init__(self, salaris):
        if isinstance(salaris, int) and salaris <= 100000:
                self._salaris = salaris
        else:
            print("Gelieve een salaris tussen 0 - 100000  in te geven.")

    def get_salaris(self):
        return self._salaris

    def set_salaris(self, salaris):
        if isinstance(salaris, int) and salaris <= 100000:
                self._salaris = salaris
        else:
            print("Gelieve een salaris tussen 0 - 100000  in te geven.")


diederik_steinway = Boss(100000)
print(diederik_steinway.get_salaris())

diederik_steinway.set_salaris(85000)
print(diederik_steinway.get_salaris())

diederik_steinway.set_salaris(110000)
print(diederik_steinway.get_salaris())



