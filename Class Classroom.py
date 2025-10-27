class Classroom:
    def __init__(self, class_name, teacher, subject, max_students):
        self.class_name = class_name          
        self.teacher = teacher               
        self.subject = subject                
        self.max_students = max_students     
        self.students = {}                   

   
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students[student["id"]] = student
            print(f"เพิ่มนักเรียน {student['name']} เข้าห้องเรียบร้อยแล้ว")
        else:
            print(" ห้องเรียนเต็มแล้ว ไม่สามารถเพิ่มนักเรียนได้")

   
    def remove_student(self, student_id):
        if student_id in self.students:
            removed = self.students.pop(student_id)
            print(f"ลบนักเรียน {removed['name']} ออกจากห้องเรียบร้อยแล้ว")
        else:
            print(" ไม่พบนักเรียนที่ต้องการลบ")


    def find_student(self, student_id):
        return self.students.get(student_id, " ไม่พบนักเรียนในระบบ")

   
    def get_class_size(self):
        return len(self.students)

    
    def is_class_full(self):
        return len(self.students) >= self.max_students

    
    def get_students_by_grade_level(self, level):
        result = [s for s in self.students.values() if s["level"] == level]
        return result

    
    def calculate_average_grade(self):
        if not self.students:
            return 0
        total = sum(s["grade"] for s in self.students.values())
        return total / len(self.students)

    
    def display_class_info(self):
        print(f"ห้องเรียน: {self.class_name}")
        print(f"ครูประจำชั้น: {self.teacher}")
        print(f"วิชา: {self.subject}")
        print(f"นักเรียนทั้งหมด: {self.get_class_size()}/{self.max_students}")
        print(f"เกรดเฉลี่ยของห้อง: {self.calculate_average_grade():.2f}")
        print("รายชื่อนักเรียน:")
        for s in self.students.values():
            print(f" - {s['id']}: {s['name']} (ชั้น {s['level']}), เกรด {s['grade']}")

class1 = Classroom("ม.6/1", "ครูสมศรี", "คณิตศาสตร์", 3)

class1.add_student({"id": 1, "name": "สมชาย", "level": "ม.6", "grade": 3.5})
class1.add_student({"id": 2, "name": "สมหญิง", "level": "ม.6", "grade": 3.8})
class1.add_student({"id": 3, "name": "สมปอง", "level": "ม.6", "grade": 3.9})

print("\n=== ข้อมูลห้องเรียน ===")
class1.display_class_info()

print("\n=== ค้นหานักเรียน ===")
print(class1.find_student(2))

print("\n=== นักเรียนชั้น ม.6 ===")
for s in class1.get_students_by_grade_level("ม.6"):
    print(f"{s['id']} - {s['name']}")

print("\n=== ลบนักเรียน ===")
class1.remove_student(3)

print("\nห้องเต็มหรือยัง:", "เต็มแล้ว" if class1.is_class_full() else "ยังไม่เต็ม")
