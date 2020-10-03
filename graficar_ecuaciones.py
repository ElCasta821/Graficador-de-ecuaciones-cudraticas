# -*- coding: UTF-8 -*-

#==================================================================================
#Alumno: Cesar Ortiz Castañeda
#Grupo: 2-A
#Carrera: Ingenieria de Software
#Contacto: cesortizcasta20@gmail.com

#Código fuente de programa para resolver y graficar ecuaciones cuadraticas,
#utilizando modulos tkinter,math,numpy y matplotlib.
#==================================================================================

from tkinter import *
from tkinter import messagebox
#======================
#VENTANA
#======================
interfaz = Tk()

interfaz.title("Ecuación Cuadratica")
interfaz.geometry("650x400")

frame = Frame()
gif =PhotoImage(file="cuadratica.png")
frame.pack(fill="both", expand="True")
frame.config(bg="blue")


#=======================
#Entrada de valores
#=======================
entrada_a = StringVar()
cuadroTexto = Entry(frame, textvariable=entrada_a)
cuadroTexto.config(justify="right")
cuadroTexto.get()
entrada_b = StringVar()
cuadroTextoDos = Entry(frame, textvariable=entrada_b)
cuadroTextoDos.config(justify="right")
cuadroTextoDos.get()
entrada_c = StringVar()
cuadroTextoTres = Entry(frame, textvariable=entrada_c)
cuadroTextoTres.config(justify="right")
cuadroTextoTres.get()

cuadroTextoTres.place(x=450, y=200)
cuadroTextoDos.place(x=250, y=200)
cuadroTexto.place(x=50, y=200)
#================================
#TEXTO FIJO E IMAGENES
#================================
labelA = Label(frame, text="a :", bg="blue", font=("Comic Sans MS",18))
labelA.place(x=25, y=190)
labelB = Label(frame, text="b :", bg="blue", font=("Comic Sans MS",18))
labelB.place(x=225, y=190)
labelC = Label(frame, text="c :", bg="blue", font=("Comic Sans MS",18))
labelC.place(x=425, y=190)
Label(frame, image=gif).place(x=160, y=10)
xUno = Label(frame, text="X1 :", bg="blue", font=("Comic Sans MS",18))
xUno.place(x=25, y=235)
xDos = Label(frame, text="X2 :", bg="blue", font=("Comic Sans MS",18))
xDos.place(x=21, y=335)

#==================================
#Funcion para resolver ecuación
#Toma como entrada a,b y c
#==================================

def calcular():
   entrada_a = cuadroTexto.get()
   entrada_b = cuadroTextoDos.get()
   entrada_c = cuadroTextoTres.get()
   a = int(entrada_a)
   b = int(entrada_b)
   c = int(entrada_c)
   d = b**2-4*a*c
   if d < 0:
       x1 = complex(-b/(2*a),(-d)**2/(2*a))
       x2 = complex(-b/(2*a),-(-d)**2/(2*a))
   else:
        x1 = round(((-b+d**0.5)/(2*a)), 5)
        x2 = round(((-b-d**0.5)/(2*a)), 5)      

    
   cuadroXUno = Label(frame,text=x1, bg="blue", font=("Comic Sans MS",18) )
   cuadroXUno.place(x=75, y=235)
   cuadroXUno.config(justify="right")
   cuadroXDos = Label(frame, text=x2,bg="blue", font=("Comic Sans MS",18) )
   cuadroXDos.place(x=75, y=335)
   cuadroXDos.config(justify="right")
   
#=============================================
#GRAFICAR FUNCION
#Se toma como entrada las variables de salida (x1,x2) del resultado de la funcion "calcular"
#=============================================

def grafica():

   import math as m
   import numpy as np
   from matplotlib import pyplot
   import matplotlib.pyplot as plt

   entrada_a = cuadroTexto.get()
   entrada_b = cuadroTextoDos.get()
   entrada_c = cuadroTextoTres.get()
   a = int(entrada_a)
   b = int(entrada_b)
   c = int(entrada_c)
   d = b**2-4*a*c

  

   disc=(b**2)-(4*a*c)
   raiz=(disc)**(0.5)


   if(disc>0):
       x1=((-b)+raiz)/(2*a)
       x2=((-b)-raiz)/(2*a)
       print("x1= ",x1)
       print("x2= ",x2)

   elif(disc==0):
       x1=((-b)+raiz)/(2*a)
       x2=((-b)-raiz)/(2*a)
       print("x1= ",x1)
       print("x2= ",x2)
   else:
       print("Solucion imaginaria")



   def f(x):
       return a*(x**2)+b*x+c

   x= np.array([-10, -5, 0, 5, 10])
   y = f(x)


   x= np.linspace(-10, 10, num=100)
   plt.plot(x, f(x), c="red")
   plt.grid()
   plt.title("Gráfico de f(x)="+entrada_a+"x**2 + "+entrada_b+"x + "+entrada_c)
   plt.ylabel("f(x)")
   plt.xlabel("x")
   plt.show()
    
#==============================================
#BOTONOES
#Se vinculan a las funciones correspondientes con el atributo "command"
#==============================================    
botonCalcular = Button(frame, text="CALCULAR", width=10, command=calcular)
botonCalcular.place(x=250, y=280)

botonGraficar = Button(frame, text="GRAFICAR", width=10, command=grafica)
botonGraficar.place(x=375, y=280)

botonSalir = Button(frame, text="SALIR", width=10, command=interfaz.destroy)
botonSalir.place(x=500, y=280)


interfaz.mainloop()

