class BankAccount:
    def __init__(self,owner, balance):
        self.owner = owner
        self._balance = balance
        
account = BankAccount("Tom", 1000)
account.balance =- 500  

print(account.balance)
