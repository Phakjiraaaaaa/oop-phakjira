class Counter:
    def __init__(self):
        self._value = 0  

    @property
    def value(self):
        return self._value

    def inc(self):
        
        self._value += 1

    def dec(self):

        if self._value == 0:
            raise ValueError("❌ ห้ามลดค่าต่ำกว่า 0") 
        self._value -= 1



# ส่วนทดสอบการทำงาน

print("=== ทดสอบการทำงานของ Counter ===")
c = Counter()

print("ค่าเริ่มต้น:", c.value)
print("เพิ่มค่า 2 ครั้ง...")
c.inc()
c.inc()
print("ค่าปัจจุบัน:", c.value)

print("ลดค่า 3 ครั้ง (ครั้งสุดท้ายจะเกิด error)...")
c.dec()
c.dec()
c.dec()  
