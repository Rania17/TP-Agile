class Registre:
    def __init__(self, nom_agence, nb_clients):
        # instance variable unique to each instance
        self.nom_agence = nom_agence
        self.nb_clients = nb_clients
        self.clients = []

    def subscribe(self, client):
        self.nb_clients = self.nb_clients + 1
        self.clients.append(client)
        return

    def is_subscribe(self, client):
        if client in self.clients:
            return True
        else:
            return False

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

    def subscribe(self, registre : Registre):
        return registre.is_subscribe(self)