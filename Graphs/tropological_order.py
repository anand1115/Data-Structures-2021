from collections import defaultdict

class Graph :

    def __init__(self, arg_nodes) :
        self.nodes = arg_nodes
        # adjlit is implemented as a dictionary. The default dictionary would create an empty 
        # list as a default (value) for the nonexistent keys.
        self.adjlist = defaultdict(list)  # Stores the graph in an adjacency list
        self.incoming_edge_count = []     # For a node, it stores the number of incoming edges. 
        self.topo_order = []              # Stores the nodes in lexical topologically sorted order.
        self.zero_incoming_edge_node = [] # Stores the nodes that have zero incoming edges.

    # Create an adjacency list for storing the edges
    def AddEdge(self, src, dst) :
        self.adjlist[src].append(dst)
        self.incoming_edge_count[dst] += 1

    def TopologicalSort(self) :

        for node in range(self.nodes) :
            if self.incoming_edge_count[node] == 0 :
               self.zero_incoming_edge_node.append(node)

        while self.zero_incoming_edge_node :
            self.zero_incoming_edge_node.sort()
            src = self.zero_incoming_edge_node.pop(0)

            # Iterate through the adjacency list
            if src in self.adjlist :
                for node in self.adjlist[src] :
                    self.incoming_edge_count[node] -= 1
                    if self.incoming_edge_count[node] == 0 :
                        self.zero_incoming_edge_node.append(node)

            self.topo_order.append(src)

        print("Topological Sorting In A Lexical Order : " + str(self.topo_order))

def main() :

    node_cnt = 7
    g = Graph(node_cnt)
    g.incoming_edge_count = [0] * node_cnt # For a node, it stores the number of incoming edges.

    g.AddEdge(0,2)
    g.AddEdge(0,5)
    g.AddEdge(1,3)
    g.AddEdge(1,6)
    g.AddEdge(2,4)
    g.AddEdge(3,5)
    g.AddEdge(5,2)
    g.AddEdge(5,4)
    g.AddEdge(6,2)

    g.TopologicalSort()

if __name__ == "__main__" :
    main()
n
