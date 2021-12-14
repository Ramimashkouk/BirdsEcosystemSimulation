import random
import numpy as np
from const import *
from itertools import count

class Bird:
    BIRD_ID = 0
    def __init__(self):
        self.id = self.__class__.BIRD_ID
        self.__class__.BIRD_ID += 1
        self.sick_tick = 0

        normal_distribution_ages = [random.normalvariate(2.5, 1) for _ in range(100)]
        self.lifespan = normal_distribution_ages[random.randint(0,len(normal_distribution_ages)-1)]
        self.age = 0 # measured in generations

        self.genes = {'would_clean':1, 'some_gene':0}
        self.fitness = 1
    
    def aging(self):
        self.age += 1

    def get_clean(self, population):
        population = population.copy()
        random.shuffle(population)
        n_birds_asked_to_clean = count(1)
        for bird in population:
            if next(n_birds_asked_to_clean)>MAX_HELP_REQUESTS:
                break
            if bird.genes['would_clean'] == 0:
                bird.fitness += 2 # as it uses this time to collect food, survive or pla pla
                continue
            self.sick_tick = 0
            return

    def mate(self, bird):
        child = Bird()
        genes = list(self.genes.keys())
        genes_from_self = np.random.choice(genes, round(len(genes)/2), replace =False)
        genes_from_other = [gene for gene in genes if gene not in genes_from_self]
        for gene in genes_from_self:
            child.genes[gene] = self.genes[gene]
        for gene in genes_from_other:
            child.genes[gene] = bird.genes[gene]
        return child

    def mutate(self):
        for gene in self.genes.keys():
            if random.uniform(0,1) < MUTATION_RATE:
                self.genes[gene] = 1- self.genes[gene]