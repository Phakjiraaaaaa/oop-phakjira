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