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

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
