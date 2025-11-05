# สร้าง Superclass (คลาสแม่)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person {self.name} ถูกสร้างขึ้น")

    def introduce(self):
        print(f"สวัสดีครับ ผมชื่อ {self.name}, อายุ {self.age} ปี")

# สร้าง Subclass (คลาสลูก)
class Student(Person):
    def __init__(self, name, age, student_id):
        # ใช้ super() เพื่อเรียก __init__ ของคลาสแม่
        super().__init__(name, age)
        self.student_id = student_id
        print(f"Student {self.name} ถูกสร้างขึ้น")

    def study(self):
        print(f"{self.name} (รหัส {self.student_id}) กำลังอ่านหนังสือ")

#  ทดสอบการทำงาน 1
if __name__ == "__main__":
    print("--- สร้าง Person ---")
    p1 = Person("สมชาย", 40)
    p1.introduce()
    

    print("\n--- สร้าง Student ---")
    s1 = Student("สมหญิง", 20, "6501001")
    s1.introduce()
    s1.study()

#การเขียนทับเมธอด (Method Overriding)
class Person2:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"สวัสดีครับ ผมชื่อ {self.name}")

class Student2(Person2):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    # เขียนทับเมธอด introduce() ของคลาสแม่
    def introduce(self):
        # จะเลือกใช้ของตัวเองแทนของแม่
        print(f"สวัสดีครับ ผมชื่อ {self.name} รหัสนักศึกษา {self.student_id}")

#  ทดสอบการทำงาน 2
print("\n=== ตัวอย่างที่ 2: การเขียนทับเมธอด ===")
p2 = Person2("สมปอง")
s2 = Student2("สมศรี", "6501002")

p2.introduce()  # ใช้ของคลาสแม่
s2.introduce()  # ใช้ของคลาสลูก (Overridden)