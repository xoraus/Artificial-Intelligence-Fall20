import sys
val=0
class Node:
    def __init__(self,h,dest,Edges,Parent,name):
        self.name = name
        self.h = h
        self.Parent = Parent
        self.isGoal = dest
        self.Solved = False
        self.Edges = Edges
        self.bestEdge = None
        self.Unsolvable = False
        
    def addEdge(self,Edge):
        self.Edges.append(Edge)
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name

            

class SubEdge:
    def __init__(self,g,Node):
        self.g = g
        self.Node = Node
   
    
class Edge:
    def __init__(self,EdgeType,ParentNode,Children):
        self.isAND = EdgeType
        self.Parent = ParentNode
        self.Children = Children
        self.cost = None
    
    def calcCost(self):
        if(self.isAND):
            cost = 0
            for node in self.Children:
                cost+= node.g + node.Node.h
            self.cost = cost
        else:
            self.cost = self.Children[0].g + self.Children[0].Node.h
        return self.cost
    def isSolved(self):
        if (self.isAND == False):
            node = self.Children[0].Node
            return node.Solved
        else:
            for node in self.Children:
                if (node.Node.Solved == False):
                    return False
            return True
    def isNotUnsolvable(self):
        if(self.isAND==True):
            for node in self.Children:
                if node.Node.Unsolvable:
                    return False
            return True
        else:
            if self.Children[0].Node.Unsolvable:
                return False
            else:
                return True
def updateF(Node1):
    if Node1 is None:
        pass
    else:
        changed = False
        minEdge = None
        minimum = 1000000
        if(not checkUnsolvableChildren(Node1)):
            Node1.Unsolvable = True
            print(Node1.name+ "unsolvable")
            changed = True
        for edge in Node1.Edges :
            edge.calcCost()
            if edge.cost< minimum and edge.isNotUnsolvable():
                minimum = edge.cost
                minEdge = edge
            if minEdge is not None:
                Node1.bestEdge = minEdge
        if(Node1.h!=minimum and minimum!=1000000):
            Node1.h = minimum
            changed = True
            print("Heuristic of Node ",Node1.name," Updated as",Node1.h)
        if(Node1.bestEdge is not None and Node1.bestEdge.isSolved()):
            print(Node1.name+" solved" )
            Node1.Solved = True
            changed = True
        if(Node1.Edges==[] and Node1.isGoal == True):
            print(Node1.name+" solved" )
            Node1.Solved= True
            changed = True
        if changed == True:
            updateF(Node1.Parent)
                    
def checkUnsolvableChildren(Node1):
    solvable = False
    Edges = Node1.Edges
    if Edges == []:
        if Node1.isGoal:
            return True
        else:
            Node1.Unsolvable = True
            print(Node1.name+" unsolvable")
            if(Node1.Parent is None):
                print("Root unsolvable")
                sys.exit()
            updateF(Node1.Parent)
            return False
    for each in Edges:
        if(each.isAND):
            check = True
            for e1 in each.Children:
                if  e1.Node.Unsolvable:
                    check = False
            if check == True:
                solvable = True
        else:
            if not each.Children[0].Node.Unsolvable:
                solvable = True
    return solvable
            
        
        

def constructGraph():
    Start = Node(7,False,[],None,'A')
    b = Node(4,False,[],Start,'B')
    c = Node(3,False,[],Start,'C')
    e1 = SubEdge(2,b)
    e2 = SubEdge(1,c)
    Start.addEdge(Edge(True,Start,[e1,e2]))
    d = Node(2,False,[],b,'D')
    e = Node(5,False,[],b,'E')
    e3 = SubEdge(2,d)
    e4 = SubEdge(1,e)
    b.addEdge(Edge(False,b,[e3]))
    b.addEdge(Edge(False,b,[e4]))
    h = Node(3,False,[],d,'H')
    i = Node(0,True,[],d,'I')
    e5 = SubEdge(1,h)
    e6 = SubEdge(10,i)
    d.addEdge(Edge(True,d,[e5,e6]))
    
    j = Node(0,True,[],e,'J')
    k = Node(0,True,[],e,'K')
    e7 = SubEdge(3,j)
    e8 = SubEdge(4,k)
    e.addEdge(Edge(True,e,[e7,e8]))
    
    
    f = Node(0,True,[],c,'F')
    g = Node(0,True,[],c,'G')
    e9 = SubEdge(9,f)
    e10 = SubEdge(7,g)
    c.addEdge(Edge(False,c,[e9]))
    c.addEdge(Edge(False,c,[e10]))    
    return Start

def findBestPath(start):
    cur =  start
    exp_list = [start]
    to_be_explored = []
    while(exp_list!= []):
        cur = exp_list.pop()
        if cur.bestEdge==None:
            if cur.Solved == False:
                to_be_explored.append(cur)
        else:
            for child in cur.bestEdge.Children:
                exp_list.append( child.Node)
    return to_be_explored[::-1]


def expand(node):
    for edge in node.Edges:
        edge.calcCost()
    updateF(node)
    
start = constructGraph()
curr = start
while(start.Solved!=True and start.Unsolvable!= True ):
    to_explore = findBestPath(start)
    if to_explore ==[]:
        break
    print("Iteration ",val+1, str(to_explore))
    val=val+1
    for curr in to_explore:
        print(curr.name)
        expand(curr)
cur =  start


print("Result Path")
exp_list = [start]
cost = 0
while(exp_list!= []):
    cur = exp_list.pop()
    print(cur)
    if cur.bestEdge==None:
        pass
    else:
        for child in cur.bestEdge.Children[::-1]:
            exp_list.append( child.Node) 
            cost+= child.g

print("Cost of the path:",cost)