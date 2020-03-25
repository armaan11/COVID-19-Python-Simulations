import numpy as np 
import scipy.spatial.distance as distance
import matplotlib.pyplot as plt
import scipy, pylab

#Number of people and infected percent
number_of_particles = 100
percent_infected = 5

# radius
# !!!! need to figure out how to set the radius or find it
radius = 0.1

#calculating number infected and bound
number_infected = round(number_of_particles * percent_infected / 100)
bound = number_of_particles - number_infected

# !!!! no clue what this is but it works
ax = pylab.subplot(111)

# set initial x and y coords. Can be randomized. Can be placed equidistant on a grid. Can also be placed using contour plots.
a = scipy.rand(100)
b = scipy.rand(100)

# create a singular array with [[x1,y1], [x2,y2] ....
position = np.column_stack((a,b))

# initializer array to hold status. free, infected, quarantined, recovered, dead
status = []

# sets random particles to infected however will need to be changed if method of creating initial x,y coords is changed
for i in range(number_of_particles):
    if i < bound:
        status.append(1)
    else: 
        status.append(2)

# plots x, y coords in accordance with status and different colors for distinguishability. Will need to be called for each timeframe.
def setupplot():
    for i in range(number_of_particles):
        if status[i] == 1:
            ax.scatter(position[i][0], position[i][1], c='b')
        elif status[i] == 2:
            ax.scatter(position[i][0], position[i][1], c='r')
            
setupplot()
plt.show()

# rapidly looks up distances between every coordinate pair
dist = distance.cdist(position, position)

# changes status if distance < radius
# still need to add time factor in and make recovered immune and dead dissapear
def changestatus():
    for i in range(int(dist.size**(0.5))):
        for j in range(int(dist.size**(0.5))):
            if (0 < dist[i][j] <= radius and status[i] == 2):
                status[j] = 2

changestatus()
setupplot()
ax.figure().show()
