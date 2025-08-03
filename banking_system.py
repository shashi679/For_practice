class bank():
  def __init__(self, balance, account_number):
    self.balance = balance
    self.account_number = account_number
    print("created account with: ", self.balance)
  
  def debit(self, amount):
    self.balance -= amount
    print("debited",amount,"new_balance:",self.balance)
    print("transaction successful: ",self.get_balance())

  def credit(self,amount):
    self.balance += amount
    print("credited",amount,"new_balance: ",self.balance)
    print("transaction successful", self.get_balance())

  def get_balance(self):
    return self.balance


acc1 = bank(10000,"12345")
acc1.debit(1999)
acc1.credit(600)

