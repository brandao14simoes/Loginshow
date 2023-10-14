# Desenvolvimento de uma Interface PT1
# Import bibliotecas
import sqlite3
from tkinter import *
from tkinter import messagebox
import tkinter as ttk
import matplotlib.pyplot as plt
import databaser

# Função para mostrar o dashboard de barras
def show_dashboard():
    databaser.cursor.execute("SELECT COUNT(*) FROM Users")
    num_registros = databaser.cursor.fetchone()[0]

    # Crie os dados para o grafico de barras
    labels = ['Cadastros'] #, 'Outros']
    sizes = [num_registros, 100 - num_registros]# Assume que há no máximo 100% de "Outros"

    # Cria o Grafico de barras
    plt.figure(figsize=(6, 4))
    plt.bar(labels, sizes,color="Orange", linewidth=0.7)
    plt.plot(labels, color="k", marker="^")
    plt.title('Quantidade de Cadastros')
    plt.show()

# Janela
root = Tk()
root.title('Login Acess Painel') # Título da janela
root.geometry('600x300')
root.configure(background = 'white')
root.resizable(width=False, height=False)
root.attributes("-alpha", 0.9)
root.iconbitmap(default="Login/icons/logoIcon.ico")

# Carregando IMG
logo = PhotoImage(file="Login/icons/logo.png")

# Widgets dos Frames
# Frame da Direita
LeftFrame = Frame(root, width=200, height=300, bg="MIDNIGHTBLUE", relief='raise')
LeftFrame.pack(side=LEFT)

# Frame da Esquerda
RightFrame = Frame(root, width=395, height=300, bg="MIDNIGHTBLUE", relief='raise')
RightFrame.pack(side=RIGHT)

# Label da IMG
LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50, y=100)

# Criação de Usuarios
UserLabel = Label(RightFrame, text="User Name:", font=("Century Gothic", 15), bg="MIDNIGHTBLUE", fg="white")
UserLabel.place(x=3, y=130)

# User Nome
UsernomeEntry = ttk.Entry(RightFrame, width=30)
UsernomeEntry.place(x=3, y=166)

# Entry da Senha
SenhaLabel = Label(RightFrame, text="Senha Usuario:", font=("Century Gothic", 15), bg="MIDNIGHTBLUE", fg="white")
SenhaLabel.place(x=5, y=190)

# User Senha
UserSenhaEntry = ttk.Entry(RightFrame, width=30, show="*")
UserSenhaEntry.place(x=5, y=220)

# Verificação de Login
def login():
    User = UsernomeEntry.get()
    password = UserSenhaEntry.get()

    databaser.cursor.execute("""
    SELECT * FROM Users
    WHERE user = ? and password = ?
    """, (User, password))

    VerifyLogin = databaser.cursor.fetchone() # Verifica o Usuario uma a um

    try:
        if VerifyLogin:
            messagebox.showinfo(title='Login Info', message="Acesso confirmado")
            show_dashboard()  # Chama a função para mostrar o dashboard
        else:
            messagebox.showerror(title="Login Error", message="Acesso negado. Usuário não existe!")
    except Exception as e:
        messagebox.showerror(title="Login Error", message=f"Erro ao verificar o login: {str(e)}") # Mosta erro para usuarios não cadastrados

# Botoões Login
LoginButton = ttk.Button(RightFrame, text="Login", width=10, command=login)
LoginButton.place(x=95, y=260)

# Definindo botões
def Register():
    # Removendo widgets de login e registro
    LoginButton.place(x=6000)
    RegistroButton.place(x=6000)

    # Inseridno widgets de cadastro
    NomeLabel = ttk.Label(RightFrame, text='Name:', font=("Century Gothic", 15), bg="MIDNIGHTBLUE", fg="white")
    NomeLabel.place(x=5, y=20)

    # Nome Entry
    NomeEntry = ttk.Entry(RightFrame, width=30)
    NomeEntry.place(x=4, y=50)

    # Campo E-mail
    EmailLabel = ttk.Label(RightFrame, text='Email:', font=("Century Gothic", 15), bg="MIDNIGHTBLUE", fg="white")
    EmailLabel.place(x=5, y=80)

    #Entry do E-mail
    EmailEntry = ttk.Entry(RightFrame, width=30)
    EmailEntry.place(x=4, y=110)
    
    # Registando informações no Banco
    def RegistertoDBA():
        Name = UsernomeEntry.get()
        Email = EmailEntry.get()
        User = UsernomeEntry.get()
        password = UserSenhaEntry.get()

        if (Name == "" and Email == ""  and User == "" and password ==""):
            messagebox.showerror(title="Register Error", message="Cadastro Incompleto!")
        else:
            databaser.cursor.execute("""
            INSERT INTO Users(name, email, user, password) VALUES (?,?,?,?)
            """, (Name, Email, User, password))
            databaser.conn.commit()
            messagebox.showinfo(title="Registro info", message="Dados Inseridos")

    # Botões de Inserir
    Register = ttk.Button(RightFrame, text="Incluir", width=10, command=RegistertoDBA)
    Register.place(x=5, y=260)

    def backtologin():
        #removendo widgets de cadastro
        NomeLabel.place(x=6000)
        EmailLabel.place(x=6000)
        EmailEntry.place(x=6000)
        NomeEntry.place(x=6000)
        Register.place(x=6000)
        back.place(x=6000)
        # Voltando widgets de login
        LoginButton.place(x=100, y=260)
        RegistroButton.place(x=5, y=260)

    back = ttk.Button(RightFrame, text="Back", width=10, command=backtologin) 
    back.place(x=100, y=260)


# Botoões Registro
RegistroButton = ttk.Button(RightFrame, text="Registrar", width=10, command=Register)
RegistroButton.place(x=5, y=260)


root.mainloop()