import tkinter as tk
from constant import *
from functions import *
from object import Pile_rec_click, Tower
from pile_file import File

if __name__ == "__main__":  # code principal
    n = 8   # nombre d'anneau 1 - 8

    # ----------fenêtre----------
    root = tk.Tk()
    root_width = 960
    root_height = 640    # resolution DVGA
    solve_button = tk.Button(root, text = "SOLUTION", command = lambda : solve(mvt_solution, rectangles))
    quit_button = tk.Button(root, text = "QUITTER", command = root.destroy)
    canvas = tk.Canvas(width=root_width, height=root_height, background="#282828")    #181818 for other shades
    
    # ----------objets----------
    to = Tower(canvas)
    rectangles = Pile_rec_click(canvas, n)
    mvt_solution = File()

    # ----------fonctions----------
    hanoi(n,1,2,3,mvt_solution)
    def click_events(event):
        to.hitboxes(event, rectangles)
        rectangles.select_rec(event)
    
    # ----------binding----------
    canvas.pack()
    solve_button.pack()
    quit_button.pack()
    root.bind("<KeyRelease-space>", lambda event : root.destroy())  #-----------TEMP UTILE POUR CODER, FERME PLUS RAPIDEMENT LE FENÊTRE
    root.bind("<Button-1>", click_events)
    root.bind('a', lambda event : rectangles.move_rec(rectangles.pile_tower1))
    root.bind('z', lambda event : rectangles.move_rec(rectangles.pile_tower2))
    root.bind('e', lambda event : rectangles.move_rec(rectangles.pile_tower3))
    root.bind('s', lambda event : solve(mvt_solution, rectangles))
    
    root.mainloop()