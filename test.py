from population import Population
from const import *
from matplotlib import pyplot as plt, animation
import os
import numpy as np

# Function to add small random values to the values, so that they would be plotted clearly
def randomize_values(lst):
    lst = lst + np.array(np.random.uniform(0,1,len(lst)))
    return lst

population = Population(INIT_NAIVES)
population.add_lier(N_LIERS)
population.get_fitness()
gen = 0

def animate(i):
    global gen
    gen +=1
    print('Generation', gen)
    print('Population is ', len(population.population))
    
    x_val, x_val_lier = population.get_birds_fitness()
    y_val, y_val_lier = population.ages()

    x_val = randomize_values(x_val)
    y_val = randomize_values(y_val)
    x_val_lier = randomize_values(x_val_lier)
    y_val_lier = randomize_values(y_val_lier)
    
    print('# of Naives', len(x_val))
    print('# of Liers', len(x_val_lier))

    
    plt.cla()
    plt.scatter(y_val, x_val, c='b', alpha=0.4)
    plt.scatter(y_val_lier, x_val_lier, c='r', marker='s', alpha=0.4)

    plt.title('Birds of the ' + str(gen) + ' generations')
    plt.xlabel('Current age')
    plt.ylabel('Birds fitness')
    plt.legend(['Naives', 'Liers'])

    population.reproduce()
    population.disease()
    population.azrael_turn()
    try:
        population.get_fitness()
    except ValueError:
        print('Birds are extinct')
        os.system('pause')

ani = animation.FuncAnimation(plt.gcf(), animate, interval =1000)
plt.tight_layout()
plt.show()