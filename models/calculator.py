from random import randint


# The class Calc is a model that represents a calculator.
class Calculate:
    # __init__ method is a special method that is called when an object is created from a class.
    # A method is a function that is defined inside a class.
    # The first parameter of a method is always the object itself(Calc). By convention, it is called self.
    # A private attribute(self.__attribute) is one that can only be accessed within the class itself.
    # A public attribute(self.attribute) is one that can be accessed from outside the class.
    def __init__(self: object, difficulty: int, /) -> None:  # The / is used to indicate that the parameters before it is positional-only.
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
    # Selecting the operation based on the value of the attribute __operation.
    def __str__(self: object) -> str:
        op: str = '' # Initializing the variable op.
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
        if self.__difficulty == 1:
            return randint(0, 10)
        elif self.__difficulty == 2:
            return randint(0, 100)
        elif self.__difficulty == 3:
            return randint(0, 1000) 
        elif self.__difficulty == 4:
            return randint(0, 10000)
        else:
            return randint(0, 100000)
        

    @property
    # The create_result method creates the result of the operation.
    def create_result(self: object) -> int:
        if self.__operation == 1: # If the operation is add, the result is the sum of the values.
            return self.__value1 + self.__value2
        elif self.__operation == 2: # If the operation is subtract, the result is the difference of the values.
            return self.__value1 - self.__value2
        elif self.__operation == 3: # If the operation is multiply, the result is the product of the values.
            return self.__value1 * self.__value2
        else:
            return 0

    @property
    # The _operation_symbol method returns the symbol of the operation.
    def _operation_symbol(self: object) -> str:
        if self.__operation == 1:
            return '+'
        elif self.__operation == 2:
            return '-'
        elif self.__operation == 3:
            return '*'
        else:
            return 'Unknown operation!'
        
    # The check_result method checks if the answer is correct.
    def check_result(self: object, answer: int) -> bool:

        if self.__result == answer:
            print("Right answer!")
            print(f'{self.__value1} {self._operation_symbol} {self.__value2} = {self.__result}')
            return True
        else:
            print("Wrong answer!")
            print(f'{self.__value1} {self._operation_symbol} {self.__value2} = {self.__result}')
            return False
        

    # The show_operation method shows the operation to the player.
    def show_operation(self: object) -> None:
        if self.__operation == 1:
            print(f'{self.__value1} + {self.__value2}')
        elif self.__operation == 2:
            print(f'{self.__value1} - {self.__value2}')
        elif self.__operation == 3:
            print(f'{self.__value1} * {self.__value2}')
        else:
            print('Unknown operation!')
            
