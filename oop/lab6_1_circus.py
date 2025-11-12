# ใบงานที่ 6.1 : โรงละครสัตว์

# 1. สร้าง Superclass Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("สัตว์ชนิดนี้ส่งเสียง...")

# 2. Subclass Dog
class Dog(Animal):
    def make_sound(self):
        print(f"{self.name}: โฮ่ง! โฮ่ง!")

# 3. Subclass Cat
class Cat(Animal):
    def make_sound(self):
        print(f"{self.name}: เมี้ยว...")

# 4. Subclass Bird
class Bird(Animal):
    def make_sound(self):
        print(f"{self.name}: จี๊บ! จี๊บ!")

# 5. ส่วนของ Polymorphism
animals = [
    Dog("บ๊อบบี้"),
    Cat("เต้าหู้"),
    Bird("ไข่เจียว"),
    Dog("ร็อกกี้"),
    Cat("มะลิ")
]

# ใช้ Polymorphism เรียก make_sound() โดยไม่ต้องรู้ชนิดของสัตว์
for animal in animals:
    animal.make_sound()
