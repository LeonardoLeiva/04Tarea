#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Resolucion del problema con alpha distinto de 0. Ademas agrega un metodo para
calcular la velocidad angular
'''

from __future__ import division
from planeta import Planeta
import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure()
fig.clf()

condicion_inicial = [10, 0, 0, 0.25]
alpha = 10**(-2.622) #RUT: 18.668.622-5

Shakuras = Planeta(condicion_inicial, alpha)
N=3*np.int(1e4)
tf=3690. #tf=123 - 124 da una vuelta
dt=tf/N
t=np.linspace(0,tf,N)
x=np.zeros(N)
y=np.zeros(N)
E=np.zeros(N)
r= np.zeros(N)
#phi = np.zeros(N)
#p = [0]

x[0]=condicion_inicial[0]
y[0]=condicion_inicial[1]
E[0]=Shakuras.energia_total()
r[0] = x[0]** 2 + y[0]** 2
#n=1
#phi[0] = np.arctan(y[0]/ x[0])

'''
#codigo fallido
for n in range (1,590) :
    Shakuras.avanza_verlet(dt)
    x[n]=Shakuras.y_actual[0]
    y[n]=Shakuras.y_actual[1]
    E[n]=Shakuras.energia_total()
    r[n] = x[n]** 2 + y[n]** 2



    if x[n] != 0 and x[n-1] != 0:
        a = y[n]/ x[n]
        phi[n] = np.arctan(a)
#    else:
#        phi[]
    if phi[n] < phi[n-1]:
            p.append(n)
#            print n

print p
print len(p)
print phi
'''



for n in range(1,N): #530 corresponde a una orbita, aproximadamente
    Shakuras.avanza_verlet(dt)
    x[n]=Shakuras.y_actual[0]
    y[n]=Shakuras.y_actual[1]
    E[n]=Shakuras.energia_total()
    r[n] = x[n]** 2 + y[n]** 2

#listas para indexar algunos valores que se iran obteniendo

xm = []
ym = []
phi = []
tm = []
w = []


for i in range(1,30):
    T=int(len(x)/30) #periodo
    ti = T*(i-1)
    tf = T*(i)
    a = x[ti: tf]
    b = y[ti: tf]
    c = r[ti: tf]
    d = t[ti: tf]
    n = np.where(c == c.max())
    xm.append(a[n])
    ym.append(b[n])
    tm.append(d[n])
    p = np.arctan(a[n]/ (b[n]))
    phi.append(p)
    if i>=2:
        dphi = phi[i-1] - phi[i-2]
        dt = tm[i-1] - tm[i-2]
        wi = dphi/ dt
        w.append(wi)

W = np.mean(w) #W = -0.00089
print W


ax1=fig.add_subplot(211)
ax1.plot(x,y)
ax2=fig.add_subplot(212)
ax2.plot(t,E)
ax1.set_xlabel('Posicion en el eje X')
ax1.set_ylabel('Posicion en el eje Y')
ax2.set_xlabel('Tiempo')
ax2.set_ylabel('Energia total')
plt.draw()
plt.show()
