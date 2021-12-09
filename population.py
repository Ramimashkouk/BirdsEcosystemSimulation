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
        self.fit_partners=[]
        self.birds_to_death = []
        for bird in self.population:
            if bird.age in range(1,round(MAX_LIFESPAN)): # younger thaN "MAX lifespan" generations
                self.fit_partners.append(bird)
            if bird.age >= bird.lifespan or bird.sick_tick:
                self.birds_to_death.append(bird)

    def reproduce(self):
        new_population=[]
        for _ in range(round(len(self.fit_partners)/2)): # All bird in fit_partners can reproduce, so they would love to :)
            for _ in range(2):
                while True:
                    partner1= self.select()
                    partner2= self.select()
                    if partner1 is not partner2:
                        break
                child = partner1.mate(partner2)
                child.mutate()
                new_population.append(child)
        self.population += new_population
        for bird in self.population:
            bird.aging()

    def select(self):
        idx = random.randint(0,len(self.fit_partners)-1)
        return self.fit_partners[idx]

    def azrael_turn(self):
        n_deaths = len(self.birds_to_death)
        print('Deaths', n_deaths,'\n')
        for bird in self.birds_to_death:
            self.population.remove(bird)
    
    def disease(self):
        for bird in self.population:
            rand = random.uniform(0,1)
            if rand < 0.3:
                bird.sick_tick = 1
        for bird in self.population:
            if bird.sick_tick:
                bird.get_clean(self.population) 