class GraphNode(object):
    """
    @param name : string name of the node
    neighbors : list of name of nodes that are immediate neighbors
    """
    def __init__(self, name, neighbors = []):
        self.name = name 
        self.neighbors = neighbors

    def getName(self):
        return self.name 

    def getNeighbors(self):
        return self.neighbors

    def addNeigbor(self, neighborNode):
        self.neighbors.append(neighborNode)

    def __str__(self):
        # s = str(self.getName()) + "\n"
        numNeighbors = len(self.getNeighbors())
        # adding appropriate spaces for node's name to represent name
        s = "    " * (numNeighbors // 2) + str(self.getName()  + "\n")
        # adding edge to represent in string as | for every vertice
        for i in range(numNeighbors):
            s += "|    "
        s += "\n"

        for i in self.getNeighbors():
            s += i.getName() + "    "
        
        s += "\n"

        return s

        # for u in self.getNeighbors():

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes

    def __str__(self):
        s= ""
        for node in self.nodes:
            s += node.__str__()

        return s  


      
if __name__ == "__main__":
    f = GraphNode("F")
    v = GraphNode("V")
    
    c = GraphNode("C", [f, v] )
    d = GraphNode("d", [f, c])
    z = GraphNode("Z")
    
    a = GraphNode("A", [z])
    x = GraphNode("X", [d, c])
    
    s = GraphNode("A", [a, x])
    
    graph = Graph([s, a, x, z, d, c, f, v])
    print(graph)
    