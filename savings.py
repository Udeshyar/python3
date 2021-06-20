class SavingAccount:
    annual_intrest_rate = 5

    def init(self, saving_balance):
        self.saving_balance = saving_balance


def MonthlyInterest(customer):
    customer.saving_balance = customer.saving_balance + customer.saving_balance * (
                customer.annual_intrest_rate / 12) * 0.01
    print("Saving Balance = ", customer.saving_balance)


def modifyintrestRate(customer):
    print("current intrest is %", customer.annual_intrest_rate)
    customer.annual_intrest_rate = input("Enter new Inerest Rate")


saver1 = SavingAccount(2000)
saver2 = SavingAccount(3000)
# MonthlyInterest(saver1)
# MonthlyInterest(saver2)
print(saver1.saving_balance)
print(saver2.saving_balance)
# modifyintrestRate(saver1)
# modifyintrestRate(saver2)
# MonthlyInterest(saver1)
# MonthlyInterest(saver2)