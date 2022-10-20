from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview

def info(msg):
    messagebox.showinfo(title='Mensagem', message=msg)  

def limparCampo():
    txtQuantidade.delete(0, END)

def inserir():
    if len(txtQuantidade.get().strip()) < 1:
        info('Preencha o campo corretamente.')
    limparCampo()

def finalizar():
    pass

def deletar():
    pass

run = Tk()
run.title('Agenda')
run.geometry('+1200+120')

lista = [['Espada', 'R$3000'], ['Escudo', 'R$2500'], ['Machado', 'R$3500']]

Label(run, text='Total da Compra').grid(row=0, column=0)

txtQuantidade = Entry(run)
txtQuantidade.grid(row=1, column=0)

Button(run, text='Inserir', command=inserir).grid(row=5, column=0, pady=10)
Button(run, text='Ver', command=finalizar).grid(row=5, column=1, pady=10)
Button(run, text='Deletar', command=deletar).grid(row=5, column=2, pady=10)

tabela = Treeview(run, columns=(0, 1, 2, 3), show='headings')

tabela.column(0, minwidth=40, width=50)
tabela.column(1, minwidth=150, width=350)
tabela.column(2, minwidth=80, width=150)
tabela.column(3, minwidth=80, width=150)

tabela.heading(0, text='Nome do produto')
tabela.heading(1, text='Preço_Unit')
tabela.heading(2, text='Qnt')
tabela.heading(3, text='Total')

tabela.grid(row=4, columnspan=3, pady=10, padx=10)

run.mainloop()