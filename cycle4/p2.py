class BankAccount:
    def __init__(self, AccNo, AccName, AccType, AccBalance=0):
        self.number = AccNo
        self.Name = AccName
        self.Atype = AccType
        self.Balance = AccBalance

    def withdraw(self, Amount):
        try:
            if Amount > self.Balance:
                print("Low balance")
            else:
                self.Balance -= Amount
        except Exception as e:
            print(f"An error occurred during withdrawal: {e}")

    def deposit(self, Amount):
        try:
            self.Balance += Amount
        except Exception as e:
            print(f"An error occurred during deposit: {e}")

    def display(self):
        try:
            print("Account Number: ", self.number)
            print("Account Name: ", self.Name)
            print("Account type: ", self.Atype)
            print("Account Balance: ", self.Balance)
        except Exception as e:
            print(f"An error occurred while displaying account info: {e}")


print("Name: Linto Mathew Joy")
print("Rollno:41")
print("Experiment:12")

try:
    accno = int(input("Enter your acc No: "))
    name = input("Enter your Name: ")
    obj = BankAccount(accno, name, "Savings")

    print("\n1.Account info\n2.Deposit\n3.Withdraw\n4.Exit")
    while True:
        try:
            opt = int(input("Select your option: "))
            if opt == 1:
                obj.display()
            elif opt == 2:
                try:
                    dep = int(input("Enter the value to deposit: "))
                    if dep < 0:
                        raise ValueError("Deposit amount cannot be negative.")
                    obj.deposit(dep)
                    print("Account Balance: ", obj.Balance)
                except ValueError as e:
                    print(f"Invalid deposit value: {e}")
            elif opt == 3:
                try:
                    wid = int(input("Enter the value to withdraw: "))
                    if wid < 0:
                        raise ValueError("Withdrawal amount cannot be negative.")
                    obj.withdraw(wid)
                    print("Account Balance: ", obj.Balance)
                except ValueError as e:
                    print(f"Invalid withdrawal value: {e}")
            elif opt == 4:
                print("Exit")
                break
            else:
                print("Invalid Option")
        except ValueError:
            print("Invalid option. Please enter a valid numeric option.")
except ValueError as e:
    print(f"Invalid account number: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
