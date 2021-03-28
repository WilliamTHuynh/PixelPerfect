import pygame
from pygame.sprite import Sprite


class Box(Sprite):
    """A class to manage the ship."""

    def __init__(self, screen, speed, start):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = screen

        # Load the ship image and get its rect.
        self.image = pygame.image.load('player/square_sprite.png')
        self.rect = self.image.get_rect()
        self.speed = speed

        # Start box at first starting point
        self.rect.x = start[0]
        self.rect.y = start[1]

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on movement flags."""
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen.get_rect().right:
            self.x += self.speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.speed

        if self.moving_up and self.rect.top > 0:
            self.y -= self.speed
        if self.moving_down and self.rect.bottom < self.screen.get_rect().bottom:
            self.y += self.speed

        # Update rect object from self.x.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def restart(self, start):
        self.rect.x = start[0]
        self.rect.y = start[1]
        self.rect.x += 35
        self.rect.y += 5
