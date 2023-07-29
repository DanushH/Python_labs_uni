##SELECTION SORT ALGORITHM
##finds the smallest element in the array and swaps it with the first element
##continues this until the entire array is sorted
##simple, easy to implement
##does not require additional space
##not suitable for large data sets

def selectionSort(sortList):                    ##function definiton

    for i in range(len(sortList)):
        minPosition = i                         ##first element as min value  

        for k in range(i+1, len(sortList)):

            if sortList[minPosition] > sortList[k]:
                minPosition = k                 ##selected value as min value  

        tempElement = sortList[i]               ##first element as a temporary element
        sortList[i] = sortList[minPosition]     
        sortList[minPosition] = tempElement     ##swap min value and temporary first element

    return sortList

list1 = []
size = int(input("Enter array size: "))     ##casted to type int

for i in range(size):
    print("Enter element", i+1) 
    list1.append(int(input()))              ##can also be casted to strings     
    ##or
    ##list1.append(input("Enter element: "))

print(list1)
print("Sorted array: ", selectionSort(list1))  ##function call  
