# ใบงานที่ 6.2 : ระบบคำนวณพื้นที่
import math

# 1. สร้าง Superclass (คลาสแม่แบบ)
class Shape:
    def calculate_area(self):
        # บังคับให้คลาสลูกต้อง override เมธอดนี้
        raise NotImplementedError("Subclass ต้องเขียนเมธอด calculate_area() เอง")

# 2. Subclass Rectangle (สี่เหลี่ยมผืนผ้า)
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

# 3. Subclass Circle (วงกลม)
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

# 4. ส่วนของ Polymorphism
shapes = [
    Rectangle(10, 5),
    Circle(7),
    Rectangle(4, 4)
]

# 5. ใช้ Polymorphism ในการคำนวณพื้นที่
for shape in shapes:
    print(f"พื้นที่ของ {shape.__class__.__name__} คือ {shape.calculate_area():.2f}")
