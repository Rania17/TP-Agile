from gestionLocation import Villa, Appartement

class MaisonFactory:

    def get_maison(self, type, nb_chambres, surface, loyer):
        if type == "Villa":
            return Villa.Villa(nb_chambres,surface,loyer)
        elif type == "Appartement":
            return Appartement.Appartement(nb_chambres,surface,loyer)


