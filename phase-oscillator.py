"""
This is a stand alone python program that plots the phase plot for a damped
oscillator. It starts with the limiting case of 
all three being approximately critical 
damping. Then you can adjust gamma higher to show the overdamped case or adjust 
gamma lower to show the underdampmed case. You can also adjust the initial
conditions to see the affect on all three curves. For this program, the 
original omega_naught value is set to 1 and not allowed to change.

created by J Cash 10/19/2016
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

#setup the plotting area
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.15, bottom=0.35)

# Here we start with initial parameters hard coded
x0 = 5
v0 = 0
w0 = 1


#Then we start initial dafault values for the ones I will allow to change
gamma0=0.01


#setup the time array
t = np.arange(0.0, 100.0, 0.001)



#initial parameters and plots
gam=gamma0
pos=x0
vel=v0

wd=np.sqrt(w0**2 - gam**2)
Au = np.sqrt(((vel + pos*gam)**2)/(wd**2)  + pos**2)
phi = np.arctan((pos*wd)/(vel+pos*gam))
x = np.exp(-gam*t)*Au*np.sin(wd*t + phi)
v = -1*Au*np.exp(-gam*t)*(gam*np.sin(wd*t + phi)-wd*np.cos(wd*t + phi))
l, = plt.plot(x,v,color='green')
#l, = plt.plot(t,v)


#setup Slider axes areas
axcolor = 'Lavender'
axpos = plt.axes([0.25, 0.25, 0.65, 0.03], axisbg=axcolor)
axvel = plt.axes([0.25, 0.2, 0.65, 0.03], axisbg=axcolor)
axgam = plt.axes([0.25, 0.15, 0.65, 0.03], axisbg=axcolor)


#initialize Slider widgets
spos = Slider(axpos, 'Initial Position', -5, 5.0, valinit=x0)
svel = Slider(axvel, 'Initial Velocity', -5, 5.0, valinit=v0)
sgam= Slider(axgam,'Gamma',0,0.999,valinit=gamma0)



#helper function to update the graphs when the slider bars change
def update(val):
    pos = spos.val
    vel = svel.val
    gam = sgam.val
    
    wd=np.sqrt(w0**2 - gam**2)
    Au = np.sqrt(((vel + pos*gam)**2)/(wd**2)  + pos**2)
    phi = np.arctan((pos*wd)/(vel+pos*gam))
    x = np.exp(-gam*t)*Au*np.sin(wd*t + phi)
    v = -1*Au*np.exp(-gam*t)*(gam*np.sin(wd*t + phi)-wd*np.cos(wd*t + phi))
    l.set_ydata(v)
    l.set_xdata(x)
         
    fig.canvas.draw_idle()
    
#commands that will monitor the slider bars and call the helper function 
spos.on_changed(update)
svel.on_changed(update)
sgam.on_changed(update)



#initialize the Button widget (including setting the location)
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

#helper function that resets the Slider values when the button is clicked
def reset(event):
    spos.reset()
    svel.reset()
    sgam.reset()
button.on_clicked(reset)


plt.show()

    
    