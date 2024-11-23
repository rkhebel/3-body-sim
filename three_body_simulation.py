import pygame
import math
from mass import Mass
from system import System

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Masses Moving in Space")

# Initialize two masses
mass1 = Mass((0, 0), (0,0), "red", radius=8, mass=1)  # Starts at (-1, 0), moves with (vx=0.1, vy=0.05)
mass2 = Mass((300, 0), (0,0), "blue", radius=8, mass=1)  # Starts at (1, 0), moves with (vx=-0.1, vy=-0.05)
masses = [mass1, mass2]

# Create a system
system = System(WIDTH, HEIGHT, masses)

# Clock to manage frame rate
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Time step (in seconds)
    dt = clock.tick(60) / 1000  # Convert milliseconds to seconds

    # Update the system
    system.update(dt)

    # Clear screen
    screen.fill((255, 255, 255))

    # Draw the masses
    for mass in masses:
        mass.draw(screen)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
