
class Animals:
    def __init__(self, name, age, gender, color, species):

        self.name = name
        self.age = age
        self.gender = gender
        self.color = color
        self.species = species
        self.weight_kg = None 

    #Getters for each property
    def get_weight_kg(self):
          return self.weight_kg

    def get_name(self):
         return self.name

    def get_age(self):
       return self.age

    def get_gender(self):
      return self.gender

    def get_color(self):
     return self.color

    def get_species(self):
        return self.species

    def update_info(self, name=None, age=None, gender=None, color=None, species=None):
        if name: self.name = name
        if age: self.age = age
        if gender: self.gender = gender
        if color: self.color = color
        if species: self.species = species

    def is_adult(self):
        return self.age >= 3

    #Override the make_sound method with the correct animal sound
    def make_sound(self):
        return "Some generic animal sound."

    def get_info(self):
        #A method to return all the information as a formatted string
        info = (
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Adult: {'Yes' if self.is_adult() else 'No'}\n"
            f"Gender: {self.gender}\n"
            f"Color: {self.color}\n"
            f"Species: {self.species}"
        )
        if self.weight_kg is not None:
            info += f"\nWeight: {self.weight_kg} kg"
        
        return info

    #A method to set the animal's weight in kilograms, by passing the value in pounds
    def set_weight_from_pounds(self, pounds):

        self.weight_kg = pounds * 0.453592
        return self.weight_kg