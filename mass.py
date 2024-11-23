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

        # Check if the mass is off-screen and display its position
        if self.x < 0:
            off_screen_text = font.render(f"Off left: ({self.x:.2f}, {self.y:.2f})", True, (255, 0, 0))
            screen.blit(off_screen_text, (10, int(self.y)))
        elif self.x > screen.get_width():
            off_screen_text = font.render(f"Off right: ({self.x:.2f}, {self.y:.2f})", True, (255, 0, 0))
            screen.blit(off_screen_text, (screen.get_width() - 150, int(self.y)))
        if self.y < 0:
            off_screen_text = font.render(f"Off top: ({self.x:.2f}, {self.y:.2f})", True, (255, 0, 0))
            screen.blit(off_screen_text, (int(self.x), 10))
        elif self.y > screen.get_height():
            off_screen_text = font.render(f"Off bottom: ({self.x:.2f}, {self.y:.2f})", True, (255, 0, 0))
            # Adjust the x position based on the direction of the mass's velocity
            if self.vx < 0:
                screen.blit(off_screen_text, (int(self.x), screen.get_height() - 30))
            else:
                screen.blit(off_screen_text, (int(self.x) - 150, screen.get_height() - 30))

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
