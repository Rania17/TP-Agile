class Habitat:
    def __init__(self, planete ):
        # instance variable unique to each instance
        self.planete = planete
        self.avengers = None
        self.nb_heros = None

    def get_planete(self):
        return self.planete

    def set_planete(self, planete):
        self.planete = planete

    def ajouter_avengers(self, avengers):
        self.avengers = avengers
        self.nb_heros = avengers.get_nb_heros()

    def get_avengers(self):
        return self.avengers

    def get_nb_heros(self):
        return self.nb_heros

    def habitat_libre(self):
        if self.avengers == None :
            return 1
        else:
            return 0
