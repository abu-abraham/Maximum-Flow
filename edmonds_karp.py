import copy
import math

class Edmonds:
    def __init__(self, graph, source, sink):
        self.graph = graph
        self.source = source
        self.sink = sink
        self.parent = [0 for _ in range(len(graph))]
        print(self.getMaxFlow())

    def getShortestPath(self):
        graph = self.graph
        parent = self.parent
        _queue = []
        visited = [False for _ in range(len(graph))]
        _queue.append(self.source)
        visited[self.source]=True

        while len(_queue)>0:
            node = _queue.pop(0)
            for index, neighour in enumerate(graph[node]):
                if visited[index] == False and neighour > 0:
                    _queue.append(index)
                    visited[index] = True
                    parent[index] = node
        if visited[self.sink] == True:
            return True
        return False

    def getMaxFlow(self):
        max_flow = 0
        parent = self.parent
        graph = self.graph
        while self.getShortestPath():
            ptr = self.sink
            path_flow = math.inf
            #Finding the smallest capacity
            while ptr !=  self.source:
                path_flow = min (path_flow, graph[parent[ptr]][ptr])
                ptr = parent[ptr]
            max_flow +=  path_flow

            v = self.sink
            #Creating the residual graph - Forward and Backward edges
            while v !=  self.source:
                u = parent[v]
                graph[u][v] -= path_flow
                graph[v][u] += path_flow
                v = parent[v]
        return max_flow






graph = [[0 for y in range(7)] for x in range(7)]
graph[0][1]=8
graph[0][3]=5
graph[1][2]=9
graph[1][4]=7
graph[2][6]=8
graph[3][4]=4
graph[3][5]=1
graph[4][6]=10
graph[5][2]=3

source = 0
sink = 6

edmonds = Edmonds(graph,source,sink)


