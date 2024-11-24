import pygame
import math

class Mass:
    """Class to represent a mass in 2D space."""
    def __init__(self, position, velocity, color, max_width, max_height, radius=5, mass=1):
        """Initialize a mass with a position, velocity, color, radius, and mass."""
        self.x, self.y = position
        self.vx, self.vy = velocity
        self.color = color
        self.radius = radius
        self.mass = mass
        self.max_width = max_width
        self.max_height = max_height

    def update_position(self, dt):
        """Update the position of the mass based on velocity."""
        self.x += self.vx * dt
        self.y += self.vy * dt

    def draw(self, screen):
        """Draw the mass on the Pygame screen."""
        font = pygame.font.Font(None, 18)
        # Only draw the mass if it's within the playable area
        if 0 <= self.x <= self.max_width and 0 <= self.y <= self.max_height:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
            text = font.render(f"({self.vx:.2f}, {self.vy:.2f})", True, (0, 0, 0))
            text_rect = text.get_rect(center=(int(self.x), int(self.y)))
            screen.blit(text, text_rect)

        # Check if the mass is off-screen and display its position
        if self.x < 0 or self.x > self.max_width or self.y < 0 or self.y > self.max_height:
            off_screen_text = font.render(f"Off screen: ({self.x:.2f}, {self.y:.2f})", True, (255, 0, 0))
            text_rect = off_screen_text.get_rect()
            if self.x < 0:
                text_rect.x = 10
            elif self.x > self.max_width:
                text_rect.x = self.max_width - 150
            if self.y < 0:
                text_rect.y = 10
            elif self.y > self.max_height:
                text_rect.y = self.max_height - 30
            screen.blit(off_screen_text, text_rect)

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
