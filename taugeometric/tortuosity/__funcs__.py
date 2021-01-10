import numpy as np
from taugeometric.poresSE import points_start
from taugeometric.poresSE import points_end



def tortuosity_geometric_2d(maze):
    p_s = points_start(maze)
    p_e = points_end(maze)
    f_data = []
    for i in p_s:
        for j in p_e:
            data = astar(maze, i, j)
            if(data != None):
                f_data.append(len(data))
    return f_data