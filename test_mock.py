import unittest
from  unittest.mock import patch
from gestionLocation import Maison, Locataire
from gestionLocation.Locataire import Registre
import gestionLocation.Locataire

class LocataireTestCase(unittest.TestCase):

    def setup(self):
        self.client = Locataire.Locataire("Pierre", "Dupont", "Monsieur", 3000)
        self.registre = Registre("Rania&Gabriel", 0)
        self.client.subscribe(self.registre)

    @patch("gestionLocation.Locataire.Registre")
    def test_maison(self, mocked_registre):
        assert mocked_registre is not None
        mocked_registre.is_subscribe.return_value = True
        self.setup()
        result = self.client.subscribe(mocked_registre)
        self.assertEqual(True, result)