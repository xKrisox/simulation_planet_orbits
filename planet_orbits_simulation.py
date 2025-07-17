import pygame
import math

pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Planet Simulation')
clock = pygame.time.Clock()

G = 6.67430e-11
