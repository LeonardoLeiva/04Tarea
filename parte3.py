#!/usr/bin/env python
# -*- coding: utf-8 -*-

from planeta import Planeta
import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure()
fig.clf()

condicion_inicial = [10, 0, 0, 0.25]
alpha = 10**(-2.622) #RUT: 18.668.622-5

Shakuras = Planeta(condicion_inicial, alpha)
N=3*np.int(1e4)
dt=7000./N
t=np.linspace(0,7000,N)
x=np.zeros(N)
y=np.zeros(N)
E=np.zeros(N)

x[0]=condicion_inicial[0]
y[0]=condicion_inicial[1]
E[0]=Shakuras.energia_total()

for n in range(1,N):
    Shakuras.avanza_verlet(dt)
    x[n]=Shakuras.y_actual[0]
    y[n]=Shakuras.y_actual[1]
    E[n]=Shakuras.energia_total()


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
