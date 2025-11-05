class fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def display_info(self):
        return f"Fruit: {self.name}, Color: {self.color}"
    
class apple(fruit):
    def __init__(self, name, color, variety):
        super().__init__(name, color)
        self.variety = variety

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Variety: {self.variety}"
    
# Example usage
my_apple = apple("Apple", "Red", "Fuji")
print(my_apple.display_info())  
# Output: Fruit: Apple, Color: Red, Variety: Fuji   

class tamarind(fruit):
    def __init__(self, name, color, origin):
        super().__init__(name, color)
        self.origin = origin

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Origin: {self.origin}"
    
# Example usage
my_tamarind = tamarind("Tamarind", "Brown", "India")
print(my_tamarind.display_info())  
# Output: Fruit: Tamarind, Color: Brown, Origin: India