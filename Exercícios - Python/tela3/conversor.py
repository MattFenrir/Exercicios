from tkinter import *
from functools import partial

largura = 400
altura = 250

root = Tk()
root.title('Conversor de Temperatura ')
root.configure(background='#2a9d8f')
root.resizable(False, False)
tempVal = "Celsius"
larguraUser = root.winfo_screenwidth()
alturaUser = root.winfo_screenheight()
posx = int((larguraUser - largura) / 2)
posy = int((alturaUser - largura) / 2 - 20)
root.geometry(f'{largura}x{altura}+{posx}+{posy}')

def store_temp(sel_temp):
    global tempVal
    tempVal = sel_temp

def converter(rlabel1, rlabe12, entrada_var):
    tem = entrada_var.get()
    if tempVal == 'Celsius':
        fahrenheit = float((float(tem) * 9 / 5) + 32)
        kelvin = float((float(tem) + 273.15))
        rlabel1.config(text="%.0f Fahrenheit" %fahrenheit)
        rlabe12.config(text="%.0f Kelvin" %kelvin)
    if tempVal == 'Fahrenheit':
        celsius = float((float(tem) - 32) * 5 / 9)
        kelvin = celsius + 273
        rlabel1.config(text="%.0f Celsius" %celsius)
        rlabe12.config(text="%.0f Kelvin" %kelvin)
    if tempVal == 'Kelvin':
        celsius = float((float(tem) - 273.15))
        fahrenheit = float((float(tem) - 273.15) * 1.8000 + 32.00)
        rlabel1.config(text="%.0f Celsius" %celsius)
        rlabe12.config(text="%.0f Fahrenheit" %fahrenheit)
    return

# Introduzir temperatura
texto = Label(text="Digite a temperatura", background='#2a9d8f', foreground="#FFFFFF")
texto.place(relx=0.1,rely=0.1)
entrada_var = IntVar()

var = Entry(textvariable=entrada_var)
var.place(relx=0.4,rely=0.1)
var.focus()

# Mostrar resultados
result_label1 = Label(root, background='#2a9d8f', foreground="#FFFFFF")
result_label1.place(relx=0.4, rely=0.6)
result_label2 = Label(root, background='#2a9d8f', foreground="#FFFFFF")
result_label2.place(relx=0.4, rely=0.7)

# Lista
var = StringVar()
lista = ["Celsius", "Fahrenheit", "Kelvin"]
oplista = OptionMenu(root, var, *lista, command=store_temp)
var.set(lista[0])
oplista.place(relx=0.4, rely=0.3)
oplista.config(background='#2a9d8f', foreground="#FFFFFF")
oplista["menu"].config(background='#2a9d8f', foreground="#FFFFFF")

converter = partial(converter, result_label1, result_label2, entrada_var)
result_button = Button(root, text="Converter", command=converter, background='#2a9d8f', foreground="#FFFFFF")
result_button.place(relx=0.4, rely=0.5)
mainloop()