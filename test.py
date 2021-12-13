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
generation = 0
n_naives_by_generations = []
n_liers_by_generations = []

def plot(x_val, x_val_lier, y_val, y_val_lier):
    x_val = randomize_values(x_val)
    y_val = randomize_values(y_val)
    x_val_lier = randomize_values(x_val_lier)
    y_val_lier = randomize_values(y_val_lier)
    
    print('# of Naives', len(x_val))
    print('# of Liers', len(x_val_lier))
    n_naives_by_generations.append(len(x_val))
    n_liers_by_generations.append(len(x_val_lier))
    
    ax1.cla()
    ax1.scatter(y_val, x_val, c='b', alpha=0.4)
    ax1.scatter(y_val_lier, x_val_lier, c='r', marker='s', alpha=0.4)

    ax1.set_title('Birds of the ' + str(generation) + ' generations')
    ax1.set_xlabel('Current age')
    ax1.set_ylabel('Birds fitness')

    ax2.cla()
    ax2.plot(range(generation), n_naives_by_generations, marker='o', c='b')
    ax2.plot(range(generation), n_liers_by_generations, marker='s', c='r')
    ax2.set_title('# of birds per generation')
    ax2.set_xlabel('Generation')
    ax2.set_ylabel('Number of birds')
    ax2.legend(['Naives', 'Liers'])

def animate(i):
    global generation
    generation +=1
    print('Generation', generation)
    print('Population is ', len(population.population))
    
    x_val, x_val_lier = population.get_birds_fitness()
    y_val, y_val_lier = population.ages()

    plot(x_val, x_val_lier, y_val, y_val_lier)

    population.reproduce()
    population.disease()
    population.azrael_turn()
    try:
        population.get_fitness()
    except ValueError:
        print('Birds are extinct')
        os.system('pause')

fig, (ax1, ax2) = plt.subplots(1,2)
ani = animation.FuncAnimation(fig, animate, interval =1000)
plt.tight_layout()
plt.show()