import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
G = 6.67430e-11  # Gravitational constant

# Initial conditions: positions (x, y), velocities (vx, vy), and masses
bodies = [
    {'pos': np.array([0.0, 0.0]), 'vel': np.array([0.0, 0.0]), 'mass': 1.0e24},
    {'pos': np.array([1.0, 0.0]), 'vel': np.array([0.0, 1.0]), 'mass': 1.0e24},
    {'pos': np.array([0.0, 1.0]), 'vel': np.array([-1.0, 0.0]), 'mass': 1.0e24}
]

def calculate_force(body1, body2):
    r_vec = body2['pos'] - body1['pos']
    r_mag = np.linalg.norm(r_vec)
    force_mag = G * body1['mass'] * body2['mass'] / r_mag**2
    force_vec = force_mag * r_vec / r_mag
    return force_vec

def update_bodies(bodies, dt):
    forces = [np.zeros(2) for _ in bodies]
    for i, body1 in enumerate(bodies):
        for j, body2 in enumerate(bodies):
            if i != j:
                forces[i] += calculate_force(body1, body2)
    
    for i, body in enumerate(bodies):
        # Update velocities
        body['vel'] += forces[i] / body['mass'] * dt
        # Update positions
        body['pos'] += body['vel'] * dt

# Simulation parameters
dt = 0.01  # Time step
num_steps = 1000

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
lines = [ax.plot([], [], 'o')[0] for _ in bodies]

def init():
    for line in lines:
        line.set_data([], [])
    return lines

def animate(frame):
    update_bodies(bodies, dt)
    for i, body in enumerate(bodies):
        lines[i].set_data([body['pos'][0]], [body['pos'][1]])
    return lines

ani = FuncAnimation(fig, animate, frames=num_steps, init_func=init, blit=True, interval=20)
plt.show()
