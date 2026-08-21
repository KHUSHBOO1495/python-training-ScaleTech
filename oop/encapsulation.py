class Account:
    def __init__(self, balance, acc_no, password):
        self.balance = balance
        self.acc_no = acc_no
        self.__acc_pass = password  # private variable

    def debit(self, amount):
        self.balance -= amount
        print(amount, " was debited")
        print("total balance is: ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print(amount, " was credited")
        print("total balance is: ", self.get_balance())

    def get_balance(self):
        return self.balance
    
    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account(1000, 12345, 1564)
acc1.debit(100)
acc1.credit(200)
acc1.reset_pass()