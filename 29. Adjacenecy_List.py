class Graph:
    def __init__(self,vertex_count=None,adj_list=None):
        self.vertex_count=vertex_count
        self.adj_list={ }
        size=0
        while size < vertex_count:
            self.adj_list[size]=[]
            size=size+1

    def print_adj_list(self):
        size=0
        while size <self.vertex_count:
            print("V",size,"=",self.adj_list[size])
            size=size+1
    
    def add_edge(self,u,v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
        self.adj_list[u]=list(set(self.adj_list[u]))
        self.adj_list[v]=list(set(self.adj_list[v]))
    
    def remove_edge(self,u,v):
        self.adj_list[u].remove(v)
        self.adj_list[v].remove(u)
    
    def has_edge(self,u,v):
        if v in self.adj_list[u] or u in self.adj_list[v]:
            print("Present")
        else:
            print("Absent")
        


myadjlst=Graph(5)
# myadjlst.add_edge(0,2)
# myadjlst.add_edge(0,3)
# myadjlst.add_edge(0,1)
# myadjlst.add_edge(1,5)
# myadjlst.add_edge(1,4)
# myadjlst.add_edge(1,0)
# myadjlst.add_edge(2,0)
# myadjlst.add_edge(2,6)
# myadjlst.add_edge(3,7)
# myadjlst.add_edge(3,0)
# myadjlst.add_edge(4,1)
# myadjlst.add_edge(4,7)
# myadjlst.add_edge(5,1)
# myadjlst.add_edge(5,7)
# myadjlst.add_edge(6,7)
# myadjlst.add_edge(6,2)
# myadjlst.add_edge(7,6)
# myadjlst.add_edge(7,3)
# myadjlst.add_edge(7,4)
# myadjlst.add_edge(7,5)
myadjlst.add_edge(0,1)
myadjlst.add_edge(1,3)
myadjlst.add_edge(1,2)
myadjlst.add_edge(2,4)
myadjlst.add_edge(3,4)

# myadjlst.remove_edge(0,3)
# myadjlst.has_edge(1,6)

myadjlst.print_adj_list() 

