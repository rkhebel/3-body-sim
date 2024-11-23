import pygame
import random
from mass import Mass
from system import System

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Three Masses Moving in Space")

NUM_MASSES = 3

# Function to initialize masses with random positions
def initialize_masses(n=NUM_MASSES):
    return [
        Mass((random.randint(50, WIDTH-50), random.randint(50, HEIGHT-150)), (0, 0), (random.randint(0,255), random.randint(0,255), random.randint(0,255)), radius=20, mass=1e16)
        for _ in range(n)
    ]

# Initialize masses
masses = initialize_masses()

# Create a system
system = System(masses, WIDTH, HEIGHT)

# Clock to manage frame rate
clock = pygame.time.Clock()

# Control variables
running = True
simulation_running = False

# Button dimensions
button_width, button_height = 100, 50
start_button = pygame.Rect(50, 10, button_width, button_height)
reset_button = pygame.Rect(200, 10, button_width, button_height)
stop_button = pygame.Rect(350, 10, button_width, button_height)

# Playable area dimensions
playable_area = pygame.Rect(0, button_height + 10, WIDTH, HEIGHT - button_height - 10)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos):
                simulation_running = True  # Start the simulation
            elif reset_button.collidepoint(event.pos):
                masses = initialize_masses()  # Reinitialize masses
                system = System(masses, WIDTH, HEIGHT)
                simulation_running = False  # Stop the simulation
            elif stop_button.collidepoint(event.pos):
                simulation_running = False  # Pause the simulation

    # Time step (in seconds)
    dt = clock.tick(60) / 1000  # Convert milliseconds to seconds

    # Update the system if the simulation is running
    if simulation_running:
        system.update(dt)

    # Clear screen
    screen.fill((200, 200, 200))  # Change background color to grey

    # Draw the playable area
    pygame.draw.rect(screen, (255, 255, 255), playable_area, 2)  # Outline of playable area

    # Draw the masses
    for mass in masses:
        mass.draw(screen)

    # Draw buttons
    pygame.draw.rect(screen, "gray", start_button)  # Start button
    pygame.draw.rect(screen, "gray", stop_button)   # Stop button
    pygame.draw.rect(screen, "gray", reset_button)  # Reset button
    font = pygame.font.Font(None, 36)
    start_text = font.render("Start", True, (255, 255, 255))
    reset_text = font.render("Reset", True, (255, 255, 255))
    stop_text = font.render("Stop", True, (255, 255, 255))
    screen.blit(start_text, (start_button.x + 10, start_button.y + 10))
    screen.blit(reset_text, (reset_button.x + 10, reset_button.y + 10))
    screen.blit(stop_text, (stop_button.x + 10, stop_button.y + 10))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
