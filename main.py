"""python-poo/main.py
__author__ = "MG"
__version__ = "1.0"
"""
from datetime import date
from tuto01 import Personne

def main():

    """point d'entée du programme"""

personnes =[]

personne = Personne("Mohamet","Gueye",date(2000,4,22),"77 123 45 67","Dakar")

personnes.append(personne)

personne2 = Personne("Aminata", "ndiaye", date(1997, 6 , 25), "77 123 45 67", "Thies")
personnes.append(personne2)

for personne in personnes:
    print(personne)


if __name__ == "__main__" :
    main ()