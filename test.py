from population import Population
from const import *
from matplotlib import pyplot as plt, animation
import os
import numpy as np

# Function to add small random values to the values, so that they would be plotted clearly
def randomize_values(lst):
    lst = lst + np.array(np.random.uniform(0,1,len(lst)))
    return lst

population = Population(INIT_SUCKERS)
population.add_cheat(N_CHEATS)

generation = 0
n_suckers_by_generations = []
n_cheats_by_generations = []

def plot(x_val, x_val_cheat, y_val, y_val_cheat):
    x_val = randomize_values(x_val)
    y_val = randomize_values(y_val)
    x_val_cheat = randomize_values(x_val_cheat)
    y_val_cheat = randomize_values(y_val_cheat)
    
    print('# of Suckers', len(x_val))
    print('# of Cheats', len(x_val_cheat))
    n_suckers_by_generations.append(len(x_val))
    n_cheats_by_generations.append(len(x_val_cheat))
    
    ax1.cla()
    ax1.scatter(y_val, x_val, c='b', alpha=0.4)
    ax1.scatter(y_val_cheat, x_val_cheat, c='r', marker='s', alpha=0.4)

    ax1.set_title('Birds of the ' + str(generation) + ' generations')
    ax1.set_xlabel('Current age')
    ax1.set_ylabel('Birds fitness')

    ax2.cla()
    ax2.plot(range(generation), n_suckers_by_generations, marker='o', c='b')
    ax2.plot(range(generation), n_cheats_by_generations, marker='s', c='r')
    ax2.set_title('# of birds per generation')
    ax2.set_xlabel('Generation')
    ax2.set_ylabel('Number of birds')
    ax2.legend(['Sucker', 'Cheat'])

stop=0
def gen():
    global stop
    i = 0
    while not stop:
        i += 1
        yield i

def animate(i):
    global generation, stop
    generation +=1
    print('\nGeneration', generation)
    print('Population is ', len(population.population))
    
    x_val, x_val_cheat = population.get_birds_fitness()
    y_val, y_val_cheat = population.ages()

    plot(x_val, x_val_cheat, y_val, y_val_cheat)
    
    try:
        population.get_fitness()
    except ValueError:
        print('Birds are extinct')
        stop=1
    population.reproduce()
    population.disease()
    population.azrael_turn()


fig, (ax1, ax2) = plt.subplots(1,2)
ani = animation.FuncAnimation(fig, animate, frames=gen, interval =1000, repeat=False)
plt.tight_layout(pad=1.6)
plt.show()

# writergif = animation.PillowWriter(fps=3)
# ani.save('results/animation.gif',writer=writergif , dpi = 300)