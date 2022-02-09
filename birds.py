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

        normal_distribution_ages = [random.normalvariate(MAX_LIFESPAN/2, MAX_LIFESPAN/4) for _ in range(100)]
        self.lifespan = normal_distribution_ages[random.randint(0,len(normal_distribution_ages)-1)]
        self.age = 0 # measured in generations

        self.genes = {'would_clean':1, 'have_memory':0}
        self.determine_type()
        self.memorized_cheats=[]
        self.fitness = 1
    
    def give_type(self, type):
        if type == 'cheat':
            self.genes.update({'would_clean':0, 'have_memory':0})
        if type == 'smart':
            self.genes.update({'would_clean':0, 'have_memory':1})
        elif type == 'sucker':
            self.genes.update({'would_clean':1, 'have_memory':0})
        elif type == 'grudger':
            self.genes.update({'would_clean':1, 'have_memory':1})
        self.determine_type()

    def determine_type(self):
        if not self.genes['would_clean'] and not self.genes['have_memory']:
            self.type = 'cheat'
        elif not self.genes['would_clean'] and self.genes['have_memory']:
            self.type = 'smart'
        elif self.genes['would_clean'] and not self.genes['have_memory']:
            self.type = 'sucker'
        elif self.genes['would_clean'] and self.genes['have_memory']:
            self.type = 'grudger'

    def aging(self):
        self.age += 1

    def get_clean(self, population):
        population = population.copy()
        random.shuffle(population)
        n_birds_asked_to_clean = count(1)
        # if self.genes['have_memory']:
        #     if len(self.genes.memorized_helpful):
        #         self.sick_tick = 0
        #         return
        for bird in population:
            if next(n_birds_asked_to_clean)>MAX_HELP_REQUESTS:
                break
            if not bird.genes['would_clean']:
                if self.genes['have_memory']:
                    self.memorized_cheats.append(bird.id)
                continue
            if bird.genes['have_memory']:
                if self.id in bird.memorized_cheats:
    
                    continue
            self.sick_tick = 0
            self.fitness += GAIN_SAVING_LIFE
            bird.fitness -= LOSE_WASTING_TIME
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