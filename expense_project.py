class Expense:
    def __init__(self,name,amount):
        self.name = name
        self.amount = amount

    def display(self):
        print(self.name)
        print(self.amount)
expenses_list=[]
while True:
    print("1.Add Expense")
    print("2.view Expense")
    print("3.Calculate Total")
    print("4.Delete Expense")
    print("5.Quit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter expense name: ")
        amount=float(input("Enter your amount: "))
        expense=Expense(name,amount)
        expenses_list.append(expense)
    elif choice == 2:
        for expense in expenses_list:
            expense.display()
    elif choice == 3:
        total=0
        for expense in expenses_list:
            total+=expense.amount
        print("Total Expense: ", total)
    elif choice == 4:
        if len(expenses_list) == 0:
            print("no expense to delete")
        else:
           for i in range(len(expenses_list)):
                print(i + 1)
                expenses_list[i].display()

           delete_number = int(input("Enter expense number to delete: "))
           index = delete_number - 1

           expenses_list.pop(index)
           print("Expense deleted successfully!")
    elif choice == 5:
        print("Quit")
        break
    else:
        print("Invalid Choice")