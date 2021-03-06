import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.15, bottom=0.35)
t = np.arange(0.0, 10.0, 0.001)
a0 = 5
f0 = 1
g0 = 0
s = a0*np.sin(2*np.pi*f0*t)
l, = plt.plot(t, s, lw=2, color='red')
plt.axis([0, 10, -10, 10])

axcolor = 'Lavender'
axfreq = plt.axes([0.25, 0.2, 0.65, 0.03], axisbg=axcolor)
axamp = plt.axes([0.25, 0.15, 0.65, 0.03], axisbg=axcolor)
axgam = plt.axes([0.25, 0.1, 0.65, 0.03], axisbg=axcolor)

sfreq = Slider(axfreq, 'Freq', 0.1, 3.0, valinit=f0)
samp = Slider(axamp, 'Amp', 0.1, 10.0, valinit=a0)
sgam= Slider(axgam,'Gamma',0,4.0,valinit=g0)


def update(val):
    amp = samp.val
    freq = sfreq.val
    gamma = sgam.val
    omegad=np.sqrt((2*np.pi*freq)**2 - gamma**2)
    l.set_ydata(amp*np.sin(omegad*t)*np.exp(-gamma*t))
    fig.canvas.draw_idle()
sfreq.on_changed(update)
samp.on_changed(update)
sgam.on_changed(update)

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')


def reset(event):
    sfreq.reset()
    samp.reset()
    sgam.reset()
button.on_clicked(reset)

rax = plt.axes([0.025, 0.1, 0.10, 0.15], axisbg=axcolor)
radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)


def colorfunc(label):
    l.set_color(label)
    fig.canvas.draw_idle()
radio.on_clicked(colorfunc)

plt.show()
