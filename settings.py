from pathlib import Path

class Settings:
    """
    A class to store all configuration settings for Alien Invasion.

    These settings include display parameters, ship properties, bullet behavior,
    alien fleet behavior, and file paths for images and sounds.
    """

    def __init__(self):
        """
        Initialize the game's static settings.
        """
        # --- Game Display ---
        self.name: str = 'Alien Invasion'
        self.screen_w = 1265  # Screen width in pixels
        self.screen_h = 625   # Screen height in pixels
        self.FPS = 60         # Frames per second
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'space1.png'  # Background image path

        # --- Ship Settings ---
        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'ship2(no bg).png'
        self.ship_w = 30            # Ship width in pixels
        self.ship_h = 50            # Ship height in pixels
        self.ship_speed = 7         # Ship movement speed
        self.starting_ship_count = 3  # Number of lives at game start

        # --- Bullet Settings ---
        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'Laser Shot.mp3'
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'synthetic_explosion_1.mp3'
        self.bullet_speed = 10      # Bullet speed
        self.bullet_w = 20          # Bullet width
        self.bullet_h = 50          # Bullet height
        self.bullet_amount = 5      # Max number of bullets on screen

        # --- Alien Settings ---
        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'Asteroid Brown.png'
        self.fleet_speed = 1        # Speed of alien fleet
        self.alien_w = 30           # Alien width
        self.alien_h = 30           # Alien height
        self.fleet_direction = 1    # 1 for right, -1 for left
        self.fleet_drop_speed = 30  # Pixels to move down when hitting edge