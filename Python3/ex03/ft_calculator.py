class calculator:
    """Calculator Class"""
    def __init__(self, input_list) -> None:
        """Calculator Init"""
        self.my_list = input_list

    def __add__(self, num) -> None:
        """Calculator Add"""
        self.my_list = [x + num for x in self.my_list]
        print(self.my_list)

    def __mul__(self, object) -> None:
        """Calculator Mul"""
        self.my_list = [x * object for x in self.my_list]
        print(self.my_list)

    def __sub__(self, object) -> None:
        """Calculator Sub"""
        self.my_list = [x - object for x in self.my_list]
        print(self.my_list)

    def __truediv__(self, object) -> None:
        """Calculator Div"""
        try:
            self.my_list = [x / object for x in self.my_list]
            print(self.my_list)
        except ZeroDivisionError as err:
            print(err)
