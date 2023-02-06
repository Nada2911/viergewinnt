from random import randint
from typing import Any


class Spielfeld:
    def __init__(self):
        field = [['X' for i in range(7)] for j in range(6)]
        self.__grid = field

    def spielfeld_aktualisieren(self, spalte: int, farbe: str) -> Any:
        """
        Aktualisiert das Spielfeld, um einen gültigen Zug und gibt das aktualisierte Feld aus.
        :param spalte: Spalte in der, der Zug gesetzt werden soll
        :param farbe: des Spielers, der gerade an der Reihe ist
        :return: Spielfeld ausgeben, nachdem ein gültiger Zug gesetzt wurde; 0, wenn der Zug ungültig ist
        """
        if self.gueltig(spalte):
            for i in range(len(self.__grid)):
                if self.__grid[i][spalte] == 'X':
                    self.__grid[i][spalte] = farbe
                    self.spielfeld_ausgeben()
                    return 1
        else:
            print('Kein gültiger Zug')  # TODO: Entscheiden: soll das hier ausgegeben werden oder im Zuge von main
            return 0

    @property
    def grid(self):
        return self.__grid

    def __repr__(self):
        return f'grid:{self.grid}'

    def gewinn_abfrage(self):  # TODO
        pass

    def gueltig(self, spalte: int) -> bool:
        pass

    def spielfeld_ausgeben(self):
        pass


class Spieler:
    def __init__(self, farbe: str, name: str):
        self.farbe = farbe
        self.name = name


class Computer(Spieler):

    def __init__(self, farbe: str, name: str):
        super().__init__(farbe, name)

    def ziehen(self) -> int:
        """
        Computer gibt einen gültigen Zug ab
        Der Zug ist eine Zufallszahl zwischen 0 und 6.
        :return: Wert für Zug
        """
        spalte = randint(0, 6)
        return spalte


if __name__ == '__main__':
    pass
