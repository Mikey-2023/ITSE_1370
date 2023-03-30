def main():
    nbrlist = [10, 20, 30]
    x = 0.5
    processList(nbrlist, x)
    print(x * nbrlist[0])


def processList(list, a):
    a = 2.0
    for i in range(len(list)):
        list[i] = list[i] * 10


# The entry point for program execution
if __name__ == "__main__":
    main()
