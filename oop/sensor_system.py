from abc import ABC, abstractmethod

# Abstract Class หลัก
class Sensor(ABC):
    @abstractmethod
    def read_value(self):
        """อ่านค่าจากเซ็นเซอร์"""
        pass

# คลาสลูกต่างๆ
class TempSensor(Sensor):
    def read_value(self):
        # ตัวอย่างการอ่านค่าอุณหภูมิ
        return "25.5°C"

class HumiditySensor(Sensor):
    def read_value(self):
        # ตัวอย่างการอ่านค่าความชื้น
        return "65% RH"

class LightSensor(Sensor):
    def read_value(self):
        # ตัวอย่างการอ่านค่าความสว่าง
        return "450 lux"

class GasSensor(Sensor):
    def read_value(self):
        # ตัวอย่างการอ่านค่าก๊าซ
        return "350 ppm"

# เซ็นเซอร์ใหม่ที่เพิ่มได้ไม่กระทบระบบหลัก
class PressureSensor(Sensor):
    def read_value(self):
        return "1013.25 hPa"

class MotionSensor(Sensor):
    def read_value(self):
        return "No motion detected"

# ระบบจัดการเซ็นเซอร์
class SensorManager:
    def __init__(self):
        self.sensors = []
    
    def add_sensor(self, sensor):
        """เพิ่มเซ็นเซอร์ลงในระบบ"""
        if isinstance(sensor, Sensor):
            self.sensors.append(sensor)
        else:
            raise TypeError("ต้องเป็นวัตถุของคลาส Sensor")
    
    def read_all_sensors(self):
        """อ่านค่าจากเซ็นเซอร์ทั้งหมด"""
        readings = {}
        for i, sensor in enumerate(self.sensors):
            readings[f"Sensor_{i+1}_{sensor.__class__.__name__}"] = sensor.read_value()
        return readings
    
    def get_sensor_count(self):
        """นับจำนวนเซ็นเซอร์ในระบบ"""
        return len(self.sensors)
    
    def display_readings(self):
        """แสดงผลการอ่านค่าทั้งหมด"""
        print("=== Sensor Readings ===")
        readings = self.read_all_sensors()
        for sensor_name, value in readings.items():
            print(f"{sensor_name}: {value}")
        print(f"\nTotal sensors: {self.get_sensor_count()}")
        print("-" * 30)

# ตัวอย่างการใช้งานเต็มรูปแบบ
def main():
    # สร้างระบบจัดการ
    manager = SensorManager()
    
    # เพิ่มเซ็นเซอร์พื้นฐาน
    print(" เริ่มต้นระบบจัดการเซ็นเซอร์")
    manager.add_sensor(TempSensor())
    manager.add_sensor(HumiditySensor())
    manager.add_sensor(LightSensor())
    manager.add_sensor(GasSensor())
    
    # แสดงผลครั้งแรก
    manager.display_readings()
    
    # เพิ่มเซ็นเซอร์ใหม่ (แสดงความยืดหยุ่น)
    print(" เพิ่มเซ็นเซอร์ใหม่")
    manager.add_sensor(PressureSensor())
    manager.add_sensor(MotionSensor())
    
    # แสดงผลหลังจากเพิ่มเซ็นเซอร์ใหม่
    manager.display_readings()
    
    # สาธิตการอ่านค่าเฉพาะ
    print(" อ่านค่าเฉพาะบางเซ็นเซอร์:")
    readings = manager.read_all_sensors()
    for name, value in list(readings.items())[:3]:  # แสดง 3 อันแรก
        print(f"  {name}: {value}")

# ฟังก์ชันทดสอบการเพิ่มเซ็นเซอร์แบบไดนามิก
def test_dynamic_sensor():
    """ทดสอบการเพิ่มเซ็นเซอร์ใหม่โดยไม่กระทบระบบ"""
    print("\n ทดสอบการเพิ่มเซ็นเซอร์แบบไดนามิก")
    
    manager = SensorManager()
    
    # เพิ่มเซ็นเซอร์ตามต้องการ
    sensors_to_add = [TempSensor(), HumiditySensor(), PressureSensor()]
    
    for sensor in sensors_to_add:
        manager.add_sensor(sensor)
    
    manager.display_readings()

if __name__ == "__main__":
    main()
    test_dynamic_sensor()