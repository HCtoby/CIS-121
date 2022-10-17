# def countdown(value):
#     if value<=0:
#         print("done")
#     else:
#         print(value)
#         countdown(value-1)



""



from xmlrpc.client import MININT


file = open("randomValues.txt","r")
data = file.read().splitlines()




def findMin(data):
    s = 1
    while s ==1:
        j = 0
        old = data[j]
        new = data[j+1]
            

print(findMin(data))

''


def findMin(index,current_min,data):
    minn = data[index]

    if minn <= current_min:
        current_min = minn
    
    if index >= len(data)-1:
        return current_min        

    else:
        return findMin(index+1,current_min,data)


def findMax(index,current_max,data):
    maxn = data[index]

    if maxn >= current_max:
        current_max = maxn

    if index >=len(data)-1:
        return current_max
    
    else:
        return findMax(index+1,current_max,data)
