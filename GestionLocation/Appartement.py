from gestionLocation import Maison

class Appartement(Maison.Maison):
    type = "Appartement"

    def get_type(self):
        return  self.type


