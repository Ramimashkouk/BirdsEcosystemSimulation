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
        
        birds_fitness = np.array([bird.fitness for bird in self.fit_partners])**3
        self.max_fitness = birds_fitness.max()
        fitness_sum = birds_fitness.sum()
        self.probabilities = birds_fitness / fitness_sum

    def reproduce(self):
        new_population=[]
        # The change in reproduction method, from mating to copying one itself, was inivitable as a new 
        # gene "have_memory" entered on the scene. Having two genes in the mating pool means that mating 
        # birds of different types would very probably reproduce a bird of yet another type. and as we care 
        # here about which type dominants the group, we don't have to take such a risk of randomness.
        for _ in range(round(len(self.fit_partners))): # All bird in fit_partners can reproduce, so they would love to :)
            partner1= self.select()
            partner2= partner1
            for _ in range(1): # Get one copy of itself
                child = partner1.mate(partner2)
                child.mutate()
                child.determine_type()
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
        
    def get_birds_attribute(self, attribute):
        suckers = []
        cheats = []
        grudgers = []
        for bird in self.population:
            if bird.type == 'sucker':
                suckers.append(vars(bird)[attribute])
            elif bird.type == 'cheat':
                cheats.append(vars(bird)[attribute])
            elif bird.type == 'grudger':
                grudgers.append(vars(bird)[attribute])
        return suckers, cheats, grudgers


    def add_bird(self, type):
        bird = Bird()
        bird.give_type(type)
        bird.aging()
        self.population.append(bird)