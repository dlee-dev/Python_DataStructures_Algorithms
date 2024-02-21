from array import array

def insert(arrays, value, insertIndex):
    length = len(arrays)
    tempArray = array('i', [0 for _ in range(length+1)])
    
    for i in range(0, length):
        if i < insertIndex:
            tempArray[i] = arrays[i]
        else:
            tempArray[i+1] = arrays[i]
            
    tempArray[insertIndex] = value
    return tempArray

def main():
    arrays = array('i', [90, 70, 50, 80, 60, 85 ])
    
    arrays = insert(arrays, 75, 2)
    
    length  = len(arrays)
    
    for i in range(length):
        print(arrays[i], end="")
        if i < length - 1:
            print(",", end=" ")

if __name__ == "__main__":
    main()
    