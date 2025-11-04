class BankAccount:
    def __init__(self,owner, balance):
        self.owner = owner
        self._balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            print("ยอดเงินไม่เพียงพอหรือจำนวนเงินไม่ถูกต้อง")
        
    def get_balance(self):
        return self._balance
        
account = BankAccount("Tom", 1000)

account.deposit(500)
#ฝากเงิน
account.withdraw(200)
#ถอนเงิน
print(account.get_balance())