#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 04:16:22 2021

@author: arantt3
"""

import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import time
import sympy as sym
import scipy as sp

# setting up time 
TIME = 4*np.pi
Nt = 10000
time = np.linspace(0, TIME, Nt)

#t = sym.Symbol('t')

# Constant terms for angle and angular velocity 
angle = np.pi / 4
angularVelocity = 1

# Masses 
m1 = 1
m2 = 1
m3 = 1

# distance from origin to particle 
b = 1
r1 = b
r2 = b

# Basis vector
e1dot = np.array([ np.cos(angularVelocity * time), np.cos(angle) * np.sin(angularVelocity * time), -np.sin(angle)*np.sin(angularVelocity * time) ])
e2dot = np.array([ -np.sin(angularVelocity * time), np.cos(angle) * np.cos(angularVelocity * time), -np.sin(angle)*np.cos(angularVelocity * time) ])                                         
e3dot = np.array([ np.sin(angle), np.cos(angle) ])

# moment of inertia 
I = np.array([ [(m1+m2)*b**2, 0, 0], [0, (m1+m2)*b**2, 0], [0, 0, 0] ])

# components for anugular velocity
w = np.array([0, angularVelocity*np.sin(angle), angularVelocity*np.cos(angle)])

# angular momentum
L = np.zeros([3])
L = I.dot(w)

# Applying basis vector to make it change with time 

angularMomentum = []

angularMomentum1 = []
angularMomentum1 = L[1] * e1dot[1] 
angularMomentum.append(angularMomentum1)

angularMomentum2 = []
angularMomentum2 = L[1] * e2dot[1] 
angularMomentum.append(angularMomentum2)

angularMomentum3 = []
for i in range(0, Nt):
    angularMomentum3.append(L[1] * e3dot[1])
angularMomentum.append(angularMomentum3)

#print angularMomentum

# Torque (Not sure how to take derivative so I'm going write it out how from what I got analytically, if you could show me how I would, it would much appreciated)
torque = []

torque1 = []
torque1 = L[1] * np.cos(angle) * np.cos(angularVelocity * time)
torque.append(torque1)

torque2 = []
torque2 = -L[1] * np.cos(angle) * np.sin(angularVelocity * time)
torque.append(torque2)

torque3 = []
for i in range(0, Nt):
    torque3.append(0)
torque.append(torque3)

#print torque


# plotting angular momentum

plt.plot(time, angularMomentum[0], lw='0.8', label = "Angular Momentum axis e1")
plt.plot(time, angularMomentum[1], lw='0.8', label = "Angular Momentum axis e2")
plt.plot(time, angularMomentum[2], lw='0.8', label = "Angular Momentum axis e3")

plt.xlabel('Time')
plt.ylabel('Angular Momentum')
plt.title('Anugular Momentum vs Time')
#plt.xlim(-25,25)
#plt.ylim(-5,5)
plt.legend()
plt.show()


# plotting torque

plt.plot(time, torque[0], lw='0.8', label = "Torque axis e1")
plt.plot(time, torque[1], lw='0.8', label = "Torque axis e2")
plt.plot(time, torque[2], lw='0.8', label = "Torque axis e3")

plt.xlabel('Time')
plt.ylabel('Torque')
plt.title('Torque vs Time')
#plt.xlim(-25,25)
#plt.ylim(-5,5)
plt.legend()
plt.show()