from tkinter import *
from tkinter import ttk

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
        print(f'| Velocidade: {obj[0].get()} | Posição Inicial: {obj[1].get()} |')
    print()

def adicionar_objeto():
    ttk.Label(frm, text="Velocidade:", background='black', foreground='white').grid(column=0, row=len(objs)+1, sticky='NSEW', pady=10)
    nova_velocidade = ttk.Entry(frm, width=width_input)
    nova_velocidade.grid(column=1, row=len(objs)+1, pady=10, padx=10)

    ttk.Label(frm, text="Posição Inicial:", background='black', foreground='white').grid(column=2, row=len(objs)+1, sticky='NSEW', pady=10)
    nova_posicao = ttk.Entry(frm, width=width_input)
    nova_posicao.grid(column=3, row=len(objs)+1, pady=10)
    
    objs.append((nova_velocidade, nova_posicao))

width_input = 6

root.title('Diagrama Sxt')
ttk.Label(frm, text="Determine as informações iniciais:", background='black', foreground='white', anchor='center').grid(column=0, row=0, columnspan=4, sticky='NSEW', pady=10)

ttk.Label(frm, text="Velocidade:", background='black', foreground='white').grid(column=0, row=1, sticky='NSEW', pady=10)
velocidade = ttk.Entry(frm, width=width_input)
velocidade.grid(column=1, row=1, pady=10, padx=10)

ttk.Label(frm, text="Posição Inicial:", background='black', foreground='white').grid(column=2, row=1, sticky='NSEW', pady=10)
posicao_inicial = ttk.Entry(frm, width=width_input)
posicao_inicial.grid(column=3, row=1, pady=10)

objs = [(velocidade, posicao_inicial)]

add_obj = ttk.Button(frm, text="Adicionar Objeto", command=lambda: adicionar_objeto())
add_obj.grid(column=0, row=20, columnspan=4, pady=10)
root.mainloop()