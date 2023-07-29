##BUBBLE SORT ALGORITHM
##compares two adjacent elements and swap them if they are not in order
##simple, easy to implement
##does not require additional space
##not suitable for large data sets
##with each iteration the smallest element in the list bubbles up to the top

def bubbleSort(sortList):                   ##function definiton
    
    for i in range(len(sortList)):

        for k in range(len(sortList) - 1):

            if sortList[k] > sortList[k+1]:
                sortList[k], sortList[k+1] = sortList[k+1], sortList[k]

    return sortList

list1 = []
#size = int(input("Enter array size: "))     ##casted to type int

for i in range(8):
    print("Enter element", i+1) 
    list1.append(int(input()))              ##can also be casted to strings     
    ##or
    ##list1.append(input("Enter element: "))

print(list1)
print("Sorted array: ", bubbleSort(list1))  ##function call  
