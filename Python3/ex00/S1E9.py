from abc import ABC, abstractmethod


class Character(ABC):
    """Character Class"""
    @abstractmethod
    def __init__(self, name, is_alive=True):
        """Character Init"""
        self.first_name = name
        self.is_alive = is_alive

    @abstractmethod
    def change_health_state(self):
        """Character Change Health"""
        pass


class Stark(Character):
    """Stark Class"""
    def __init__(self, name, is_alive=True):
        """Stark Init"""
        self.first_name = name
        self.is_alive = is_alive

    def change_health_state(self):
        """Stark Change Health State"""
        self.is_alive = not self.is_alive

    def die(self):
        """Stark Die"""
        self.is_alive = False
