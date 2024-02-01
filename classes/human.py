class Human:

    # self is the thing itself (the actual instance)
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self._age = 0
        print("Human waking up")

    def __repr__(self):
        return f"Human(first_name={self.first_name}, last_name={self.last_name}, age={self._age})"
    
    def say_full_name(self):
        return self.first_name + " " + self.last_name
    
    def happy_birthday(self):
        print("ITS MY BIRTHDAY!")
        self._age += 1
        print(f"I am {self._age} years old")

    def pay_taxes(self):
        if self.age > 18:
            print("YOU JUST LOST HALF YOUR PAYCHECK MWAHAHAHAHA")
            print("YOINK!")
        else:
            print("You can keep your money... FOR NOW MWHAHAHAHA")
            print("🤌🤌🤌🤌🤌")

    @property # GETTER #
    def age(self):
        return self._age
    
    @age.setter # SETTER #
    def age(self, new_age):
        raise TypeError("Quit lying about your age!")
        #just a test