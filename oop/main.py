# main.py

import converter

# ตัวอย่างการใช้งาน

# แปลง 25°C เป็น °F
result_f = converter.c_to_f(25)
print(f"25°C = {result_f}°F")

# แปลง 77°F เป็น °C
result_c = converter.f_to_c(77)
print(f"77°F = {result_c}°C")
