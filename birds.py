import random
import numpy as np
from const import *

class Bird:
    BIRD_ID = 0
    def __init__(self):
        self.id = self.__class__.BIRD_ID
        self.__class__.BIRD_ID += 1
        # self.is_clean = 1 if random.uniform(0,1) > INFLAMATION_RATE else 0
        self.sick_tick = 0
        self.would_clean = 1

        normal_distribution_age = [random.normalvariate(2.5, 1) for _ in range(100)] # mean of 2.5 generations and std of 1 gen
        self.lifespan = normal_distribution_age[random.randint(0,len(normal_distribution_age)-1)]
        self.age = 0 # in generations

        self.genes=[self.would_clean]+list(np.random.randint(0,2,N_GENES))
    
    def aging(self):
        self.age += 1

    def get_clean(self, population):
        for bird in population:
            if bird.would_clean == 0:
                continue
            self.sick_tick = 0

    def mate(self, bird):
        child = Bird()
        mate_point = random.randint(0,len(self.genes))
        for idx in range(len(self.genes)):
            if idx < mate_point:
                child.genes[idx] = self.genes[idx]
            else:
                child.genes[idx] = bird.genes[idx]
        return child

    def mutate(self):
        for idx in range(len(self.genes)):
            if random.uniform(0,1) < MUTATION_RATE:
                self.genes[idx] = 1- self.genes[idx]


# class Lier(Bird):
#     def __init__(self):
#         Bird.__init__(self)
#         self.would_clean = 0
#         self.type = 'lier'

# class Naive(Bird):
#     def __init__(self):
#         Bird.__init__(self)
#         self.would_clean = 1
#         self.type = 'naive'
    