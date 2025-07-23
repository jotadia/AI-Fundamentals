from classAnimals.classAnimals import Animals

class Dog(Animals):
    def __init__(self, name, age, gender, color, breed):
        #Inherit all properties and methods from Animals
        super().__init__(name, age, gender, color, species="Dog")
        #Add at least one unique attribute (e.g., breed for Dog, is_dairy for Cow, etc.)
        self.breed = breed

    #Override the make_sound method with the correct animal sound
    def make_sound(self):
        return "Woof!"

    #Add at least one unique method relevant to that animal (e.g., fetch for Dog, scratch for Cat)
    def fetch(self, item):
        return f"{self.name} fetches the {item}!"


    def get_info(self):
        return super().get_info() + f"\nBreed: {self.breed}"