class BankAccount:
    def __init__(self, owner,bank_name, account_number, balance):
        self.owner = owner
        self.__balance = balance
        self.bank_name = bank_name
        self.account_number = account_number
    def show_balance(self):
        print("Owner:", self.owner)
        print("Balance:", self.__balance)
        print("Bank Name:", self.bank_name)
        print("Account ID:", self.account_number)
account1 = BankAccount("Spandana", "UNION BANK OF INDIA", "222U1A3371",100000)
account1.show_balance()

class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.account_type = "Savings"
        self._balance = balance
    def deposit(self, amount):
        if 0 < amount <= self.__balance:
            self._balance -= amount
            print("withdrawl Successful")
        else:
            print("Insufficient balance or invalid amount") 
    def show_balance(self):
        print("Balance:", self._balance)
account = BankAccount("John", 1000)
print("Owner:", account.owner)
print("Account type:", account.account_type)



# Encapsulation Example Using Access Modifiers
class student:
    def __init__(self,name, age, marks, grade):
        self.name = name    # public
        self.__age = age      # private
        self._marks = marks # protected
        self.grade = grade
    def details(self):
        print("name :", self.name)
        print("age: ", self.__age)
        print("marks :", self._marks)
        print("grade: ", self.grade)
result = student("spandana", 20, 70, "A")
result.details()



        