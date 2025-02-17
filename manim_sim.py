from manimlib import *
import numpy as np
import random

class Mass:
    def __init__(self, position, velocity, color, radius=0.2, mass=1):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.color = color
        self.radius = radius
        self.mass = mass

    def update_position(self, dt):
        self.position += self.velocity * dt  # Update position based on velocity

class System:
    def __init__(self, masses):
        self.masses = masses

    def update(self, dt):
        for mass in self.masses:
            net_force = np.array([0.0, 0.0, 0.0])  # Reset net force
            for other_mass in self.masses:
                if mass != other_mass:
                    force = self.compute_grav_force(mass, other_mass)
                    net_force += force

            # Update velocity and position
            mass.velocity += (net_force / mass.mass) * dt
            mass.update_position(dt)

    def compute_grav_force(self, mass, other_mass):
        G = 1e-1  # Scaled gravitational constant
        displacement = other_mass.position - mass.position
        distance = np.linalg.norm(displacement)
        if distance == 0:
            return np.array([0.0, 0.0, 0.0])  # Avoid division by zero
        force_magnitude = G * (mass.mass * other_mass.mass) / (distance**2)
        force_direction = displacement / distance
        return force_magnitude * force_direction

class NBodySimulation(Scene):
    def construct(self):        
        # Write title
        text = Text("N-Body Simulation")
        text.to_edge(UP)
        self.play(
            Write(text)
        )
        
        # Initialize masses
        colors = [RED, GREEN, BLUE, YELLOW, GOLD, ORANGE, PINK, PURPLE, MAROON, TEAL]
        NUM_MASSES = 3
        masses = [
            Mass(
                position=[-1, 0, 0],
                velocity=[0, 0.5, 0],
                color=colors[0],
                radius=.1,
                mass=2
            ),
            Mass(
                position=[1, 0, 0],
                velocity=[0, -0.5, 0],
                color=colors[1],
                radius=.1,
                mass=2
            ),
            Mass(
                position=[0, 2, 0],
                velocity=[.3, 0, 0],
                color=colors[2],
                radius=.1,
                mass=2
            )
        ]
        
        system = System(masses)

        # Create dots and tracers
        dots = [Dot(point=mass.position, color=mass.color, radius=mass.radius) for mass in masses]
        tracers = [TracedPath(dot.get_center, stroke_width=2, color=dot.color) for dot in dots]

        # Add dots and tracers to the scene
        self.add(*dots, *tracers)

        # Updater for each dot
        def update_dot(dot, mass):
            def updater(mob, dt):
                system.update(dt)  # Update the system
                mob.move_to(mass.position)  # Move the dot to the updated position
            return updater

        # Attach updaters to each dot
        for dot, mass in zip(dots, masses):
            dot.add_updater(update_dot(dot, mass))

        # Let the animation run for 60 seconds
        self.wait(60)