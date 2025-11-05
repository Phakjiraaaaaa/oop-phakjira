class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    def start_engine(self):
        print("เครื่องยนต์ทำงาน...")
    
    def show_details(self):
        print(f"ยี่ห้อ: {self.brand}, ปีที่ผลิต: {self.year}")

class Car(Vehicle):
    def __init__(self, brand, year, num_doors):
        super().__init__(brand, year)  # ใช้ super() เรียก __init__ ของ Vehicle
        self.num_doors = num_doors
    
    def show_details(self):
        super().show_details()
        print(f"จำนวนประตู: {self.num_doors}")

class Motorcycle(Vehicle):
    def __init__(self, brand, year, cc):
        super().__init__(brand, year)  # ใช้ super() เรียก __init__ ของ Vehicle
        self.cc = cc
    
    def show_details(self):
        super().show_details()
        print(f"ขนาดเครื่องยนต์: {self.cc} cc")

# ทดลองสร้างอ็อบเจกต์จาก Car และ Motorcycle
print("=== ทดสอบรถยนต์ ===")
car1 = Car("Toyota", 2023, 4)
car1.start_engine()
car1.show_details()

print("\n=== ทดสอบรถมอเตอร์ไซค์ ===")
motorcycle1 = Motorcycle("Honda", 2022, 150)
motorcycle1.start_engine()
motorcycle1.show_details()

print("\n=== ทดสอบเพิ่มเติม ===")
car2 = Car("Honda", 2020, 2)
motorcycle2 = Motorcycle("Yamaha", 2021, 125)

car2.show_details()
motorcycle2.show_details()