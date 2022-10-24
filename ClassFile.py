"""
#Name    Haozhe Chen
#Date    10/23

This implements the RoboFriend class.
"""

class RoboFriend:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age

        self.stateName = "Hi. I'm "+str(self.name)
        self.stateAge = "I'm "+str(self.age)
    
    
    def __str__(self):

        print(self.stateName)
        print(self.stateAge)

        return " "