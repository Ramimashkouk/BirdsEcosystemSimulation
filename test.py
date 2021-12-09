from population import Population
from const import *

population = Population(INIT_POPULATION)
population.get_fitness()
# population.add_bird('lier')

for gen in range(1,11):
    print('Generation', gen)
    print('Population is ', len(population.population))

    population.azrael_turn()
    population.reproduce()
    population.disease()
    population.get_fitness()

    # for bird in population:
    #     if not bird.is_clean:
    #         for cleaner in population:
    #             if bird.get_clean(cleaner):
    #                 break
    #     if not bird.is_clean:
    #         del bird
    #         print(f'Bird {bird.id} is died')