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



# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"

# CoffeeOrder class
class CoffeeOrder:
    DRINK_MENU = {
        "coffee": {"hot": 40, "iced": 50, "frappe": 60},
        "tea": {"hot": 35, "iced": 45, "frappe": 55},
        "milk": {"hot": 30, "iced": 40, "frappe": 50},
        "juice": {"iced": 45},
        "cocoa": {"hot": 35, "iced": 45, "frappe": 55},
        "smoothie": {"frappe": 65}
    }
    ADDON_PRICE = {
        "milk": 10,
        "choco": 15,
        "caramel": 15,
        "whip": 20,
        "vanilla": 10
    }

    def __init__(self, drink_type, menu, size, add_ons=None):
        self.drink_type = drink_type
        self.menu = menu
        self.size = size
        self.add_ons = add_ons or []
        base = self.DRINK_MENU.get(drink_type, {}).get(menu, 0)
        self.base_price = base if base >= 40 else 40

    # Add-ons methods
    def add_addon(self, name):
        if name not in self.add_ons and name in self.ADDON_PRICE:
            self.add_ons.append(name)

    def remove_addon(self, name):
        if name in self.add_ons:
            self.add_ons.remove(name)

    def num_addons(self):
        return len(self.add_ons)

    # Price
    def total_price(self):
        addon_cost = sum(self.ADDON_PRICE.get(a, 0) for a in self.add_ons)
        size_extra = {"S": 0, "M": 5, "L": 10, "XL": 20}.get(self.size, 0)
        return self.base_price + size_extra + addon_cost

    # Display
    def show_order(self):
        print(f"\n{MAGENTA}{BOLD}☕ รายการสั่งเครื่องดื่ม ☕{RESET}")
        print(f"- ประเภท: {BLUE}{self.drink_type.capitalize()}{RESET}")
        print(f"- เมนู: {BLUE}{self.menu.capitalize()}{RESET}")
        print(f"- ขนาด: {YELLOW}{self.size}{RESET}")
        if self.add_ons:
            print(f"- Add-ons: {GREEN}{', '.join(self.add_ons)}{RESET}")
        else:
            print(f"- ไม่มี Add-ons")
        print(f"💰 ราคารวม: {RED}{self.total_price()} บาท{RESET}")

# -------------------------------
# Interactive Coffee Order
menu_options = ["coffee", "tea", "milk", "juice", "cocoa", "smoothie"]
orders = []
count = 0

print(f"{YELLOW}{BOLD}╔═════════════════════════════╗{RESET}")
print(f"{YELLOW}{BOLD}║      ☕  สั่งเครื่องดื่ม  ☕      ║{RESET}")
print(f"{YELLOW}{BOLD}╚═════════════════════════════╝{RESET}")

while True:
    count += 1
    print(f"\n--- {CYAN}รายการที่ {count}{RESET} ---")
    for i, name in enumerate(menu_options, start=1):
        print(f"{CYAN}{i}. {name.capitalize()}{RESET}")

    choice = input("เลือกประเภทเครื่องดื่ม (1-6): ").strip()
    if not choice.isdigit() or int(choice) not in range(1, 7):
        print(f"{RED}กรุณาเลือกหมายเลขระหว่าง 1-6 เท่านั้น{RESET}")
        continue
    drink_type = menu_options[int(choice)-1]

    available_menus = CoffeeOrder.DRINK_MENU[drink_type]
    print(f"\n{BOLD}เมนูของ {drink_type.capitalize()}: {RESET}")
    menu_list = list(available_menus.keys())
    for i, m in enumerate(menu_list, start=1):
        price = max(available_menus[m], 40)
        print(f"{i}. {m.capitalize()} ({GREEN}{price} บาท{RESET})")

    menu_choice = input("เลือกเมนูย่อย (หมายเลข): ").strip()
    if not menu_choice.isdigit() or int(menu_choice) not in range(1, len(menu_list)+1):
        print(f"{RED}เลือกเมนูไม่ถูกต้อง{RESET}")
        continue
    menu = menu_list[int(menu_choice)-1]

    print("\nขนาดที่มีให้เลือก: S / M / L / XL")
    size = input("เลือกขนาด: ").strip().upper()
    if size not in ["S","M","L","XL"]:
        print(f"{RED}ขนาดไม่ถูกต้อง{RESET}")
        continue

    # เลือก add-ons แบบง่าย
    add_ons = []
    while True:
        print("\nAdd-ons ที่มีให้เลือก:")
        for i, name in enumerate(CoffeeOrder.ADDON_PRICE.keys(), start=1):
            status = "✓" if name in add_ons else " "
            print(f"{i}. [{status}] {name.capitalize()} (+{GREEN}{CoffeeOrder.ADDON_PRICE[name]} บาท{RESET})")
        inp = input("เลือกหมายเลข add-on เพื่อเพิ่ม/ลบ (Enter เสร็จสิ้น): ").strip()
        if inp == "":
            break
        if not inp.isdigit() or int(inp) not in range(1, len(CoffeeOrder.ADDON_PRICE)+1):
            print(f"{RED}กรอกหมายเลขไม่ถูกต้อง{RESET}")
            continue
        addon_name = list(CoffeeOrder.ADDON_PRICE.keys())[int(inp)-1]
        if addon_name in add_ons:
            add_ons.remove(addon_name)
            print(f"{YELLOW}ลบ add-on '{addon_name}' เรียบร้อยแล้ว{RESET}")
        else:
            add_ons.append(addon_name)
            print(f"{GREEN}เพิ่ม add-on '{addon_name}' เรียบร้อยแล้ว{RESET}")

    order = CoffeeOrder(drink_type, menu, size, add_ons)
    order.show_order()
    orders.append(order.total_price())

    cont = input("\nต้องการสั่งเพิ่มไหม (y/n): ").strip().lower()
    if cont != "y":
        break

# สรุปยอดทั้งหมด
print(f"\n{YELLOW}{BOLD}===  สรุปยอดทั้งหมด  ==={RESET}")
print(f"รวมทั้งหมด {CYAN}{len(orders)} แก้ว{RESET}")
print(f"ยอดรวมทั้งหมด: {GREEN}{sum(orders)} บาท{RESET}")
print(f"{MAGENTA}ขอบคุณที่ใช้บริการค่ะ {RESET}")


# LibraryBook class
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



import math

class Point2D:
    def __init__(self, x, y):
        # กำหนดพิกัด x และ y
        self.x = x
        self.y = y

    def distance(self, other):
        """
        คำนวณระยะ Euclidean ไปยังจุดอื่น
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)

    def midpoint(self, other):
        """
        คืนจุดกึ่งกลางเป็น Point2D ใหม่
        """
        mx = (self.x + other.x) / 2
        my = (self.y + other.y) / 2
        return Point2D(mx, my)

    def __str__(self):
        """
        แสดงผลเป็น "(x, y)"
        """
        return f"({self.x}, {self.y})"


# ===== ตัวอย่างการใช้งาน =====
p1 = Point2D(1, 2)
p2 = Point2D(4, 6)

print("p1:", p1)
print("p2:", p2)
print("ระยะทาง:", p1.distance(p2))
print("จุดกึ่งกลาง:", p1.midpoint(p2))
