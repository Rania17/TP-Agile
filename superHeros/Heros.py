class Heros:

    def __init__(self, nom, taille, pouvoir, force):
        # instance variable unique to each instance
        self.nom = nom
        self.taille = taille
        self.pouvoir = pouvoir
        self.force = force

    def infos_heros(self):
        return self.nom, self.taille, self.pouvoir

    def get_nom(self):
        return self.nom

    def set_nom(self, n):
        self.nom = n

    def get_taille(self):
        return self.taille

    def set_taille(self, t):
        self.taille = t

    def get_pouvoir(self):
        return self.pouvoir

    def set_taille(self, p):
        self.pouvoir = p

    def get_force(self):
        return self.force

    def set_force(self, f):
        self.force = f


