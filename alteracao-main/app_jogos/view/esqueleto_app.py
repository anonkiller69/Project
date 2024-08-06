from tkinter import ttk
import tkinter as tk
from elementos_tkinter import Labelcustomizada, Buttoncustomizado, CheckButtoncustomizado, LabelcustomizadaTitulo, Mensagens, Framecustomizado



class Header:
    pass

class Body:
    def __init__(self, root):
        self.root = root
        self.container_frame = Framecustomizado(self.root, width=400, height=400, bg='blue')
        self.container_frame.grid_propagate(False)
        self.container_frame.grid(row=0, column=0)
        
    
class AppGames:
    def __init__(self, root):
        self.root = root
        self.root.title('AppRom')
        self.principal()
    
    def principal(self):
        self.body_app = Body(self.root)

root = tk.Tk()
app = AppGames(root)
root.mainloop()
    

        