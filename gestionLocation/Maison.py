class Maison:

    def __init__(self, nb_chambres, surface, loyer):
        # instance variable unique to each instance
        self.nb_chambres = nb_chambres
        self.surface = surface
        self.loyer = loyer
        self.locataire = None

    def infos_locataire(self):
        return self.locataire.get_civilite(), self.locataire.get_nom(), self.locataire.get_prenom()

    def infos_maison(self):
        return self.nb_chambres, self.surface, self.infos_locataire()

    def affecter_locataire(self, locataire):
        self.locataire = locataire

    def ajouter_chambre(self):
        self.nb_chambres += 1

    def get_loyer(self):
        return self.loyer

    def set_loyer(self,l):
        self.loyer = l

    def get_nb_chambres(self):
        return self.nb_chambres

    def set_nb_chambres(self, n):
        self.nb_chambres = n

    def get_surface(self):
        return self.surface

    def set_surface(self, s):
        self.surface = s
