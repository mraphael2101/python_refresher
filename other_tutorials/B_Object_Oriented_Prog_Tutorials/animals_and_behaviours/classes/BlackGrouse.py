from other_tutorials.B_Object_Oriented_Prog_Tutorials.animals_and_behaviours.classes.Bird import Bird
from other_tutorials.B_Object_Oriented_Prog_Tutorials.animals_and_behaviours.interfaces.ICanFly import InformalInterfaceICanFly


class BlackGrouse(Bird, InformalInterfaceICanFly):
    """
    BlackGrouse is a concrete class (a subclass of Bird and also implements the
    InformalInterfaceICanFly which provides an implementation of the interface’s methods)
    """

    def __init__(self, age, name):
        print("Inside constructor of BlackGrouse class")

    def calculate_random_age(self) -> None:
        self.age = 0
        print('Overriden method from concrete class Bird. Called in class BlackGrouse -> age {}'.format(self.age))
        super(BlackGrouse, self).calculate_random_age()

    def ascend(self, altitude: float) -> float:
        print("Overriden method (1 of 2) from InformalInterfaceICanFly class")
        return 1.01