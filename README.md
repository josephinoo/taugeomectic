# TauGeometric  🐍

-----
# Installation 

TauGeometric relies heavily on the Scipy Stack, as it uses the Porespy library. Make sure you get Python 3.6+ version.

    git clone https://github.com/eljosephavila123/taugeomectic.git 

Create the virtual environment[]

    virtualenv env

The virtual environment is activated

    source env/bin/activate

Install the python library used in the module

    pip install -r requirements.txt

On Mac or Linux, you need to open a normal terminal window,
then type source activate {env} where you replace {env} with the name 
of the environment you want to install TauGeometric.

# Examples

``` python
import taugeometric as tg
import porespy as ps
import numpy as np

im = ps.generators.blobs(shape=[20, 20], porosity=0.8, blobiness=0.5)
maze = np.logical_not(im)
maze = np.array(maze, dtype=int)

print(tg.tortuosity.tortuosity_geometric_2d(maze))
```


