import tkinter as tk
from elementos_tkinter import Framecustomizado, LabelImage
from images import CarregaImagem  # Assumindo que `CarregaImagem` está definido corretamente

class Body:
    def __init__(self, principal):
        self.principal = principal
        self.container_frame = Framecustomizado(self.principal, width=400, height=400, bg='blue')
        self.container_frame.grid_propagate(False)
        self.container_frame.grid(row=0, column=0)
        self.card_frames()

    def card_frames(self):
        # Configuração do card
        largura_padrao = 200
        altura_padrao = 300
        card = Framecustomizado(self.container_frame, bg='red', width=largura_padrao, height=altura_padrao)
        card.grid(row=5, column=0)

        # Carregar e exibir a imagem dentro do card
        imagem_path = 'contra.jpg'  # Substitua pelo caminho correto da sua imagem
        imagem_carregada = CarregaImagem(imagem_path)  # Carrega a imagem usando a classe CarregaImagem

        label_exibe_imagem = LabelImage(card, image=imagem_carregada.photo)
        label_exibe_imagem.pack()

class AppGames:
    def __init__(self, root):
        self.root = root
        self.root.title('AppRom')
        self.corpo()

    def corpo(self):
        self.body_app = Body(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = AppGames(root)
    root.mainloop()
