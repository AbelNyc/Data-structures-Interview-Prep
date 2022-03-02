class Unionfind:
    def __init__(self, size) -> None:
        self.root = [ i for i in range(size)]
    
    def find(self, x):
        return self.root[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx!= rooty:
            for i in range(len(self.root)):
                print(self.root[i])
                if self.root[i]==rooty:
                    self.root[i] == rootx
    def connected(self, x, y):
        return self.find(x) == self.find(y)


uf = Unionfind(10)
uf.union(1, 2)
