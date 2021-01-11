import taugeometric as tg
import porespy as ps
import numpy as np

im = ps.generators.blobs(shape=[20, 20], porosity=0.8, blobiness=0.5)
maze = np.logical_not(im)
maze = np.array(maze, dtype=int)

print(tg.tortuosity.tortuosity_geometric_2d(maze))
