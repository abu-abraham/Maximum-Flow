#Ford-Fulkerson method uses a lot of additional space! However, it is still used here.
import math
from edmonds_karp import Edmonds



bipartite = [[0 for j in range(9)] for i in range(9)]
bipartite[1][6] = 1
bipartite[1][7] = 1
bipartite[2][5] = 1
bipartite[3][5] = 1
bipartite[3][6] = 1
bipartite[4][5] = 1
bipartite[4][7] = 1
bipartite[0][0] = 0
bipartite[8][8] = 0

#From source a connection to all nodes in Part-A
for i in range(1,5):
    bipartite[0][i]=1

#From all nodes in Part-B to terminal node
for i in range(5,8):
    bipartite[i][8]=1

for n in bipartite:
    print(n)


source = 0
sink = 8

Edmonds(bipartite,source,sink)