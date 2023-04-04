# Taken from https://www.geeksforgeeks.org/minimum-cost-path-in-a-directed-graph-via-given-set-of-intermediate-nodes/

# Function to Perform BFS on graph g
# starting from vertex v
def getMinPathSum(graph, visited, necessary, src, dest, currSum, minSum):

    # If destination is reached
    if src == dest:
        if minSum is None:
            return currSum

        return min(minSum, currSum)

    else:

        # Mark the current node
        # visited
        visited[src] = True

        # Traverse adjacent nodes
        for node in graph[src]:

            if not visited[node[0]]:

                # Mark the neighbour visited
                visited[node[0]] = True

                # Find minimum cost path
                # considering the neighbour
                # as the source
                return getMinPathSum(
                    graph, visited, necessary, node[0], dest, currSum + node[1], minSum
                )

                # Mark the neighbour unvisited
                visited[node[0]] = False

        # Mark the source unvisited
        visited[src] = False


def get_input():
    number_of_intersections = int(input())
    shortcuts = input().split(" ").map(lambda x: int(x))
    return number_of_intersections, shortcuts


def build_graph(number_of_intersections, shortcuts):
    graph = {}

    for intersection in range(1, number_of_intersections + 1):
        intersection_graph_idx = intersection - 1
        edges = [[shortcuts[intersection_graph_idx - 1] - 1, 1]]  # shortcut

        if intersection > 1:
            # Edge to previous intersection
            edges.append([intersection_graph_idx - 1, 1])

        if intersection < number_of_intersections:
            # Edge to next intersection
            edges.append([intersection_graph_idx + 1, 1])

        graph[intersection_graph_idx] = edges

    return graph


def compute_energy(number_of_intersections, shortcuts):
    # Stores the graph
    # TODO: Add description of what a graph looks like
    graph = build_graph(number_of_intersections, shortcuts)

    source = 1

    energy = []

    for destination in range(1, number_of_intersections + 1):
        # Keeps a check on visited and unvisited nodes
        visited = [False for i in range(number_of_intersections + 1)]

        energy_value = getMinPathSum(
            graph, visited, [1, destination], source, destination, 0, None
        )

        energy.append(str(energy_value))

    print(" ".join(energy))


compute_energy(get_input())
