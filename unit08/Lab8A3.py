# Lab8A3
# Michael Camp
# Creates a window that computes cost from given miles and hours
from breezypythongui import EasyFrame


class MilesConverter(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Miles Converter")
        self.addLabel(text="Enter the number of hours and miles", row=0, column=0, columnspan=2)

        self.addLabel(text="Hours", row=1, column=0)
        self.hoursField = self.addFloatField(value=0, row=1, column=1)

        self.addLabel(text="Miles", row=2, column=0)
        self.milesField = self.addFloatField(value=0, row=2, column=1)

        self.convertButton = self.addButton(text="Compute", row=3, column=0, columnspan=2, command=self.convert)

        self.addLabel(text="Rental Cost", row=4, column=0)
        self.rentalCostField = self.addFloatField(value=0, row=4, column=1)

    def convert(self):
        try:
            hours = self.hoursField.getNumber()
            miles = self.milesField.getNumber()
            if hours < 0 or miles < 0:
                self.messageBox(title="ERROR", message="Enter non-negative numbers")
                self.rentalCostField.setValue(0)
                hours, miles = -1, -1
        except ValueError:
            self.messageBox(title="ERROR", message="Enter non-negative numbers")
            self.rentalCostField.setValue(0)
            hours, miles = -1, -1

        if hours >= 0 and miles >= 0:
            self.rentalCostField.setValue(200 + 150 * hours + 2 * miles)


def main():
    MilesConverter().mainloop()


if __name__ == '__main__':
    main()
