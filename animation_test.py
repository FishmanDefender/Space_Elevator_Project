import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# First set up the figure, the axis, and the plot element we want to animate
ffig = plt.figure()
fax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
fline, = fax.plot([], [], lw=2)

# initialization function: plot the background of each frame
def a_init():
    fline.set_data([], [])
    return fline,

# animation function.  This is called sequentially
def a_animate(i):
    fx = np.linspace(0, 2, 1000)
    fy = np.sin(2 * np.pi * (fx - 0.01 * i))
    fline.set_data(fx, fy)
    return fline,

# call the animator.  blit=True means only re-draw the parts that have changed.
a_anim = animation.FuncAnimation(ffig, a_animate, init_func=a_init, frames=200, interval=20, blit=True)

plt.show()
