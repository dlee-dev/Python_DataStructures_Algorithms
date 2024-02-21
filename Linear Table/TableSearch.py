from array import array

def search(arrays, value):
    length = len(arrays)
    
    for i in range(0, length):
        if(arrays[i] == value):
            return i
               
    return -1

def main():
    arrays = array('i', [90, 70, 50, 80, 60, 85])
    value = int(input("Please enter the value you want to search : \n"))
    
    index = search(arrays, value)
    
    if(index > 0):
        print("Found value: ", value, "the index is ", index)
    else:
        print("The value was not found: ", value)

if __name__ == "__main__":
    main()
    