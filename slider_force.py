import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

#setup the plotting area
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.15, bottom=0.35)

# Here we start with initial parameters hard coded
x0 = 5
v0 = 0
F0 = 1
m = 1
w0 = 1


#Then we start initial dafault values for the ones I will allow to change
gamma0=0.1
omegaf=0.5

gamma=gamma0
wf=omegaf


#setup the time array
t = np.arange(0.0, 100.0, 0.001)



#calculate the various parameters in the final equations
wd=np.sqrt(w0**2-gamma**2)
amp = (F0/m)/np.sqrt((w0**2-wf**2)**2 + (2*gamma*wf)**2)
phi = np.arctan((2*gamma*wf)/(w0**2-wf**2))
sphi=np.sin(phi)
cphi=np.cos(phi)
phih = np.arctan((wd*(x0-amp*cphi))/(gamma*(x0-amp*cphi)-amp*wf*sphi))
amph = (x0 - amp*np.cos(phi))/(np.sin(phih))

#calculate the two parts (transient and steady state)
s1 = amph*np.exp(-gamma*t)*np.sin(wd*t + phih)
s2 = amp*np.cos(wf*t - phi)
s=s1+s2

#make intial plots
l, = plt.plot(t, s, lw=2, color='red')
l2, = plt.plot(t,s1,lw=0.5,color='blue')
l3, = plt.plot(t,s2,lw=0.5,color='green')
plt.axis([0, 100, -10, 10])



#setup the slider bars
axcolor = 'Lavender'
axfreq = plt.axes([0.25, 0.2, 0.65, 0.03], axisbg=axcolor)
axgam = plt.axes([0.25, 0.1, 0.65, 0.03], axisbg=axcolor)

#setup the ranges and default values for the sliders
sfreq = Slider(axfreq, 'Freq', 0.1, 3.0, valinit=omegaf)
sgam= Slider(axgam,'Gamma',0.01,0.999,valinit=gamma0)




def update(val):
    #recalculate the parameters
    wf = sfreq.val
    gamma = sgam.val
    wd=np.sqrt(w0**2-gamma**2)
    amp = (F0/m)/np.sqrt((w0**2-wf**2)**2 + (2*gamma*wf)**2)
    phi = np.arctan((2*gamma*wf)/(w0**2-wf**2))
    sphi=np.sin(phi)
    cphi=np.cos(phi)
    phih = np.arctan((wd*(x0-amp*cphi))/(gamma*(x0-amp*cphi)-amp*wf*sphi))
    amph = (x0 - amp*np.cos(phi))/(np.sin(phih))
    #recalculate the two parts
    s1 = amph*np.exp(-gamma*t)*np.sin(wd*t + phih)
    s2 = amp*np.cos(wf*t - phi)
    #update the plots
    l.set_ydata(s1+s2)
    l2.set_ydata(s1)
    l3.set_ydata(s2)
    fig.canvas.draw_idle()
sfreq.on_changed(update)
sgam.on_changed(update)

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')


def reset(event):
    sfreq.reset()
    sgam.reset()
button.on_clicked(reset)



plt.show()
