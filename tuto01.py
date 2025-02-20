"""__version__: 1.0
__since__: 13-02-2025
__author__: MG
__copyright__: MG
"""
class Personne:
    """represente une personne"""
    def __init__(self,nom,prenom,date_naissance, telephone, adresse):
        self.nom=nom
        self.prenom=prenom
        self.date_naissance=date_naissance
        self.telephone=telephone
        self.adresse=adresse
    def __str__(self):
        return f"[nom :{self.nom} , prenom :{self.prenom}, date_naissance :{self.date_naissance}, telephone :{self.telephone}, adresse :{self.adresse}]"


    

