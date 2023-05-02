# Lab8A1
# Michael Camp
# Creates a window that converts given miles to kilometers
from breezypythongui import EasyFrame


class ConvertMilesKilometers(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Miles Converter")

        self.addLabel(text="Enter the number of miles below", row=0, column=0, columnspan=2)

        self.addLabel(text="Miles", row=1, column=0)
        self.inputField = self.addFloatField(value=0, row=1, column=1)
        self.inputField.bind("<Return>", lambda event: self.convert())

        self.addLabel(text="Kilometers", row=2, column=0)
        self.outputField = self.addFloatField(value=0, row=2, column=1, state="readonly")

        self.computeButton = self.addButton(text="Compute", row=3, column=0, columnspan=2, command=self.convert)

    def convert(self):
        try:
            miles = self.inputField.getNumber()
            kilos = miles * 1.609344
            self.outputField.setNumber(kilos)
        except ValueError:
            self.messageBox(title="ERROR", message="Enter a number")


def main():
    root = ConvertMilesKilometers()
    root.mainloop()


if __name__ == '__main__':
    main()
