# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 00:02:24 2024

@author: Antonio Godoi
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


class cell(object):        
    def __init__(self, state):
        self.state = state  # {s,i,r}
        self.next_state = None
        self.neighbors = []    
    def __str__(self):
        return str(self.state)       
    
    
def calculate_next_state(cells):
    beta = .2 # Probability of Infecting
    gama = .1 # Probability of Recovering
                
    for c in cells:        
        c.next_state = c.state # Remain in the same state when no change occurs
        
        if c.state == 'S':
        # Find the number of infected neighbors
            infected_neighbors = 0            
            for v in c.neighbors:
                if v.state == 'I':
                    infected_neighbors += 1
                    
        # Transition rule from S to I
            for contacts in range(infected_neighbors):
                r = np.random.rand()
                if r < beta:
                    c.next_state = 'I'
        
        # Transition rule from I to R
        if c.state == 'I':
            r = np.random.rand()
            if r < gama:
                c.next_state = 'R'
                
    # Update all cells
    for c in cells:
        c.state = c.next_state


def save_plot(net_topology, fname):
    subfolder = 'plots' # Folder name 
    dir_path = os.path.dirname(os.path.realpath('automato.py'))
    dir_path = dir_path+'\\'+str(subfolder)
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path) # Create "plots" folder to save graphs
    colors = ["#00ff00","#0000ff","#ff0000"] # S = Green / I = Red / R = Blue
    custom_cmap = LinearSegmentedColormap.from_list("custom_cmap", colors)
    dic = {'S':1, 'I':3, 'R':2}
    temp2 = []
    for y in range(len(net_topology)):
        temp=[]
        for x in range(len(net_topology[y])):
            temp.append(int(dic[net_topology[y][x].state]))
        temp2.append(temp)
    plt.imshow(temp2, cmap=custom_cmap, vmin=1, vmax=3)
    plt.savefig(subfolder+"\\"+fname)
    plt.close()
    
"""----------------------------Simulation Example---------------------------"""

# Create 6 cells with initial states
c1 = cell('I')
c2 = cell('S')
c3 = cell('S')
c4 = cell('S')
c5 = cell('S')
c6 = cell('S')

# Set the neighbors of each cell
c1.neighbors = [c2,c4]
c2.neighbors = [c1, c3, c5]
c3.neighbors = [c2,c6]
c4.neighbors = [c1, c5]
c5.neighbors = [c2,c4,c6]
c6.neighbors = [c3,c5]

# Optional: Set a 2D topology
# In this example, we have two rows, with 3 cell each
topology = [[c1,c2,c3],[c4,c5,c6]]
# C1-C2-C3
# C4-C5-C6

# Run the simulation for t = 20
for t in range(20):
    print(f"t={t})  \n\t{c1}-{c2}-{c3}\n\t{c4}-{c5}-{c6}\n----------")
    # save_plot(topology, str("plot")+str(t)+str(".png")) # Uncomment this line to save 2D plots
    calculate_next_state([c1,c2,c3,c4,c5,c6])
