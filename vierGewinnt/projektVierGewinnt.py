class Spielfeld:
    def __init__(self, grid: list):
        self.grid = grid

    def __repr__(self):
        return f'grid:{self.grid}'

    def spielfeld_erstellen(self):  # TODO
        pass

    def spielfeld_aktualisieren(self):  # TODO
        pass

    def gewinn_abfragen(self):  # TODO
        pass

class Spieler():
	def __init__(self, Spielernummer:int, Farbe:str, Name:str):
		self.Spielernummer = Spielernummer
		self.Farbe = Farbe
		self.Name = Name



if __name__ == '__main__':
	pass

