from random import randint


# The class Calc is a model that represents a calculator.
class Calc:
    # __init__ method is a special method that is called when an object is created from a class.
    # The first parameter of a method is always the object itself. By convention, it is called self.
    # A private attribute(self.__attribute) is one that can only be accessed within the class itself.
    # A public attribute(self.attribute) is one that can be accessed from outside the class.
    def __init__(self: object, difficulty: int, /) -> None:  # The / is used to indicate that the parameters before it
        self.__difficulty: int = difficulty  # In this case, the class is Calc and the attribute is __difficulty.
        self.__value1: int = self.create_value  # The first value of the operation.
        self.__value2: int = self.create_value  # The second value of the operation.
        self.__operation: int = randint(1, 3)  # 1 -> add, 2 -> subtract, 3 -> multiply.
        self.__result: float = self.create_result  # The result of the operation.

    # Creating getter properties for the private attributes

    # The @property decorator is used to give some methods especial functions and make them act like getters and
    # setters. A getter is a method that gets the value of a property. A setter is a method that sets the value of a
    # property.

    @property
    def difficulty(self: object) -> int:  # getter -> 'get_difficulty()'
        return self.__difficulty

    @property
    def value1(self: object) -> int:  # getter -> 'get_value1()'
        return self.__value1

    @property
    def value2(self: object) -> int:  # getter -> 'get_value2()'
        return self.__value2

    @property
    def operaion(self: object) -> int:  # getter -> 'get_operation()'
        return self.__operation

    @property
    def result(self: object) -> float:  # getter -> 'get_result()'
        return self.__result

    # __str__ method is a special method that is called when an object is printed.
    def __str__(self: object) -> str:
        op: str = ''
        if self.__operation == 1:
            op = 'Add'
        elif self.__operation == 2:
            op = "Subtract"
        elif self.__operation == 3:
            op = "Multiply"
        else:
            op = "Unknown operation"
        return f'Value 1: {self.value1} \nValue 2: {self.value2} \nDifficulty: {self.difficulty} \nOperation: {op}'

    @property
    # The create_value method creates a random value based on the difficulty.
    def create_value(self: object) -> int:
        pass

    @property
    # The create_result method creates the result of the operation.
    def create_result(self: object) -> int:
        pass

    # The check_result method checks if the answer is correct.
    def check_result(self: object, answer: int) -> bool:
        pass

    def show_operation(self: object) -> None:
        pass
