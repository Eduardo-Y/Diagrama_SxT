from tkinter import *
from tkinter import ttk
from grafico import Corpo, diagrama_SxT

root = Tk()
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.configure(background='black')

style = ttk.Style()
style.configure('TFrame', background='black')

frm = ttk.Frame(root, padding=20)
frm.grid()

def printar_entradas():
    for obj in objs:
        print(f'| Velocidade: {obj[2].get()} | Posição Inicial: {obj[3].get()} |')
    print()

def adicionar_objeto():
    nova_label1 = ttk.Label(frm, text="Velocidade:", background='black', foreground='white')
    nova_label1.grid(column=0, row=len(objs)+1, sticky='NSEW', pady=10)
    nova_velocidade = ttk.Entry(frm, width=width_input)
    nova_velocidade.grid(column=1, row=len(objs)+1, pady=10, padx=10)

    nova_label2 = ttk.Label(frm, text="Posição Inicial:", background='black', foreground='white')
    nova_label2.grid(column=2, row=len(objs)+1, sticky='NSEW', pady=10)
    nova_posicao = ttk.Entry(frm, width=width_input)
    nova_posicao.grid(column=3, row=len(objs)+1, pady=10)
    
    objs.append((nova_label1, nova_label2, nova_velocidade, nova_posicao))

def remover_objeto():
    try:
<<<<<<< HEAD
        ttk.Label(frm, text=' ', background='black', foreground='white', anchor='center').grid(column=0, row=22,columnspan=4, sticky='NSEW', pady=10)
=======
>>>>>>> 4eef476 (Adionando funcionalidades de 'remover objeto', 'gerar gráfico' e o input da variável tempo)
        objs[-1][0].destroy()
        objs[-1][1].destroy()
        objs[-1][2].destroy()
        objs[-1][3].destroy()
<<<<<<< HEAD
        objs.pop()

    except AttributeError:
        ttk.Label(frm, text='Não é possivel remover o primeiro Objeto.', background='black', foreground='white', anchor='center').grid(column=0, row=22,columnspan=4, sticky='NSEW', pady=10)

style = ttk.Style()
style.configure('TFrame', background='black')

def gerar_grafico(t):
    try:
        ttk.Label(frm, text="", background='black', foreground='white', anchor='center').grid(column=0, row=22, columnspan=4, sticky='NSEW', pady=10)
        corpos = [Corpo(float(obj[2].get()), float(obj[3].get())) for obj in objs]
        diagrama_SxT(tempo=float(t), corpos=corpos)
    except ValueError:
        ttk.Label(frm, text='Valor(es) invalido(s) ou vazio(s)!', background='black', foreground='white', anchor='center').grid(column=0, row=22, columnspan=4, sticky='NSEW', pady=10)
=======

    except AttributeError:
        print('Não é possivel remover o primeiro Objeto.')


def gerar_grafico(t):
    corpos = [Corpo(float(obj[2].get()), float(obj[3].get())) for obj in objs]
    diagrama_SxT(tempo=float(t), corpos=corpos)
>>>>>>> 4eef476 (Adionando funcionalidades de 'remover objeto', 'gerar gráfico' e o input da variável tempo)

width_input = 6

root.title('Diagrama Sxt')
orientacao = ttk.Label(frm, text="Determine as informações iniciais:", background='black', foreground='white', anchor='center')
orientacao.grid(column=0, row=0, columnspan=4, sticky='NSEW', pady=20)
orientacao.configure(font=("Arial", 12, "bold"))

label1 = ttk.Label(frm, text="Velocidade:", background='black', foreground='white').grid(column=0, row=1, sticky='NSEW', pady=10)
velocidade = ttk.Entry(frm, width=width_input)
velocidade.grid(column=1, row=1, pady=10, padx=10)

label2 = ttk.Label(frm, text="Posição Inicial:", background='black', foreground='white').grid(column=2, row=1, sticky='NSEW', pady=10)
posicao_inicial = ttk.Entry(frm, width=width_input)
posicao_inicial.grid(column=3, row=1, pady=10)

objs = [(label1, label2, velocidade, posicao_inicial)]

add_obj = ttk.Button(frm, text="Adicionar Objeto +", command=lambda: adicionar_objeto())
add_obj.grid(column=0, row=20, columnspan=2, pady=10)

rmv_obj = ttk.Button(frm, text="Remover Objeto -", command=lambda: remover_objeto())
rmv_obj.grid(column=2, row=20, columnspan=2, pady=10)

<<<<<<< HEAD
ttk.Label(frm, text="Tempo:", background='black', foreground='white').grid(column=0, row=21, sticky='NSEW', pady=10)
=======
ttk.Label(frm, text="Tempo", background='black', foreground='white').grid(column=0, row=21, sticky='NSEW', pady=10)
>>>>>>> 4eef476 (Adionando funcionalidades de 'remover objeto', 'gerar gráfico' e o input da variável tempo)
time = ttk.Entry(frm, width=width_input, justify='left')
time.grid(column=1, row=21, pady=10, padx=10)

crr_graf = ttk.Button(frm, text="Gerar Gráfico", command=lambda: gerar_grafico(time.get()))
crr_graf.grid(column=2, row=21, columnspan=4, pady=10)

root.mainloop()