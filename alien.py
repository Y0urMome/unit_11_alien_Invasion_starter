import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_fleet import AlienFleet

class Alien(Sprite):
    """
    Represents a single alien in the alien fleet.
    Handles position, movement, boundary detection, and rendering.
    """

    def __init__(self, fleet: 'AlienFleet', x: float, y: float):
        """
        Initialize an alien at a specific x and y position.

        Args:
            fleet (AlienFleet): The parent fleet this alien belongs to.
            x (float): Initial x-coordinate for the alien.
            y (float): Initial y-coordinate for the alien.
        """
        super().__init__()

        self.fleet = fleet
        self.screen = fleet.game.screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings

        # Load and scale the alien image
        self.image = pygame.image.load(str(self.settings.alien_file))
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.alien_w, self.settings.alien_h)
        )

        # Set the rect for positioning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Store float versions for precise movement
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        """
        Update the alien’s horizontal position based on fleet direction and speed.
        """
        temp_speed = self.settings.fleet_speed
        self.x += temp_speed * self.fleet.fleet_direction
        self.rect.x = self.x
        self.rect.y = self.y  # In case vertical position is updated elsewhere

    def check_edges(self):
        """
        Check if the alien has reached the screen boundary.

        Returns:
            bool: True if the alien has reached the left or right edge of the screen.
        """
        return (
            self.rect.right >= self.boundaries.right or
            self.rect.left <= self.boundaries.left
        )

    def draw_alien(self):
        """
        Draw the alien at its current location on the screen.
        """
        self.screen.blit(self.image, self.rect)