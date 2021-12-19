import math
import matplotlib.pyplot as plt
import numpy as np
import tkinter as Tk

from tkinter import *


def calc():
    v1=float(e1.get())
    v2=float(e2.get())
  
    eox = float(3.9 * 8.854 * (math.pow(10,-14)))
    esi = float(11.9 * 8.854 * (math.pow(10,-14)))
    xi = 4.05
    phim = 4.1
    Eg = 1.12
    ni = 1.5 * (math.pow(10,10))
    q = 1.6 * (math.pow(10,-19))
    vt = .026
    Na = 1*math.pow(10,20)
    QI = 1*math.pow(10,-8)
    tox = 1*math.pow(10,-9)
    def threshold(tox,Vsb):
        cox = eox / tox
        ln= (np.log(Na)) - (np.log(ni))
        phif = (vt * ln)
        gamma = (np.sqrt(2 * q * esi * Na)) / cox
        Vfb = phim - xi - (Eg / 2) - phif - (QI / cox)
        Vth = Vfb + (2 * phif) + (gamma * np.sqrt((2 * phif) + Vsb))
        return Vth
    x = tox
    y = 1000*tox
    z = 1*tox
    tox1 = np.arange(x,y,z)
    plt.title('VARIATION OF THRESHOLD VOLTAGE WITH OXIDE THICKNESS')
    plt.plot(tox1,threshold(tox1,v1),label='First Vsb :'+str(v1))
    plt.plot(tox1,threshold(tox1,v2),label='Second Vsb :'+str(v2))
    plt.legend()
   
    plt.xlabel('Oxide Thickness')
    plt.ylabel('Threshold Voltage')
    plt.grid(True)
    #plt.text(.0000006, 10, v2)
    #plt.text(.0000006, 20, v1)
    plt.show()
    
 
master = Tk()
master.geometry("500x200")
myText=StringVar()

Label(master, text="First Vsb").grid(row=0, sticky=W)
Label(master, text="Second Vsb").grid(row=1, sticky=W)




 
e1 = Entry(master)
e2 = Entry(master)
 
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

 
b = Button(master, text="Draw the vt-oxide thickness graph", command=calc)
b.grid(row=0, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)
 
 
mainloop()
