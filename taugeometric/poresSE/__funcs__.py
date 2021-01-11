def points_start(maze):
    p_t = maze[0]
    p_end = []
    for i in range(len(p_t)):
        if(maze[i][0] == 0):
            p_end.append((i, 0))
    return p_end


def points_end(maze):
    p_t = maze[0]
    size = len(p_t)-1
    p_end = []
    for i in range(size+1):
        if(maze[i][size] == 0):
            p_end.append((i, size))
    return p_end
