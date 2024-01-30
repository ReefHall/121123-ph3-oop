# a class is an object
# it stores information
# it has attributes
# it has methods

class Robot:
    
    def __init__(self, name, age, tv_show, car="BMW"):
        self.name = name
        self._age = age
        self.tv_show = tv_show
        self.car = car
        print("ROBOT BEING BOOTED UP")

    def __repr__(self):
        return f"Robot(name={self.name}, age={self.age}, tv_show={self.tv_show})"
    
    def drive(self):
        print(f"I AM {self.name} AND I AM DRIVING A {self.car} TO AUTOZONE TO BUY NEW PARTS")

    # GETTER / READ #
    @property
    def age(self):
        print("I AM A PROPERTY GETTER!")
        return self._age

    # SETTER / WRITE #
    @age.setter
    def age(self, new_age):
        print(new_age)
        if type(new_age) == int and new_age % 2 == 0:
            print("I AM THE PROPERY SETTER")
            self._age = new_age
        else:
            raise TypeError("Robot age must be a number idiot!")