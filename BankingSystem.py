# banking account stytem 

class BankAccount:
    def __init__(self , account_number , account_holder , balance =0.0): # this is an attribute creatred
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self , amount):
        # conditional statements
        if amount > 100:
            self.balance += amount
            print(f"Successfully deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print ("insufficent funds to deposite in your BankAccount")

    def Withdrawl (self , amount):
        if amount < 0:
           self.balance -= amount
           print(f"Successfuly withdrawl ${amount:.2f}. New Balance: ${self.balance:.2f}")
        else:
            print (f"Account balance is ${self.balance:.2f}")

    def balance (self ):
        print (f"the account {self.account_number} Holder {self.account_holder}  balance is {self.balance}")

class SavingAccount (BankAccount): # inherit from bankaccount to save in a savingAccount
    def __init__(self, account_number, account_holder, balance=0 , interest_rate = 4.0):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest applied: ${interest}. New balance: ${self.balance}")

person1 = BankAccount(100, "Tobias Omondi", 20000)
print (person1.account_holder)
print (person1.account_number)
print (person1.balance)
person2 = BankAccount(110 , "Mike Mutuwa" , 300000000.00)
print(person2.account_number)
print(person2.account_holder)
print(person2.balance)

person3 = SavingAccount(111, 'Peter Kilwa', 300000, 5.0)
print(person3.account_number)
print(person3.account_holder)
print(person3.balance)
print(person3.interest_rate)
