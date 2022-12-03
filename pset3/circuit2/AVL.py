import bst

def height(node):
    if node is None:
        return -1
    else:
        return node.height

def update_height(node):
    node.height = max(height(node.left), height(node.right)) + 1

class AVL(bst.BST):
    """
AVL binary search tree implementation.
Supports insert, find, and delete-min operations in O(lg n) time.
"""
    def left_rotate(self, x):
        y = x.right
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.right = y.left
        if x.right is not None:
            x.right.parent = x
        y.left = x
        x.parent = y
        update_height(x)
        update_height(y)

    def right_rotate(self, x):
        y = x.left
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            #if x is left child
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.left = y.right
        if x.left is not None:
            x.left.parent = x
        y.right = x
        x.parent = y
        update_height(x)
        update_height(y)

    def insert(self, t):
        """Insert key t into this tree, modifying it in-place."""
        node = bst.BST.insert(self, t)
        #Test
        node.numberofNodesInSubtree = 1
        self.rebalance(node)

    def updateNumberOfNodesInSubtree(self, node):
        left, right = 0 , 0 
        if node.left != None:
            left = node.left.numberofNodesInSubtree
        if node.right != None : 
            right = node.right.numberofNodesInSubtree
        
        node.numberofNodesInSubtree = left + right + 1

    def Rank(self, key):
        """returns the number of nodes smaller than this node"""
        node = self.find(key)
        return node.left.numberofNodesInSubtree

    def List(self, l , h):
        node = self.LCA(self, l, h)
        print(f"node key returned from lca : {node.key}")
    
    def LCA(self, l , h ):
        print(f"LCA l: {l} h : {h}")
        node = self.root
        count = 0
        while node != None:
            # count += 1
            # print(f"count : {count}")
            
            if l <= node.key and h >= node.key:
                print(f"working")
                break
            else :
                if l < node.key:
                    node = node.left
                else:
                    node = node.right 
        print(f"node to return from LCA: {node}")
        return node

    def rebalance(self, node):
        while node is not None:
            # print("height before update: {node.height}")
            update_height(node)

            
            # print(f"Height : {node.height}")
            # print(f"height(node.left) : {height(node.left)}")
            # print(f"height(node.right) : {height(node.right)}")
            # print(f"height(node.left) >= 2 + height(node.right) : {height(node.left) >= 2 + height(node.right)}")
            if height(node.left) >= 2 + height(node.right):
                if height(node.left.left) >= height(node.left.right):
                    # print("right rotating")
                    self.right_rotate(node)
                else:
                    # print("Left rotating")
                    self.left_rotate(node.left)
                    self.right_rotate(node)
            elif height(node.right) >= 2 + height(node.left):
                # print("Right child heavy")
                if height(node.right.right) >= height(node.right.left):
                    # print("Left rotating")
                    self.left_rotate(node)
                else:
                    self.right_rotate(node.right)
                    self.left_rotate(node)
            #Test
            self.updateNumberOfNodesInSubtree(node)
            # endTest
            node = node.parent

    def delete_min(self):
        node, parent = bst.BST.delete_min(self)
        self.rebalance(parent)
        #raise NotImplemented('AVL.delete_min')

def test(args=None):
    # bst.test(args, BSTtype=AVL)
    avl = AVL()
    print(avl)
    # avl.insert(4)
    # print(avl)
    # print("inserting 3")
    # avl.insert(3)
    # print(avl)
    # print("inserting 2")
    # avl.insert(2)
    # print(avl)
    
    #checking rotation
    # avl.insert(1)
    # print(avl)
    # print(f"number of nodes at root of node.key = 1: {avl.find(1).numberofNodesInSubtree}")
    # print("inserting 2")
    # avl.insert(2)
    # print(avl)
    # print("inserting 3")
    # avl.insert(3)
    # print(f"number of nodes at root of node.key = 1: {avl.find(1).numberofNodesInSubtree}")
    # print(f"number of nodes at root of node.key = 2: {avl.find(2).numberofNodesInSubtree}")
    # print(avl)

    avl.insert(8)
    avl.insert(3)
    avl.insert(2)
    avl.insert(5)
    avl.insert(11)
    avl.insert(13)
    print(avl)
    avl.LCA(1,6)
    

if __name__ == '__main__': test()