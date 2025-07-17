import pygame
import math

pygame.init()
WIDTH = 1200
HEIGHT = 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Planet Simulation')
clock = pygame.time.Clock()

G = 6.67430e-11
SCALE = 5e-11
ZOOM_SCALE = 1e-9
DT = 86400 #sec

zoomed = False

class Body:

    def __init__(self, x, y, vx, vy, mass, radius, color, x_moon, y_moon, vx_moon, vy_moon, moon_mass, moon_radius, color_moon = (169, 169, 169), number_of_moons = 0):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.mass = mass
        self.color = color
        self.trail = []
        self.x_moon = x_moon
        self.y_moon = y_moon
        self.vx_moon = vx_moon
        self.vy_moon = vy_moon
        self.moon_mass = moon_mass
        self.moon_radius = moon_radius
        self.color_moon = color_moon
        self.number_of_moons = number_of_moons

    def update_position(self, bodies):
        fx = fy = 0
        fx_moon = fy_moon = 0
        for other in bodies:
            if other != self:
                dx = other.x - self.x
                dy = other.y - self.y
                r = math.sqrt(dx ** 2 + dy ** 2)
                if r > 0:
                    # F = G * (m1 * m2)/ r^2
                    f = G * self.mass * other.mass / (r**2)
                    fx += f * dx / r
                    fy += f * dy / r
        for moon in bodies:
            dx_m = self.x - self.x_moon
            dy_m = self.y - self.y_moon 
            r_m = math.sqrt(dx_m ** 2 + dy_m ** 2)
            if r_m > 0:
                f_moon = G * self.mass * self.moon_mass / (r_m**2)
                fx_moon += f_moon * dx_m / r_m
                fy_moon += f_moon * dy_m / r_m

        # F = ma
        ax = fx / self.mass
        ay = fy / self.mass
        self.vx += ax * DT
        self.vy += ay * DT
        self.x += self.vx * DT
        self.y += self.vy * DT

        if self.number_of_moons > 0:
            ax_moon = fx_moon / self.moon_mass
            ay_moon = fy_moon / self.moon_mass
            self.vx_moon += ax_moon * DT
            self.vy_moon += ay_moon * DT
            self.x_moon += self.vx_moon * DT
            self.y_moon += self.vy_moon * DT

        current_scaling = ZOOM_SCALE if zoomed else SCALE

        self.trail.append((int(self.x * current_scaling + WIDTH // 2), int(self.y * current_scaling + HEIGHT // 2)))
        if len(self.trail) > 200:
            self.trail.pop(0)

    def draw(self, screen, scale, offset_x, offset_y):
        # draw trail
        if len(self.trail)>1:
            pts = [(int(x*scale+offset_x), int(y*scale+offset_y)) for x,y in self.trail]
            pygame.draw.lines(screen, (50,50,50), False, pts,1)
        # draw planet
        px = int(self.x*scale+offset_x)
        py = int(self.y*scale+offset_y)
        pygame.draw.circle(screen, self.color, (px,py), self.radius)
        # draw moon
        if self.number_of_moons:
            mx = int(self.x_moon*scale+offset_x)
            my = int(self.y_moon*scale+offset_y)
            pygame.draw.circle(screen, self.color_moon, (mx,my), self.moon_radius)

# define bodies

sun = Body(
    0, 0, 0, 0,
    1.9885e30, 8, (255, 255, 0),
    0, 0, 0, 0,
    0, 0, 0
)

mercury = Body(
    5.79e10, 0, 0, 47360,
    3.3011e23, 2, (169, 169, 169),
    0, 0, 0, 0,
    0, 0, 0
)

venus = Body(
    1.082e11, 0, 0, 35020,
    4.8675e24, 4, (255, 215, 0),
    0, 0, 0, 0,
    0, 0, 0
)

earth = Body(
    1.496e11, 0, 0, 29780,
    5.97237e24, 5, (100, 149, 237),
    1.496e11 + 3.844e8, 0, 0, 29780 + 1022,
    7.342e22, 6, 1
)

mars = Body(
    2.279e11, 0, 0, 24070,
    6.4171e23, 3, (188, 39, 50),
    0, 0, 0, 0,
    0, 0, 0
)

jupiter = Body(
    7.785e11, 0, 0, 13070,
    1.8982e27, 10, (216, 168, 105),
    0, 0, 0, 0,
    0, 0, 0
)

saturn = Body(
    1.433e12, 0, 0, 9690,
    5.6834e26, 9, (244, 164, 96),
    0, 0, 0, 0,
    0, 0, 0
)

uranus = Body(
    2.877e12, 0, 0, 6800,
    8.6810e25, 7, (175, 238, 238),
    0, 0, 0, 0,
    0, 0, 0
)

neptune = Body(
    4.503e12, 0, 0, 5430,
    1.02413e26, 7, (0, 0, 205),
    0, 0, 0, 0,
    0, 0, 0
)

bodies = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
            zoomed = not zoomed
            for b in bodies:
                b.trail.clear()

    scale = ZOOM_SCALE if zoomed else SCALE
    focus = bodies[0]  # Słońce
    offset_x = WIDTH//2  - focus.x * scale
    offset_y = HEIGHT//2 - focus.y * scale

    screen.fill((0, 0, 0))
    for b in bodies:
        b.update_position(bodies)
        b.draw(screen, scale, offset_x, offset_y)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

