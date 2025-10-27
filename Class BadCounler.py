class Counter:
    def __init__(self):
        self._value = 0

    @property
    def value(self):
        return self._value

    def inc(self):
        self._value += 1

    def dec(self):
        if self._value > 0:
            self._value -= 1

# ตัวอย่างใช้งาน
c = Counter()
print(c.value)  
c.inc()
print(c.value)  