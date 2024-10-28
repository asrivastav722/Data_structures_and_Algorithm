class Graph:
    def __init__(self,vertex_count=None,adj_matrix=None):
        self.vertex_count=vertex_count
        self.adj_matrix=adj_matrix
        self.adj_matrix=[]
        self.count=0
        size=0
        while size<vertex_count:
            self.adj_matrix.append([])
            size=size+1
        x=0
        y=0
        while x != vertex_count:
            while y != vertex_count:
                self.adj_matrix[x].append(0)
                y=y+1
            y=0
            x=x+1
        print(vertex_count,"= Vertices count")
        print("0 = Edge present")
        print("1 = Edge Absent")
        print("================================================")
        
    def print_matrix(self):
        size=self.vertex_count
        index=0
        print("================================================")
        # print("Adjacency Matrix of Graph")
        # while index < self.vertex_count: 
        #     print(self.adj_matrix[index],end="\n")
        #     index=index+1
        # print("================================================")

        for i in self.adj_matrix:
            print(" ".join(map(str,i)))

    def add_edge(self,u,v,weight):
        self.adj_matrix[u-1][v-1]=weight
        if self.count==0:
            print("Operation Log")
            self.count=1
        print("Edge added between vertex",u,"&",v)
        

    def remove_edge(self,u,v):
        self.adj_matrix[u-1][v-1]=0
        self.adj_matrix[v-1][u-1]=0
        print("Edge removed between vertex",u,"&",v)
        

    def has_edge(self,u,v):
        if v > len(self.adj_matrix) or u > len(self.adj_matrix):
            print("No vertices Found")
        if self.adj_matrix[u-1][v-1] == 1:
            print("Edge is  Present Between",u,"&",v)
        else:
            print("Edge is not Present Between",u,"&",v)
        
            
         
    



myadjmtx=Graph(5)
myadjmtx.add_edge(1,2,1)
myadjmtx.add_edge(1,3,1)
myadjmtx.add_edge(1,4,1)
myadjmtx.add_edge(1,5,1)
myadjmtx.add_edge(2,1,1)
myadjmtx.add_edge(2,3,1)
myadjmtx.add_edge(2,5,1)
myadjmtx.add_edge(3,1,1)
myadjmtx.add_edge(3,4,1)
myadjmtx.add_edge(3,2,1)
myadjmtx.add_edge(4,1,1)
myadjmtx.add_edge(4,5,1)
myadjmtx.add_edge(4,3,1)
myadjmtx.add_edge(5,1,1)
myadjmtx.add_edge(5,2,1)
myadjmtx.add_edge(5,4,1)
myadjmtx.remove_edge(5,4)
myadjmtx.print_matrix()
myadjmtx.has_edge(5,5)



    
    




        