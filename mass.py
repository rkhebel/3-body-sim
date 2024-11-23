from pygame import draw

class Mass:
    """Class to represent a mass in 2D space."""
    def __init__(self, position, velocity, color, radius=5, mass=1):
        """Initialize a mass with a position, velocity, color, radius, and mass."""
        self.x, self.y = position
        self.vx, self.vy = velocity
        self.color = color
        self.radius = radius
        self.mass = mass

    def update(self, force_x, force_y, dt):
        """Update the position of the mass based on velocity."""
        self.x += self.vx * dt
        self.y += self.vy * dt

    def draw(self, screen):
        """Draw the mass on the Pygame screen."""
        draw.circle(screen, self.color.value, (self.x, self.y), self.radius)
        
    def compute_grav_force(self, other_mass):
        """Compute the gravitational force between two masses."""