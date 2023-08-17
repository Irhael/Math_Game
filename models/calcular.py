from random import randint

class Calc:
    # The first parameter of a method is always the object itself. By convention, we call it self.
    def __init__(self: object, difficulty: int) -> None:
       self.__difficulty: int = difficulty
       self.__value1: float = self._create_value
       self.__value2: float = self._create_value
       self.__operation: int = randint(1, 3)

