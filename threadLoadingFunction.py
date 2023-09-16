IMAGE_PATH = 'BGloop/'+str(i)+'.png'

import pygame
import threading

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
IMAGE_PATHS = ['image1.png', 'image2.png', 'image3.png']  # Add paths to your images here

# Colors
WHITE = (255, 255, 255)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Loading Multiple Images in Threads")

# Function to load an image
def load_image(image_path):
    return pygame.image.load(image_path)

# Create a thread for loading each image
image_threads = []
loaded_images = []

for image_path in IMAGE_PATHS:
    thread = threading.Thread(target=lambda p=image_path: loaded_images.append(load_image(p)))
    image_threads.append(thread)
    thread.start()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check if all image loading threads are done
    if all(not thread.is_alive() for thread in image_threads):
        # Draw the loaded images on the screen
        screen.fill(WHITE)
        for i, image in enumerate(loaded_images):
            screen.blit(image, (i * 200, 200))
        pygame.display.flip()

pygame.quit()
