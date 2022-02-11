#Import random

#Create the function below:
def matrixBuilder (Integer):
    list = []
    for i in range(0, Integer):
        contain = []
        for i in range(0, Integer):
             contain.append(1)
        list.append(contain)
    return list

print(matrixBuilder(5))

