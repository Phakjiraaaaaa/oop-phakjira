from abc import ABC, abstractmethod

# Abstract Class
class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass


# Subclasses
class SMSNotification(Notification):
    def send(self, message):
        print("ส่ง SMS แล้ว:", message)


class EmailNotification(Notification):
    def send(self, message):
        print("ส่ง Email แล้ว:", message)


class LineNotification(Notification):
    def send(self, message):
        print("ส่ง LINE แล้ว:", message)


# Main Program
notifies = [
    SMSNotification(),
    EmailNotification(),
    LineNotification()
]

for n in notifies:
    n.send("พัสดุของคุณกำลังจัดส่ง")
