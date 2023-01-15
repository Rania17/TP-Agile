class Avengers:

    def __init__(self, nom):
        # instance variable unique to each instance
        self.nom = nom
        self.nb_heros = 0
        self.heros = []

    def get_nom(self):
        return self.nom

    def set_nom(self, n):
        self.nom = n

    def get_nb_heros(self):
        return self.nb_heros

    def get_heros(self):
        return self.heros

    def ajouter_heros(self,h):
        self.heros.append(h)
        self.nb_heros = self.nb_heros + 1

