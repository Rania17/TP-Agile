from GestionLocation import Maison, Locataire
from unittest import TestCase

maison1 = Maison.Maison(3,25)

def test_maison1():
    assert maison1.get_surface() == 25

locataire1 = Locataire.Locataire("Jean", "Pierre", "Monsieur", 3500)
maison1.affecter_locataire(locataire1)

maison1.infos_maison()

def test_maison1_locataire1():
    assert maison1.locataire.get_nom() == "Jean"