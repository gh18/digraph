#!/usr/bin/python3


# input handler
def read_input(filename):
    with open(filename) as file:
        vertices_num = int(file.readline())
        data = file.readlines()
        parsed_data = [[int(i) for i in x.split()] for x in data]
    return vertices_num, parsed_data


# print(read_input('in.txt'))
num_vertices = read_input('in.txt')[0]
print(num_vertices)
parsed_matrix = read_input('in.txt')[1]
print(parsed_matrix)

# filling a list with 0 (False has int(0))
visited = [False] * num_vertices


# checks adjacent vertices for the same color (0 or 1)
def get_adjacent_not_visited_nodes(vertex):
    for _ in range(num_vertices):
        if parsed_matrix[vertex][_] == 1 and visited[_] is False:
            return _
    return None


def check_graph(graph):

    # lists to store connected components of a possible digraph
    fraction_1 = [0]
    fraction_2 = []

    # list to store visited vertices
    visited[0] = True

    # creates queue with first vertex, paints it to 0
    queue = [0]
    while queue:
        # get the first element out of the queue
        node_1 = queue.pop(0)

        # starts bfs from node_1
        node_2 = get_adjacent_not_visited_nodes(node_1)
        while node_2 is not None:

            # puts vertex in either of fraction lists
            if node_1 in fraction_2:
                fraction_1.append(node_2)
            else:
                fraction_2.append(node_2)
            for i in range(num_vertices):
                if (parsed_matrix[node_2][i] == 1 and
                        ((node_2 in fraction_2 and i in fraction_2) or
                         (node_2 in fraction_1 and i in fraction_1))):
                    return 'N'

            # adds the vertex to a visited[] list and to a queue to check it later
            visited[node_2] = True
            queue.append(node_2)
            node_2 = get_adjacent_not_visited_nodes(node_1)

    return 'Y' + '\n' \
           + ' '.join([str(i + 1) for i in fraction_1]) + '\n' + '0' + '\n' \
           + ' '.join([str(i + 1) for i in fraction_2]) + '\n'


if __name__ == '__main__':

    # output handler
    with open('output.txt', 'w') as file:
        file.write(check_graph(parsed_matrix))

# The idea behind is to complete a series of BFS searches (from every single not visited vertex). Vertex to start with
# is placed into first fraction. If the search moves to a new vertex, this vertex is placed in second fraction.
# If the search moves to visited vertex, a check is made to ensure current and visited vertices are in different
# fractions. Otherwise this graph is not a digraph

