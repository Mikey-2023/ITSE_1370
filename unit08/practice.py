from breezypythongui import EasyFrame


class LabelDemo(EasyFrame):  # LabelDemo is a subclass of EasyFrame
    def __init__(self):
        EasyFrame.__init__(self)
        self.addLabel(text="Hey",row=0,column=0)


def main():
    root = LabelDemo()
    root.mainloop()


if __name__ == '__main__':
    main()