##INSERTION SORT ALGORITHM
##picks one element and place it appropriately among the previous elements
##continues this until the entire array is sorted
##simple, easy to implement
##does not require additional space
##not suitable for large data sets

def insertionSort(sortList):                    ##function definiton
    
    for i in range(1, len(sortList)):
        currentValue = sortList[i]              #element to be compared  
        #comparing the current element with the sorted portion and swapping

        while i > 0 and sortList[i-1] > currentValue:
            sortList[i] = sortList[i-1]          
            i = i-1
            sortList[i] = currentValue
            
    return sortList

list1 = []
size = int(input("Enter array size: "))     ##casted to type int

for i in range(size):
    print("Enter element", i+1) 
    list1.append(int(input()))              ##can also be casted to strings     
    ##or
    ##list1.append(input("Enter element: "))

print(list1)
print("Sorted array: ", insertionSort(list1))  ##function call  

##Or, 
##print ("Sorted array is:") 
##for i in range(len(list1)): 
##	print ("%d" %list1[i]) 
