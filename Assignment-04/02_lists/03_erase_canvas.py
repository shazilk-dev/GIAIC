import pygame
import sys

# Implement an 'eraser' on a canvas.

# The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white.


# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
ERASER_SIZE = 40
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BACKGROUND = (200, 200, 200)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Eraser Canvas")

# Initialize the canvas with blue cells
canvas = [[BLUE for _ in range(WIDTH // CELL_SIZE)] for _ in range(HEIGHT // CELL_SIZE)]

def draw_canvas():
    for y in range(len(canvas)):
        for x in range(len(canvas[0])):
            pygame.draw.rect(screen, canvas[y][x], 
                            (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def erase(x, y):
    # Determine the area affected by the eraser
    start_x = max(0, x - ERASER_SIZE // 2) // CELL_SIZE
    start_y = max(0, y - ERASER_SIZE // 2) // CELL_SIZE
    end_x = min(WIDTH, x + ERASER_SIZE // 2) // CELL_SIZE
    end_y = min(HEIGHT, y + ERASER_SIZE // 2) // CELL_SIZE
    
    # Set cells in the eraser area to white
    for cy in range(start_y, end_y + 1):
        for cx in range(start_x, end_x + 1):
            if 0 <= cy < len(canvas) and 0 <= cx < len(canvas[0]):
                canvas[cy][cx] = WHITE

# Main game loop
running = True
erasing = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            erasing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            erasing = False
    
    # Erase if mouse button is pressed
    if erasing:
        mouse_pos = pygame.mouse.get_pos()
        erase(mouse_pos[0], mouse_pos[1])
    
    # Draw everything
    screen.fill(BACKGROUND)
    draw_canvas()
    
    # Draw eraser outline at mouse position
    mouse_pos = pygame.mouse.get_pos()
    pygame.draw.rect(screen, (0, 0, 0), 
                    (mouse_pos[0] - ERASER_SIZE // 2, 
                     mouse_pos[1] - ERASER_SIZE // 2, 
                     ERASER_SIZE, ERASER_SIZE), 1)
    
    pygame.display.flip()

pygame.quit()
sys.exit()