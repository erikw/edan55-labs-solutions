class Edge:
    
    def __init__(self, v1, v2, weight):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight
    
    def __str__(self):
        return "{:d} < {:d} > {:d}".format(self.v1, self.v2, self.weight)
        
