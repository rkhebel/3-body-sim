import pygame
import random
from mass import Mass
from system import System

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
MENU_HEIGHT = 100
PLAYABLE_WIDTH = SCREEN_WIDTH 
PLAYABLE_HEIGHT = SCREEN_HEIGHT - MENU_HEIGHT
BUFFER = 50
BUTTON_HEIGHT = 50
BUTTON_WIDTH = 100
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("N Masses Moving in Space")

NUM_MASSES = 3

# Function to initialize masses with random positions
def initialize_system(n=NUM_MASSES):
    masses = [
        Mass(
            position=(x := random.randint(BUFFER, PLAYABLE_WIDTH-BUFFER), y := random.randint(BUFFER, PLAYABLE_HEIGHT-BUFFER)), 
            velocity=(0, 0), 
            color=(r := random.randint(0, 255), g := random.randint(0, 255), b := random.randint(0, 255)),
            max_width=PLAYABLE_WIDTH, 
            max_height=PLAYABLE_HEIGHT,
            radius=20, 
            mass=1e16
        )
        for _ in range(n)
    ]
    return System(masses, PLAYABLE_WIDTH, PLAYABLE_HEIGHT)

# Clock to manage frame rate
clock = pygame.time.Clock()

# Control variables
running = True
simulation_running = False

# Button dimensions
start_button = pygame.Rect(50, SCREEN_HEIGHT - BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
reset_button = pygame.Rect(200, SCREEN_HEIGHT - BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
stop_button = pygame.Rect(350, SCREEN_HEIGHT - BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)

system = initialize_system(NUM_MASSES)

def draw_grid():
    grid_color = (150, 150, 150)
    for x in range(0, PLAYABLE_WIDTH, 50):
        pygame.draw.line(screen, grid_color, (x, 0), (x, PLAYABLE_HEIGHT))
    for y in range(0, PLAYABLE_HEIGHT, 50):
        pygame.draw.line(screen, grid_color, (0, y), (PLAYABLE_WIDTH, y))
    font = pygame.font.Font(None, 24)
    for x in range(0, PLAYABLE_WIDTH, 50):
        text = font.render(f"{x}", True, (0, 0, 0))
        screen.blit(text, (x+5, 5))
    for y in range(0, PLAYABLE_HEIGHT, 50):
        text = font.render(f"{y}", True, (0, 0, 0))
        screen.blit(text, (5, y+5))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos):
                simulation_running = True
            elif reset_button.collidepoint(event.pos):
                system = initialize_system(NUM_MASSES)
                simulation_running = False
            elif stop_button.collidepoint(event.pos):
                simulation_running = False

    dt = clock.tick(60) / 1000

    if simulation_running:
        system.update(dt)

    screen.fill((200, 200, 200))

    draw_grid()

    for mass in system.masses:
        mass.draw(screen)

    pygame.draw.rect(screen, "gray", start_button)
    pygame.draw.rect(screen, "gray", stop_button)
    pygame.draw.rect(screen, "gray", reset_button)
    font = pygame.font.Font(None, 36)
    start_text = font.render("Start", True, (255, 255, 255))
    reset_text = font.render("Reset", True, (255, 255, 255))
    stop_text = font.render("Stop", True, (255, 255, 255))
    screen.blit(start_text, (start_button.x + 10, start_button.y + 10))
    screen.blit(reset_text, (reset_button.x + 10, reset_button.y + 10))
    screen.blit(stop_text, (stop_button.x + 10, stop_button.y + 10))

    pygame.display.flip()

pygame.quit()

