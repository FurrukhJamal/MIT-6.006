from logging import raiseExceptions
import math

class Heap(object):
    def __init__(self, array):
        self.array = array
        self.original = array[:]
    def __str__(self):
        if len(self.array) == 0 :
            return "[]"
        counterForLastLevel = 0
        numOfLevels =math.floor(math.log2(len(self.array))) + 1
        # print(f" num of levels: {numOfLevels}")
        index = 0
        treeString = ""
        for i in range(numOfLevels):
            # logic to apply space for each line of tree to make a triangular shape
            strng = " " * (len(self.array) - i)
            # for the rows
            for j in range(2** i):
                # print(f"i : {i}")
                # print(f"j : {j}")
                # print(f"index : {index}")
                if(i + 1 == numOfLevels):
                    #for when the tree is not complete on the last level
                    counterForLastLevel += 1
                    # print(f"counterForLastLevel : {counterForLastLevel}")
                value = str(self.array[index])
                strng += value + " "
                index += 1
                #print(f"len(self.array)//2 + 2 + counterForLastLevel: {len(self.array)//2 + 2 + counterForLastLevel} len(self.array) : {len(self.array)}")
                # if(len(self.array)//2 + 2 + counterForLastLevel == len(self.array)):
                #     # +2 instead of +1 cuz the formula for leaf in n/2 + 1 for 1-indexed array, we are using 0 indexed
                #     break
                # print(f"len(self.array)//2 + counterForLastLevel  + (2** (i - 1) - (j + 1)): {len(self.array)//2 + counterForLastLevel + (2** (i - 1) - j)} len(self.array) : {len(self.array)}")
                # if(len(self.array)//2 + counterForLastLevel + (2** (i - 1) - (j + 1)) == len(self.array)):
                #     break
                NodesinPreviousLevels = 0
                if i + 1 == numOfLevels:
                    for level in range(i - 1 , -1 , -1):
                        NodesinPreviousLevels += 2**level
                
                # print(f"total nodes in previous levels: {NodesinPreviousLevels}")
                # print(f"NodesinPreviousLevels + counterForLastLevel: {NodesinPreviousLevels + counterForLastLevel} len(self.array) : {len(self.array)}")
                if(NodesinPreviousLevels + counterForLastLevel  == len(self.array)):
                    break 
            treeString += strng + "\n"
        return treeString

    """assumes a zero indexed index"""
    def getParentIndex(self, index):
        if index == 0:
            return index
        return math.floor((index - 1)/2)

    """
    index : a 1-indexed value for an index
    return: the index of rightChild else None for a 0-indexed array
    """
    def getRightChildIndex(self, index):
        if index >= len(self.array) or (2 * index + 1 - 1) >= len(self.array):
            return None
        return (2 * index + 1) - 1

    """
    index : a 1-indexed value for an index
    return: the index of left Child for a 0-inexed array else None 
    """
    def getLeftChildIndex(self, index):
        if index >= len(self.array) or (2 * index -1) >= len(self.array):
            return None 
        return (2 * index) - 1

    """assumes the value of index to be for a zero indexed array"""
    def getValue(self, index):
        return self.array[index]

    def getHeapArray(self):
        return self.array

    def getOriginal(self):
        return self.original

    """assumes index to be of 1-indexed array"""
    def max_Heapify(self, index):
        # left and right are 0-indexed and index is 1-indexed
        # print(self)
        left = self.getLeftChildIndex(index) 
        right = self.getRightChildIndex(index) 
        largest = index

        if left == None and right == None :
            return 

        # print(f"right : {right} left :{left} index : {index}")
        
        #for getValue index - 1 is used cuz index in the method is 1-indexed
        if(left <= len(self.array) and self.getValue(index - 1) < self.getValue(left)):
            largest = left
        # check for a node that has just one child node
        if right != None:
            if(right <= len(self.array) and self.getValue(largest) < self.getValue(right)):
                largest = right
        
        # print(f"index : {index} largest : {largest}")
        
        """Bug fix, since the index is 1-indexed and children are zero indexed, when the algo was
        was checking for the root with index as 1 and if it was lesser than the left child than the
        test of largest != index was coming out as 1 = 1 so had to fix it that if it was a root with index 1
        make index as 0 and then make it back to 1 in the if (largest != index) test to avoid a lot of 
        code correction"""
        if index == 1:
            index -= 1


        if (largest != index):
            #Bug fix
            if(index == 0):
                index += 1
            
            #check for when there are two levels and root is already a max
            if index == 1 and self.array[index - 1] > self.array[largest]:
                return
            else :

                # index - 1 cuz index is for 1-indexed array and left right are returned for zero indexed so largest too would be of zero indexed
                self.array[largest], self.array[index -1] = self.array[index -1] , self.array[largest]
                # adding 1 cuz max_Heapify accepts 1-indexed index
                self.max_Heapify(largest + 1)
        else :
            return

    """assumes index to be of 1-indexed array"""
    def min_Heapify(self, index):
        # left and right are 0-indexed and index is 1-indexed
        # print(self)
        left = self.getLeftChildIndex(index) 
        right = self.getRightChildIndex(index) 
        smallest = index

        if left == None and right == None :
            return 

        # print(f"right : {right} left :{left} index : {index}")
        flag = False
        #for getValue index - 1 is used cuz index in the method is 1-indexed
        if(left <= len(self.array) and self.getValue(index - 1) > self.getValue(left)):
            smallest = left
            flag = True
        # check for a node that has just one child node
        if right != None:
            #Bug Fix
            if flag :       
                if(right <= len(self.array) and self.getValue(smallest) > self.getValue(right)):
                    smallest = right
            else : 
                if(right <= len(self.array) and self.getValue(smallest - 1) > self.getValue(right)):
                    smallest = right

        
            #end Bug Fix
        
        # print(f"index : {index} smallest : {smallest}")
        
        """Bug fix, since the index is 1-indexed and children are zero indexed, when the algo was
        was checking for the root with index as 1 and if it was lesser than the left child than the
        test of largest != index was coming out as 1 = 1 so had to fix it that if it was a root with index 1
        make index as 0 and then make it back to 1 in the if (largest != index) test to avoid a lot of 
        code correction"""
        if index == 1:
            index -= 1


        if (smallest != index):
            #Bug fix
            if(index == 0):
                index += 1

            #check for when there are two levels and root is already a minimum
            if index == 1 and self.array[index - 1] < self.array[smallest]:
                return
            else:

                    
                # index - 1 cuz index is for 1-indexed array and left right are returned for zero indexed so largest too would be of zero indexed
                self.array[smallest], self.array[index -1] = self.array[index -1] , self.array[smallest]
                # adding 1 cuz max_Heapify accepts 1-indexed index
                self.min_Heapify(smallest + 1)
        
        else :
            return

    
    # def insert(self, item):
    #     # print(f"adding : {item}")
    #     self.array.append(item)
    #     self.buildMinHeap()


    def insert(self, item):
        # print(f"adding item : {item}")
        self.array.append(item)
        self.shiftUpMin(len(self.array))
        # print(self)

    #assumes 1-indexed index
    def shiftUpMin(self,index):
        # print(f"index in shiftUp : {index}")
        if index == 1:
            return 
        
        parent = index//2
        # print(f"parent : {parent}")

        if self.array[index - 1] < self.array[parent - 1] :
            # print(f"self.array[index - 1] : {self.array[index - 1]} self.array[parent - 1] : {self.array[parent - 1] }")
            self.array[index - 1], self.array[parent - 1] = self.array[parent - 1], self.array[index - 1]
            # print(f"self.array[index - 1] : {self.array[index - 1]} self.array[parent - 1] : {self.array[parent - 1] }")
           
            self.shiftUpMin(parent)
        else : 
            return 
                
    
    def buildMaxHeap(self):
        #self.array = [16,14, 10, 8, 7, 9, 3, 2, 4, 1]
        for i in range(len(self.array)//2 , 0 , -1):
            self.max_Heapify(i)
            
        return self.array

    def buildMinHeap(self):
        for i in range(len(self.array)//2 , 0 , -1):
            # print(f"Heapify-Index : {i}")
            self.min_Heapify(i)
        
        return self.array

    """returns a max sorted array using heapSort
    @param : "max" or "min"
    """
    def heapSort(self, type):
        array = []
        if type == "max": 
            self.buildMaxHeap()
        elif type == "min":
            self.buildMinHeap()
         
        while len(self.array) != 0:
            # switching max element at 0 with that of the leaf
            self.array[0], self.array[len(self.array) - 1] = self.array[len(self.array) - 1] , self.array[0]
            # adding the leaf in the return array
            array.append(self.array.pop(len(self.array) - 1))
            # print(self.array)
            #run max_heapify to fix the element thats now in the root
            if type == "max" :
                self.max_Heapify(1)
            elif type == "min" :
                self.min_Heapify(1) 
            # print(self)
        
        return array 


def main():
    # test = Heap([1,2, 3 ,4 ,5 ,6 ,7 ,8])
    test = ["a",2, 3 ,4 ,5 ,6 ,7 ,8]
    # converting each value to a string
    #test = [ str(i) for i in test]

    print(test)
    #counter to keep track for the last rows of leafs to stop if the tree is not complete
    # counter = len(test)/2 + 1
    counter = 0
    endCounter =  math.log(len(test))
    numOfLevels = math.floor(endCounter) + 1
    
    # print(numOfLevels)
    #to track the index for the heap array
    index = 0
    # implementing log n + 1 for the number of levels of a tree
    for i in range(numOfLevels + 1):
        # for appropriate number of spaces for each row to make the print out look like a tree
        strng = " " * (len(test) - i)
        
        for j in range( 2 ** i):
            # str = " " * (len(test) - i)
            #print(f"j : {j}")
            if(i == numOfLevels):
                #check if on the last row for leafs
                # print("update counter hitting")
                counter += 1
            value = str(test[index])
            # print(f"index : {index}")
            strng += value + " "
            index += 1
            # print(f"len(test)//2 + 1 + counter: {len(test)//2 + 1 + counter} i : {i} j : {j}")
            # +2 instead of +1 cuz the formula for leaf in n/2 + 1 for 1-indexed array, we are using 0 indexed
            if (len(test)//2 + 2 + counter == len(test) -1):
                # print("hitting break")
                break
        # print(f"counter : {counter}")
        strng += "\n"
        print(strng)
    
    print("HEAP TESTS")
    heap = Heap([16, 14, 10, 7, 6, 5, 4, 3, 2, 1])
    print(heap)



if __name__ == "__main__":
    main()
    
        