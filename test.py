import tkinter as tk

def on_key_press(event):
    print(event.char)
root = tk.Tk()
root.bind("<Key>", on_key_press)
root.mainloop()