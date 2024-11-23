# cellular_automata_SIR
Stochastic Cellular Automata SIR epidemic model in Python

This software simulates the dynamics of a susceptible-infected-recovered (SIR) epidemic model by means of stochastic cellular automata.

The cell is represented by a Class named "cell", and each one can be instantiated with "c = cell("X")", where "X" is the initial state {"S", "I" or "R"}
After creating the cells, each one should be assigned a list of neighbor cells, by using "c.neighbors = [c1, c2, ..., cn]".
The number of neighbors of each cell can be arbitrariry set. Therefore, the model can represent any 2D or 3D topology.

There is a function, called "calculate_next_state", that gets a list of cell of the automata, and determines the next states by applying the transition rules of the SIR epidemic model.

In addition, there is a function named "save_plot", that can be used to plot a 2D color map of the automata. To use the function, the user should adopt a 2D topology, described by a list of lists "[[c1,c2,..],[c3,c4...],...]", where each sublist represents a row of cells. In the plots, the S, I and R are representd by green, red and blue rectangles, respectively.
User should give the topology list and the name to save the figure, as arguments to the "save_plot" function.

Finally, the "automato.py" code also brings a simulation example to illustrate the use
