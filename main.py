import sys
from gestionLocation import MaisonFactory

Factory = MaisonFactory.MaisonFactory()
appart = Factory.get_maison("Appartement", 3, 45, 3500)

print(appart.get_type())
