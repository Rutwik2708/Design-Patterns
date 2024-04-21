class dog():
    def __init__(self,name):
        self.name =name
    
    def speak(self):
        return "Woof!"

class cat():
    def __init__(self,name):
        self.name =name
    
    def speak(self):
        return "Meow!"
    
def get_pet(type ):
    """ Factory method"""
    
    pets = dict(cat=cat("Hope"), dog= dog("Tommy"))
    # print(pets[cat])
    return pets[type]

d = get_pet("dog")
print(d.speak())

c= get_pet("cat")
print(c.speak())



