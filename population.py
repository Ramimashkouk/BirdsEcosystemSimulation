from birds import *
from const import *

class Population():
    def __init__(self, length):
        self.population = []
        for _ in range(length):
            bird = Bird()
            bird.aging()
            self.population.append(bird)
    
    def get_fitness(self):    
        self.fit_partners=[]    # Birds, in the age of reproduction
        self.birds_to_death = []    # Birds older than their total age, written by fate 
        for bird in self.population:
            if bird.age in range(1,round(MAX_LIFESPAN)):
                self.fit_partners.append(bird)
        
        birds_fitness = np.array([bird.fitness for bird in self.fit_partners])**2
        self.max_fitness = birds_fitness.max()
        fitness_sum = birds_fitness.sum()
        self.probabilities = birds_fitness / fitness_sum

    def reproduce(self):
        new_population=[]
        for _ in range(round(len(self.fit_partners)/2)): # All bird in fit_partners can reproduce, so they would love to :)
            while True:
                partner1= self.select()
                partner2= self.select()
                if partner1 is not partner2:
                    break
            for _ in range(2): # Get two children for these partners
                child = partner1.mate(partner2)
                child.mutate()
                new_population.append(child)
        self.population += new_population
        for bird in self.population:
            bird.aging()

    def select(self):
        index = -1
        rand = random.uniform(0, 1)

        while rand > 0:
            index += 1
            rand -= self.probabilities[index]
        return self.fit_partners[index]

    def azrael_turn(self):
        # remove sick or old birds
        for bird in self.birds_to_death:
            self.population.remove(bird)
        self.birds_to_death = []

        # remove birds, which environment can't afford anymore
        def sort_by(value):
            return value.fitness
        not_survivals = sorted(self.population, key= sort_by, reverse =True)[MAX_POPULATION:]
        self.birds_to_death += [bird for bird in not_survivals if bird not in self.birds_to_death]
        if len(self.birds_to_death):
            self.azrael_turn()
        return
    
    def disease(self):
        for bird in self.population:
            rand = random.uniform(0,1)
            if rand < INFECTION_RATE:
                bird.sick_tick = 1
        for bird in self.population:
            if bird.sick_tick:
                bird.get_clean(self.population) 
        # Nature judges birds who are (sick or old) with death
        for bird in self.population:
            if bird.age >= bird.lifespan or bird.sick_tick:
                    self.birds_to_death.append(bird)

    def get_birds_fitness(self):
        fitness = []
        fitness_cheat = []
        for bird in self.population:
            if bird.genes['would_clean']:
                fitness.append(bird.fitness)
            else:
                fitness_cheat.append(bird.fitness)
        return fitness, fitness_cheat

    def ages(self):
        ages_cheat = []
        ages = []
        for bird in self.population:
            if bird.genes['would_clean']:
                ages.append(bird.age)
            else:
                ages_cheat.append(bird.age)
        return ages, ages_cheat

    def add_cheat(self, n_cheats):
        for _ in range(n_cheats):
            bird = Bird()
            bird.genes['would_clean']=0
            bird.aging()
            self.population.append(bird)