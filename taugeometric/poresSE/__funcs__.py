def points_start(maze):
    p_t = maze[0]
    points_final = []
    for i in range(len(p_t)):
        if(maze[i][0] == 0):
            points_final.append((i, 0))

    return points_final


def points_end(maze):
    p_t = maze[0]
    size = len(p_t)-1
    points_final = []
    for i in range(size+1):
        if(maze[i][size] == 0):
            points_final.append((i, size))
