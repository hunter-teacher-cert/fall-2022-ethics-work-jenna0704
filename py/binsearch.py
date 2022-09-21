# Binary Search
# Jenna Lin
# CSCI 77800 Fall 2022
# collaborators: 
# consulted:

def binSearchRec(a, target, loPos, hiPos):
    
    # initial return variable to flag value
    targetPosition = -1
    
    # initial tracker variable for middle position
    mPos = (loPos + hiPos) // 2
    
    # exsit case. If lo & hi have crossed, target not present
    if loPos > hiPos:
        return targetPosition
    
    elif a[mPos] == target:
        return mPos
    
    elif a[mPos] > target:
        return binSearchRec(a, target, loPos, mPos - 1)
    
    else:
        return binSearchRec(a, target, mPos + 1, hiPos)
    
    return targetPosition


def binSearch(a, target):
    return binSearchRec(a, target, 0, len(a)-1)


# Test Binary Search
a = [2, 4, 6, 8, 13, 42]
target = 6

index = binSearch(a, target)

if index != -1:
    print('The element is present it index ' + str(index) + '.')
    
else:
    print('The element is not present in the array.')