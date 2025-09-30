class Maillon:
    """maillon d'une liste chaînée"""
    def __init__(self, v=None, p=None):
        """constructeur de la classe"""
        self.valeur=v
        self.precedent=p

    def __str__(self):
        """Méthode pour l'affichage"""
        if self.precedent == None:
            return str(self.valeur)
        else:
            return str(self.valeur) + " - " + str(self.precedent)

class Pile:
    """Class pour définir une pile"""
    def __init__(self):
        """constructeur"""
        self.dernier=None

    def __str__(self):
        """méthode pour l'affichage du haut vers le bas"""
        return str(self.dernier)

    def est_vide(self):
        """méthode qui retourne un booléen qui indique
        si la pile est vide ou non"""
        return self.dernier==None

    def empiler(self,v):
        """méthode qui permet d'ajouter un élément sur la pile"""
        m=Maillon(v,self.dernier) # le precedent sera forcément le haut de la pile
        self.dernier=m
        # ce code marche aussi dans le cas où la pile est vide

    def depiler(self):
        """"méthode qui supprime l'élément sur la pile et le retourne"""
        if self.est_vide():
            return None
        else:
            v=self.dernier.valeur
            self.dernier=self.dernier.precedent
            return v

    def longueur(self):
        """méthode qui retourne le nombre d'éléments de la pile"""
        i=0
        p=self.dernier
        while p!=None:
            p=p.precedent
            i=i+1
        return i
    
class Maillon2:
    """maillon d'une liste chaînée"""
    def __init__(self, v=None, s=None):
        """constructeur de la classe"""
        self.valeur=v
        self.suivant=s

    def __str__(self):
        """Méthode pour l'affichage"""
        if self.suivant == None:
            return str(self.valeur)
        else:
            return str(self.valeur) + " - " + str(self.suivant)

class File:
    """Class pour définir une file"""
    def __init__(self):
        """constructeur"""
        self.premier=None
        self.dernier=None

    def __str__(self):
        """méthode pour l'affichage"""
        return str(self.premier)

    def est_vide(self):
        """méthode qui retourne un booléen qui indique
        si la file est vide ou non"""
        return self.premier==None

    def enfiler(self,v):
        """méthode qui permet d'ajouter un élément en fin de file"""
        m=Maillon2(v,None)
        if self.est_vide():
            self.premier=m
            self.dernier=m
        else:
            self.dernier.suivant=m
            self.dernier=m

    def defiler(self):
        """"méthode qui supprime l'élément en début de file et le retourne"""
        if self.est_vide():
            return None
        else:
            v=self.premier.valeur
            self.premier=self.premier.suivant
            return v

    def longueur(self):
        """méthode qui retourne le nombre d'éléments de la file"""
        i=0
        p=self.premier
        while p!=None:
            p=p.suivant
            i=i+1
        return i