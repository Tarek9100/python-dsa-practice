class Graph:
    def __init__(self):
        """Initialize an empty graph."""
        self.number_of_nodes = 0
        self.adjacency_list = {}

    def add_vertex(self, vertex: str) -> None:
        """Add a vertex to the graph."""
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = set()
            self.number_of_nodes += 1

    def add_edge(self, vertex1: str, vertex2: str) -> None:
        """Add an edge between two vertices."""
        if vertex1 == vertex2:
            raise ValueError("Self-loops are not allowed.")
        for v in (vertex1, vertex2):
            if v not in self.adjacency_list:
                self.add_vertex(v)
        self.adjacency_list[vertex1].add(vertex2)
        self.adjacency_list[vertex2].add(vertex1)

    def remove_edge(self, vertex1: str, vertex2: str) -> None:
        """Remove an edge between two vertices."""
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].discard(vertex2)
            self.adjacency_list[vertex2].discard(vertex1)

    def remove_vertex(self, vertex: str) -> None:
        """Remove a vertex and all its edges."""
        if vertex in self.adjacency_list:
            for adjacent in list(self.adjacency_list[vertex]):
                self.adjacency_list[adjacent].discard(vertex)
            del self.adjacency_list[vertex]
            self.number_of_nodes -= 1

    def get_vertices(self) -> list:
        """Return a list of all vertices in the graph."""
        return list(self.adjacency_list.keys())

    def get_edges(self) -> list:
        """Return a list of all edges in the graph."""
        edges = []
        for vertex in self.adjacency_list:
            for adjacent_vertex in self.adjacency_list[vertex]:
                if (adjacent_vertex, vertex) not in edges:
                    edges.append((vertex, adjacent_vertex))
        return edges

    def __str__(self) -> str:
        """Return a string representation of the graph."""
        result = ""
        for vertex in self.adjacency_list:
            result += f"{vertex}: {self.adjacency_list[vertex]}\n"
        return result.strip()

    def __len__(self) -> int:
        """Return the number of vertices in the graph."""
        return self.number_of_nodes


class WeightedGraph(Graph):
    def __init__(self):
        """Initialize an empty weighted graph."""
        super().__init__()
        self.weights = {}

    def add_edge(self, vertex1: str, vertex2: str, weight: float) -> None:
        """Add a weighted edge between two vertices."""
        super().add_edge(vertex1, vertex2)
        self.weights[(vertex1, vertex2)] = weight
        self.weights[(vertex2, vertex1)] = weight  # For undirected graph

    def get_weight(self, vertex1: str, vertex2: str) -> float:
        """Return the weight of the edge between two vertices."""
        return self.weights.get((vertex1, vertex2), float('inf'))
    