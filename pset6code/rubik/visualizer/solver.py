from operator import ne
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
    print(f"start : {start}")
    print(rubik.perm_to_string(start))
    print(f"end : {end}")

    print(f"After rotation F : {rubik.perm_apply(rubik.quarter_twists[0], start)}")
    print(f"rotating back 'F : {rubik.perm_apply(rubik.quarter_twists[1], rubik.perm_apply(rubik.quarter_twists[0], start))}")
    print(f"after second rotation : {rubik.perm_apply(rubik.quarter_twists[0], rubik.perm_apply(rubik.quarter_twists[0], start))}")
    # testEndState = (9, 10, 11, 6, 7, 8, 3, 4, 5, 0, 1, 2, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23)
    graph = Graph()
    # graph.computeNeigbors(start)
    # print(f"1st neighbors in graph : {graph.adj[start]}")

    result = BFS(graph, start, end)
    print(f"result : {result.parent}")
    if len(result.parent) != 0:
        parent = result.parent[end][0]
        print(f"parent of final state : {parent}")
        moves = []
        moves.append(result.parent[end][1])
        # print(f"moves : {moves}")
        while parent != None:
            if result.parent[parent][1] != None:
                moves.append(result.parent[parent][1])
            parent = result.parent[parent][0]
        print(f"moves : {moves}")
        # converting the moves names to actual moves in rubik.py
        Moves = []
        for move in moves:
            for key, value in rubik.quarter_twists_names.items():
                if value == move:
                    Moves.append(key)
            # testMoves = [rubik.quarter_twists_names[key] for key , val in rubik.quarter_twists_names.items() if val == move]
        print(f"testMoves : {Moves}")
        # reversing the order of all the moves
        Moves.reverse()
        return Moves




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

    q = deque()
    q.append(source)
    graph.computeNeighbors(source)
    test = 0
    test2 = 0
    while q:
        u = q.popleft()
        # print(f"u : {u}")
        # numberOfNeighbor = 0
        for neighbor in graph.getNeighbors(u):
            
            if neighbor[0] not in r.level:
                r.addParent(neighbor[0], (u , neighbor[1]))
                r.setLevel(neighbor[0], r.getLevel(u) + 1)
                q.append(neighbor[0])
                if neighbor[0] == endState:
                    print("found desired config")
                    return r
                 
            # compute neighbors of this neighbor and add to queue
            graph.computeNeighbors(neighbor[0])
            # q.append(neighbor[0])
            # numberOfNeighbor += 1
        # print(f"number of neighbors : {numberOfNeighbor}")
        # if test2 == 1:
        #     break
        
        # if test == 2:
        #     test2 += 1
        
    #     test += 1
    return {} 