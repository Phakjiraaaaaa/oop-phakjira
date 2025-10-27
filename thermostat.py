class Thermostat:
    def __init__(self, temp: int = 24):
        self.temperature = temp  # ใช้ setter ตรวจสอบค่าเริ่มต้น

    @property
    def temperature(self) -> int:
        return self._temperature

    @temperature.setter
    def temperature(self, v: int):
        if not (16 <= v <= 30):
            raise ValueError("อุณหภูมิต้องอยู่ในช่วง 16-30°C เท่านั้น")
        self._temperature = v

    def increase(self):
        """เพิ่มอุณหภูมิ 1°C แต่ไม่เกิน 30"""
        if self._temperature < 30:
            self._temperature += 1

    def decrease(self):
        """ลดอุณหภูมิ 1°C แต่ไม่ต่ำกว่า 16"""
        if self._temperature > 16:
            self._temperature -= 1


# -------- ทดสอบแบบสั้น --------
t = Thermostat(24)
print("ค่าเริ่มต้น:", t.temperature, "°C")

# เพิ่มจนถึง 30
while t.temperature < 30:
    t.increase()
print("หลังเพิ่มสูงสุด:", t.temperature, "°C")  # 30°C

# ลดจนถึง 16
while t.temperature > 16:
    t.decrease()
print("หลังลดต่ำสุด:", t.temperature, "°C")  # 16°C
