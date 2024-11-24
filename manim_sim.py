from manim import *
import random

class Mass:
    def __init__(self, position, velocity, color, radius=0.2, mass=1):
        self.position = position
        self.velocity = velocity
        self.color = color
        self.radius = radius
        self.mass = mass
        self.trail = []

    def update_position(self, dt):
        self.trail.append(self.position)
        self.position[0] += self.velocity[0] * dt
        self.position[1] += self.velocity[1] * dt

        if len(self.trail) > 10:
            self.trail.pop(0)

class System:
    def __init__(self, masses):
        self.masses = masses

    def update(self, dt):
        for mass in self.masses:
            net_force_x, net_force_y = 0, 0
            for other_mass in self.masses:
                if mass != other_mass:
                    force_x, force_y = self.compute_grav_force(mass, other_mass)
                    net_force_x += force_x
                    net_force_y += force_y
            
            mass.velocity[0] += (net_force_x / mass.mass) * dt
            mass.velocity[1] += (net_force_y / mass.mass) * dt
            mass.update_position(dt)

    def compute_grav_force(self, mass, other_mass):
        G = 6.67430e-11
        dx = other_mass.position[0] - mass.position[0]
        dy = other_mass.position[1] - mass.position[1]
        distance = np.sqrt(dx**2 + dy**2)
        if distance == 0:
            return 0, 0
        force = G * (mass.mass * other_mass.mass) / (distance**2)
        angle = np.arctan2(dy, dx)
        force_x = force * np.cos(angle)
        force_y = force * np.sin(angle)
        return force_x, force_y

class MassScene(Scene):
    def construct(self):
        masses = [
            Mass(
                position=[random.uniform(-3, 3), random.uniform(-3, 3), 0],
                velocity=[0, 0, 0],
                color=BLUE,
                radius=0.2,
                mass=1e16
            ) for _ in range(3)
        ]
        system = System(masses)

        dots = [Dot(point=mass.position, color=mass.color, radius=mass.radius) for mass in masses]
        self.add(*dots)

        # Animation loop
        for _ in range(100):
            dt = 0.1
            system.update(dt)
            for i, mass in enumerate(masses):
                dots[i].move_to(mass.position)
                if len(mass.trail) > 0:
                    trail_dots = [Dot(point=pos, color=mass.color, radius=0.05) for pos in mass.trail]
                    self.add(*trail_dots)
            self.wait(dt)
