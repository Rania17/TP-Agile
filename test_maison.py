from gestionLocation import Maison

class TestMaison:
    maison1 = Maison.Maison(3,25,800)

    def test_surface_maison1(self):
        result = self.maison1.get_surface()
        assert result == 25

    def test_chambres_maison1(self):
        result = self.maison1.get_nb_chambres()
        assert result == 3
