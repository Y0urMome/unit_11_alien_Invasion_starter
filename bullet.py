import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    """
    Represents a single bullet fired by the player's ship.

    Manages its position, movement, and rendering to the screen.
    """

    def __init__(self, game: 'AlienInvasion'):
        """
        Initialize a bullet at the ship's current position.

        Args:
            game (AlienInvasion): Reference to the main game object.
        """
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # Load and scale bullet image
        self.image = pygame.image.load(str(self.settings.bullet_file))
        self.image = pygame.transform.scale(
            self.image, (self.settings.bullet_w, self.settings.bullet_h)
        )

        # Position the bullet at the top center of the ship
        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop

        # Use float for smooth vertical movement
        self.y = float(self.rect.y)

    def update(self):
        """
        Move the bullet upward based on bullet speed.
        """
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """
        Draw the bullet at its current position on the screen.
        """
        self.screen.blit(self.image, self.rect)