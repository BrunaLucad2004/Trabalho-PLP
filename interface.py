from tkinter import *
from tkinter import messagebox
from pyswip import Prolog

# Inicializar Prolog
prolog = Prolog()
prolog.consult("sistema_especialista.pl")  # Certifique-se de que o arquivo Prolog está na mesma pasta.

# Função para realizar consulta
def verificar_compatibilidade():
    doador = entrada_doador.get()
    receptor = entrada_receptor.get()
    
    try:
        resultado = list(prolog.query(f"podedoar({doador.lower()}, {receptor.lower()})"))
        if resultado:
            messagebox.showinfo("Resultado", f"{doador} pode doar para {receptor}.")
        else:
            messagebox.showinfo("Resultado", f"{doador} NÃO pode doar para {receptor}.")
    except Exception as e:
        messagebox.showerror("Erro", "Erro ao realizar consulta. Verifique os nomes inseridos.")

# Função para listar receptores de um doador
def listar_receptores():
    doador = entrada_doador.get()
    try:
        receptores = list(prolog.query(f"podedoar({doador.lower()}, X)"))
        if receptores:
            receptores_str = ", ".join([r['X'] for r in receptores])
            messagebox.showinfo("Receptores", f"{doador} pode doar para: {receptores_str}")
        else:
            messagebox.showinfo("Receptores", f"{doador} não pode doar para ninguém.")
    except Exception as e:
        messagebox.showerror("Erro", "Erro ao realizar consulta. Verifique o nome inserido.")

# Configurar janela
janela = Tk()
janela.title("Sistema Especialista de Doação de Sangue")

# Layout
Label(janela, text="Doador:").grid(row=0, column=0, padx=5, pady=5)
entrada_doador = Entry(janela)
entrada_doador.grid(row=0, column=1, padx=5, pady=5)

Label(janela, text="Receptor:").grid(row=1, column=0, padx=5, pady=5)
entrada_receptor = Entry(janela)
entrada_receptor.grid(row=1, column=1, padx=5, pady=5)

# Botões
Button(janela, text="Verificar Compatibilidade", command=verificar_compatibilidade).grid(row=2, column=0, columnspan=2, pady=10)
Button(janela, text="Listar Receptores", command=listar_receptores).grid(row=3, column=0, columnspan=2, pady=5)

# Rodar janela
janela.mainloop()
