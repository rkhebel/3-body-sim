import pygame
import random
from mass import Mass
from system import System

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
MENU_HEIGHT = 100
PLAYABLE_WIDTH= SCREEN_WIDTH 
PLAYABLE_HEIGHT = SCREEN_HEIGHT - MENU_HEIGHT
BUTTON_HEIGHT = 100
BUTTON_WIDTH = 50
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("N Masses Moving in Space")

NUM_MASSES = 3

# Function to initialize masses with random positions
def initialize_system(n=NUM_MASSES):
    masses = [
        Mass(
            position = (x := random.randint(50, PLAYABLE_WIDTH-50), y := random.randint(50, PLAYABLE_HEIGHT-150)), 
            velocity = (0, 0), 
            color = (r := random.randint(0,255), g := random.randint(0,255), b := random.randint(0,255)),
            max_width = PLAYABLE_WIDTH, 
            max_height = PLAYABLE_HEIGHT,
            radius=20, 
            mass=1e16
        )
        for _ in range(n)
    ]
    # Create a system
    return System(masses, PLAYABLE_WIDTH, PLAYABLE_HEIGHT)

# Clock to manage frame rate
clock = pygame.time.Clock()

# Control variables
running = True
simulation_running = False

# Button dimensions
start_button = pygame.Rect(50, 10, BUTTON_HEIGHT, BUTTON_WIDTH)
reset_button = pygame.Rect(200, 10, BUTTON_HEIGHT, BUTTON_WIDTH)
stop_button = pygame.Rect(350, 10, BUTTON_HEIGHT, BUTTON_WIDTH)

system = initialize_system(NUM_MASSES)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos):
                simulation_running = True  # Start the simulation
            elif reset_button.collidepoint(event.pos):
                system = initialize_system(NUM_MASSES)
                simulation_running = False  # Stop the simulation
            elif stop_button.collidepoint(event.pos):
                simulation_running = False  # Pause the simulation

    # Time step (in seconds)
    dt = clock.tick(60) / 1000  # Convert milliseconds to seconds

    # Update the system if the simulation is running
    if simulation_running:
        system.update(dt)

    for mass in system.masses:
        mass.draw(screen)
        
    # Clear screen
    screen.fill((200, 200, 200))  # Change background color to grey

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
