import tkinter as tk
from tkinter import ttk

# Criar a janela principal
root = tk.Tk()
root.title("Exemplo de Scrollbar no Tkinter")

# Criar um frame para conter o Text widget e a Scrollbar
frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Criar um widget Text
text = tk.Text(frame, wrap=tk.NONE)
text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Criar uma Scrollbar vertical
scrollbar_y = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=text.yview)
scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

# Associar a Scrollbar ao Text widget
text.config(yscrollcommand=scrollbar_y.set)

# Inserir algum texto no widget Text para demonstração
for i in range(100):
    text.insert(tk.END, f"Linha {i+1}\n")

# Executar a aplicação
root.mainloop()
