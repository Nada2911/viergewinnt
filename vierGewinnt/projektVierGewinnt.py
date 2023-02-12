import abc
from random import randint
from typing import Any


class Spielfeld:
    """
    Attributes
    ----------
    __grid: list
        Spielfeld leere Positionen sind durch ein X markiert

    Methods
    -------
    spielfeld_aktualisieren(self, spalte: int, farbe: str)
        Aktualisiert das Spielfeld, um einen gültigen Zug und gibt das aktualisierte Feld aus.
    gewinn_abfrage(self, farbe: str)
        erkennt, ob ein Spiel gewonnen wurde
    gueltig(self, spalte: int)
        erkennt, ob ein Zug gültig ist
    spielfeld_ausgeben(self)
        gibt das Spielfeld auf der Konsole aus
    """
    def __init__(self):
        field = [['X' for i in range(7)] for j in range(6)]
        self.__grid = field

    def spielfeld_aktualisieren(self, spalte: int, farbe: str) -> Any:
        """
        Aktualisiert das Spielfeld, um einen gültigen Zug und gibt das aktualisierte Feld aus.
        Parameters
        ----------
        spalte: int
            Spalte in der, der Zug gesetzt werden soll
        farbe: str
            des Spielers, der gerade an der Reihe ist
        Returns
        -------
        Any
            Spielfeld ausgeben, nachdem ein gültiger Zug gesetzt wurde; 0, wenn der Zug ungültig ist
        """
        if self.gueltig(spalte):
            for i in range(len(self.__grid)):
                if self.__grid[i][spalte] == 'X':
                    self.__grid[i][spalte] = farbe
                    self.spielfeld_ausgeben()
                    return 1
        else:
            print('Kein gültiger Zug')
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
        Parameters
        ----------
        farbe: str
            des Spielers, der den letzten Zug getätigt hat

        Returns
        -------
        bool
            True bei Gewinn, sonst False
        """
        nachbarn = [(0, 1), (1, -1), (1, 0), (1, 1)]
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

        Parameters
        ----------
        spalte: int
            Spalte in der ein Zug moeglich sein soll.
        Returns
        -------
        bool
            True bei gueltig, sonst False.
        """
        if not 0 <= spalte <= 6:
            return False
        for i in range(len(self.__grid)):
            if self.__grid[i][spalte] == "X":
                return True
        return False

    def spielfeld_ausgeben(self):
        """
        Gibt das aktuelle Spielfeld Zeile für Zeile aus. Der Index 0 ist die tiefste Zeile.
        Returns
        -------
        Gibt nichts zurueck.
        """
        for z in range(len(self.__grid) - 1, -1, -1):
            print(self.__grid[z])


class Spieler(abc.ABC):
    """
    Attributes
    ----------
    farbe: str
        gibt die Farbe für den Spieler an
    name: str
        Name des Spielers
    Methods
    -------
    ziehen(self)
        Erlaubt dem Spieler einen Zug zu machen
    """
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
    """
    Attributes
    ----------
    farbe: str
        gibt die Farbe für den Spieler an
    name: str
        Name des Spielers
    Methods
    -------
    ziehen(self)
        Erlaubt dem Spieler einen Zug zu machen
    """
    def ziehen(self) -> int:
        """
        Fordert den Spieler an, in welcher Spalte er/sie seinen/ihren Zug setzen möchte.
        Ungültiger Input wird verhindert.
        Returns
        -------
        int
            Spalte als int, -1 bei ungültigem Input
        """
        print(f'{self.name} Eine Zahl zwischen 1 bis 7')
        x = int()
        try:
            x = int(input())
        except ValueError:
            print(f'Bitte eine Zahl zwischen 1 und 7 angeben.')
            return -1
        if x == 0:
            return -10
        return x - 1

    def __init__(self, farbe: str, name: str, ):
        super().__init__(farbe, name)

    def __repr__(self):
        return super().__repr__()


class Computer(Spieler):
    """
    Attributes
    ----------
    farbe: str
        Defaultwert ist C
    name: str
        Defaultname ist Computer
    Methods
    -------
    ziehen(self)
        Erlaubt dem Spieler einen Zug zu machen
    """

    def __init__(self):
        super().__init__('C', 'Computer')

    def __repr__(self):
        return super().__repr__()

    def ziehen(self) -> int:
        """
        Computer gibt einen gültigen Zug ab.
        Der Zug ist eine Zufallszahl zwischen 0 und 6.
        Returns
        -------
        int
            Wert für Zug
        """
        spalte = randint(0, 6)
        return spalte


def spiel_konfigurieren() -> tuple[Spieler, Spieler]:
    """
    Fragt nach den Einstellungen für ein neues Spiel. Die Optionen sind 'S' für Multiplayer-Modus und 'C',
    um gegen den Computer zu spielen.
    Name und Farbe für Spieler wird erfragt.
    Returns
    -------
    tuple of Spieler, Spieler
        Die Spieler eines neuen Spiels.
    """
    print("Bitte den Spielmodus auswählen: \n S steht für Multiplayer-Modus und C für den Computer")
    s1 = str()
    falsche_eingabe = True
    while falsche_eingabe:
        gegner = input('Modus: ')
        if gegner == 'C':
            s1 = Computer()
            falsche_eingabe = False
        elif gegner == 'S':
            name1 = input('SpielerIn 1 bitte Name angeben:')
            farbe1 = input('SpielerIn 1 bitte Farbe wählen:')
            s1 = Mensch(farbe1, name1)
            falsche_eingabe = False
        else:
            print('Ungültige Eingabe.\n Bitte S oder C wählen.')
    name2 = input('SpielerIn 2 bitte Name angeben:')
    farbe2 = input('SpielerIn 2 bitte Farbe wählen:')
    s2 = Mensch(farbe2, name2)
    print(f'{s1.name}:{s1.farbe} spielt gegen {s2.name}:{s2.farbe} \n Um das Spiel abzubrechen als Spalte 0 wählen.')
    return s1, s2


if __name__ == '__main__':
    grid = Spielfeld()
    spieler1, spieler2 = spiel_konfigurieren()
    weitermachen = True
    an_der_Reihe = spieler1
    input(f'{spieler1.name} beginnt das Spiel. \n Zum Starten eine beliebige Taste drücken.')
    while weitermachen:
        gueltig = 0
        while gueltig == 0:
            spalte = an_der_Reihe.ziehen()
            if spalte == -10:
                weitermachen = False
                break
            gueltig = grid.spielfeld_aktualisieren(spalte, an_der_Reihe.farbe)
        gewonnen = grid.gewinn_abfrage(an_der_Reihe.farbe)
        if gewonnen:
            print(f'Bravo! {an_der_Reihe.name} hat gewonnen.')
            weitermachen = False
        if an_der_Reihe == spieler1:
            an_der_Reihe = spieler2
        else:
            an_der_Reihe = spieler1


