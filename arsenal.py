import pygame
from typing import TYPE_CHECKING
from bullet import Bullet

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Arsenal:
    """
    Manages the player's active bullets (the 'arsenal').
    
    Responsible for creating, updating, drawing, and removing bullets
    during gameplay.
    """

    def __init__(self, game: 'AlienInvasion'):
        """
        Initialize the arsenal for bullet management.

        Args:
            game (AlienInvasion): Reference to the main game object.
        """
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        """
        Update the position of all bullets and remove any that have exited the screen.
        """
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self):
        """
        Remove bullets that have moved off the top of the screen.
        """
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw(self):
        """
        Draw all bullets currently in the arsenal to the screen.
        """
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self):
        """
        Fire a bullet if the maximum number of on-screen bullets hasn't been reached.

        Returns:
            bool: True if a bullet was successfully fired, False otherwise.
        """
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False