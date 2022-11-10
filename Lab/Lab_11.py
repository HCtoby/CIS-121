class Employee:
    def __init__(self,ID,name):
        self.ID = ID
        self.name = name

    def displayInfo(self):
        print("===Info===")
        print(f"ID: {self.ID}")
        print(f"Name: {self.name}")
        print(" ")


class HourlyEmployee(Employee):
    def __init__(self,ID,name,wage,hour):
        super().__init__(ID,name)
        self.payroll = wage
        self.time = hour

    def culculate_payroll(self):
        return self.payroll * self.time

    def displayInfo(self):
        print("===Info===")
        print(f"ID: {self.ID}")
        print(f"Name: {self.name}")
        print(f"HOurly work: {self.time}")
        print(f"Wage: {self.payroll}")
        print(f"Payroll: {self.culculate_payroll()}")
        print(" ")


class SalaryEmployee(Employee):
    def __init__(self,ID,name,wage):
        super().__init__(ID,name)
        self.wage = wage

    def culculate_payroll1(self):
        return self.wage

    def displayInfo(self):
        print("===Info===")
        print(f"ID: {self.ID}")
        print(f"Name: {self.name}")
        print(f"Payroll: {self.culculate_payroll1()}")
        print(" ")


class CommissionEmployee(SalaryEmployee):
    def __init__(self,ID,name,wage,comission):
        super().__init__(ID,name,wage)
        self.comission = comission

    def culculate_payroll(self):
        return super().culculate_payroll1() + self.comission

    def displayInfo(self):
        print("====Info====")
        print(f"ID: {self.ID}")
        print(f"Name: {self.name}")
        print(f"Weekly Rate: {self.wage}")
        print(f"Comission: {self.comission}")
        print(f"Totally Salary: {self.culculate_payroll()}")
        print(" ")


class PayrollInterface:
    def printInfo():
        ID = int(input("Enter your ID: "))
        name = str(input("Enter your name: "))
        wage = int(input("Enter your wage: "))
        comission = int(input("Enter your comission: "))
        p = CommissionEmployee(ID,name,wage,comission)
        p.displayInfo()

i = PayrollInterface
i.printInfo