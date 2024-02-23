from array import array

def sort(arrays):
    length = len(arrays)
    for i in range(0, length - 1):
        isSwap = False
        for j in range(0, length - i -1):
            if(arrays[j] > arrays[j+1]):
                temp = arrays[j]
                arrays[j] = arrays[j+1]
                arrays[j+1] = temp
                isSwap = True
            
            if isSwap == False:
                break

def main():
    arrays = array('i', [60, 50, 95, 80, 70])
    
    sort(arrays)
    
    for index, item in enumerate(arrays):
        if index == len(arrays) - 1:
            print(item, end="")
        else:
            print(item, end=", ")
        
if __name__ == "__main__":
    main()