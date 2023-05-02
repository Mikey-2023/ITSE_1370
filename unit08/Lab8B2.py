# Lab8B2
# Michael Camp
# Creates a window that displays the proper  for a given amount of
from breezypythongui import EasyFrame


class Remainder(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Remainder of Division")
        self.addLabel(text="Enter an integer numerator and integer denominator", row=0, column=0, columnspan=2)

        self.addLabel(text="Numerator", row=1, column=0)
        self.numerator = self.addIntegerField(value=0, row=1, column=1)
        self.numerator.bind("<Return>", lambda event: self.remainder)

        self.addLabel(text="Denominator", row=2, column=0)
        self.denominator = self.addIntegerField(value=0, row=2, column=1)
        self.denominator.bind("<Return>", lambda event: self.remainder)

        self.computeButton = self.addButton(text="Convert", row=3, column=0, columnspan=2, command=self.remainder)

        self.addLabel("Remainder", row=4, column=0)
        self.remainder = self.addIntegerField(value=0, row=4, column=1)

    def remainder(self):
        try:
            numerator = self.numerator.getNumber()
            denominator = self.denominator.getNumber()
            self.remainder.setNumber(numerator % denominator)
        except ValueError:
            self.messageBox(title="ERROR", message="Enter an integer")


def main():
    Remainder().mainloop()


if __name__ == '__main__':
    main()
