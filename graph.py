from typing import Union



class Edge:
    def __init__(self, from_node: int, to_node: int, weight: float):
        self.from_node: int = from_node
        self.to_node: int = to_node
        self.weight: float = weight


class Node:
    def __init__(self, index: int, label=None):
        self.index = index
        self.edges: dict = {}
        self.label = label

    def num_edges(self) -> int:
        return len(self.edges)

    def get_edge(self, neighbour: int) -> Union[Edge, None]:
        if neighbour in self.edges:
            return self.edges[neighbour]
        return None

    def add_edge(self, neighbour: int, weight: float):
        self.edges[neighbour] = Edge(
            from_node=self.index,
            to_node=neighbour,
            weight=weight,
        )

    def remove_edge(self, neighbour: int):
        if neighbour in self.edges:
            del self.edges[neighbour]

    def get_edge_list(self) -> list:
        return list(self.edges.values())

    def get_sorted_edge_list(self) -> list:
        result = []
        neighbours = list(self.edges.keys())
        neighbours.sort()
        for n in neighbours:
            result.append(self.edges[n])
        return result


class Graph:
    def __init__(self, num_nodes: int, undirected: bool = False):
        self.num_nodes = num_nodes
        self.undirected = undirected
        self.nodes: list = [Node(i) for i in range(self.num_nodes)]

    def get_edge(self, from_node: int, to_node:int) -> Union[Edge, None]:
        if not 0 <= from_node < self.num_nodes:
            raise IndexError
        if not 0 <= to_node < self.num_nodes:
            raise IndexError
        return self.nodes[from_node].get_edges(to_node)