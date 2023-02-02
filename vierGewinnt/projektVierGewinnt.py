from random import randint


class Spielfeld:
    def __init__(self):
        field = [['X' for i in range(7)] for j in range(6)]
        self.__grid = field

    @property
    def grid(self):
        return self.__grid

    def __repr__(self):
        return f'grid:{self.grid}'

    def spielfeld_aktualisieren(self):  # TODO
        pass

    def gewinn_abfragen(self):  # TODO
        pass


class Spieler():
    def __init__(self, farbe: str, name: str):
        self.farbe = farbe
        self.name = name


class Computer(Spieler):

    def __init__(self, farbe: str, name: str):
        super().__init__(farbe, name)

    def entscheiden(self) -> int:
        """
        Computer gibt einen gültigen Zug ab
        Der Zug ist eine Zufallszahl zwischen 0 und 6.

        :return:
            Wert für Zug: int
        """
        zug = randint(0, 6)
        return zug


if __name__ == '__main__':
    pass
