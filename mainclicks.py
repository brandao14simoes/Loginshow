import tkinter as tk
import random # Biblioteca para cores e random aleatorio

# Janela para click de contagem
root = tk.Tk()  # Corrigido: 'tk.TK()' para 'tk.Tk()'
root.geometry('500x500')
root.title('Contador de Clicks')
root.configure(background='black')

numero = 0

# Função para gerar uma cor aleatória
def cor_aleatoria():
    return "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Função para atualizar a cor de fundo
def atualizar_cor_fundo():
    root.configure(background=cor_aleatoria())

# Acrescenta numeros em tela
def acrescentar():
    global numero
    numero = numero + 1
    contagem_click.configure(text=numero)  # Corrigido: 'contagem_clicks' para 'contagem_click'
    atualizar_cor_fundo() # Atualiza cor do fundo

# Diminui numeros em tela
def diminuir():
    global numero
    numero = numero - 1
    contagem_click.configure(text=numero)
    atualizar_cor_fundo() # Atualiza cod do fundo
    
# Botões de clicks
botao_acrescentar = tk.Button(root, bg='#FFFFFF', text='+', font=('Montserrat', 16, 'bold'), padx=10, command=acrescentar)  # Corrigidos os erros de formatação e atribuição
botao_acrescentar.pack()

contagem_click = tk.Label(root, text=numero, fg='#FFFFFF', bg='#1d1d1d', font=('Montserrat', 16))
contagem_click.pack()

botao_diminuir = tk.Button(root, bg='#FFFFFF', text='-', font=('Montserrat', 16, 'bold'), padx=10, command=diminuir) # Corrigidos os erros de formatação e atribuição
botao_diminuir.pack()

root.mainloop()
