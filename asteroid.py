import random

import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="white",
            center=self.position,
            radius=self.radius,
        )
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # too small to split → just die
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return

        # big enough to split
        self.kill()
        log_event("asteroid_split")

        angle = random.uniform(20, 50)
        left_velo = self.velocity.rotate(angle)
        right_velo = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid_1.velocity = left_velo * 1.2
        asteroid_2.velocity = right_velo * 1.2




