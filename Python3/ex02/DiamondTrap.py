from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """King Class"""
    def __init__(self, first_name, is_alive=True):
        """King Constructor"""
        Lannister.__init__(self, first_name, is_alive)
        Baratheon.__init__(self, first_name, is_alive)

    def set_eyes(self, color):
        """Set the eyes color"""
        self.eyes = color

    def get_eyes(self):
        """Get the eyes color"""
        return self.eyes

    def set_hairs(self, color):
        """Set the hairs color"""
        self.hairs = color

    def get_hairs(self):
        """Get the hairs color"""
        return self.hairs
