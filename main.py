from Entity.Graph import Graph
from Entity.Tree import Tree

if __name__ == '__main__':
    graph = Graph()

    node_a = graph.add_node('A')
    node_b = graph.add_node('B')
    node_c = graph.add_node('C')
    node_d = graph.add_node('D')
    node_e = graph.add_node('E')

    graph.add_edge('A', 'B', 3)
    graph.add_edge('A', 'C', 5)
    graph.add_edge('B', 'C', 8)
    graph.add_edge('B', 'D', 1)
    graph.add_edge('C', 'D', 3)
    graph.add_edge('D', 'E', 2)

    graph.display()

    tree = Tree(node_a, graph)
    tree.load_tree()
    tree.display_2()

    path = graph.hill_climb('A', 'E')
    graph.print_path(path)
