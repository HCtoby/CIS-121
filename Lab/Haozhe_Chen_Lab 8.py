def clear(data):
    temp = []
    for i in data:
        if i.isdigit():
            temp.append(int(i))
    return temp


def openfile(filename):
    file = open(filename,"r")
    data = file.read().splitlines()
    data = clear(data)
    return data

data = openfile("randomValues.txt")



def findMax(index,current_max,data):
    maxn = data[index]

    if maxn >= current_max:
        current_max = maxn

    if index >=len(data)-1:
        return current_max
    
    else:
        return findMax(index+1,current_max,data)


def findMin(index,current_min,data):
    minn = data[index]

    if minn <= current_min:
        current_min = minn
    
    if index >= len(data)-1:
        return current_min        

    else:
        return findMin(index+1,current_min,data)


def extrema(data,calculate_min=True,calsulate_max=True):
    if calculate_min==True and calsulate_max==True:
        return [findMin(0,data[0],data),findMax(0,data[0],data)]
    elif calculate_min == False and calsulate_max == False:
        return ["Nothing was done"]
    elif calculate_min == False:
        return [findMin(0,data[0],data)]
    elif calsulate_max == False:
        return [findMax(0,data[0],data)]



print(extrema(data))
print(extrema(data,False))
print(extrema(data,True,False))
print(extrema(data,False,False))