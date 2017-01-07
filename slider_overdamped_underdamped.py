"""
This is a stand alone python program that plots the damped harmonic oscillator.
It starts with the limiting case of all three being approximately critical 
damping. Then you can adjust gamma higher to show the overdamped case or adjust 
gamma lower to show the underdampmed case. You can also adjust the initial
conditions to see the affect on all three curves. For this program, the 
original omega_naught value is set to 1 and not allowed to change.

created by J Cash 10/14/2016
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.15, bottom=0.35)
t = np.arange(0.0, 12.0, 0.001)
# Here we set some initial default values for the initial conditions
w0 = 1
g0 = 1
x0 = 5
v0 = 0

#initial critical
Ac = v0 +  w0*x0
Bc = x0
crit = Ac*t*np.exp(-g0*t) + Bc*np.exp(-g0*t)
l1, = plt.plot(t,crit,lw=2,color='blue')

#initial overdamped
g1 = 1.01
q = np.sqrt(g1**2 - w0**2)
A1 = (x0*(q+g1) + v0)/(2*q)
A2 = (x0*(q-g1) - v0)/(2*q)
over = A1*np.exp(-(g1-q)*t) + A2*np.exp(-(g1+q)*t)
l2, = plt.plot(t, over, lw=2, color='red')
plt.axis([0, 12, -10, 10])

#initial underdamped
g2=0.99
wd=np.sqrt(w0**2 - g2**2)
Au = np.sqrt(((v0 + x0*g2)**2)/(wd**2)  + x0**2)
phi = np.arctan((x0*wd)/(v0+x0*g2))
under = np.exp(-g2*t)*Au*np.sin(wd*t + phi)
l3, = plt.plot(t,under,lw=2,color='green')

#setup Slider axes areas
axcolor = 'Lavender'
axpos = plt.axes([0.25, 0.25, 0.65, 0.03], axisbg=axcolor)
axvel = plt.axes([0.25, 0.2, 0.65, 0.03], axisbg=axcolor)
axgam1 = plt.axes([0.25, 0.15, 0.65, 0.03], axisbg=axcolor)
axgam2 = plt.axes([0.25, 0.10, 0.65, 0.03], axisbg=axcolor)

#initialize Slider widgets
spos = Slider(axpos, 'Initial Position', 0, 10.0, valinit=x0)
svel = Slider(axvel, 'Initial Velocity', 0, 10.0, valinit=v0)
sgam1= Slider(axgam1,'Gamma Over',1.01,5,valinit=1.01)
sgam2= Slider(axgam2,'Gamma Under',0,0.99,valinit=0.99)


#helper function to update the graphs when the slider bars change
def update(val):
    pos = spos.val
    vel = svel.val
    gamma1 = sgam1.val
    gamma2 = sgam2.val
    
    #plot for the critical damping
    Ac = vel +  w0*pos
    Bc = pos
    l1.set_ydata(Ac*t*np.exp(-g1*t) + Bc*np.exp(-g1*t))
    
    #plot for the overdamped case
    q = np.sqrt(gamma1**2 - w0**2)
    A1 = (pos*(q+gamma1) + vel)/(2*q)
    A2 = (pos*(q-gamma1) - vel)/(2*q)
    l2.set_ydata(A1*np.exp(-(gamma1-q)*t) + A2*np.exp(-(gamma1+q)*t))

    #plot for the underdamped case
    wd=np.sqrt(w0**2 - gamma2**2)
    Au = np.sqrt(((vel + pos*gamma2)**2)/(wd**2)  + pos**2)
    phi = np.arctan((pos*wd)/(vel+pos*gamma2))
    l3.set_ydata(np.exp(-gamma2*t)*Au*np.sin(wd*t + phi))
        
    fig.canvas.draw_idle()
    
#commands that will monitor the slider bars and call the helper function 
spos.on_changed(update)
svel.on_changed(update)
sgam1.on_changed(update)
sgam2.on_changed(update)


#initialize the Button widget (including setting the location)
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

#helper function that resets the Slider values when the button is clicked
def reset(event):
    spos.reset()
    svel.reset()
    sgam1.reset()
    sgam2.reset()
button.on_clicked(reset)


plt.show()
