import taugeometric
import numpy as np
import porespy as ps

im = ps.generators.blobs(shape=[60, 60], porosity=1, blobiness=0.5)
maze = np.logical_not(im)
maze = np.array(maze, dtype=int)

