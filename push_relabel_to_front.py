import math

class PushRelabel:

    def __init__(self, graph, source, sink):
        self.graph = graph
        self.source = source
        self.sink = sink

        n = len(graph)
        self.reserve = [[0 for _ in range(n)] for _ in range(n)]
        self.seen = [0 for _ in range(n)]
        self.height = [0 for _ in range(n)]
        self.excess = [0 for _ in range(n)]


        self.height[source] = n
        self.excess[source] = math.inf
        nodelist = [i for i in range(1,n-1)]

        for v in range(n):
            self.push(source,v)

        p = 0
        while p < len(nodelist):
            u = nodelist[p]
            o = self.height[u]
            self.discharge(u)
            if self.height[u] > o:
                nodelist.insert(0, nodelist.pop(p))
                p = 0
            else:
                p+=1
        print(sum(self.reserve[source]))

    def push(self, u, v):
        flow = min(self.excess[u], self.graph[u][v]-self.reserve[u][v])
        self.reserve[u][v] = self.reserve[u][v]+flow
        self.reserve[v][u] = self.reserve[v][u]-flow
        self.excess[u] = self.excess[u]-flow
        self.excess[v] = self.excess[v] + flow

    def discharge(self, u):
        while self.excess[u]>0:
            if self.seen[u]<len(self.graph):
                v = self.seen[u]
                if self.graph[u][v]-self.reserve[u][v]>0 and self.height[u]>self.height[v]:
                    self.push(u,v)
                else:
                    self.seen[u]+=1
            else:
                self.relabel(u)
                self.seen[u] = 0

    def relabel(self, u):
        height = math.inf
        for v in range(len(self.graph)):
            if self.graph[u][v]-self.reserve[u][v]>0:
                height = min(height, self.height[v])
                self.height[u] =height+1



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

PushRelabel(graph, source, sink)