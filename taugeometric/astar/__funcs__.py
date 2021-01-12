from heapq import heappush, heappop
from math import hypot, sqrt


SQRT2 = sqrt(2.0)


DIRECTIONS = ((1, 0, 1.0), (0, 1, 1.0), (-1, 0, 1.0), (0, -1, 1.0),
              (1, 1, SQRT2), (-1, -1, SQRT2), (1, -1, SQRT2), (-1, 1, SQRT2))


class Node:

    def __init__(self, x, y, cost=float("inf"), h=0, parent=None):
        self.x = x
        self.y = y
        self.cost = cost
        self.h = h
        self.parent = parent

    def update(self, new_parent, new_cost):
        self.parent = new_parent
        self.cost = new_cost

    def __repr__(self):
        return "Node(x={x}, y={y}, cost={cost}, h={h}, parent={parent})".format(**self.__dict__)

    @property
    def priority(self):
        return self.cost + self.h

    @property
    def pos(self):
        return self.x, self.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        """This allows Node to be used in the priority queue directly"""
        return self.priority < other.priority


def make_grid(n_rows, n_cols, value):
    """Make a n_rows x n_cols grid filled with an initial value"""
    return [[value for _ in range(n_cols)] for _ in range(n_rows)]


def euclidean_distance(node1, node2):
    """Compute the Euclidean/L2 distance between two nodes"""
    return hypot(node1[0] - node2[0], node1[1] - node2[1])


def is_valid(x, y, grid, x_max, y_max):
    """Check the bounds and free space in the map"""
    if 0 <= x < x_max and 0 <= y < y_max:
        return grid[x][y] == 0
    return False


def astar(grid, start, goal):
    x_max, y_max = len(grid), len(grid[0])

    # None will later be used as sentinel for "no node here (yet)"
    nodes = make_grid(x_max, y_max, None)

    start_node = Node(*start, cost=0, h=euclidean_distance(start, goal))
    nodes[start_node.x][start_node.y] = start_node
    goal_node = Node(*goal)
    nodes[goal_node.x][goal_node.y] = goal_node

    # openlist will be used a priority queue and has to be accessed using
    # heappush and heappop from the heapq module. The Node class was modified
    # to work well with this kind of datastructure.
    openlist = []
    heappush(openlist, start_node)

    found = False
    while not found:
        # get the node with the least overall cost (actual + heuristic)
        current = heappop(openlist)
        for direction in DIRECTIONS:
            # compute new coordinates
            x_n, y_n = current.x + direction[0], current.y + direction[1]
            if not is_valid(x_n, y_n, grid, x_max, y_max):
                continue
            # we have valid coordinates
            if nodes[x_n][y_n] is None:
                nodes[x_n][y_n] = Node(
                    x_n, y_n, h=euclidean_distance((x_n, y_n), goal)
                )
            # the new cost is made up if the current cost + transition
            new_cost = nodes[current.x][current.y].cost + direction[2]
            if new_cost < nodes[x_n][y_n].cost:
                # cool, we have found a faster path to this node, let's update
                # it's predecessor
                nodes[x_n][y_n].update(current.pos, new_cost)
                heappush(openlist, nodes[x_n][y_n])
                if nodes[x_n][y_n] == goal_node:
                    # we're done, get out of here
                    found = True
                    break
        # openlist is empty and we have not bailed out with found. seems like
        # there is nothing we can do here
        if not openlist:
            return []

    # backtracking
    path = []
    current = goal_node
    # this is a little bit weird because I decided to store only the
    # coordinates instead of the parent itself. Why? Because repr(node) is way
    #  more readable that way ;-)
    while True:
        path.append(current.pos)
        if current.parent is not None:
            current = nodes[current.parent[0]][current.parent[1]]
        else:
            break
    # the path is built by backtracking from the goal, so we have to reverse it
    return path[::-1]