from superHeros import Avengers, Heros, Habitat

class TestAvengers:
    # Créer des héros
    spiderman = Heros.Heros("SPIDERMAN", "2.20m", "Agile et adhère aux murs", "Toiles d'araignée")
    iron_man = Heros.Heros("IRON MAN", "5.20m", "Voler, tirer des missiles", "Armure")
    captain_america = Heros.Heros("CAPTAIN AMERICA", "4.20m", "Super soldat", "Sérum militaire")

    # Créer les avengers
    les_avengers = Avengers.Avengers("Les avengers!")
    les_avengers.ajouter_heros(spiderman)
    les_avengers.ajouter_heros(iron_man)
    les_avengers.ajouter_heros(captain_america)

    # Créer un habitat
    habitat_avengers = Habitat.Habitat("Mars")
    habitat_avengers.ajouter_avengers(les_avengers)

    def test_nb_heros_avengers(self):
        result = self.les_avengers.get_nb_heros()
        assert result == 3

    def test_heros_avengers(self):
        result = self.les_avengers.get_heros()
        assert result[0].get_nom() == "SPIDERMAN" and result[1].get_nom() == "IRON MAN" and result[2].get_nom() == "CAPTAIN AMERICA"

    def test_habitat(self):
        result = self.habitat_avengers.get_nb_heros()
        assert result == self.habitat_avengers.get_avengers().get_nb_heros()