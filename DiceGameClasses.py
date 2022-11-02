import random

class Die:
    def __init__(self,face):
        self.face = face
    
    def __add(self):
        return (self.D1+self.D2)

    def D1(self):
        print("Num =",self.face)
        print("Roll =",random.randint(1,self.face))

    def D2(self):
        print("Num =",self.face)
        print("Roll =",random.randint(1,self.face))
    

    def __str__(self):
        print()