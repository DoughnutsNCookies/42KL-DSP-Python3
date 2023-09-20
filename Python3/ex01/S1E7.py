from S1E9 import Character


class Baratheon(Character):
    """Baratheon Class"""
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        return f"Vector: ('{self.first_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return self.__str__()

    def die(self):
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
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def create_lannister(first_name, is_alive):
        """Lannister Create"""
        return Lannister(first_name, is_alive)
