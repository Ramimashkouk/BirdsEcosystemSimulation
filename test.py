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
for _ in range(INIT_GRUDGERS):
    population.add_bird('grudger')
for _ in range(N_CHEATS):
    population.add_bird('cheat')

generation = 0
n_suckers_by_generations = []
n_cheats_by_generations = []
n_grudgers_by_generations = []

def plot(x_val, x_val_cheat, x_grudgers, y_val, y_val_cheat, y_grudgers):
    x_val = randomize_values(x_val)
    y_val = randomize_values(y_val)
    x_val_cheat = randomize_values(x_val_cheat)
    y_val_cheat = randomize_values(y_val_cheat)
    x_grudgers = randomize_values(x_grudgers)
    y_grudgers = randomize_values(y_grudgers)
    
    print('# of Suckers', len(x_val))
    print('# of Cheats', len(x_val_cheat))
    n_suckers_by_generations.append(len(x_val))
    n_cheats_by_generations.append(len(x_val_cheat))
    n_grudgers_by_generations.append(len(x_grudgers))
    
    ax1.cla()
    ax1.scatter(y_val, x_val, c='b', alpha=0.4)
    ax1.scatter(y_val_cheat, x_val_cheat, c='r', marker='s', alpha=0.4)
    ax1.scatter(y_grudgers, x_grudgers, c='g', marker='*', alpha=0.4)


    ax1.set_title('Birds of the ' + str(generation) + ' generations')
    ax1.set_xlabel('Current age')
    ax1.set_ylabel('Birds fitness')

    ax2.cla()
    ax2.plot(range(generation), n_suckers_by_generations, marker='o', c='b')
    ax2.plot(range(generation), n_cheats_by_generations, marker='s', c='r')
    ax2.plot(range(generation), n_grudgers_by_generations, marker='*', c='g')
    ax2.set_title('# of birds per generation')
    ax2.set_xlabel('Generation')
    ax2.set_ylabel('Number of birds')
    ax2.legend(['Sucker', 'Cheat', 'Grudger'])

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
    
    x_val, x_val_cheat, x_grudgers = population.get_birds_attribute('fitness')
    y_val, y_val_cheat, y_grudgers = population.get_birds_attribute('age')

    plot(x_val, x_val_cheat, x_grudgers, y_val, y_val_cheat, y_grudgers)
    
    try:
        population.get_fitness()
    except ValueError:
        print('Birds are extinct')
        stop=1
    population.reproduce()
    # Grudgers benifits more when the disease happens more frequently in the same generation
    for _ in range(N_DISEASE_PER_GEN):
        population.disease()
        population.azrael_turn()
    if generation == 150:
        stop=1


fig, (ax1, ax2) = plt.subplots(1,2)
fig.suptitle('INFECTION_RATE = '+ str(INFECTION_RATE)+ ', MUTATION_RATE = '+ str(MUTATION_RATE) +  ', MAX_LIFESPAN = '+str(MAX_LIFESPAN) + ',\n MAX_POPULATION = ' + str(MAX_POPULATION) + ', MAX_HELP_REQUESTS = '+str(MAX_HELP_REQUESTS) + ', GAIN_SAVING_LIFE = '+ str(GAIN_SAVING_LIFE) + ',\n LOSE_WASTING_TIME = ' +str(LOSE_WASTING_TIME))
ani = animation.FuncAnimation(fig, animate, frames=gen, interval =1000, repeat=False)
plt.tight_layout(pad=1.6)
plt.show()

# writergif = animation.PillowWriter(fps=3)
# ani.save('results/animation.gif',writer=writergif , dpi = 300)