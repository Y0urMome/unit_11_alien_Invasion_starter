import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal

class Ship:
    """
    Represents the player's ship.

    Manages the ship's movement, drawing, firing projectiles, and collision response.
    """

    def __init__(self, game: 'AlienInvasion', arsenal: "Arsenal"):
        """
        Initialize the ship and its properties.

        Args:
            game (AlienInvasion): Reference to the main game object.
            arsenal (Arsenal): The ship's bullet management system.
        """
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        # Load and scale the ship image
        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.ship_w, self.settings.ship_h)
        )

        self.rect = self.image.get_rect()
        self._center_ship()

        self.moving_right = False
        self.moving_left = False
        self.arsenal = arsenal

    def _center_ship(self):
        """
        Position the ship at the center-bottom of the screen.
        """
        self.rect.midbottom = self.boundaries.midbottom
        self.x = float(self.rect.x)  # Use float for smooth horizontal movement

    def update(self):
        """
        Update the ship's position and its arsenal.
        """
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        """
        Handle left and right movement of the ship within screen bounds.
        """
        temp_speed = self.settings.ship_speed
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed

        self.rect.x = self.x

    def draw(self):
        """
        Draw the ship and its bullets to the screen.
        """
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self):
        """
        Attempt to fire a bullet from the ship.

        Returns:
            bool: True if a bullet was fired, False otherwise.
        """
        return self.arsenal.fire_bullet()

    def check_collisions(self, other_group):
        """
        Check for collisions between the ship and another sprite group.

        If a collision occurs, reset the ship's position.

        Args:
            other_group (pygame.sprite.Group): The group to check for collisions with.

        Returns:
            bool: True if a collision was detected, False otherwise.
        """
        if pygame.sprite.spritecollideany(self, other_group):
            self._center_ship()
            return True
        return False