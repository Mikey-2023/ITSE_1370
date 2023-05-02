# Lab8A2
# Michael Camp
# Creates a window that displays the proper change for a given amount of currency
from breezypythongui import EasyFrame


class CurrencyChange(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Money Converter")
        self.addLabel(text="Enter a currency amount in cents and then press the button", row=0, column=0, columnspan=2)

        self.addLabel(text="Amount", row=1, column=0)
        self.inputField = self.addIntegerField(value=0, row=1, column=1)
        self.inputField.bind("<Return>", lambda event: self.makeChange())

        self.computeButton = self.addButton(text="Convert", row=2, column=0, columnspan=2, command=self.makeChange)

        self.addLabel("Dollars", row=3, column=0)
        self.dollars = self.addIntegerField(value=0, row=3, column=1)

        self.addLabel("Quarters", row=4, column=0)
        self.quarters = self.addIntegerField(value=0, row=4, column=1)

        self.addLabel("Dimes", row=5, column=0)
        self.dimes = self.addIntegerField(value=0, row=5, column=1)

        self.addLabel("Nickels", row=6, column=0)
        self.nickels = self.addIntegerField(value=0, row=6, column=1)

        self.addLabel("Pennies", row=7, column=0)
        self.pennies = self.addIntegerField(value=0, row=7, column=1)

    def makeChange(self):
        dollars, quarters, dimes, nickels, pennies = 0, 0, 0, 0, 0
        currency, leftover = 0, 0

        try:
            currency = self.inputField.getNumber()
            if currency < 0:
                self.messageBox(title="ERROR", message="Enter a non-negative number")
        except ValueError:
            self.messageBox(title="ERROR", message="Enter a number")

        if currency >= 100:
            dollars = int(currency / 100)
            leftover = currency % 100
        elif 0 < currency < 100:
            leftover = currency

        if leftover / 25 >= 1:
            quarters = int(leftover / 25)
            leftover = leftover % 25
        if leftover / 10 >= 1:
            dimes = int(leftover / 10)
            leftover = leftover % 10
        if leftover / 5 >= 1:
            nickels = int(leftover / 5)
            leftover = leftover % 5
        if leftover / 1 >= 1:
            pennies = int(leftover / 1)

        self.dollars.setNumber(dollars)
        self.quarters.setNumber(quarters)
        self.dimes.setNumber(dimes)
        self.nickels.setNumber(nickels)
        self.pennies.setNumber(pennies)


def main():
    CurrencyChange().mainloop()


if __name__ == '__main__':
    main()
