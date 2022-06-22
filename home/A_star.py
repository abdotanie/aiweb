from queue import PriorityQueue 
cityes=[]
straight_line={}
# Add a connect from A and B in arry
def add(c1,d2,f3): 
  r=[c1,d2,int(f3)]  
  cityes.append(r)
  print(cityes)
# Add a string line   
def addHeuristics(c,n):
    straight_line[c]=int(n)
class Graph:
    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()
    # Create an undirected graph by adding symmetric edges
    def make_undirected(self):
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.graph_dict.setdefault(b, {})[a] = dist
    # Add a link from A and B of given distance, and also add the inverse link if the graph is undirected
    def connect(self, A, B, distance=1):
        self.graph_dict.setdefault(A, {})[B] = distance
        if not self.directed:
            self.graph_dict.setdefault(B, {})[A] = distance
def a_star(source, destination,g):
    p_q = PriorityQueue()
    visited={}
    p_q.put((straight_line[source], 0, source, [source]))
    visited[source] = straight_line[source]
    while not p_q.empty():
        (heuristic, cost, vertex, path) = p_q.get()
        #print('Queue Status:',heuristic, cost, vertex, path)
        if vertex == destination:
           return heuristic, cost, path
        for next_node in g[vertex].keys():
            current_cost = cost + g[vertex][next_node]
            heuristic = current_cost + straight_line[next_node]
            if not next_node in visited or visited[next_node] >= heuristic:
                visited[next_node] = heuristic
                p_q.put((heuristic, current_cost, next_node,path + [next_node]))
def main(start,end):
    graph = Graph()
    # Make graph undirected, create symmetric connections
    for g in cityes:
        graph.connect(g[0],g[1],g[2])
    graph.make_undirected()
    g=graph.graph_dict
    heuristic, cost, optimal_path = a_star(start,end,g)
    # print('min of total heuristic_value =', heuristic)
    # print('total min cost =', cost)
    # print('\nRoute:')
    path =' -> '.join(city for city in optimal_path)
    #print(' -> '.join(city for city in optimal_path))
    print(path)
    return(path)



