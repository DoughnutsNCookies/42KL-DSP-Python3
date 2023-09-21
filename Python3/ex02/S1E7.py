from S1E9 import Character


class Baratheon(Character):
    """Baratheon Class"""
    def __init__(self, first_name, is_alive=True):
        """Baratheon Init"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """Baratheon Str"""
        return f"Vector: ('{self.first_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Baratheon Repr"""
        return self.__str__()

    def die(self):
        """Baratheon Die"""
        self.is_alive = False


class Lannister(Character):
    """Lannister Class"""
    def __init__(self, first_name, is_alive=True):
        """Lannister Init"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """Lannister Str"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Lannister Repr"""
        return self.__str__()

    @staticmethod
    def create_lannister(first_name, is_alive):
        """Lannister Create"""
        return Lannister(first_name, is_alive)
