class calculator:
    """Calculator class"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculates the dot product of two vectors"""
        print(f"Dot product is: {sum([x * y for x, y in zip(V1, V2)])}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Calculates the sum of two vectors"""
        print(f"Add Vector is : {[float(x + y) for x, y in zip(V1, V2)]}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Calculates the difference of two vectors"""
        print(f"Sub Vector is : {[float(x - y) for x, y in zip(V1, V2)]}")
