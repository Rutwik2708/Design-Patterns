from abc import ABCMeta, abstractclassmethod

class IPerson(metaclass=ABCMeta):
    """Person Interface """
    @abstractclassmethod
    def person_method():
        """Interface Method"""

class Student(IPerson):

    def __init__(self):
        self.name = "Basic Student Name"
    
    def person_method(self):
        print("This is a student")

class Teacher(IPerson):

    def __init__(self):
        self.name = "Basic Teacher Name"

    def person_method(self):
        print("This is a Teacher")

class PersonFactory:
    """Facory Class"""
    @staticmethod
    def build_person(person_type):
        if person_type.lower() =="teacher":
            return Teacher()
        elif person_type.lower() =="student":
            return Student()
        else:
            print("Invalid Person Type!!")
            return -1



if __name__=='__main__':
    choice = input("enter the type of person you want to create")

    person = PersonFactory.build_person(choice)
    person.person_method()