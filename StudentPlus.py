class StudentPlus:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def average(self):
        if len(self.scores) == 0:
            return 0
        return sum(self.scores) / len(self.scores)

    def grade(self):
        avg = self.average()
        if avg >= 80:
            return 'A'
        elif avg >= 70:
            return 'B'
        elif avg >= 60:
            return 'C'
        elif avg >= 50:
            return 'D'
        else:
            return 'F'

    def passed(self):
        return self.average() >= 50


# สร้างอ็อบเจกต์อย่างน้อย 2 ชุด
student1 = StudentPlus("สมหญิง", [85, 78, 92])
student2 = StudentPlus("สมชาย", [45, 55, 50])
student3 = StudentPlus("มีชัย", [60, 80, 60])

# พิมพ์สรุปผล
for s in [student1, student2, student3]:
    print(f"Name: {s.name}")
    print(f"Scores: {s.scores}")
    print(f"Average: {s.average():.2f}")
    print(f"Grade: {s.grade()}")
    print(f"Passed: {s.passed()}")
    print("-----")
