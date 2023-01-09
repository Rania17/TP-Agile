class Locataire:


    def __init__(self, nom, prenom, civilite, revenu_mens):
        # instance variable unique to each instance
        self.nom = nom
        self.prenom = prenom
        self.civilite = civilite
        self.revenu_mens = revenu_mens

    # les getters
    def get_nom(self):
        return self.nom

    def get_prenom(self):
        return self.prenom

    def get_civilite(self):
        return self.civilite

    def get_revenu_mens(self):
        return self.revenu_mens

    # les setters
    def set_nom(self, nom):
        self.nom = nom

    def set_prenom(self, prenom):
        self.prenom = prenom

    def set_civilite(self, civilite):
        self.civilite = civilite

    def set_revenu_mens(self, revenu_mens):
        self.revenu_mens = revenu_mens