from population import Population
from const import *
from matplotlib import pyplot as plt, animation
import os
import numpy as np

population = Population(INIT_POPULATION)
population.get_fitness()

gen = 0
def animate(i):
    global gen
    gen +=1
    if gen == MAX_GENERATIONS:
        os.system('pause')
    print('Generation', gen)
    print('Population is ', len(population.population))
    
    x_val = population.get_rush_hour()
    y_val = population.ages()
    y_val += np.array(np.random.uniform(0,0.5,len(y_val)))
    plt.cla()
    plt.scatter(x_val, y_val)
    plt.xlim(0,5)
    plt.ylim(0,5)
    plt.title('Birds of the ' + str(gen) + ' generation')
    plt.xlabel('Age, one would live')
    plt.ylabel('Current age')

    population.azrael_turn()
    population.reproduce()
    population.disease()
    population.get_fitness()

ani = animation.FuncAnimation(plt.gcf(), animate, interval =1000)
plt.tight_layout()
plt.show()