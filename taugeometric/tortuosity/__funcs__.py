import numpy as np
import matplotlib.pyplot as plt
import matplotlib
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


    
def show_streamlines(maze,paths):
    plt.imshow(maze,cmap="gray_r")
    for i in paths:
        for j in i:
            maze[j[0]][j[1]]=2
    colors = 'white dimgray black '.split()
    cmap = matplotlib.colors.ListedColormap(colors, name='colors', N=None)
    plt.imshow(maze,cmap=cmap)
    
def tortuosity_geometric_2d(maze,showStreamline=False):
    line_maze_h=maze.shape[1]-1
    p_s = points_start(maze)
    p_e = points_end(maze)

    f_data = []
    path_show=[]
    for i in p_s:
        selection_path=[]
        
        pahts=[]
        for j in p_e:
            data = astar(maze, i, j)
            if(data != None):
                selection_path.append(metric_euclidian(data))
                pahts.append(data)
        if(len(selection_path)!=0):
            minimum=np.array(selection_path).min()
            position=selection_path.index(minimum)
            path_show.append(pahts[position])
            f_data.append(minimum)
    if(showStreamline):
        show_streamlines(maze,path_show)
    t_g=np.mean(f_data)/(line_maze_h)
    print(t_g)
    if(t_g<1):
       return None
    return t_g
    


    
