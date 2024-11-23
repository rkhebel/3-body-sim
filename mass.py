import pygame
import math

class Mass:
    """Class to represent a mass in 2D space."""
    def __init__(self, position, velocity, color, radius=5, mass=1):
        """Initialize a mass with a position, velocity, color, radius, and mass."""
        self.x, self.y = position
        self.vx, self.vy = velocity
        self.color = color
        self.radius = radius
        self.mass = mass

    def update_position(self, dt):
        """Update the position of the mass based on velocity."""
        self.x += self.vx * dt
        self.y += self.vy * dt

    def draw(self, screen):
        """Draw the mass on the Pygame screen."""
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        font = pygame.font.Font(None, 18)
        text = font.render(f"({self.vx:.2f}, {self.vy:.2f})", True, (0, 0, 0))
        text_rect = text.get_rect(center=(int(self.x), int(self.y)))
        screen.blit(text, text_rect)
        
    def compute_grav_force(self, other_mass):
        """Compute the gravitational force between two masses."""
        G = 6.67430e-11  # Gravitational constant
        dx = other_mass.x - self.x
        dy = other_mass.y - self.y
        distance = (dx**2 + dy**2) ** 0.5
        if distance == 0:
            return 0, 0  # Avoid division by zero
        force = G * (self.mass * other_mass.mass) / (distance**2)
        angle = math.atan2(dy, dx)
        force_x = force * math.cos(angle)
        force_y = force * math.sin(angle)
        return force_x, force_y
