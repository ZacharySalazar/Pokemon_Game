import pygame

def load_image(name):
    img = pygame.image.load(name)
    img = pygame.transform.scale(img, (300, 300))
    return img


geodude_back = load_image('Images\geodude_back.JPG')
sandshrew_facing = load_image('Images\sandshrew_facing.png')
