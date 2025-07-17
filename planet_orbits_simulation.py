import pygame
import math

pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Planet Simulation')
clock = pygame.time.Clock()

G = 6.67430e-11
SCALE = 6e-11
ZOOM_SCALE = 1e-9
DT = 86400 #sec

zoomed = False

class Body:

    def __init__(self, x, y, vx, vy, mass, radius, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.mass = mass
        self.color = color
        self.trail = []

    def update_position(self, bodies):
        fx = fy = 0

        for other in bodies:
            if other != self:
                dx = other.x - self.x
                dy = other.y - self.y
                r = math.sqrt(dx ** 2 + dy ** 2)
                if r > 0:
                    # F = G * (m1 * m2)/ r^2
                    f = G*self.mass * other.mass / (r**2)
                    fx += f * dx / r
                    fy += f * dy / r
        # F = ma
        ax = fx / self.mass
        ay = fy / self.mass
        self.vx += ax * DT
        self.vy += ay * DT
        self.x += vx * DT
        self.y += vy * DT

        current_scaling = ZOOM_SCALE if zoomed else SCALE

        self.trail.append((int(self.x * current_scaling + WIDTH // 2), int(self.y * current_scaling + HEIGHT // 2)))
        if len(self.trail) > 200:
            self.trail.pop(0)


    def draw(self,screen):
        if len(self.trail) > 1:
            pygame.draw.lines(screen, (50,50,50), False, self.trail, 1)

        current_scaling = ZOOM_SCALE if zoomed else SCALE

        screen_x = int(self.x * current_scaling + WIDTH //2)
        screen_y = int(self.y * current_scaling + HEIGHT //2)

        pygame.draw.circle(screen, self.color, (screen_x, screen_y), self.radius)

bodies = [
    # Słońce
    Body(0, 0, 0, 0,
         1.9885e30,     # masa [kg]
         8,             # promień do rysowania [px]
         (255, 255, 0)),# kolor żółty

    # Merkury
    Body(5.79e10, 0, 0, 47360,
         3.3011e23,
         2,
         (169, 169, 169)),

    # Wenus
    Body(1.082e11, 0, 0, 35020,
         4.8675e24,
         4,
         (255, 215, 0)),

    # Ziemia
    Body(1.496e11, 0, 0, 29780,
         5.97237e24,
         5,
         (100, 149, 237)),

    # Mars
    Body(2.279e11, 0, 0, 24070,
         6.4171e23,
         3,
         (188, 39, 50)),

    # Jowisz
    Body(7.785e11, 0, 0, 13070,
         1.8982e27,
         10,
         (216, 168, 105)),

    # Saturn
    Body(1.433e12, 0, 0, 9690,
         5.6834e26,
         9,
         (244, 164, 96)),

    # Uran
    Body(2.877e12, 0, 0, 6800,
         8.6810e25,
         7,
         (175, 238, 238)),

    # Neptun
    Body(4.503e12, 0, 0, 5430,
         1.02413e26,
         7,
         (0, 0, 205)),
]
