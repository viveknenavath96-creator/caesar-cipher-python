class BankAccount:
    def __init__(self,name,balance=0):
        self.holder_name=name
        self.acc_balance=balance

    def deposit(self,amount):
        self.acc_balance=self.acc_balance+amount
        print(f"{amount} successfully deposited")

    def withdraw(self,amount):
        if amount>self.acc_balance:
            print("Not enough money")

        else:
            self.acc_balance=self.acc_balance-amount
            print(f"Money withdraw {amount} successfully ") 

#    def __str__(self):                this is also a way to define 
#        return f"Account Holder Name: {self.account_holder}\nBalance: {self.balance}"        
 #obj = BankAccount("Vivek", 1000)
#print(obj)
#obj.deposit(200)
#obj.withdraw(500)
#print(obj)

b1=BankAccount("vivek",1000) 
print("Account Holder Name:", b1.holder_name)
print("Balance:", b1.acc_balance)

b1.deposit(200)
b1.withdraw(500)

print("Account Holder Name:", b1.holder_name)
print("Balance:", b1.acc_balance)