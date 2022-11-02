# import random

# # Parent class
# class student:
#     def __init__(self,name,lastname):
#         self.name = name
#         self.lastname = lastname
#         #  data encapsulation
#         self.ssn = random.randint(1000000000,9999999999)

# #  poly
#     def displayInfo(self):
#         print(f"Name: {self.name}")
#         print(f"Lastname: {self.lastname}")
#         print(f"SSN: {self.ssn}")

#     def gesSSN(self):
#         return self.ssn


# # child class
# # Inhe
# class highSchoolStudent:
#     def __init__(self,name,lastname,grade):
#         super().__init__(name,lastname)
#         self.grade = grade

# #  Poly
#     def displayInfo(self):
#         print(f"Name: {self.name}")
#         print(f"Lastname: {self.lastname}")
#         print(f"SSNL {self.ssn}")



""



class client:
    def __init__(self,username,password,recovery_phrase):
        self.username = username
        self.password = password
        self.recovery_phrase = recovery_phrase

    
    def changeUsername(self,new_name):
        self.username = new_name

    def changePassword(self,new_password):
        self.password = new_password

    def displayInfo(self):
        print(f"Name: {self.username}")
        print(f"Password: {self.password}")


class updateUser(client):
    
    def changeUsername(self,new_name):
        self.username = new_name

    def changePassword(self,new_password):
        self.password = new_password


''