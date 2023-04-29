from breezypythongui import EasyFrame


class ButtonDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self)
        self.label = self.addLabel(text="Hey world.",row=0,column=0,columnspan=2)
        self.clearBtn = self.addButton(text="Clear",row=1,column=0)
        self.restoreBtn = self.addButton(text="Restore",row=1,column=1,state="disabled")


def main():
    root = ButtonDemo()
    root.mainloop()


if __name__ == '__main__':
    main()
