from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk

class CarregaImagem:
    def __init__(self, url_imagem):
        self.url_imagem = url_imagem
        self.width_padrao = 200
        self.height_padrao = 200
        self.base_path = "C:/Users/mateu/Project/alteracao-main/app_jogos/view/"
        self.image = Image.open(self.base_path + self.url_imagem).resize((self.width_padrao, self.width_padrao))
        self.photo = ImageTk.PhotoImage(self.image)
        