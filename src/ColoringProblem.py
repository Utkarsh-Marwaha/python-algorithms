class ColoringProblem:

    def __init__(self, num_vertices, num_colors, graph):
        self.num_vertices = num_vertices
        self.num_colors = num_colors
        self.colors = [0] * num_vertices
        self.graph = graph

    def solve_coloring_problem(self):

        if not self.solve(0):
            print("No feasible solution found within the given parameters")
        else:
            self.show_result()

    def solve(self, node_index):

        if node_index == self.num_vertices:
            return True

        for color_index in range(1, self.num_colors+1):

            if self.is_color_valid(node_index, color_index):
                # assign color and proceed to next vertex
                self.colors[node_index] = color_index

                if self.solve(node_index+1):
                    return True
                # else BACKTRACK
        return False

    def is_color_valid(self, node_index, color_index):

        # None of the adjacent nodes can have the same color
        for i in range(self.num_vertices):
            if self.graph[node_index][i] == 1 and color_index == self.colors[i]:
                return False
        return True

    def show_result(self):
        for i in range(self.num_vertices):
            print("None %d has color index: %d" % (i, self.colors[i]))


if __name__ == '__main__':

    graph_matrix = [
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 1, 1, 0, 1],
        [0, 0, 0, 1, 0]
    ]

    coloring_problem = ColoringProblem(num_vertices=5, num_colors=3, graph=graph_matrix)
    coloring_problem.solve_coloring_problem()
