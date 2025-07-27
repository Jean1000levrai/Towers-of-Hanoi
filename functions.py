import pile_file as pf

def temp_error_message(canvas, thresold, message = "ERREUR", i = 0):
    global error_message, error_raised
    if i == 0:
        error_message = canvas.create_text(480, 620, text=message,font=("Arial", 20), fill="#AA1111")
    if i<thresold:
        canvas.after(thresold,temp_error_message,canvas, thresold, message, i+1)
    else:
        canvas.delete(error_message)

def hanoi(n, t1, t2, t3, f = pf.File()):
    if n == 1:
        f.enfiler((t1, t3))
        return
    hanoi(n - 1, t1, t3, t2, f)
    f.enfiler((t1, t3))
    hanoi(n - 1, t2, t1, t3, f)

def solve(solution, rectangles):
    if solution.longueur() <= 0:
        return
    move = solution.defiler()
    tower_map = {
        1: rectangles.pile_tower1,
        2: rectangles.pile_tower2,
        3: rectangles.pile_tower3
    }
    if move[0] in tower_map:
        rectangles.selected = tower_map[move[0]].dernier.valeur.image
        if move[1] in tower_map:
            rectangles.move_rec(tower_map[move[1]])

if __name__ == "__main__":  # -----------test----------------
    n = 3
    moves_queue = pf.File()
    hanoi(n, 1, 2, 3, moves_queue)
    print(moves_queue)

    for i in range(moves_queue.longueur()):
        print(moves_queue.defiler())