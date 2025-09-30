from constant import *
from functions import *
from PIL import Image, ImageTk
import tkinter as tk
import pile_file as pf

class Rec:
    """
    Classe utilisé pour représenter un anneau des tours de Hanoï

    -----attributs-----
    - num : int désignant les 8 rectangles existant, 0 étant le plus grand et 7 le plus petit
    - canvas : la toile sur laquelle on l'instantiera

    -----methodes----
    - instantiate : instantie l'anneau
    """
    def __init__(self, canvas, num) -> None:
        """
        paramètres : 
        - canvas : la toile
        - num : l'anneau
        """
        self.num = num   # entre 0 et 7 désignant les 8 rectangles existant
        self.canvas = canvas
    
    def instantiate(self):
        """
        méthode qui instantie l'anneau correspondant à num
        toutes les images sont aussi stockées ici
        """
        couleurs = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'magenta', 'pink']
        tailles = [100, 90, 80, 70, 60, 50, 40, 35]
        hauteur = [2, 40, 78, 116, 154, 192, 230, 268]
        
        if 0 <= self.num <= 7:
            self.image = self.canvas.create_rectangle(
                centre[0][0] - tailles[self.num], centre[0][1] - hauteur[self.num],
                centre[0][2] + tailles[self.num], centre[0][3] - (hauteur[self.num] + 48),
                fill=couleurs[self.num]
            )

class Pile_rec_click:
    """
    Classe utilisé pour gérer les anneaux

    -----attributs-----
    - has_selected : booléen pour ne pouvoir selectionner qu'un seul rectangle
    - selected : (Rec) une copie de l'anneau selectionné pour le gardé en mémoire
    - num : le nombre de rectangle dans le jeu
    - 3 piles : contenant les anneaux de chaques tours

    -----méthodes-----
    - load_rec : rempli la 1ere tour avec les anneaux
    - highlight_rec : met en évidences un anneau sélectionné
    - unhighlight_rec : enlève cette évidence
    - select_rec : permet de sélectionner un anneau
    - move_rec : permet de bouger l'anneau sélectionné
    """
    def __init__(self, canvas, num):
        """"""
        self.has_selected = False   # pour ne pouvoir selectionner qu'un seul rectangle
        self.selected = None
        self.num = num  # le nombre de rectangle dans le jeu
        self.canvas = canvas
        # Piles contenant les rectangles de chaques tours
        self.pile_tower1 = pf.Pile()
        self.pile_tower2 = pf.Pile()
        self.pile_tower3 = pf.Pile()
        self.load_rec()

    def load_rec(self):
        for i in range(self.num):
            self.pile_tower1.empiler(Rec(self.canvas, i))
            self.pile_tower1.dernier.valeur.instantiate()

    def highlight_rec(self, rec):
        if not self.has_selected:
            self.has_selected = True
            self.canvas.itemconfig(rec, outline="light gray", width=3)

    def unhighlight_rec(self, rec):
        if self.has_selected:
            self.has_selected = False
            self.canvas.itemconfig(rec, outline="black", width=1)

    def select_rec(self, event):
        clicked_items = self.canvas.find_overlapping(event.x, event.y, event.x, event.y) # rend les éléments créés clickables et stocke dans un tuple les éléments clickés
        for item in clicked_items:  # boucle sur tous les éléments clickés
            # rend seulement les rectangles du dessus clickables
            if  (self.pile_tower1.dernier is not None and item == self.pile_tower1.dernier.valeur.image) or (
                self.pile_tower2.dernier is not None and item == self.pile_tower2.dernier.valeur.image) or (
                self.pile_tower3.dernier is not None and item == self.pile_tower3.dernier.valeur.image):   

                # cas où rien n'est selectionné et on selectionne un rectangle
                if self.has_selected == False:
                    self.highlight_rec(item)    # on met en évidence le rectangle
                    self.selected = item        # le garde en mémoire
                    self.has_selected = True
                    return  # arrète le programme, pour ne pas exécuter la fin, risque de problème + optimise

                # cas où un rectangle est selectionné et on selectionne un autre
                elif self.has_selected == True and self.selected != item:
                    self.unhighlight_rec(self.selected) # déselectionne le rectangle
                    self.highlight_rec(item)            # on met en évidence rectangle clické
                    self.selected = item                # le garde en mémoire
                    return  # arrète le programme, pour ne pas exécuter la fin, risque de problème + optimise

        # cas où on clicke ailleur que sur un rectangle et qu'un est selectionné
        if self.has_selected == True and self.selected != None:
            self.unhighlight_rec(self.selected) # déselectionne le rectangle
            self.selected = None                # on réinitialise la mémoire du rectangle sélectionné
            self.has_selected = False

    def move_rec(self, target_tower = pf.Pile()):       
        current_tower = None    # pile où l'on stockera la tour dans laquelle le rectangle se trouve
        # on détermine où se trouve notre rectangle (self.selected) et l'assigne à "current_tower"
        # les candidats possibles sont les derniers de chaques pile(les seuls qu'on peut selectionner)
        # check avant si pile vide, résoudrait à une erreur si vide
        if self.pile_tower1.dernier != None and self.selected == self.pile_tower1.dernier.valeur.image:
            current_tower = self.pile_tower1
        elif self.pile_tower2.dernier != None and self.selected == self.pile_tower2.dernier.valeur.image:
            current_tower = self.pile_tower2
        elif self.pile_tower3.dernier != None and self.selected == self.pile_tower3.dernier.valeur.image:
            current_tower = self.pile_tower3

        # cas où le rectangle n'appartient pas aux tours
        if current_tower == None:
            return  # sort de la méthode car on ne peut pas dépiler une pile vide
        selected_rec = current_tower.depiler()
        # cas où la tour contient un rectangle plus petit (ici on inverse ">" num représentant le plus grand rec = 0)
        if target_tower.dernier != None and selected_rec.num < target_tower.dernier.valeur.num:
            current_tower.empiler(selected_rec) # on réempile sur la tour de base
            return                              # puis on sort de la méthode
        
        # tous les critères pour bouger l'anneau sont respectés
        target_tower.empiler(selected_rec)      # on empile sur la tour cible

        # on calcule ses coordonnées
        floor = centre[0][1] - etage_y[target_tower.longueur()+1]   # les coordonnés y soit de l'étage (peut importe le centre choisi)
        tower = None    # les coordonnés x soit de la tour
        if target_tower == self.pile_tower1:
            tower = centre[0][0]
        elif target_tower == self.pile_tower2:
            tower = centre[1][0]
        elif target_tower == self.pile_tower3:
            tower = centre[2][0]

        # on met à jour les coordonnées du rectangle en spécifiant les coordonnées des coins en bas à gauche et en haut à droite
        # x : pour le centrer sur la tour, on fait + et - la moitié de la longueur du rectangle de chaque côté
        # y : seulement l'étage pour le coin en bas, puis l'étage + sa hauteur pour le coin en haut
        self.canvas.coords(self.selected, tower-rec_size[target_tower.dernier.valeur.num][0]/2, floor, tower+10+rec_size[target_tower.dernier.valeur.num][0]/2, floor+rec_size[4][1])

        self.unhighlight_rec(self.selected) # on enlève la mise en évidence du rectangle
        self.selected = None                # on réinitialise le rectangle selctionné

