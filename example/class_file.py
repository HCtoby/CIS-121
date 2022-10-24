
# class Car:
#     def __init__(self,number_of_wheels,engine,model,year):
#         self.number_of_wheels = number_of_wheels
#         self.engine = engine
#         self.model = model
#         self.year = year

# def __str__(self):
#     print("===Car info===")
#     print(f"Model: {self.model}")
#     print(f"Engine: {self.engine}")
#     print(f"Year: {self.year}")
#     print(f"Number of wheels: {self.number_of_wheels}")



#     return ""





# def changeYear(self,new_year):
#     self.year = new_year


# def changeEngine(self,new_engine):
#     self.engine = new_engine





""




# class Employee:
#     def __init__(self,hourly_wage,hours_worked_a_week,position,name):
#         self.hourly_wage = hourly_wage
#         self.hours_worked_a_week = hours_worked_a_week
#         self.position = position
#         self.name = name


#     def yearly_salary(self):

#         return (self.hourly_wage*self.hours_worked_a_week*365)



#     def change(self,x):
#         self.x = x

#     L = ["hourly_wage","hours_worked_a_week","position","name"]


#     def __str__(self):
#         print("====Employee info====")
        
#         print(f"Yearly salary: {self.yearly_salary}")
#         print(f"Time: {self.hours_worked_a_week}")
#         print(f"Position: {self.position}")
#         print(f"Name: {self.name}")
#         return " "




""






import math


class Circle:
    
    def __init__(self,radius):
        self.radius = radius
        self.area = math.pi*self.radius**2
        self.perimeter = math.pi*self.radius*2

    def __str__(self):
        print("===For a circle===")
        print(f"Radius: {self.radius}")
        print(f"Area: {self.area}")
        print(f"Perimeter: {self.perimeter}")
        return " "
