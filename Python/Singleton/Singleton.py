# A singleton is a class that can only have one instance.
class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

# Singleton class
class Singleton(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

if __name__ == "__main__":
    # The client code.
    # The client code may not be aware of the Singleton class, since it works with the Singleton instance
    # through a well-defined method.
    # The client code works with the Singleton instance via a method of the Singleton class.
    # It should always use the same instance of the Singleton class.
    s1 = Singleton(1)
    print(s1)

    # The same instance of the Singleton class.
    s2 = Singleton(2)
    print(s2)
    # We can verify that both the instances are same
    print(s1 == s2)
    print(s1 is s2)