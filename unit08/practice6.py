from breezypythongui import EasyFrame


class CounterDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,title="Counter Demo")
        self.setSize(200,75)
        self.count = 0
        self.label = self.addLabel(text="0",row=0,column=0,columnspan=2)
        self.addButton(text="Next",row=1,column=0,command=self.next)
        self.addButton(text="Reset",row=1,column=1,command=self.reset)

    def next(self):
        self.count += 1
        self.label["text"] = str(self.count)  # this must mean the attributes of Label object label are stored as a dict or something

    def reset(self):
        self.count = 0
        self.label["text"] = "0"  # less computing necessary than self.label["text"] = str(self.count)


def main():
    root = CounterDemo()
    root.mainloop()


if __name__ == '__main__':
    main()

