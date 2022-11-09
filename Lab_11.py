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
    def __init__(self,ID,name,wage):
        super().__init__(ID,name)
        self.payroll = wage

    def culculate_payroll1(self):
        return self.payroll * 8

    def displayInfo(self):
        print("===Info===")
        print(f"ID: {self.ID}")
        print(f"Name: {self.name}")
        print(f"Payroll: {self.culculate_payroll1()}")
        print(" ")


class CommissionEmployee(Employee):
    def __init__(self,ID,name,wage):
        super().__init__(ID,name)
        self.payroll = wage

    def culculate_payroll2(self):
        return self.payroll * 8 * 5
        
    def displayInfo(self):
        print("===Info===")
        print(f"ID: {self.ID}")
        print(f"Name: {self.name}")
        print(f"Payroll: {self.culculate_payroll2()}")
        print(" ")


class SalaryEmployee(HourlyEmployee):
    def __init__(self,ID,name,wage):
        super().__init__(ID,name,wage)

    def culculate_payroll3(self):
        return self.payroll * 8 * 5 * 52

    def displayInfo(self):
        print("===Info===")
        print(f"ID: {self.ID}")
        print(f"Name: {self.name}")
        print(f"Payroll: {self.culculate_payroll3()}")
        print(" ")        

Bob = Employee(123456,"Bob")
Bob.displayInfo()
Mike = CommissionEmployee(123,"Mike",6)
Mike.displayInfo()