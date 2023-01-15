from superHeros import Avengers, Heros, Habitat
from gestionLocation import Maison
from designPatterns import LogementAdaptateur

class TestLogementAdaptateur:
    # Créer des héros
    spiderman = Heros.Heros("SPIDERMAN", "2.20m", "Agile et adhère aux murs", "Toiles d'araignée")
    iron_man = Heros.Heros("IRON MAN", "5.20m", "Voler, tirer des missiles", "Armure")
    captain_america = Heros.Heros("CAPTAIN AMERICA", "4.20m", "Super soldat", "Sérum militaire")

    # Créer les avengers
    les_avengers = Avengers.Avengers("Les avengers!")
    les_avengers.ajouter_heros(spiderman)
    les_avengers.ajouter_heros(iron_man)
    les_avengers.ajouter_heros(captain_america)

    # Créer une maison
    maison = Maison.Maison(4, 200, 5000)

    #Créer un logement adaptateur
    logement = LogementAdaptateur.LogementAdaptateur("Mars")

    def test_affectation_avengers_logement(self):
        self.logement.loger_avengers(self.les_avengers,self.maison)
        result = self.logement.get_nb_heros()
        assert result == 3