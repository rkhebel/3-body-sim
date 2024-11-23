import pygame
from mass import Mass
from system import System

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Masses Moving in Space")


# Initialize two masses
mass1 = Mass(-1, 0, 0.1, 0.05, pygame.Color.r, radius=8)  # Starts at (-1, 0), moves with (vx=0.1, vy=0.05)
mass2 = Mass(1, 0, -0.1, -0.05, pygame.Color.b, radius=8)  # Starts at (1, 0), moves with (vx=-0.1, vy=-0.05)
masses = [mass1, mass2]

# Clock to manage frame rate
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Time step (in seconds)
    dt = clock.tick(60) / 1000  # Convert milliseconds to seconds

    # Update the masses
    mass1.update(dt)
    mass2.update(dt)

    # Clear screen
    screen.fill(WHITE)

    # Draw the masses
    mass1.draw(screen)
    mass2.draw(screen)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
