class Maison:

    def __init__(self, nb_chambres, surface):
        # instance variable unique to each instance
        self.nb_chambres = nb_chambres
        self.surface = surface
        self.locataire = None

    def infos_locataire(self):
        print("Le locataire est " + self.locataire.get_civilite() + " " + self.locataire.get_nom() +
              " " + self.locataire.get_prenom() )

    def infos_maison(self):
        print("Cette maison a" , self.nb_chambres , "une surface de ", self.surface)
        self.infos_locataire()

    def affecter_locataire(self, locataire):
        self.locataire = locataire

    def get_nb_chambres(self):
        return self.nb_chambres

    def get_surface(self):
        return self.surface

    def set_nb_chambres(self, n):
        self.nb_chambres = n

    def set_surface(self, s):
        self.surface = s

    def ajouter_chambre(self):
        self.nb_chambres += 1

