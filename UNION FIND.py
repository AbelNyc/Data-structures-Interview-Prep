class Unionfind:
    def __init__(self, size) -> None:
        self.root = [i for i in range(size)]


    def find(self, x):
        return self.root[x]


    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            for i in range(len(self.root)):
                if self.root[i] == rooty:
                    self.root[i] = rootx

    def connected(self, x, y):
        return self.find(x)==self.find(y)

    def print_root(self):
        return self.root

# Test Case
uf = Unionfind(10)

print(uf.print_root())
uf.union(1, 2)
uf.union(2, 5)
print(uf.print_root())

print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))