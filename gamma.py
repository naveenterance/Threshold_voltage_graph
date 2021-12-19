import math
import matplotlib.pyplot as plt
import numpy as np
import tkinter as Tk

from tkinter import *


def calc():
    v1=float(e1.get())
    v2=float(e2.get())
    v3=float(e3.get())
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
    gamma=100
    def thresvol(gamma,Vsb):
        cox = eox / tox
        ln= (np.log(Na)) - (np.log(ni))
        phif = (vt * ln)
        
        Vfb = phim - xi - (Eg / 2) - phif - (QI / cox)
        Vth = Vfb + (2 * phif) + (gamma * np.sqrt((2 * phif) + Vsb))
        return Vth
    s = gamma
    r= 100 * gamma
    u = 1* gamma
    g1 = np.arange(s,r,u)
    plt.title('VARIATION OF THRESHOLD VOLTAGE WITH GAMMA')
    plt.plot(g1,thresvol(g1,v1),label='First Vsb:'+str(v1))
    plt.plot(g1,thresvol(g1,v2),label='Second Vsb:'+str(v2))
    plt.plot(g1,thresvol(g1,v3),label='Third Vsb:'+str(v3))
    plt.legend()
    plt.xlabel('Gamma')
    plt.ylabel('Threshold voltage')
    plt.grid(True)
    #plt.text(.6e22, .635, v3)
    #plt.text(.6e22, .534, v2)
    #plt.text(.6e22, .369, v1) 
    plt.show()

 
master = Tk()
master.geometry("500x200")
myText=StringVar()
Label(master, text="First Vsb").grid(row=0, sticky=W)
Label(master, text="Second Vsb").grid(row=1, sticky=W)
Label(master, text="Third Vsb").grid(row=2, sticky=W)


result=Label(master, text="", textvariable=myText).grid(row=3,column=1, sticky=W)
 
e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master) 
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
 
b = Button(master, text="Calculate", command=calc)
b.grid(row=0, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)
 
 
mainloop()

