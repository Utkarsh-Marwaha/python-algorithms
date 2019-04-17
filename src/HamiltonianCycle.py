class HamiltonianCycle:

    def __init__(self, graph):
        self.num_vertices = len(graph)
        self.hamiltonian_path = [None]*self.num_vertices
        self.graph = graph

    def hamiltonian_cycle(self):
        self.hamiltonian_path[0] = 0

        if not self.solve(1):
            print("No feasible solution found")
            return
        else:
            self.show_hamiltonian_path()

    def solve(self, position):

        # check if the base case has been hit i.e. all vertices have been evaluated
        if position == self.num_vertices:

            # check if the hamiltonian path is also a hamiltonian cycle

            # grab the last vertex added to the hamiltonian path
            last_vertex = self.hamiltonian_path[position - 1]
            # grab the first vertex added to the hamiltonian path
            first_vertex = self.hamiltonian_path[0]

            # check if the last and the first nodes of the hamiltonian path are adjacent to each other
            return self.graph[first_vertex][last_vertex] == 1

        for vertex in range(1, self.num_vertices):

            if self.is_feasible(vertex, position):
                self.hamiltonian_path[position] = vertex

                if self.solve(position + 1):
                    return True

                # else BACKTRACK

        # if we don't hit the base case after iterating through all the rows and columns then solution is absent
        return False

    def is_feasible(self, vertex, actual_position):

        # first criteria: the current node should be adjacent to the last node in the hamiltonian path

        if self.graph[vertex][self.hamiltonian_path[actual_position-1]] == 0:
            return False

        # second criteria: the current node should not be already present in the hamiltonian path

        for i in range(actual_position):
            if self.hamiltonian_path[i] == vertex:
                return False

        return True

    def show_hamiltonian_path(self):

        print("Hamiltonian Cycle exists: -")

        for i in range(self.num_vertices):
            print(self.hamiltonian_path[i], end=" -> ")

        print(self.hamiltonian_path[0])


if __name__ == '__main__':

    graph = [[0, 1, 0], [1, 0, 1], [1, 1, 0]]
    hamiltonian = HamiltonianCycle(graph)
    hamiltonian.hamiltonian_cycle()
