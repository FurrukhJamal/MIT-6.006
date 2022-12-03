from operator import ne
from turtle import backward
import rubik
from collections import deque

def shortest_path(start, end):
    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
    """
    
    if start == end :
        return []
    
    graph = Graph()
    result = BFS(graph, start, end)
    
    if result == None:
        return None
    
    commonNode = result[2]
 
    parent = result[1].parent[commonNode][0]
        
    """the moves in result[1] which is rBackward from BFS doesnot have to be reversed
    the idea is the sequence has to be 
    start --node-- node--...commonNode(result[2]) -- node --node--... end
    so the sequence of moves derived from result[0] have to be reversed to show the sequence that should
    have been for when it starts from the start position upto the common node and the sequence of moves derieved from
    result[1] should be appended cuz it already is a  sequence of moves running from the end to the common 
    node backwards"""
    movesrB = []
    movesrB.append(result[1].parent[commonNode][1])
    while parent != None:
        if result[1].parent[parent][1] != None:
            movesrB.append(result[1].parent[parent][1])
        parent = result[1].parent[parent][0]
    
    # converting the moves to actual tuple form moves
    movesrB = ConvertMovesFromNames(movesrB)
    # inverting the moves
    movesrB = invertMoves(movesrB)
        
    movesr = []
    parent = result[0].parent[commonNode][0]
    movesr.append(result[0].parent[commonNode][1])
    while parent != None:
        if result[0].parent[parent][1] != None:
            movesr.append(result[0].parent[parent][1])
        parent = result[0].parent[parent][0]
    

    # converting the moves to actual rubik cubes move
    movesr = ConvertMovesFromNames(movesr)
    # reversing the order of moves cuz in the left half of bfs the sequence of moves is from
    # commonNode to start position and we have to reverse it 
    movesr.reverse()
    # adding both the moves
    movesr.extend(movesrB)
    return movesr


def ConvertMovesFromNames(arrMoves):
    result = []
    for move in arrMoves:
        for key, value in rubik.quarter_twists_names.items():
            if value == move:
                result.append(key)
    return result

def invertMoves(arrMoves):
    result = []
    for move in arrMoves:
        result.append(rubik.perm_inverse(move))
    return result

class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v):
        if u not in self.adj:
            self.adj[u] = []
        self.adj[u].append(v)
    
    """adds a nieghbor as a tuple (vertex of parent, move that achieved the current state from previous vertex)"""
    def computeNeighbors(self, u):
        # creat all the neighbors of u and add them as neighbors
        for i in range(len(rubik.quarter_twists)):
            config = rubik.perm_apply(rubik.quarter_twists[i], u)
            # adding the name of the move with which this configuration was reached
            moveName = rubik.quarter_twists_names[rubik.quarter_twists[i]]
            self.add_edge(u, (config, moveName))

    def getNeighbors(self, vertex):
        return self.adj[vertex]


class BFSResult:
    def __init__(self):
        self.level = {}
        self.parent = {}
    def addParent(self, p, val):
        self.parent[p] = val
    
    def incrementLevel(self, val):
        self.level[val] += 1
    def setLevel(self, node, value = 0):
        self.level[node] = value
    def getLevel(self, node):
        if node in self.level:
            return self.level[node]


def BFS(graph, source, endState):
    r = BFSResult()
    r.addParent(source , (None, None))
    r.setLevel(source)

    rBackward = BFSResult()
    rBackward.addParent(endState, (None, None))
    rBackward.setLevel(endState)

    seen = set()

    q = deque()
    q.append(source)
    graph.computeNeighbors(source)
    
    backwardQ = deque()
    
    backwardQ.append(endState)
    graph.computeNeighbors(endState)
    while q and backwardQ:
        u = q.popleft()
        
        if u in seen:
            return (r, rBackward, u)
        # Bug fix to return the no solution answer quicker, the moment this bfs goese beyond halfway that means
        # if there was a common node between the two bfs it should have reached at level 7
        if r.getLevel(u) == 8:
            return None
        
        seen.add(u)    
        
        for neighbor in graph.getNeighbors(u):
            
            if neighbor[0] not in r.level:
                                
                r.addParent(neighbor[0], (u , neighbor[1]))
                r.setLevel(neighbor[0], r.getLevel(u) + 1)
                if neighbor[0] not in seen:
                    q.append(neighbor[0])
                    graph.computeNeighbors(neighbor[0])
        
        v = backwardQ.popleft()
        
        if v in seen:
            return(r, rBackward, v)
        
        seen.add(v)
       
        for neighbor2 in graph.getNeighbors(v):
            if neighbor2[0] not in rBackward.level:
                rBackward.addParent(neighbor2[0], (v, neighbor2[1]))
                rBackward.setLevel(neighbor2[0], rBackward.getLevel(v) + 1)
                if neighbor2[0] not in seen:
                    backwardQ.append(neighbor2[0])
                    graph.computeNeighbors(neighbor2[0])
                 

        # check if all 14 levels of nodes have been checked for one bfs which means there 
        # is no solution
        # if max(r.level.values()) > 8 :
        #     return None

    return {}            
                    
