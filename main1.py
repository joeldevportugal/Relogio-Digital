# Importar módulos necessários ---------------------------------------------------------------------------------------------------------------
import customtkinter
import tkinter as tk
from tkinter import ttk
from PIL import ImageColor
import datetime

# Definir as Cores a Usar -------------------------------------------------------------------------------------------------------------------
co0 = '#7F7FFF'  # cor de fundo Azul

#Cria a funçao para actualizar Relogio-------------------------------------------------------------------------------------------------------
def atualizar_relogio():
    # Obter a data e hora do sistema --------------------------------------------------------------------------------------------------------
    data_hora_atual = datetime.datetime.now()

    # Formatar a hora e a data --------------------------------------------------------------------------------------------------------------
    hora_formatada = data_hora_atual.strftime('%H:%M:%S')
    data_formatada = data_hora_atual.strftime('%Y-%m-%d')

    # Atualizar os rótulos de hora e data ---------------------------------------------------------------------------------------------------
    Lhoras['text'] = hora_formatada
    Ldata['text'] = data_formatada

    # Atualizar a janela a cada 1000 milissegundos (1 segundo) ------------------------------------------------------------------------------
    Janela.after(1000, atualizar_relogio)
# função para actualizar cores --------------------------------------------------------------------------------------------------------------
def atualizar_cores(event):
    # Obter valores dos sliders--------------------------------------------------------------------------------------------------------------
    valor_vermelho = int(svermelho.get())
    valor_verde = int(sverde.get())
    valor_Azul = int(sAzul.get())

    # Atualizar as labels de cor conforme os valores dos sliders ---------------------------------------------------------------------------
    Lvermelho.configure(text=f'Vermelho: {valor_vermelho:02}')
    Lverde.configure(text=f'Verde: {valor_verde:02}')
    LAzul.configure(text=f'Azul: {valor_Azul:02}')

    # Criar a string da cor ---------------------------------------------------------------------------------------------------------------
    cor_string = f'#{valor_vermelho:02X}{valor_verde:02X}{valor_Azul:02X}FF'  # Adicionando valor de alfa
    color_var.set(cor_string)

    # Remover os rótulos existentes e recriá-los ------------------------------------------------------------------------------------------
    criar_rotulos()

def criar_rotulos():
    global Lhoras, Ldata

    # Destruir rótulos antigos ------------------------------------------------------------------------------------------------------------
    if 'Lhoras' in globals() and isinstance(Lhoras, ttk.Label):
        Lhoras.destroy()

    if 'Ldata' in globals() and isinstance(Ldata, ttk.Label):
        Ldata.destroy()

    # Verificar se a variável de cor está definida ----------------------------------------------------------------------------------------
    cor = color_var.get()

    # Tentar converter a cor para um formato aceitável pelo Tkinter -----------------------------------------------------------------------
    try:
        cor_tkinter = '#{:02x}{:02x}{:02x}'.format(*ImageColor.getcolor(cor, "RGBA"))

        # Tentar criar os rótulos
        Lhoras = ttk.Label(Janela, text='00:00:00', font=('arial', 65), foreground=cor_tkinter, background=co0)
        Lhoras.place(x=10, y=10)

        Ldata = ttk.Label(Janela, text='AAAA-MM-DD', font=('arial', 65), foreground=cor_tkinter, background=co0)
        Ldata.place(x=10, y=100)

    except tk.TclError:
        print(f"Erro: Cor inválida - {cor}")
# Criar a janela principal ----------------------------------------------------------------------------------------------------------------
Janela = customtkinter.CTk()
Janela.geometry('450x380+100+100')
Janela.title('Relógio Digital com Alteração de Tema')
Janela.resizable(False, False)
Janela.config(bg=co0)
Janela.iconbitmap('icon.ico')

# Variável de controle para a cor --------------------------------------------------------------------------------------------------------
color_var = tk.StringVar()
color_var.set("#000000")  # Cor inicial

# Criar os sliders para alterar a cor-----------------------------------------------------------------------------------------------------
svermelho = ttk.Scale(Janela, from_=0, to=255, orient="horizontal", command=atualizar_cores, length=560, style="custom.Horizontal.TScale")
svermelho.place(x=0, y=230)

sverde = ttk.Scale(Janela, from_=0, to=255, orient="horizontal", command=atualizar_cores, length=560, style="custom.Horizontal.TScale")
sverde.place(x=0, y=305)

sAzul = ttk.Scale(Janela, from_=0, to=255, orient="horizontal", command=atualizar_cores, length=560, style="custom.Horizontal.TScale")
sAzul.place(x=0, y=390)

# Definir o estilo para os sliders------------------------------------------------------------------------
style = ttk.Style()
style.configure("custom.Horizontal.TScale", troughcolor=co0, sliderlength=20, background=co0)

# Criar as labels para identificar as cores---------------------------------------------------------------
Lvermelho = ttk.Label(Janela, text='Vermelho:00', font=('arial 12'), background=co0)
Lvermelho.place(x=0, y=205)

Lverde = ttk.Label(Janela, text='Verde:00', font=('arial 12'),background=co0)
Lverde.place(x=0, y=275)

LAzul = ttk.Label(Janela, text='Azul:00', font=('arial 12'), background=co0)
LAzul.place(x=0, y=365)

# Inicialmente, criar os rótulos -------------------------------------------------------------------------
criar_rotulos()
#---------------------------------------------------------------------------------------------------------
# Iniciar a função de atualização do relógio -------------------------------------------------------------
atualizar_relogio()
#--------------------------------------------------------------------------------------------------------
# Iniciar a execução da janela---------------------------------------------------------------------------
Janela.mainloop()
#--------------------------------------------------------------------------------------------------------