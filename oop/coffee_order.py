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

    def total_price(self):
        addon_cost = sum(self.ADDON_PRICE.get(a, 0) for a in self.add_ons)
        size_extra = {"S": 0, "M": 5, "L": 10, "XL": 20}.get(self.size, 0)
        return self.base_price + size_extra + addon_cost

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
        price = available_menus[m]
        if price < 40:
            price = 40
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

    print("\nAdd-ons ที่มีให้เลือก:")
    for name, price in CoffeeOrder.ADDON_PRICE.items():
        print(f"- {name.capitalize()} (+{GREEN}{price} บาท{RESET})")
    addons_input = input("เลือก Add-ons (คั่นด้วยจุลภาค หากไม่มีให้กด Enter): ").strip()
    add_ons = [a.strip().lower() for a in addons_input.split(",") if a.strip()]

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
