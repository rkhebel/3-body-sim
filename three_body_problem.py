import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # gravitational constant

# Initial conditions
m1, m2, m3 = 1.0, 1.0, 1.0  # masses
x1, y1, x2, y2, x3, y3 = 0.0, 0.0, 1.0, 0.0, -1.0, 0.0  # initial positions
vx1, vy1, vx2, vy2, vx3, vy3 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0  # initial velocities

# Time parameters
t_end = 10.0  # end time
dt = 0.01  # time step

# Lists to store the positions and velocities
xs, ys = [], []
vsx, vsy = [], []

# Main simulation loop
for t in np.arange(0, t_end, dt):
    # Calculate accelerations
    r12 = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    r13 = np.sqrt((x3 - x1)**2 + (y3 - y1)**2)
    r23 = np.sqrt((x3 - x2)**2 + (y3 - y2)**2)

    ax1 = G * m2 * (x2 - x1) / r12**3 + G * m3 * (x3 - x1) / r13**3
    ay1 = G * m2 * (y2 - y1) / r12**3 + G * m3 * (y3 - y1) / r13**3
    ax2 = G * m1 * (x1 - x2) / r12**3 + G * m3 * (x3 - x2) / r23**3
    ay2 = G * m1 * (y1 - y2) / r12**3 + G * m3 * (y3 - y2) / r23**3
    ax3 = G * m1 * (x1 - x3) / r13**3 + G * m2 * (x2 - x3) / r23**3
    ay3 = G * m1 * (y1 - y3) / r13**3 + G * m2 * (y2 - y3) / r23**3

    # Update positions and velocities
    x1, y1, x2, y2, x3, y3 = x1 + vx1 * dt, y1 + vy1 * dt, x2 + vx2 * dt, y2 + vy2 * dt, x3 + vx3 * dt, y3 + vy3 * dt
    vx1, vy1, vx2, vy2, vx3, vy3 = vx1 + ax1 * dt, vy1 + ay1 * dt, vx2 + ax2 * dt, vy2 + ay2 * dt, vx3 + ax3 * dt, vy3 + ay3 * dt

    # Store the positions and velocities
    xs.append(x1)
    ys.append(y1)
    vsx.append(vx1)
    vsy.append(vy1)

# Plot the results
plt.plot(xs, ys)
plt.xlabel('x')
plt.ylabel('y')
plt.title('3-Body Problem Simulation')
plt.show()
