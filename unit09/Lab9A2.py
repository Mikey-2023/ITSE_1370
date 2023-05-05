# Lab9A2
# Michael Camp
# This program defines a class 'EmployeeData' that creates employee objects that store the
# employee's name, job title, salary, and years of service; it also contains a method for giving the employee a raise

class EmployeeData:
    def __init__(self, name: str, title: str, salary: float, years: int):
        """Creates object given employee's name, title, salary, and years of service"""
        self.name = name
        self.title = title
        self.salary = salary
        self.years = years

    def giveName(self):
        return self.name

    def giveSalary(self):
        return self.salary

    def giveTitle(self):
        return self.title

    def giveYears(self):
        return self.years

    def applyRaise(self, amount: float):
        """Applies raise to employee object by given percentage"""
        self.salary *= 1 + amount


def main():
    employee1 = EmployeeData("Helen Calder", "Analyst", 45000, 5)
    employee2 = EmployeeData("Fred Aramis", "Accountant", 67000, 3)

    employee1.applyRaise(0.20)
    employee2.applyRaise(0.15)

    print("employee1 name: {}, salary: {}, title: {}".format(employee1.name, employee1.salary, employee1.title))
    print("employee2 name: {}, salary: {}, title: {}".format(employee2.name, employee2.salary, employee2.title))


if __name__ == '__main__':
    main()
