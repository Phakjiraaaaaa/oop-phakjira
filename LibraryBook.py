class LibraryBook:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True         # True = ว่าง, False = ถูกยืม
        self.current_borrower = None  # ใครกำลังยืมหนังสืออยู่
        self.history = []             # ประวัติการยืม-คืน
        self.hold_queue = []          # คนที่รอหนังสือ

    # ยืมหนังสือ
    def checkout(self, borrower="ไม่ระบุ"):
        if self.available:
            self.available = False
            self.current_borrower = borrower
            self.history.append(f"ยืมโดย {borrower}")
            print(f"'{self.title}' ถูกยืมเรียบร้อยแล้วโดย {borrower}")
        else:
            print(f"'{self.title}' ไม่สามารถยืมได้ เพราะมีคนยืมอยู่")
            if borrower not in self.hold_queue:
                self.hold_queue.append(borrower)
                print(f"{borrower} ถูกเพิ่มในคิวรอหนังสือ '{self.title}'")

    # คืนหนังสือ
    def checkin(self, returner="ไม่ระบุ"):
        if not self.available:
            self.available = True
            self.history.append(f"คืนโดย {returner}")
            print(f"'{self.title}' ถูกส่งคืนเรียบร้อยแล้วโดย {returner}")
            self.current_borrower = None
            # แจ้งคนที่อยู่ในคิวรอ
            if self.hold_queue:
                next_borrower = self.hold_queue.pop(0)
                print(f"📌 แจ้งว่า {next_borrower} สามารถยืม '{self.title}' ต่อได้")
        else:
            print(f"'{self.title}' ยังว่างอยู่ ยืมได้")

    # แสดงประวัติและสถานะ
    def show_status(self):
        status = "ว่าง" if self.available else f"ถูกยืมโดย {self.current_borrower}"
        print(f"สถานะของ '{self.title}': {status}")
        if self.hold_queue:
            print(f"คิวรอ: {', '.join(self.hold_queue)}")
        else:
            print("คิวรอ: ว่างอยู่")
        if self.history:
            print("ประวัติการยืม-คืน:")
            for record in self.history:
                print(" -", record)
        else:
            print("ประวัติการยืม-คืน: ว่างอยู่")


# --- ตัวอย่างการทดสอบ ---
book1 = LibraryBook("Harry Potter", "J.K. Rowling")
book2 = LibraryBook("1984", "George Orwell")

# book1: สมหญิงยืมแล้วคืน
book1.checkout("สมหญิง")
book1.checkin("สมหญิง")

# book2: สมชายยืมแล้วยังไม่คืน
book2.checkout("สมชาย")

# แสดงสถานะทั้งหมด
book1.show_status()
print()
book2.show_status()
