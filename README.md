# TauGeometric  🐍

TauGeometric is a set of tools to get the geometric tortuosity from 2D images of porous materials. It calculates the geometric tortuosity using A* algorithm and [Porespy](http://porespy.org/) python library resources. The basis of the computation is to extract all the paths of the porous media generated by porespy and after that, extract the distance of these using A* algorithm. The minimum of these values are taken for every entrance node where the paths starts. At the end, the tortuosity is calculated following the equation (1). 
Where Ld is the mean of the values calculated previously and L is the lenght of the axis taken, commonly the horizontal axis.
### Equation (1)

<img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;\frac{l_d}{L}" title="\frac{l_d}{L}" />

To find the total geometric paths the carnality of each set is multiplied.

S=set of start nodes

E= set of end nodes 

Total geometric paths=N(S)×N(E)

<img src="images/paths.png"/>

The fundamental equation of the process explained in the algorithm can resumed in the equation (2).


### Equation (2)
<img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;\frac{\frac{1}{m}\\\sum&space;_{i=1}^{m}min\left&space;\{&space;C_i&space;\right&space;\}}{L}" title="\frac{\frac{1}{m}\\\sum _{i=1}^{m}min\left \{ C_i \right \}}{L}" />

Where:

` i`: is the quatity of entrance nodes

` Ci`: represents all the paths generated for every entrance node

` L`: shorter length (it can be a straight line)

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


