from heap import Heap
def testToStringCompleteTree():
    #data = [1, 2 , 3, 4, 5, 6, 7, 8 ,9, 10, 11, 12, 13, 14 ,15, 16, 17 , 18 ,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33]
    data = [1, 2 , 3, 4, 5, 6 ,7 ,8]
    testHeap = Heap(data)
    test = testHeap.__str__()
    # print(test)
    # assert test == "     1 \n    2 3 \n   4 5 \n", "expected output in __str__"

def testGetParent():
    data = [16, 14, 10, 8, 7 , 9, 3, 2, 4, 1]
    testHeap = Heap(data)
    pIndex = testHeap.getParentIndex(1)
    assert pIndex == 0 ; "returning a wrong parent index"
    assert testHeap.getValue(pIndex) == 16; "expected value of parent not returning"

    pIndex = testHeap.getParentIndex(0)
    assert pIndex == 0 ; "returning a wrong parent index for root"
    assert testHeap.getValue(pIndex) == 16 ; "expected value of root's parent not returning"

def testChildren():
    data = [16, 14, 10, 8, 7 , 9, 3, 2, 4, 1]
    testHeap = Heap(data)
    LCindex = testHeap.getLeftChildIndex(4)
    assert LCindex == 8 ; "expected left child index of 8 not returning"
    assert testHeap.getValue(LCindex) == 2 ; "expected value of left child"
    RCindex = testHeap.getRightChildIndex(4)
    assert RCindex == 9 ; "expected right child index of 9 not returning"
    assert testHeap.getValue(RCindex) == 4 ; "expected value of right child"

    noLeafIndex = testHeap.getRightChildIndex(5)
    assert noLeafIndex == None ; "expected return for leaf w no child"


def testChildofLeaf():
    data = [16,14,10,8,7,9,3, 2 ,4 ,1]
    testHeap = Heap(data)
    noChildIndex = testHeap.getRightChildIndex(9)
    assert noChildIndex == None ; "expected no child returning at a leaf" 


    
def testMax_heapify():
    data = [16, 4, 10, 14, 7 , 9, 3, 2, 8, 1]
    testHeap = Heap(data)
    # print(testHeap)

    testHeap.max_Heapify(2)
    # print(testHeap.getValue(1))
    assert testHeap.getValue(1) == 14 ; "left child of root max_heap property voilated was"
    assert testHeap.getValue(3) == 8 ; "left child of left child of root's max_heap property voilated"
    assert testHeap.getValue(8) == 4 ; "expected leaf not there"

def testMax_heapifyWithOneLeaf():
    data = [16, 14 ,10, 8, 1 ,9, 3, 2, 4, 7]
    testHeap = Heap(data)
    testHeap.max_Heapify(5)
    assert testHeap.getValue(4) == 7 ; "expected value at A[5] not 7"
    assert testHeap.getValue(9) == 1 ; "expected value of 1 at A[9] not returned"


def testMin_heapify():
    data = [1, 4, 3, 2, 5, 6, 7]
    testHeap = Heap(data)
    testHeap.min_Heapify(2)
    assert testHeap.getValue(1) == 2 ; "expected value at A[1] not 2"
    assert testHeap.getValue(3) == 4 ; "expected value at A[3] not 4"

def testMin_HeapifyWithOneLeaf():
    data = [1, 8, 3, 2, 5, 6, 7, 4]
    testHeap = Heap(data)
    testHeap.min_Heapify(2)
    # print(testHeap)
    assert testHeap.getValue(1) == 2 ; "expected value at A[1] not 2"
    assert testHeap.getValue(3) == 4 ; "expected value at A[3] not 4"
    assert testHeap.getValue(7) == 8 ; "expected value at A[7] not 8"


def testBuildHeap():
    data = [4,1,3,2,16,9,10,14,8,7]
    testHeap = Heap(data)
    testHeap.buildMaxHeap()
    maxHeap = testHeap.getHeapArray()
    # print(testHeap)
    assert maxHeap[0] == 16
    assert maxHeap[1] == 14
    assert maxHeap[2] == 10
    assert maxHeap[3] == 8
    assert maxHeap[4] == 7
    assert maxHeap[5] == 9
    assert maxHeap[6] == 3
    assert maxHeap[7] == 2
    assert maxHeap[8] == 4
    assert maxHeap[9] == 1

