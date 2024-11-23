 import matplotlib.pyplot as pimport matplotlib.pyplot as plt
 import matplotlib.animation as animation

 fig, ax = plt.subplots()
 ax.set_xlim(-1, 2)
 ax.set_ylim(-1, 2)
 point, = ax.plot([], [], 'o')

 def init():
     point.set_data([], [])
     return point,

 def animate(i):
     x = i % 2
     y = i % 2
     point.set_data(x, y)
     return point,

 ani = animation.FuncAnimation(
     fig, animate, frames=4, interval=500, init_func=init
 )

 plt.show()import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
ax.set_xlim(-1, 2)
ax.set_ylim(-1, 2)
point, = ax.plot([], [], 'o')

def init():
    point.set_data([], [])
    return point,

def animate(i):
    x = i % 2
    y = i % 2
    point.set_data(x, y)
    return point,

ani = animation.FuncAnimation(
    fig, animate, frames=4, interval=500, init_func=init
)

plt.show()
