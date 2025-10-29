class Thermostat:
    """
    คลาสควบคุมอุณหภูมิ (Thermostat)
    - ใช้ควบคุมอุณหภูมิให้อยู่ระหว่าง 16°C ถึง 30°C เท่านั้น
    - สามารถเพิ่มหรือลดอุณหภูมิได้ทีละ 1°C ผ่านเมธอด increase() / decrease()
    """

    def __init__(self, temp: int = 24):
        """
        สร้างวัตถุ Thermostat พร้อมกำหนดค่าเริ่มต้น (temp)
        โดยจะตรวจสอบค่าเริ่มต้นผ่าน setter อัตโนมัติ
        """
        self.temperature = temp  # เรียกใช้ setter ตรวจสอบค่าเริ่มต้น

    @property
    def temperature(self) -> int:
        """Getter: อ่านค่าอุณหภูมิปัจจุบัน"""
        return self._temperature

    @temperature.setter
    def temperature(self, v: int):
        """
        Setter: ตั้งค่าอุณหภูมิ พร้อมตรวจสอบเงื่อนไข
        - ต้องอยู่ในช่วง 16°C ถึง 30°C
        """
        MIN_TEMP = 16
        MAX_TEMP = 30

        if v < MIN_TEMP or v > MAX_TEMP:
            raise ValueError(f"อุณหภูมิที่ตั้งต้องอยู่ในช่วง {MIN_TEMP}°C ถึง {MAX_TEMP}°C เท่านั้น (ตั้ง: {v}°C)")

        self._temperature = v
        print(f"ตั้งอุณหภูมิสำเร็จ: {v}°C")

    def increase(self):
        """เพิ่มอุณหภูมิ 1°C แต่ไม่เกิน 30°C"""
        if self.temperature < 30:
            self.temperature += 1
        else:
            print(" ไม่สามารถเพิ่มอุณหภูมิได้: ถึงขีดจำกัดสูงสุด (30°C)")

    def decrease(self):
        """ลดอุณหภูมิ 1°C แต่ไม่ต่ำกว่า 16°C"""
        if self.temperature > 16:
            self.temperature -= 1
        else:
            print(" ไม่สามารถลดอุณหภูมิได้: ถึงขีดจำกัดต่ำสุด (16°C)")


# --- โปรแกรมทดสอบครบทุกกรณี ---
print("--- เริ่มการทดสอบ Thermostat ---")
thermo = Thermostat(20)

#  1. เคสปกติ (Increase / Decrease)
print("\n เคสปกติ:")
thermo.increase()  # 21°C
thermo.increase()  # 22°C
thermo.decrease()  # 21°C
print(f"   ➜ อุณหภูมิปัจจุบัน: {thermo.temperature}°C")

#  2. เคสเพิ่มจนถึงขีดจำกัดบน (30°C)
print("\n ทดสอบเพิ่มจนถึงขีดจำกัดบน:")
thermo.temperature = 29
thermo.increase()  # 30°C
thermo.increase()  # ไม่สามารถเพิ่มได้
print(f"   ➜ อุณหภูมิปัจจุบัน: {thermo.temperature}°C")

#  3. เคสลดจนถึงขีดจำกัดล่าง (16°C)
print("\n ทดสอบลดจนถึงขีดจำกัดล่าง:")
thermo.temperature = 17
thermo.decrease()  # 16°C
thermo.decrease()  # ไม่สามารถลดได้
print(f"   ➜ อุณหภูมิปัจจุบัน: {thermo.temperature}°C")

#  4. เคสตั้งค่าเริ่มต้นผิดช่วง (ต่ำกว่า 16)
print("\n ทดสอบตั้งค่าเริ่มต้นผิดช่วง (ต่ำกว่า 16):")
try:
    Thermostat(15)
except ValueError as e:
    print(f"    Error: {e}")

#  5. เคสตั้งค่าผิดช่วงผ่าน setter (เกิน 30)
print("\n ทดสอบตั้งค่าผิดช่วงผ่าน setter (เกิน 30):")
try:
    thermo.temperature = 35
except ValueError as e:
    print(f"    Error: {e}")
