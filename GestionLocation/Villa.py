from gestionLocation import Maison

class Villa(Maison.Maison):
    type = "Villa"

    def get_type(self):
        return  self.type

