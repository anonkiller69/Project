from tkinter import ttk
import tkinter as tk
from elementos_tkinter import Labelcustomizada, Buttoncustomizado, CheckButtoncustomizado, LabelcustomizadaTitulo, Mensagens, Framecustomizado, LabelImage
from images import CarregaImagem


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
    def card_frames(self):
        #config de card
        self.largura_padrao = 200
        self.altura_padrao = 300
        self.card = Framecustomizado(self.container_frame, bg='red', width=self.largura_padrao, height=self.altura_padrao)
        self.card.grid(row=5, column=0)

        self.label_exibe_imagem = LabelImage(self.card, image = CarregaImagem('contra.jpg'))



    
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
    

        