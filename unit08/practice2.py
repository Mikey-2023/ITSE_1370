from breezypythongui import EasyFrame


class LayoutDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self)
        self.addLabel(text="TopLeft",row=0,column=0)
        self.addLabel(text="TopRight",row=0,column=1)
        self.addLabel(text="BottomLeft",row=1,column=0)
        self.addLabel(text="BottomRight",row=1,column=1)


def main():
    root = LayoutDemo()
    root.mainloop()


if __name__ == '__main__':
    main()