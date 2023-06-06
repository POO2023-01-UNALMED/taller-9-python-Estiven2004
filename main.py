from tkinter import Tk, Button, Entry

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("310x260")

ent=""

#Funciones (Eventos)

def operador(evento):
   global ent
   pantalla.insert("end", str(evento.widget["text"]))
   ent += str(evento.widget["text"])
   
def boton(evento):
    global ent
    pantalla.insert("end", str(evento.widget["text"]))
    ent += str(evento.widget["text"])
   
def calcular(evento):
    if "+" in ent:
        partes = ent.split("+")
        resultado = float(partes[0]) + float(partes[1])
        pantalla.delete(0, "end")
        pantalla.insert(0, str(resultado))
    elif "-" in ent:
        partes = ent.split("-")
        resultado = float(partes[0]) - float(partes[1])
        pantalla.delete(0, "end")
        pantalla.insert(0, str(resultado))
    elif "*" in ent:
        partes = ent.split("*")
        resultado = float(partes[0]) * float(partes[1])
        pantalla.delete(0, "end")
        pantalla.insert(0, str(resultado))
    elif "/" in ent:
        partes = ent.split("/")
        resultado = float(partes[0]) / float(partes[1])
        pantalla.delete(0, "end")
        pantalla.insert(0, str(resultado))
    
# Configuración pantalla de salida 
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=40, padx=1, pady=1)

# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=0, padx=1, pady=1)
boton_1.bind("<Button-1>", boton)

boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=1, padx=1, pady=1)
boton_2.bind("<Button-1>", boton)

boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=2, padx=1, pady=1)
boton_3.bind("<Button-1>", boton)

boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=0, padx=1, pady=1)
boton_4.bind("<Button-1>", boton)

boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=1, padx=1, pady=1)
boton_5.bind("<Button-1>", boton)

boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=2, padx=1, pady=1)
boton_6.bind("<Button-1>", boton)

boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=0, padx=1, pady=1)
boton_7.bind("<Button-1>", boton)

boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=1, padx=1, pady=1)
boton_8.bind("<Button-1>", boton)

boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=2, padx=1, pady=1)
boton_9.bind("<Button-1>", boton)

boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2").grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_igual.bind("<Button-1>", calcular)

boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0).grid(row=4, column=2, padx=1, pady=1)
boton_punto.bind("<Button-1>", operador)

boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=1, column=3, padx=1, pady=1)
boton_mas.bind("<Button-1>", operador)

boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=2, column=3, padx=1, pady=1)
boton_menos.bind("<Button-1>", operador)

boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=3, column=3, padx=1, pady=1)
boton_multiplicacion.bind("<Button-1>", operador)

boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=4, column=3, padx=1, pady=1)
boton_division.bind("<Button-1>", operador)

root.mainloop()