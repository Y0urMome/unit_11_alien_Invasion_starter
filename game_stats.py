class GameStats:
    """
    Track statistics for the game session.

    Currently tracks the number of remaining ships (lives), but can be extended
    to include score, levels, etc.
    """

    def __init__(self, ship_limit):
        """
        Initialize the stats object.

        Args:
            ship_limit (int): The number of ships (lives) the player starts with.
        """
        self.ships_left = ship_limit  # Remaining player lives