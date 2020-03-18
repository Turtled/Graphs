"""
Simple graph implementation
"""
from queue import Queue, LifoQueue

class Graph:

    # {
    #     '0': {'1', '3'},
    #     '1': {'0'},
    #     '2': set(),
    #     '3': {'0'}
    # }

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[str(vertex_id)] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if str(v1) not in self.vertices.keys() or str(v2) not in self.vertices.keys():
            raise Exception('Trying to add edge between non-existant vert(s)')
            return

        self.vertices[str(v1)].add(str(v2))

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[str(vertex_id)]

    def bft(self, starting_vertex):
        visited = set()
        queue = Queue(maxsize=0)
        queue.put(str(starting_vertex))

        while not queue.empty():
            vert = queue.get()
            if vert not in visited:
                print(vert)
                visited.add(vert)
                for v in self.get_neighbors(vert):
                    queue.put(v)

    def dft(self, starting_vertex):
        visited = set()
        stack = LifoQueue(maxsize=0)
        stack.put(str(starting_vertex))
        while not stack.empty():
            vert = stack.get()
            if vert not in visited:
                print(vert)
                visited.add(vert)
                for v in self.get_neighbors(vert):
                    stack.put(v)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        print(str(starting_vertex))
        visited.add(vert)

        if len(visited) is 0:
            visited.add(str(starting_vertex))

        for vert in self.get_neighbors(starting_vertex):
            if vert not in visited:
                self.dft_recursive(vert, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        visited = set()
        queue = Queue(maxsize=0)
        start_path = list()
        start_path.append(starting_vertex)
        #print(start_path)
        queue.put(start_path)
        while not queue.empty():
            path = queue.get()
            #print("path" + str(path))
            vert = path[len(path) - 1]
            if vert not in visited:
                visited.add(vert)

                if str(vert) == str(destination_vertex):
                    return path

                for v in self.get_neighbors(vert):
                    path_copy = path.copy()
                    path_copy.append(v)
                    queue.put(path_copy)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        visited = set()
        stack = LifoQueue(maxsize=0)
        start_path = list()
        start_path.append(starting_vertex)
        #print(start_path)
        stack.put(start_path)
        while not stack.empty():
            path = stack.get()
            #print("path" + str(path))
            vert = path[len(path) - 1]
            if vert not in visited:
                visited.add(vert)

                if str(vert) == str(destination_vertex):
                    return path

                for v in self.get_neighbors(vert):
                    path_copy = path.copy()
                    path_copy.append(v)
                    stack.put(path_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=list()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        path.append(str(starting_vertex))
        #print ("if " + str(starting_vertex) + " == " + str(destination_vertex))
        if str(starting_vertex) == str(destination_vertex):
            return path

        if len(visited) is 0:
            visited.add(str(starting_vertex))

        for vert in self.get_neighbors(starting_vertex):
            if vert not in visited:
                visited.add(vert)
                return self.dfs_recursive(vert, destination_vertex, visited, path)

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)
    print("BFT end")

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    print("DFT end")
    graph.dft_recursive(1)
    print("DFT Recursive end")

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))
    print("BFS end")

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print("DFS end")

    print(graph.dfs_recursive(1, 6))
    print("DFS Recursive end")
