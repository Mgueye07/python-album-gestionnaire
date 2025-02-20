"""python-poo/main.py
__author__ = "MG"
__version__ = "1.0"
"""
from datetime import date
from tuto01 import Personne
from tuto01 import CompteBancaire

def main():

    """point d'entée du programme"""

personnes =[]


personne = Personne("Mohamet","Gueye",date(2000,4,22),"77 123 45 67","Dakar")

personnes.append(personne)

compte1 = CompteBancaire("123456789", 100000, "ibou", "compte courant")
compte2 = CompteBancaire("987654321", 500000, "moussa", "compte epargne")
print(compte1)
# creidter
compte1.crediter(50000)
print(compte1)
# DEBITER
compte1.debiter(100000)
print(compte1)

#virement
compte2.virement(compte1, 100000)
print("apres virement")
print(compte1)
print(compte2)


# personne2 = Personne("Aminata", "ndiaye", date(1997, 6 , 25), "77 123 45 67", "Thies")
# personnes.append(personne2)

# for personne in personnes:
#     print(personne)


if __name__ == "__main__" :
    main ()