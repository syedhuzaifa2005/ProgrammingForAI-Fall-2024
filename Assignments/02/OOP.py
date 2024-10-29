# Base class for Animal
class Animal:
  def __init__(self, name, age, habitat):
    self.name = name
    self.age = age
    self.habitat = habitat
    self.available = True

  def mark_availability(self, status):
    if status.lower() == 'quarantine':
        self.available = False
    elif status.lower() == 'available':
        self.available = True
    else:
        print("Status not recognized. Please use 'quarantine' or 'available'.")

  def display_info(self):
    availability = "Available for viewing" if self.available else "In quarantine"
    print(f"Name: {self.name}, Age: {self.age}, Habitat: {self.habitat}, Status: {availability}")


# Subclass for Mammal
class Mammal(Animal):
  def __init__(self, name, age, habitat, fur_length, diet):
    super().__init__(name, age, habitat)
    self.fur_length = fur_length
    self.diet = diet

  def display_info(self):
    super().display_info()
    print(f"Fur Length: {self.fur_length}, Diet Type: {self.diet}")


# Subclass for Bird
class Bird(Animal):
  def __init__(self, name, age, habitat, wingspan, flight_altitude):
    super().__init__(name, age, habitat)
    self.wingspan = wingspan
    self.flight_altitude = flight_altitude

  def display_info(self):
    super().display_info()
    print(f"Wingspan: {self.wingspan} meters, Flight Altitude: {self.flight_altitude} meters")


# Subclass for Reptile
class Reptile(Animal):
  def __init__(self, name, age, habitat, scale_pattern, venomous_status):
    super().__init__(name, age, habitat)
    self.scale_pattern = scale_pattern
    self.venomous_status = venomous_status

  def display_info(self):
    super().display_info()
    venomous = "Yes" if self.venomous_status else "No"
    print(f"Scale Pattern: {self.scale_pattern}, Venomous: {venomous}")


# Creating instances of each type of animal
lion = Mammal("Lion", 2, "Jungle", "Short", "Carnivore")
eagle = Bird("Eagle", 3, "Mountains", 2.0, 1000)
cobra = Reptile("Razor Diamondback", 3, "Jungle", "Diamond", True)

# Display information of each animal
print("Animal Information:")
lion.display_info()
print("\n")
eagle.display_info()
print("\n")
cobra.display_info()
print("\n")

# Changing availability status
print("Updating Availability Status:")
lion.mark_availability("quarantine")
eagle.mark_availability("available")
cobra.mark_availability("quarantine")

# Display updated information
print("\nUpdated Animal Information:")
lion.display_info()
print("\n")
eagle.display_info()
print("\n")
cobra.display_info()