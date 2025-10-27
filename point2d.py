import math

class Point2D:
    def __init__(self, x, y):
        # กำหนดพิกัด x และ y
        self.x = x
        self.y = y

    def distance(self, other):
        """
        คำนวณระยะ Euclidean ไปยังจุดอื่น
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)

    def midpoint(self, other):
        """
        คืนจุดกึ่งกลางเป็น Point2D ใหม่
        """
        mx = (self.x + other.x) / 2
        my = (self.y + other.y) / 2
        return Point2D(mx, my)

    def __str__(self):
        """
        แสดงผลเป็น "(x, y)"
        """
        return f"({self.x}, {self.y})"


# ===== ตัวอย่างการใช้งาน =====
p1 = Point2D(1, 2)
p2 = Point2D(4, 6)

print("p1:", p1)
print("p2:", p2)
print("ระยะทาง:", p1.distance(p2))
print("จุดกึ่งกลาง:", p1.midpoint(p2))
