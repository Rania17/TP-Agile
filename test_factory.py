from gestionLocation import MaisonFactory

class TestFactory:
    Factory = MaisonFactory.MaisonFactory()
    appart = Factory.get_maison("Appartement", 3, 45, 3500)
    villa = Factory.get_maison("Villa", 6, 200, 5000)

    def test_type_maison_1(self):
        result = self.appart.get_type()
        assert result == "Appartement"

    def test_type_maison_2(self):
        result = self.villa.get_type()
        assert result == "Villa"


