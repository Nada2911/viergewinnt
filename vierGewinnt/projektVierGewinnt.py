import abc
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

    def gewinn_abfrage(self, farbe: str) -> bool:
        """
        Wenn die gleiche Farbe 4-mal in einer beliebigen Richtung hintereinander vorkommt, so wurde das Spiel von dem
        Spieler mit dieser Farbe gewonnen. Um alle Richtungen zu testen, wird die Liste nachbarn benötigt.
        :param farbe: des Spielers, der den letzten Zug getätigt hat
        :return: True bei Gewinn, sonst False
        """
        nachbarn = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for zeile in range(len(self.__grid)):
            for spalte in range(len(self.__grid[zeile])):
                if self.__grid[zeile][spalte] == farbe:
                    for n in nachbarn:
                        gewinn_vier = 1
                        pos = ((zeile + n[0] * 3), (spalte + n[1] * 3))
                        if (0 <= pos[0] < len(self.__grid)) and (0 <= pos[1] < len(self.__grid[zeile])):
                            for i in range(1, 4, 1):
                                if self.__grid[zeile + n[0] * i][spalte + n[1] * i] == farbe:
                                    gewinn_vier += 1
                                if gewinn_vier == 4:
                                    return True
        return False

    def gueltig(self, spalte: int) -> bool:
        """
        Testet ob die Spalte im Spielfeld existiert und ob der Zug moeglich ist.
        :param spalte: Spalte in der ein Zug moeglich sein soll.
        :return: True bei gueltig, sonst False.
        """
        if not 0 <= spalte <= 6:
            return False
        for i in range(len(self.__grid)):
            if self.__grid[i][spalte] == "X":
                return True
        return False

    def spielfeld_ausgeben(self):
        """
        Wurde verkehrt umgesetzt, da es einfacher ist.
        :return: Gibt nichts zurueck.
        """
        for z in range(len(self.__grid) - 1, -1, -1):
            print(self.__grid[z])


class Spieler(abc.ABC):
    def __init__(self, farbe: str, name: str):
        self.farbe = farbe
        self.name = name

    @abc.abstractmethod
    def ziehen(self) -> int:
        pass

    @property
    def farbe(self):
        return self._farbe

    @farbe.setter
    def farbe(self, value):
        if value == "X":
            self._farbe = "O"
        else:
            self._farbe = value

    def __repr__(self):
        return f'{self.name} Name {self.farbe} Farbe'



class Mensch(Spieler):
    def ziehen(self) -> int:
        """
        Fordert den Spieler an, in welcher Spalte er/sie seinen/ihren Zug setzen möchte.
        Ungültiger Input wird verhindert.
        :return: Spalte als int, -1 bei ungültigem Input
        """
        print(f'{self.name} Eine Zahl zwischen 1 bis 7')
        x = 0
        try:
            x = int(input())
        except ValueError:
            print(f'Bitte eine Zahl zwischen 1 und 7 angeben.')
        return x - 1

    def __init__(self, farbe: str, name: str, ):
        super().__init__(farbe, name)
    def __repr__(self):
        return super().__repr__()


class Computer(Spieler):

    def __init__(self):
        super().__init__('C', 'Computer')
    def __repr__(self):
        return super().__repr__()

    def ziehen(self) -> int:
        """
        Computer gibt einen gültigen Zug ab
        Der Zug ist eine Zufallszahl zwischen 0 und 6.
        :return: Wert für Zug
        """
        spalte = randint(0, 6)
        return spalte

def spiel_kofigurieren()->tuple[Spieler,Spieler]:
    """
    Fragt nach den Einstellungen für ein neues Spiel. Die Optionen sind 'S' für Multiplayer-Modus und 'C', um gegen den Computer zu spielen.
    Name und Farbe für Spieler wird erfragt.
    :return: Die Spieler eines neuen Spiels.
    """
    print("S steht für Multiplayer-Modus und C für den Computer")
    s1 = None
    gegner = input()
    if gegner == 'C':
        s1 = Computer()
    elif gegner == 'S':
        name1 = input('SpielerIn 1 bitte Name angeben:')
        farbe1 = input('SpielerIn 1 bitte Farbe wählen:')
        s1 = Mensch(farbe1, name1)
    else:
        print('nicht gueltig')
    name2 = input('SpielerIn 2 bitte Name angeben:')
    farbe2 = input('SpielerIn 2 bitte Farbe wählen:')
    s2 = Mensch(farbe2, name2)
    return s1, s2





if __name__ == '__main__':
    grid = Spielfeld()
    print(grid)
    grid.spielfeld_ausgeben()
    grid.spielfeld_aktualisieren(5,"rot")
    print('SpielerIn 2 bitte Name angeben:')
    name1 = input()
    print('SpielerIn 2 bitte Farbe wählen:')
    farbe1 = input()
    s1 = Mensch(farbe1, name1)
    pass
