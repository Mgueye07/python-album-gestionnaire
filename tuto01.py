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


    




class CompteBancaire:
    """represente un compte bancaire"""

    nombre_compte_cree = 0
    """represente un compte bancaire"""
    def __init__(self, numero_compte,solde, titlaire,type_compte):
        self.numero_compte=numero_compte
        self.solde=solde
        self.titlaire=titlaire
        self.type_compte=type_compte
        CompteBancaire.nombre_compte_cree+=1
    def crediter(self,montant):
        """permet de crediter un compte"""

        self.solde+=montant
    def debiter(self,montant):
        """permet de debiter un compte"""
        self.solde-=montant
    def virement(self,compte,montant):
        """permet de faire un virement entre deux comptes"""
        self.debiter(montant)
        compte.crediter(montant)

#getter et setter pour le solde 
    @property
    def solde(self):
        return self._solde
    @solde.setter
    def solde(self, solde):
        if solde<=0:
            raise ValueError("le solde ne peut pas etre negatif")
        self._solde=solde



    def __str__(self):
        return f"Numéro de comopte:{self.numero_compte} Titulaire:{self.titlaire} Solde:{self.solde} Type de compte:{self.type_compte}"
    
    @classmethod
    def get_total_compte(cls):
        """permet de retourner le nombre de compte cree"""
        return cls.nombre_compte_cree
    
class Calcul:
    """permet de faire des calculs mathematiques"""

    @staticmethod
    def addition(nombre1,nombre2):
        return nombre1+nombre2
    
    @staticmethod
    def multiplication(nombre1,nombre2):
        return nombre1*nombre2