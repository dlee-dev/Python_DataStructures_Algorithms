from array import array

def add(arrays, value):
    length = len(arrays)
    tempArray = array('i', [0 for _ in range(length+1)])
    
    for i in range(0, length):
        tempArray[i] = arrays[i]
        
    tempArray[length] = value
    return tempArray


def main():
    arrays = array('i', [90, 70, 50, 80, 60, 85 ])
    
    arrays = add(arrays, 75)
    
    length  = len(arrays)
    
    for i in range(length):
        print(arrays[i], end="")
        if i < length - 1:
            print(",", end=" ")

if __name__ == "__main__":
    main()