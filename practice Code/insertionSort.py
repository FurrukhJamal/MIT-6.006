def insertionSort(L):
    A = []

    for i in range(len(L)):
        if i == 0:
            continue
        
        j = i - 1
        
        while j > -1 and L[j] > L[j + 1]:
            
            temp = L[j]
            L[j] = L[j + 1]
            L[j+ 1] = temp
            j -= 1
    
    print(L)

def mergeSort(L):
    if len(L) == 1:
        return L
    else:
        L1 = mergeSort(L[0 : len(L)//2])
        L2 = mergeSort(L[len(L)//2 : len(L)])

        print(f"L1: {L1}")
        print(f"L2 : {L2}")

        returnList = []
        while len(L1) > 0 and len(L2) > 0:
            if L1[0] < L2[0]:
                returnList.extend(L1[0:1])
                L1.pop(0)
            elif L1[0] > L2[0]:
                returnList.extend(L2[0:1])
                L2.pop(0)
            else:
                returnList.extend(L1[0: 1])
                L1.pop(0)
        
        if len(L1) == 0:
            returnList.extend(L2) 
        else:
            returnList.extend(L1)

        return returnList

def main():
    L = [4, 8, 1, 8, 9, 3, 7]
    print(L)
    print("After insertion sort")
    insertionSort(L)

    print("Start of mergeSort\n\n")
    L = [2, 1, 13, 7, 20, 20, 9, 11, 12]
    mergedArray = mergeSort(L)
    print("MERGED ARRAY")
    print(mergedArray)
    

if __name__ == "__main__":
    main() 