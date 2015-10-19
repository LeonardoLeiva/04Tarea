#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
G=1
M=1
m=1

class Planeta(object):
    '''
    Complete el docstring.
    '''

    def __init__(self, condicion_inicial, alpha=0):
        '''
        __init__ es un método especial que se usa para inicializar las
        instancias de una clase.

        Ej. de uso:
        >> Aiur = Planeta([x0, y0, vx0, vy0])
        >> print(mercurio.alpha)
        >> 0.
        '''
        self.y_actual = condicion_inicial
        self.t_actual = 0.
        self.alpha = alpha

    def ecuacion_de_movimiento(self,dr=np.array([0,0,0,0])):
        '''
        Implementa la ecuación de movimiento, como sistema de ecuaciónes de
        primer orden.
        '''
        G=1
        M=1
        x, y, vx, vy = self.y_actual
        dx=dr[0]
        dy=dr[1]
        dvx=dr[2]
        dvy=dr[3]
        x=x+dx
        y=y+dy
        vx=vx+dvx
        vy=vy+dvy
        R=np.sqrt(x**2+y**2)
        ax=x*(G*M)*(((2.*self.alpha)/(R**4.))-(1./(R**3.)))
        ay=y*(G*M)*((2.*self.alpha)/(R**4.)-1./(R**3.))
        return np.array([vx, vy, ax, ay])

    def avanza_euler(self, dt):
        '''
        Toma la condición actual del planeta y avanza su posicion y velocidad
        en un intervalo de tiempo dt usando el método de Euler explícito. El
        método no retorna nada, pero re-setea los valores de self.y_actual.
        '''
        yn=self.y_actual + dt*(self.ecuacion_de_movimiento())
        self.y_actual=yn
        self.t_actual+=dt
#        pass

    def avanza_rk4(self, dt):
        '''
        Similar a avanza_euler, pero usando Runge-Kutta 4.
        '''
        k1=dt*self.ecuacion_de_movimiento()
        k2=dt*self.ecuacion_de_movimiento(k1/2.)
        k3=dt*self.ecuacion_de_movimiento(k2/2.)
        k4=dt*self.ecuacion_de_movimiento(k3)
        yn=self.y_actual+(k1+2*k2+2*k3+k4)/6.
        self.y_actual=yn
        self.t_actual=self.t_actual+dt
#        pass

    def avanza_verlet(self, dt):
        '''
        Similar a avanza_euler, pero usando Verlet.
        '''
        r=self.y_actual[0],self.y_actual[1]
        v=self.y_actual[2],self.y_actual[3]
        a=self.ecuacion_de_movimiento[2],self.ecuacion_de_movimiento[3]
        rn=r+dt*v+dt**2*a/2.
        dr=rn-r
        ec_de_mov_dt=self.ecuacion_de_movimiento([dr[0],dr[1],0,0])
        a2=ec_de_mov_dt[2],ec_de_mov_dt[3]
        vn=v+(a+a2)*dt/2.
        self.y_actual=rn[0],rn[1],vn[0],vn[1] #poner como np.array?
#        pass

    def energia_total(self):
        '''
        Calcula la enérgía total del sistema en las condiciones actuales.
        '''
        G=1
        M=1
        m=1
        r=self.y_actual[0],self.y_actual[1]
        v=self.y_actual[2],self.y_actual[3]
        R=np.sqrt(r[0]**2+r[1]**2)
        T=m*(v[0]**2+v[1]**2)/2.
        V=(G*M*m)*(self.alpha/R**2 - 1./R)
        return T+V
#        pass
