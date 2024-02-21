from array import array

def main():
    arrays = array('i', [90, 70, 50, 80, 60, 85 ])
    
    length  = len(arrays)
    
    for i in range(length):
        print(arrays[i], end="")
        if i < length - 1:
            print(",", end=" ")

if __name__ == "__main__":
    main()