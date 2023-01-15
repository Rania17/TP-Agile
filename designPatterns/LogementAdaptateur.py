from superHeros import Habitat

class LogementAdaptateur(Habitat.Habitat):
    maison = None

    def get_nb_heros(self):
        return self.nb_heros

    def loger_avengers(self, avengers, maison):
        if (maison.get_nb_chambres() >= avengers.get_nb_heros()):
            self.avengers = avengers
            self.maison = maison
            self.nb_heros = avengers.get_nb_heros()