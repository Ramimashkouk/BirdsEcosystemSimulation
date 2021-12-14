# BirdsEcosystemSimulation
## Based on genetic algorithm
*This project is built upon an idea from **The Selfish Gene** book by **Richard Dawkins**.
It's a simulation of an evolutionary ecosystem of birds of the same kind, which differ from each other in some different genes responsible for the reply of help-asking.
I wouldn't explain the ecosystem better than Richard Dawkins would do the system, so here's the problem introduction, quoting the text in his book:*

>"Suppose B has a parasite on the top of his head.A pulls it off him. Later, the time comes when A has a parasite on his head. He naturally seeks out B in order that B may pay back his good deed. B simply turns up his nose and walks off. B is a cheat, an individual who accepts the benefit of other individuals' altruism, but who does not pay it back, or who pays it back insufficiently. Cheats do better than indiscriminate altruists because they gain the benefits without paving the costs. To be sure, the cost of grooming another individual's head seems small compared with the benefit of having a dangerous parasite removed, but it is not negligible. Some valuable energy and time has to be spent. Let the population consist of individuals who adopt one of two strategies. As in Maynard Smith's analyses, we are not talking about conscious strategies, but about unconscious behaviour programs laid down by genes. Call the two strategies Sucker and Cheat. Suckers groom anybody who needs it, indiscriminately. Cheats accept altruism from suckers, but they never groom anybody else, not even somebody who has previously groomed them." 

*I encourage you now to have a look at the animation below, trying to know what is going on in the ecosystem, before continuing to the ecosystem explanation, following*

>"If the incidence of parasites is high, any individual sucker in a population of suckers can reckon on being groomed about as often as he grooms. The average pay-off for a sucker among suckers is therefore positive. They all do quite nicely in fact, and the word sucker seems inappropriate. But now suppose a cheat arises in the population. Being the only cheat, he can count on being groomed by everybody else, but he pays nothing in return. His average pay-off is better than the average for a sucker. Cheat genes will therefore start to spread through the population. Sucker genes will soon be driven to extinction. This is because, no matter what the ratio in the population, cheats will always do better than suckers. When the proportion of cheats reaches 90 per cent, the average pay-off for all individuals will be very low: many of both types may by now be dying of the infection carried by the ticks. But still the cheats will be doing better than the suckers. Even if the whole population declines toward extinction, there will never be any time when suckers do better than cheats. Therefore, as long as we consider only these two strategies, nothing can stop the extinction of the suckers and, very probably, the extinction of the whole population too."

*Playing around with parameters like INFECTION_RATE, MUTATION_RATE, INIT_SUCKER, N_CHEATS (init_cheats) would surprise you how ecosystem can be affected by small differences in nature's values.*



[animation](results/animation1.gif) example, using the following parameters:<br />
INFECTION_RATE = 0.42, MUTATION_RATE = 0.009


