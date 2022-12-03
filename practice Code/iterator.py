class Reverse(object):
    """Iteratorforloopingoverasequencebackwards."""
    def __init__(self,data):
        self.data=data
        self.index=len(data)
    
    def __iter__(self):
        # yield self.next()
        return self
    
    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1 
        return self.data[self.index]

# Produces hash values for a rolling sequence.
class RollingHash:
    def __init__(self, s):
        self.HASH_BASE = 7
        self.seqlen = len(s)
        n = self.seqlen - 1
        h = 0
        for c in s:
            h += ord(c) * (self.HASH_BASE ** n)
            n -= 1
        self.curhash = h

    # Returns the current hash value.
    def current_hash(self):
        return self.curhash

    # Updates the hash by removing previtm and adding nextitm.  Returns the updated
    # hash value.
    def slide(self, previtm, nextitm):
        self.curhash = (self.curhash * self.HASH_BASE) + ord(nextitm)
        self.curhash -= ord(previtm) * (self.HASH_BASE ** self.seqlen)
        return self.curhash

def testGenerator(S):
    for char in S:
        yield char

def testfile():
    file = open("test.txt", "r")
    text = file.readline()
    print(text)
    print(file.readline())


if __name__ == "__main__":
    rev = Reverse("hello")
    # iter(rev)
    try:
        while True:
            print(rev.next())
    except StopIteration:
        pass

    # print(f"outside loop rev.next() : {rev.next()}")
    
    testString = "ABCDEF"
    word = testString[0:3]
    arrword = list(word)
    rHash = RollingHash(word)
    hashes = {}
    position = 3
    for char in testGenerator(testString[3:]):
        print(f"position : {position}")
        # if position < 3:
        #     position += 1
        #     continue
        hash = rHash.current_hash()
        if hash in hashes:
            hashes[hash].append((word, position - 3))
                        
        else:
            L = []
            hashes[hash] = L
            hashes[hash].append((word, position - 3))
            
        rHash.slide(arrword[0], char)
        arrword.append(char)
        del arrword[0]
        word = "".join(arrword)
        position += 1 

    print(hashes)

    testfile()