class Tower:
    """
    Classe utilisé pour représenter les tours

    -----attributs-----
    canvas : la toile sur laquelle sera dessiné les tours 

    -----methodes----
    - instantiate : pour instantier les tours
    """
    def __init__(self, canvas) -> None:
        self.hitbox1 = None
        self.hitbox2 = None
        self.hitbox3 = None

        self.canvas = canvas

        temp_btn_img = Image.open("tower_btn.png")
        temp_btn_img = temp_btn_img.resize((70,70))
        self.btn_img = ImageTk.PhotoImage(temp_btn_img)

        self.instantiate()

    def instantiate(self):      
        self.canvas.create_rectangle(50,590,910,580,fill="black")
        self.canvas.create_rectangle(215,50,225,590,fill="black")
        self.canvas.create_rectangle(475,50,485,590,fill="black")
        self.canvas.create_rectangle(745,50,755,590,fill="black")

        self.hitbox1 = self.canvas.create_image(220,40,image=self.btn_img)
        self.hitbox2 = self.canvas.create_image(480,40,image=self.btn_img)
        self.hitbox3 = self.canvas.create_image(750,40,image=self.btn_img)

    def hitboxes(self, event, rec = Pile_rec_click):
        clicked_items = self.canvas.find_overlapping(event.x, event.y, event.x, event.y)       
        for item in clicked_items:
            if item == self.hitbox1:
                rec.move_rec(rec.pile_tower1)
            elif item == self.hitbox2:
                rec.move_rec(rec.pile_tower2)
            elif item == self.hitbox3:
                rec.move_rec(rec.pile_tower3)