def testBuildMinHeap():
    data = [4,1,3,2,16,9,10,14,8,7]
    testHeap = Heap(data)
    testHeap.buildMinHeap()
    maxHeap = testHeap.getHeapArray()
    # print(testHeap)
    assert maxHeap[0] == 1 , "unexpected output"
    assert maxHeap[1] ==  2, "unexpected output"
    assert maxHeap[2] ==  3, "unexpected output"
    assert maxHeap[3] ==  4, "unexpected output"
    assert maxHeap[4] ==  7, "unexpected output"
    assert maxHeap[5] ==  9, "unexpected output"
    assert maxHeap[6] ==  10, "unexpected output"
    assert maxHeap[7] ==  14, "unexpected output"
    assert maxHeap[8] ==  8, "unexpected output"
    assert maxHeap[9] ==  16, "unexpected output"

def testHeapMinSort():
    data = [4,1,3,2,16,9,10,14,8,7]
    testHeap = Heap(data)
    heapSorted = testHeap.heapSort("min")
    # print(heapSorted)
    assert heapSorted[0] == 1 ; "expected heapsorted value not returned"
    assert heapSorted[1] == 2 ; "expected heapsorted value not returned"
    assert heapSorted[2] == 3 ; "expected heapsorted value not returned"
    assert heapSorted[3] == 4 ; "expected heapsorted value not returned"
    assert heapSorted[4] == 7 ; "expected heapsorted value not returned"
    assert heapSorted[5] == 8 ; "expected heapsorted value not returned"
    assert heapSorted[6] == 9 ; "expected heapsorted value not returned"
    assert heapSorted[7] == 10 ; "expected heapsorted value not returned"
    assert heapSorted[8] == 14 ; "expected heapsorted value not returned"
    assert heapSorted[9] == 16 ; "expected heapsorted value not returned"

def testMaxHeapifyWithTwoElementsAndRootMax():
    data = [2,1]
    testHeap = Heap(data)
    testHeap.max_Heapify(1)
    assert testHeap.getValue(0) == 2 , "expected out put for max_heapify when len== 2 and max at root"

def testHeapSort():
    data = [1, 2 ,3 ,5 ,4 ,6 ,7 ,8 ,9 ,10]
    testHeap = Heap(data)
    heapSorted = testHeap.heapSort("max")
    assert heapSorted[0] == 10 ; "expected heapsorted value not returned"
    assert heapSorted[1] == 9 ; "expected heapsorted value not returned"
    assert heapSorted[2] == 8 ; "expected heapsorted value not returned"
    assert heapSorted[3] == 7 ; "expected heapsorted value not returned"
    assert heapSorted[4] == 6 ; "expected heapsorted value not returned"
    assert heapSorted[5] == 5 ; "expected heapsorted value not returned"
    assert heapSorted[6] == 4 ; "expected heapsorted value not returned"
    assert heapSorted[7] == 3 ; "expected heapsorted value not returned"
    assert heapSorted[8] == 2 ; "expected heapsorted value not returned"
    assert heapSorted[9] == 1 ; "expected heapsorted value not returned"

def testInsertAsMin():
    data = [1, 2, 3 , 4, 7, 9, 10,14, 8 ,16]
    data.reverse()
    testHeap = Heap([])
    for val in data:
        testHeap.insert(val)
    
    assert testHeap.getValue(0) == 1 ,"expected value after insert"
    assert testHeap.getValue(1) == 2 ,"expected value after insert"
    assert testHeap.getValue(2) == 7 ,"expected value after insert"
    assert testHeap.getValue(3) == 4 ,"expected value after insert"
    assert testHeap.getValue(4) == 3 ,"expected value after insert"
    assert testHeap.getValue(5) == 14 ,"expected value after insert"
    assert testHeap.getValue(6) == 8 ,"expected value after insert"
    assert testHeap.getValue(7) == 16 ,"expected value after insert"
    assert testHeap.getValue(8) == 9 ,"expected value after insert"
    assert testHeap.getValue(9) == 10 ,"expected value after insert"

def main():
    # testGetParent()
    # testGetParent()
    # testMax_heapify()
    # testChildofLeaf()
    # testBuildHeap()
    # testMax_heapifyWithOneLeaf()
    # testHeapSort()
    # testMin_heapify()
    # testMin_HeapifyWithOneLeaf()
    # testToStringCompleteTree()
    # testBuildMinHeap()
    # testHeapMinSort()
    # testMaxHeapifyWithTwoElementsAndRootMax()
    testInsertAsMin()


if __name__ == "__main__":
    main()