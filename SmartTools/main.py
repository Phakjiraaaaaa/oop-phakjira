from tools import circle_area, bmi, cm_to_inch, inch_to_cm, kg_to_lb, lb_to_kg, c_to_f, f_to_c

def main():
    while True:
        print("\n=== SmartTools Menu ===")
        print("1. คำนวณพื้นที่วงกลม")
        print("2. คำนวณ BMI")
        print("3. แปลงหน่วยต่าง ๆ")
        print("4. ออกจากโปรแกรม")

        choice = input("เลือกเมนู (1-4): ")

        if choice == "1":
            r = float(input("กรุณาใส่รัศมี (cm): "))
            print(f"พื้นที่วงกลม = {circle_area(r):.2f} ตารางเซนติเมตร")

        elif choice == "2":
            w = float(input("ใส่น้ำหนัก (kg): "))
            h_cm = float(input("ใส่ส่วนสูง (cm): "))
            h = h_cm / 100  # แปลง cm → m
            bmi_value = bmi(w, h)
            
            # กำหนดสถานะ BMI
            if bmi_value < 18.5:
                status = "น้ำหนักน้อย"
            elif bmi_value < 25:
                status = "ปกติ"
            elif bmi_value < 30:
                status = "น้ำหนักเกิน"
            else:
                status = "อ้วน"
            
            print(f"BMI = {bmi_value:.2f}, สถานะ: {status}")

        elif choice == "3":
            while True:
                print("\n-- Converter Menu --")
                print("1. cm → inch")
                print("2. inch → cm")
                print("3. kg → lb")
                print("4. lb → kg")
                print("5. °C → °F")
                print("6. °F → °C")
                print("7. กลับสู่เมนูหลัก")

                conv_choice = input("เลือกการแปลง (1-7): ")

                if conv_choice == "1":
                    cm = float(input("ใส่ความยาว (cm): "))
                    print(f"{cm:.2f} cm = {cm_to_inch(cm):.2f} inch")
                elif conv_choice == "2":
                    inch = float(input("ใส่ความยาว (inch): "))
                    print(f"{inch:.2f} inch = {inch_to_cm(inch):.2f} cm")
                elif conv_choice == "3":
                    kg = float(input("ใส่น้ำหนัก (kg): "))
                    print(f"{kg:.2f} kg = {kg_to_lb(kg):.2f} lb")
                elif conv_choice == "4":
                    lb = float(input("ใส่น้ำหนัก (lb): "))
                    print(f"{lb:.2f} lb = {lb_to_kg(lb):.2f} kg")
                elif conv_choice == "5":
                    c = float(input("ใส่อุณหภูมิ (°C): "))
                    print(f"{c:.2f} °C = {c_to_f(c):.2f} °F")
                elif conv_choice == "6":
                    f = float(input("ใส่อุณหภูมิ (°F): "))
                    print(f"{f:.2f} °F = {f_to_c(f):.2f} °C")
                elif conv_choice == "7":
                    break
                else:
                    print("เลือก 1-7 เท่านั้น!")

        elif choice == "4":
            print("ออกจากโปรแกรมแล้ว ขอบคุณที่ใช้ SmartTools ")
            break
        else:
            print("เลือก 1-4 เท่านั้น!")

if __name__ == "__main__":
    main()
