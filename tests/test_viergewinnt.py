import unittest
from vierGewinnt.projektVierGewinnt import Spieler, Spielfeld, Mensch, Computer


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass

    def setUp(self) -> None:
        self.s1 = Computer()
        self.s2 = Mensch('K', 'Susi')
        self.s3 = Mensch('X', 'Susu')
        self.feld = Spielfeld()
        self.feld2 = Spielfeld()
        self.feld3 = Spielfeld()
        self.feld4 = Spielfeld()
        self.feld5 = Spielfeld()

    def test_init_computer(self):
        self.assertEqual(self.s1.farbe, 'C')
        self.assertEqual(self.s1.name, 'Computer')

    def test_init_mensch(self):
        self.assertEqual(self.s2.farbe, 'K')
        self.assertEqual(self.s2.name, 'Susi')
        self.assertEqual(self.s3.farbe, 'O')

    def test_init_spielfeld(self):
        anfangs_konfiguration = [['X', 'X', 'X', 'X', 'X', 'X', 'X'],
                                 ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
                                 ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
                                 ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
                                 ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
                                 ['X', 'X', 'X', 'X', 'X', 'X', 'X']]
        self.assertEqual(self.feld.grid, anfangs_konfiguration)

    def test_gueltig(self):
        self.assertTrue(self.feld.gueltig(5))

    def test_aktualisieren(self):
        for i in range(6):
            self.assertEqual(self.feld.spielfeld_aktualisieren(2, 'F'), 1)
        self.assertEqual(self.feld.spielfeld_aktualisieren(2, 'F'), 0)

    def test_gewinn_abfrage(self):
        # vertikale Gewinnposition wird getestet
        for i in range(4):
            self.feld.spielfeld_aktualisieren(2, 'F')
        self.assertTrue(self.feld.gewinn_abfrage('F'))
        # horizontale Gewinnposition
        for i in range(4):
            self.feld2.spielfeld_aktualisieren(i, 'F')
        self.assertTrue(self.feld2.gewinn_abfrage('F'))
        # keine Gewinnposition
        for i in range(1, 10):
            self.feld3.spielfeld_aktualisieren(10//i, 'R')
            self.feld3.spielfeld_aktualisieren(10//i, 'K')
        self.assertFalse(self.feld3.gewinn_abfrage('K'))
        self.assertFalse(self.feld3.gewinn_abfrage('R'))
        # diagonal von links unten nach rechts oben
        for i in range(4):
            for j in range(i):
                self.feld4.spielfeld_aktualisieren(i, 'F')
            self.feld4.spielfeld_aktualisieren(i, 'G')
        self.assertTrue(self.feld4.gewinn_abfrage('G'))
        self.assertFalse(self.feld4.gewinn_abfrage('F'))
        # diagonal von links oben nach rechts unten
        for i in range(3, 0, -1):
            for j in range(i):
                self.feld5.spielfeld_aktualisieren(3-i, 'F')
            self.feld5.spielfeld_aktualisieren(3-i, 'G')
        self.feld5.spielfeld_aktualisieren(3, 'G')
        self.assertTrue(self.feld5.gewinn_abfrage('G'))
        self.assertFalse(self.feld5.gewinn_abfrage('F'))

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
