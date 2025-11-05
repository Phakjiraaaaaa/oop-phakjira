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
        super().__init__(brand, year)
        self.num_doors = num_doors
    
    def start_engine(self):
        print("รถยนต์: บริ้น... เครื่องยนต์ทำงาน")
    
    def show_details(self):
        super().show_details()  # เรียกการทำงานเดิมของคลาสแม่
        print(f"จำนวนประตู: {self.num_doors}")

class Motorcycle(Vehicle):
    def __init__(self, brand, year, cc):
        super().__init__(brand, year)
        self.cc = cc
    
    def start_engine(self):
        print("มอเตอร์ไซค์: ครีน... เครื่องยนต์ทำงาน")
    
    def show_details(self):
        super().show_details()  # เรียกการทำงานเดิมของคลาสแม่
        print(f"ขนาดเครื่องยนต์: {self.cc} cc")

# ทดลองสร้างอ็อบเจกต์และเรียกเมธอดที่ถูก Override
print("=== ทดสอบรถยนต์ ===")
car1 = Car("Toyota", 2023, 4)
car1.start_engine()  # เรียกเมธอดที่ถูก Override
car1.show_details()   # เรียกเมธอดที่ถูก Override

print("\n=== ทดสอบรถมอเตอร์ไซค์ ===")
motorcycle1 = Motorcycle("Honda", 2022, 150)
motorcycle1.start_engine()  # เรียกเมธอดที่ถูก Override
motorcycle1.show_details()   # เรียกเมธอดที่ถูก Override

print("\n=== ทดสอบเพิ่มเติม ===")
car2 = Car("Honda", 2020, 2)
motorcycle2 = Motorcycle("Yamaha", 2021, 125)

vehicles = [car2, motorcycle2]

for vehicle in vehicles:
    vehicle.start_engine()
    vehicle.show_details()
    print("---")