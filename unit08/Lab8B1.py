# Lab8B1
# Michael Camp
# Creates a window that converts given minutes to seconds
from breezypythongui import EasyFrame


class ConvertMinutesSeconds(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Minutes Converter")

        self.addLabel(text="Enter the number of minutes below", row=0, column=0, columnspan=2)

        self.addLabel(text="Minutes", row=1, column=0)
        self.inputField = self.addFloatField(value=0, row=1, column=1)
        self.inputField.bind("<Return>", lambda event: self.convert())

        self.addLabel(text="Seconds", row=2, column=0)
        self.outputField = self.addFloatField(value=0, row=2, column=1, state="readonly")

        self.computeButton = self.addButton(text="Compute", row=3, column=0, columnspan=2, command=self.convert)

    def convert(self):
        try:
            self.outputField.setNumber(self.inputField.getNumber()*60)
        except ValueError:
            self.messageBox(title="ERROR", message="Enter a number")


def main():
    root = ConvertMinutesSeconds()
    root.mainloop()


if __name__ == '__main__':
    main()
