# INHERITANCE

class Animal:

    def __init__(self):
        self.number_of_eyes = 2

    def breathe(self):
        print("Inhale...Exhale")


class Fish(Animal):

    def __init__(self):
        super().__init__()
        
    def breathe(self):
        super().breathe()
        return "doing this under water"


nemo = Fish()
print(nemo.breathe())
