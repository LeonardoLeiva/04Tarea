#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Programa que plotea las orbitas de un planeta. El metodo usado es euler
'''

from planeta import Planeta
import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure()
fig.clf()

condicion_inicial = [10, 0, 0, 0.25]

Mar_Sara = Planeta(condicion_inicial)
N=3*np.int(1e4)
dt=1000./N
t=np.linspace(0,1000,N)
x=np.zeros(N)
y=np.zeros(N)
E=np.zeros(N)

x[0]=condicion_inicial[0]
y[0]=condicion_inicial[1]
E[0]=Mar_Sara.energia_total()

for n in range(1,N):
    Mar_Sara.avanza_euler(dt)
    x[n]=Mar_Sara.y_actual[0]
    y[n]=Mar_Sara.y_actual[1]
    E[n]=Mar_Sara.energia_total()
print t
print x


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
