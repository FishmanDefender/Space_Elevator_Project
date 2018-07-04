import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = plt.axes(xlim=(0, 2*np.pi), ylim=(-1.5, 1.5))

x = np.arange(0, 2*np.pi, 100)
line, = plt.plot(x, np.sin(x))

y_data = []

for x in range(0, 200):
    y_data.append(np.cos(np.arange(0, 2*np.pi, 0.01)+0.1*x))


def animate(i, y_data):
    y = y_data[0][i]
    line.set_data(x, y)
    return line,


ani = animation.FuncAnimation(fig, animate, 200, fargs=[y_data], interval=50)

plt.show()
