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



