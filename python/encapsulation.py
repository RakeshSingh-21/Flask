#encapsulation with getter and setter methods
#public,protected,private variables or access variables
# class Person:
#     def __init__(self,name,age):
#         self.name = name ##public variables/instance variable
#         self.age = age   ##public variables

# def get_name(person):
#     return person.name

# person= Person("John",18)
# print(person.name)  
# print(dir(person))
# get_name(person)
# print(get_name(person))

#-----------------------------------------------------------
# variables that are imp and dont want to access from outside

# class Person:
#     def __init__(self,name,age):
#         self.__name = name ##private variables/instance variable
#         self.__age = age   ##private variables

# def get_name(person):
#     return person.__name
    # return person._Person__age
# person= Person("John",18)
# print(dir(person))
# print(get_name(person))

#-----------------------------------------------------------
# class Person:
#     def __init__(self,name,age,gender):
#         self._name = name ##protected variables/instance variable
#         self._age = age   ##protected variables
#         self._gender = gender

# class Employee(Person):
#     def __init__(self,name,age,gender):
#         super().__init__(name,age,gender)  #protected var is accessible from derived class

# employee = Employee("John",23,"M")
# print(employee._name)

#-------------------------------------------------------------
# Encapsulation with getter and setter
class Person:
    def __init__(self,name,age):
        self.__name = name ##private access modifier or variables
        self.__age = age   #it should be restricted within the class itself

    # getter method for name
    def get_name(self):
        return self.__name  

    ##setter method
    def set_name(self,name):
        self.__name = name 

    def get_age(self):
        return self.__age
    # setter method
    def set_age(self,age):
        if age>0:
            self.__age=age
        else:
            print("Age cannot be negative")

person= Person("John",18)
# access and modify private variables using getter and setter methods
print(person.get_name())
print(person.get_age())

person.set_age(35)
print(person.get_age())

person.set_age(-5)

