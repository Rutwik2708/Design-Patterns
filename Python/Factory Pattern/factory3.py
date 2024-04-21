from __future__ import annotations
from abc import ABC, abstractmethod

class Creator(ABC):
    """ Abstract Class having the factory method"""

    @abstractmethod
    def factory_method(self):
        """Abstract method, creator may give some default implemetation as well"""
        pass

    
    def some_operation(self):

        product = self.factory_method()

        result = f"Creator: The creator's code has just excuted with {product.operation()}"
        return result
    

class ConcreteCreator1(Creator):

    def factory_method(self) -> Product:
        return ConcreteProduct1()

class ConcreteCreator2(Creator):

    def factory_method(self) -> Product:
        return ConcreteProduct2()



# Interface and the classes implementing the interface
class Product(ABC):
    """product abstract class can be an interface as well"""
    @abstractmethod
    def operation(self):
        """This will be implemented by all the classes implementing Product class"""
        pass


# Below 2 classes implement the Product Class
class ConcreteProduct1(Product):
    def operation(self):
        return "Result of ConcreteProduct1"


class ConcreteProduct2(Product):
    def operation(self):
        return "Result of ConcreteProduct2"
    
def client_code(creator: Creator) -> None:
    print(f"Client: I am not aware of the creator's class, but it still works.\nClient: {creator.some_operation()}")

if __name__=="__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())

