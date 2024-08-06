from tkinter import ttk
import tkinter as tk
from elementos_tkinter import Labelcustomizada, Buttoncustomizado, CheckButtoncustomizado, LabelcustomizadaTitulo, Mensagens, Framecustomizado



class Header:
    pass

        
        

class Body:
    def __init__(self, principal):
        self.principal = principal
        self.container_frame = Framecustomizado(self.principal, width=400, height=400, bg='blue')
        self.container_frame.grid_propagate(False)
        self.container_frame.grid(row=0, column=0)
        self.card_frame()

    #as imagens e os jogos estarão dentro de um frame
    def card_frame(self):
        self.card = Framecustomizado(self.container_frame, bg='red', width=200, height=200)
        self.card.grid(row=5, column=0)


        
    
class AppGames:
    def __init__(self, root):
        self.root = root
        self.root.title('AppRom')
        self.corpo()
    
    def corpo(self):
        self.body_app = Body(self.root)

root = tk.Tk()
app = AppGames(root)
root.mainloop()
    

        