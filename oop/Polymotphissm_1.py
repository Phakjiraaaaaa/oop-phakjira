class Person:

    def __init__(self, name):

        self.name = name

    def introduce(self):

        print(f"สวัสดีครับ ผมชื่อ {self.name} (เป็น Person)")

 

class Student(Person):

    def __init__(self, name, student_id):

        super().__init__(name)

        self.student_id = student_id

    # Override

    def introduce(self):

        print(f"สวัสดีค่ะ หนูชื่อ {self.name} รหัสนักศึกษา {self.student_id} (เป็น Student)")

 

class Teacher(Person):

    def __init__(self, name, subject):

        super().__init__(name)

        self.subject = subject

    # Override

    def introduce(self):

        print(f"สวัสดีครับ ผมครู {self.name} สอนวิชา {self.subject} (เป็น Teacher)")

 

# ----- พลังของ Polymorphism เริ่มตรงนี้ -----

# 1. เราสร้างอ็อบเจกต์จากคลาสที่ *ต่างกัน* แต่มี *แม่คนเดียวกัน*

p1 = Person("สมชาย")

s1 = Student("สมหญิง", "6501001")

t1 = Teacher("สมศักดิ์", "OOP")

 

# 2. เราจับพวกเขามัดรวมกันใน List เดียวกัน

# เราปฏิบัติต่อทุกคนในฐานะ "Person"

people_list = [p1, s1, t1]

 

print("--- เริ่มการแนะนำตัว ---")

 

# 3. เราใช้ Loop เดียว และเรียกเมธอด "introduce()" เดียวกัน

for person in people_list:

    # โค้ดบรรทัดนี้ "person.introduce()" คือ Polymorphism

    # มันเรียกเมธอดที่ถูกต้องตามชนิดของอ็อบเจกต์นั้นๆ อัตโนมัติ!

    person.introduce()