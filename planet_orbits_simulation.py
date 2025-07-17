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


