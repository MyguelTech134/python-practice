class Employee:
    def __init__(self, name = "Employe", id = 0000, balance = 0):
        self.name = name
        self.id = id
        self.balance = balance


    def deposit(self, money):
        if money <= 0:
            print("ERROR! Cant deposit a negative or a 0 amount of money!")
        else:
            self.balance += money

    def withdraw(self, money):
        if money > self.balance:
            print("ERROR! Not enoght monney on your account.")
        if money <= 0:
            print("ERROR! Cant withdraw a negative amount of money or 0.")
        else:
            self.balance -= money

    def show_balance(self):
        print(f"Your balance is: $USD {self.balance:.2f}")

