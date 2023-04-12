import itertools

class Category:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.spent = 0
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def check_funds(self, amount):
        return self.balance >= amount

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
        self.ledger.append({"amount": -amount, "description": description})
        self.balance -= amount
        self.spent += amount
        return True

    def get_balance(self):
        return self.balance

    def transfer(self, amount, other_category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to "+other_category.name)
            other_category.deposit(amount, "Transfer from "+self.name)
            return True
        return False

    def __str__(self):
        printing = self.name.center(30, "*") + '\n'
        for l in self.ledger:
            amount = str(format(list(l.items())[0][1], '.2f'))
            amount = " "*(7 - len(amount)) + amount[0:7]
            category = list(l.items())[1][1]
            category = category[0:23] + " "*(23 - len(category))
            printing += category + amount + '\n'
        self_balance_str = str(self.balance)
        printing += "Total: " + self_balance_str
        return printing

def create_spend_chart(categories):
    names = []
    amounts = []
    for c in categories:
        names.append(c.name)
        amounts.append(c.spent)
    # getting nearest lower number divided by 10 for each percentage
    amounts[:] = [round(100 * x/sum(amounts), -1) for x in amounts]
    # list of percentage range
    percents = list(range(100, -1, -10))
    # storing return value lien by line
    lines = 'Percentage spent by category\n'
    for p in percents:
        lines += str(p).rjust(3) + "| "
        for a in amounts:
            if p <= a:
                lines += "o  "
            else:
                lines += len(amounts)*" "
        lines += "\n"
    # adding dashed lines between percentages and category names
    lines += 4*" " + (3*len(amounts)+1)*"-" + "\n"
    # printing vertically using method described in https://stackoverflow.com/a/32872470
    for i in itertools.zip_longest(*names, fillvalue=" "):
        # starting each line with 5 spaces
        lines += 5*" "
        # printing letters from each word with 2 spaces in between
        if any(j != " " for j in i):
            lines += "  ".join(i)
        # creating new line and compensating for the last 2 spaces
        lines += "  \n"
    # deleting the last empty line
    return lines.rstrip("\n")
