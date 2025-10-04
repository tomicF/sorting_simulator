import pygame
import random
# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hello Pygame")

sorting_arr = random.sample(range(1, 16), 15)

color_green= (0, 255, 0)

x_factor = 10
b = 0

def bubble_sort(arr, i):
    if arr[i] > arr[i + 1]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]


# Game loop
running = True
while running:
    
    
    screen.fill((0, 0, 0))  
    
    for i in range(len(sorting_arr)):
     height = sorting_arr[i] * 20
     pygame.draw.rect(screen, color_green, pygame.Rect(x_factor, 540 - height, 30, height))
     x_factor +=  50
     
    
    bubble_sort(sorting_arr, b)
    b += 1
    if b == len(sorting_arr) - 1:
      b = 0
    
    pygame.time.wait(30)
     
    x_factor = 10
    pygame.display.flip() 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()