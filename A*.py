import queue as q

def initialize_graph():
    weighted_graph = {}
    weighted_graph["a"] =[]
    weighted_graph["b"] =[]
    weighted_graph["y"] =[]
    weighted_graph["d"] =[]
    weighted_graph["i"] =[]
    weighted_graph["e"] =[]
    weighted_graph["k"] =[]
    weighted_graph["m"] =[]
    weighted_graph["f"] =[]
    weighted_graph["j"] =[]
    
    weighted_graph["a"].append(("d",3))
    weighted_graph["d"].append(("a",3))
    
    weighted_graph["a"].append(("y",4))
    weighted_graph["y"].append(("a",4))
    
    weighted_graph["b"].append(("y",1))
    weighted_graph["y"].append(("b",1))
    
    weighted_graph["y"].append(("d",2))
    weighted_graph["d"].append(("y",2))
    
    weighted_graph["y"].append(("i",5))
    weighted_graph["i"].append(("y",5))
    
    weighted_graph["i"].append(("d",6))
    weighted_graph["d"].append(("i",6))
    
    weighted_graph["f"].append(("d",3))
    weighted_graph["d"].append(("f",3))
    
    weighted_graph["e"].append(("d",3))
    weighted_graph["d"].append(("e",3))
    
    weighted_graph["f"].append(("e",1.5))
    weighted_graph["e"].append(("f",1.5))
    
    weighted_graph["j"].append(("f",3.5))
    weighted_graph["f"].append(("j",3.5))
    
    weighted_graph["e"].append(("k",2))
    weighted_graph["k"].append(("e",2))
    
    weighted_graph["m"].append(("k",2))
    weighted_graph["k"].append(("m",2))
    
    weighted_graph["k"].append(("j",2.5))
    weighted_graph["j"].append(("k",2.5))
    
    weighted_graph["i"].append(("j",7))
    weighted_graph["j"].append(("i",7))
    
    return weighted_graph


def initialize_h():
    h = {}
    h["a"] = 6
    h["b"] = 5
    h["y"] = 4
    h["d"] = 5
    h["i"] = 0
    h["e"] = 6
    h["k"] = 7
    h["m"] = 8
    h["f"] = 5
    h["j"] = 5
    return h

def a_star(graph, first, dest):
    openList = q.PriorityQueue()
    h = initialize_h()
    openList.put((0,[(first, 0)]))
    closedList = set()
    while not openList.empty():
        # shortest available path
        i, path = openList.get()
        # openList contains paths with final node unclosedList
        node = path[-1][0]
        g_cost = path[-1][1]
        closedList.add(node)
        if node == dest:
            # return only path without cost
            print("Cost:",path[-1][1])
            return [x for x, y in path]
        for neighbor, distance in graph[node]:
            cumulative_cost = g_cost + distance
            f_cost = cumulative_cost + h[neighbor]
            new_path = path + [(neighbor, cumulative_cost)]
            # add new_path to openList
            if neighbor not in closedList:
                openList.put((f_cost, new_path))
            # update cost of path in openList
            elif neighbor in openList.queue:
                openList.put((f_cost,new_path))
                print(path)
    return None


start = "a"
dest = "i"
graph = initialize_graph()
print(a_star(graph, start, dest))