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

# Create a thread for loading each image
image_threads = []
loaded_images = [None]*3

# Function to load an image
def load_image(image_path,loaded_images):
    for i in range(0,len(image_path)):
        loaded_images[i] = pygame.image.load(image_path[i])

image_thread = threading.Thread(target=load_image, args=(IMAGE_PATHS,loaded_images))
image_thread.start()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check if all image loading threads are done
    if not image_thread.is_alive():
        # Draw the loaded images on the screen
        screen.fill(WHITE)
        for i, image in enumerate(loaded_images):
            screen.blit(image, (i * 200, 200))
        pygame.display.flip()

pygame.quit()
