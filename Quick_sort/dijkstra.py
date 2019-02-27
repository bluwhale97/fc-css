class ShortestPath:
    def __init__(self, s, distance, p):
        self.source=s
        self.distance=distance
        self.p=p

class Graph:
    #모든 가중치보다 충분히 큰 수
    BIG_NUMBER=2000
    @staticmethod
    def print_shortest_path(sp, dest):
        if sp.source==dest:
            print("{}".format(dest), end="  ")
            return
        if sp.p[dest]!=None:
            Graph.print_shortest_path(sp, sp.p[dest])
        else:
            print("There is no path")
            return
        print("{}".format(dest), end="  ")

    def __init__(self, vnum):
        self.adjacency_matrix=[[None for _ in range(vnum)] for _ in range(vnum)]
        self.vertex_num=vnum

    def insert_edge(self, u, v, w):
        self.adjacency_matrix[u][v]=w

    def find_min(self, distance, S):
        _min = self.BIG_NUMBER
        min_v = -1
        for v in range(self.vertex_num):
            if v not in S and _min > distance[v]:
                _min = distance[v]
                min_v = v
        return min_v

    def dijkstra(self, s):
        distance = [self.BIG_NUMBER for _ in range(self.vertex_num)]
        p = [None for _ in range(self.vertex_num)]
        S = set()

        distance[s] = 0

        while len(S) < self.vertex_num:
            v = self.find_min(distance, S)
            S.add(v)

            for u in range(self.vertex_num):
                w = self.adjacency_matrix[v][u]
                if w != None and u not in S and distance[v] + w < distance[u]:
                    distance[u] = distance[v] + w
                    p[u] = v

        sp = ShortestPath(s, distance, p)
        return sp


if __name__=="__main__":
    g=Graph(4)
    g.insert_edge(0, 1, 10)
    g.insert_edge(0, 2, 3)
    g.insert_edge(1, 3, 5)
    g.insert_edge(2, 1, 5)
    g.insert_edge(2, 3, 8)
    g.insert_edge(3, 1, 4)
    g.insert_edge(3, 2, 12)

    source=0
    sp=g.dijkstra(source)
    for i in range(g.vertex_num):
        print('distance[{0}] : {1}, p[{0}] : {2}'.format(i, sp.distance[i], sp.p[i]))
    
    dest=3
    print("path from {} to {}".format(source, dest))
    g.print_shortest_path(sp, dest)
    print()

