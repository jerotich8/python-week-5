class Pet:
    def __init__(self,name,breed,color):
        self.name = name
        self.breed = breed
        self.color = color
    
    def sleep(self):
        return f"The {self.color} {self.breed} {self.name} is sleeping"
    
my_pet = Pet("Cat","sokoke","black")

print(my_pet.breed)
print(my_pet.sleep())

class fastPets(Pet):
    pass

Luna = fastPets("Dog","Samoyed","White")
print(Luna.sleep())