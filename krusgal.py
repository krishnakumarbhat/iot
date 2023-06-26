class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        parent[y if rank[x] < rank[y] else x] = max(x, y)
        rank[x] += rank[x] == rank[y]

    def KruskalMST(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = list(range(self.V))
        rank = [0] * self.V

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x, y = self.find(parent, u), self.find(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        minimumCost = sum(weight for _, _, weight in result)
        print("Edges in the constructed MST")
        for u, v, weight in result:
            print(f"{u} -- {v} == {weight}")
        print("Minimum Spanning Tree", minimumCost)


if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1, 10)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 3, 15)
    g.addEdge(2, 3, 4)
    g.addEdge(2, 0, 4)

    g.KruskalMST()
