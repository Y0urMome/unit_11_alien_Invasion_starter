import pygame
from alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class AlienFleet:
    """
    Manages the alien fleet's creation, movement, rendering, and interaction with the game.
    """

    def __init__(self, game: 'AlienInvasion'):
        """
        Initialize the alien fleet with reference to the main game and create the initial fleet.
        
        Args:
            game (AlienInvasion): The main game instance.
        """
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_fleet()

    def create_fleet(self):
        """
        Determine fleet dimensions and positioning, then create the triangle fleet formation.
        """
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_w
        screen_h = self.settings.screen_h

        fleet_w, fleet_h = self.calculate_fleet_size(alien_w, screen_w, alien_h, screen_h)
        x_offset, y_offset = self.calculate_offsets(alien_w, alien_h, screen_w, fleet_w, fleet_h)

        self._create_triangle_fleet(alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset)

    def _create_triangle_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
        """
        Create an upside-down triangle fleet, centered horizontally and vertically adjusted.

        Args:
            alien_w (int): Width of an alien sprite.
            alien_h (int): Height of an alien sprite.
            fleet_w (int): Max number of aliens per row.
            fleet_h (int): Max number of rows.
            x_offset (int): Horizontal offset for centering.
            y_offset (int): Vertical offset from top.
        """
        triangle_base_width = 27  # Width of the top row in the triangle

        for row in range((triangle_base_width + 1) // 2):
            aliens_in_row = triangle_base_width - 2 * row
            total_width = aliens_in_row * alien_w
            start_x = (self.settings.screen_w - total_width) // 2

            for i in range(aliens_in_row):
                current_x = start_x + i * alien_w
                current_y = y_offset + row * alien_h
                self._create_alien(current_x, current_y)

    def calculate_offsets(self, alien_w, alien_h, screen_w, fleet_w, fleet_h):
        """
        Calculate offsets to center the fleet on the screen.

        Args:
            alien_w (int): Width of an alien.
            alien_h (int): Height of an alien.
            screen_w (int): Width of the screen.
            fleet_w (int): Width of the fleet (number of aliens per row).
            fleet_h (int): Height of the fleet (number of rows).

        Returns:
            tuple: x_offset and y_offset for positioning.
        """
        half_screen = self.settings.screen_h // 2
        fleet_horizontal_space = fleet_w * alien_w
        fleet_vertical_space = fleet_h * alien_h
        x_offset = (screen_w - fleet_horizontal_space) // 2
        y_offset = (half_screen - fleet_vertical_space) // 2
        return x_offset, y_offset

    def calculate_fleet_size(self, alien_w, screen_w, alien_h, screen_h):
        """
        Calculate how many aliens can fit on the screen.

        Args:
            alien_w (int): Width of an alien.
            screen_w (int): Width of the screen.
            alien_h (int): Height of an alien.
            screen_h (int): Height of the screen.

        Returns:
            tuple: fleet_w (columns), fleet_h (rows)
        """
        fleet_w = screen_w // alien_w
        fleet_h = (screen_h // 2) // alien_h

        # Make fleet width and height odd for triangle symmetry
        fleet_w -= 1 if fleet_w % 2 == 0 else 2
        fleet_h -= 1 if fleet_h % 2 == 0 else 2

        return int(fleet_w), int(fleet_h)

    def _create_alien(self, current_x: int, current_y: int):
        """
        Create an alien at the specified position and add it to the fleet.

        Args:
            current_x (int): X-coordinate.
            current_y (int): Y-coordinate.
        """
        new_alien = Alien(self, current_x, current_y)
        self.fleet.add(new_alien)

    def _check_fleet_edges(self):
        """
        Check if any alien has reached the screen edge.
        If so, reverse the fleet's direction and move it downward.
        """
        for alien in self.fleet:
            if alien.check_edges():
                self._drop_alien_fleet()
                self.fleet_direction *= -1
                break

    def _drop_alien_fleet(self):
        """
        Move the entire fleet downward by the drop speed.
        """
        for alien in self.fleet:
            alien.y += self.fleet_drop_speed

    def update_fleet(self):
        """
        Update the fleet’s position based on direction and handle edge logic.
        """
        self._check_fleet_edges()
        self.fleet.update()

    def draw(self):
        """
        Draw all aliens in the fleet.
        """
        for alien in self.fleet:
            alien.draw_alien()

    def check_collisions(self, other_group):
        """
        Check for collisions between the fleet and another sprite group.

        Args:
            other_group (pygame.sprite.Group): Group to check for collisions with.

        Returns:
            dict: Collisions detected.
        """
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)

    def check_fleet_bottom(self):
        """
        Check if any alien in the fleet has reached the bottom of the screen.

        Returns:
            bool: True if an alien has reached the bottom, else False.
        """
        for alien in self.fleet:
            if alien.rect.bottom >= self.settings.screen_h:
                return True
        return False

    def check_destroyed_status(self):
        """
        Check if the fleet has been entirely destroyed.

        Returns:
            bool: True if fleet is empty.
        """
        return not self.fleet