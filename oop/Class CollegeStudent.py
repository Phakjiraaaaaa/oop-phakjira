class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
        self.subjects = []  

    def add_subject(self, subject_name):
       
        if subject_name not in self.subjects:
            self.subjects.append(subject_name)
            print(f"เพิ่มวิชา '{subject_name}' สำเร็จ")
        else:
            print(f"วิชา '{subject_name}' มีอยู่แล้ว")

    def remove_subject(self, subject_name):
        
        if subject_name in self.subjects:
            self.subjects.remove(subject_name)
            print(f"ลบวิชา '{subject_name}' สำเร็จ")
        else:
            print(f"ไม่พบวิชา '{subject_name}'")

    def calculate_grade_level(self):
       
        if self.age < 13:
            return "ประถมศึกษา"
        elif 13 <= self.age <= 15:
            return "มัธยมศึกษาตอนต้น"
        elif 16 <= self.age <= 18:
            return "มัธยมศึกษาตอนปลาย"
        else:
            return "มหาวิทยาลัย"

    def display_info(self):
      
        print(f"รหัสนักเรียน: {self.student_id}")
        print(f"ชื่อ: {self.name}")
        print(f"อายุ: {self.age} ปี ({self.calculate_grade_level()})")
        print(f"เกรดเฉลี่ย: {self.grade}")
        print(f"รายวิชาที่เรียน: {', '.join(self.subjects) if self.subjects else 'ยังไม่มีรายวิชา'}")

    def __str__(self):
       
        return f"{self.student_id} - {self.name} (GPA: {self.grade})"

stu1 = Student("S001", "มีใจ", 16, 3.75)
stu1.add_subject("คณิตศาสตร์")
stu1.add_subject("วิทยาศาสตร์")

stu1.remove_subject("สังคมศึกษา")
stu1.display_info()
print(stu1)




class CollegeStudent(Student):
    def __init__(self, student_id, name, age, grade, major, gpa):
        
        super().__init__(student_id, name, age, grade)
        self.major = major
        self.credits = 0 
        self.gpa = gpa   

    def add_credits(self, credit_amount):
       
        if credit_amount > 0:
            self.credits += credit_amount
            print(f"เพิ่มหน่วยกิต {credit_amount} สำเร็จ (รวมทั้งหมด {self.credits})")
        else:
            print("จำนวนหน่วยกิตต้องมากกว่า 0")

    def calculate_tuition(self):
       
        tuition = self.credits * 1500
        return tuition

    def update_gpa(self, new_gpa):
      
        if 0.0 <= new_gpa <= 4.0:
            self.gpa = new_gpa
            print(f"อัพเดท GPA เป็น {self.gpa}")
        else:
            print("ค่า GPA ต้องอยู่ระหว่าง 0.0 ถึง 4.0")

    def get_academic_status(self):
    
        if self.gpa >= 2.0:
            return "ปกติ"
        else:
            return "Probation (ติดโปร)"

    def __str__(self):
        
        return (f"{self.student_id} - {self.name} | สาขา: {self.major} | "
                f"GPA: {self.gpa} | หน่วยกิต: {self.credits} | สถานะ: {self.get_academic_status()}")


stu2 = CollegeStudent("C001", "สมชาย", 20, 3.85, "เทคโนโลยีสารสนเทศ", 3.25)


stu2.add_subject("ฐานข้อมูล")
stu2.add_subject("โครงสร้างข้อมูล")

stu2.add_credits(18)

print(f"ค่าเทอม: {stu2.calculate_tuition():,.2f} บาท")

stu2.update_gpa(1.95)

stu2.display_info()
print(stu2)