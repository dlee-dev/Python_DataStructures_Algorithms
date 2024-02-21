from array import array

class List:
    _elements = array('i')
    _size = 0
    
    def __init__(self, initialCapacity = 10):
        self._elements = array('i',[0 for _ in range(initialCapacity)])
    
    def get(self, index):
        if(index >= 0 and index < self._size):
            return self._elements[index]
        
        return None
    
    def append(self, item):
        if(self._size < len(self._elements)):
            self._elements[self._size] = item
            self._size += 1
        else:
            newCapacity = 2 * len(self._elements)
            tempArray = array('i',[0 for _ in range(newCapacity)])
            
            for i in range(0, self._size):
                tempArray[i] = self._elements[i]
            
            tempArray[self._size] = item
            self._elements = tempArray
            self._size += 1
        
    def insert(self, index, item):
        if(self._size < len(self._elements)):
            for i in range(self._size - 1, index - 1, -1):
                self._elements[i+1] = self._elements[i]    
            self._elements[index] == item
            self._size += 1
        else:
            newCapacity = 2 * len(self._elements)
            tempArray = array('i', [0 for _ in range(newCapacity)])
            
            for i in range(0, self._size):
                if(i < index):
                    tempArray[i] = self._elements[i]
                else:
                    tempArray[i+1] = self._elements[i]
                    
            tempArray[index] = item
            self._elements = tempArray
            self._size += 1
    
    def contains(self, item):
        for i in range(0, self._size):
            if(self._elements[i] == item):
                return True
        
        return False
    
    def isEmpty(self):
        if(self._size == 0):
            return True
        
        return False
    
    def size(self):
        return self._size
    
    def remove(self, index):
        if(index < 0 or index >= self._size):
            return None
        
        returnItem = self._elements[index]
        for i in range(index, self._size -1):
            self._elements[i] = self._elements[i+1]
        
        self._size -= 1
        return returnItem
    
########################## test ################
li = List()
li.append(90)
li.append(70)
li.append(50)
li.append(80)
li.append(90)
li.append(85)
li.append(75)

for i in range(0, li.size()):
    item = li.get(i)
    print(item, end="")
    if i < li.size() - 1:
        print(",", end="")