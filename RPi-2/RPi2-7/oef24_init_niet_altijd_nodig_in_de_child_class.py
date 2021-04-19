class Top:

    def __init__(self):
        print("dunder init in Top werd aangeroepen!")


class Midden(Top):
    pass




class Beneden(Midden):
    pass


b1 = Beneden()

