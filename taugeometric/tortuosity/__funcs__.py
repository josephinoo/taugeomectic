import numpy as np
from taugeometric.poresSE import points_start
from taugeometric.poresSE import points_end
from taugeometric.astar import astar
from scipy.spatial import distance as ds

def metric_euclidian(points):
    p_s=points[0]
    distance=0
    for i in range(1,len(points)):
        p_e=points[i]
        distance+=ds.euclidean(p_s,p_e)
        p_s=points[i]
    return distance


    
    
def tortuosity_geometric_2d(maze):
    line_maze_h=maze.shape[1]-1
    p_s = points_start(maze)
    p_e = points_end(maze)

    f_data = []
    for i in p_s:
        selection_path=[]
        for j in p_e:
            data = astar(maze, i, j)
            if(data != None):
                selection_path.append(metric_euclidian(data))
        
        f_data.append(np.array(selection_path).min())
    t_g=np.mean(f_data)/(line_maze_h)
    return t_g