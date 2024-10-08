# Given a target string, the goal is to produce target string starting from a random string of the
# same length. In the following implementation, following analogies are made:
# •Characters A-Z, a-z, 0-9 and other special symbols are considered as genes
# •A string generated by these character is considered as chromosome/solution/Individual
# Population size= 70
# •Target string to be generated: TARGET = "Artificial Intelligence Lab"
# •Fitness score is the number of characters which differ from characters in target string at a
# particular index. So, individual having lower fitness value is given more preference.


import random
import string

TARGET = "Artificial Intelligence Lab"
POPULATION_SIZE = 70
MUTATION_RATE = 0.01
GENERATIONS = 1000

def random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation + ' ') for _ in range(length))

def fitness(individual):
    return sum(1 for a, b in zip(individual, TARGET) if a != b)

def crossover(p1, p2):
    idx = random.randint(0, len(p1) - 1)
    return p1[:idx] + p2[idx:]

def mutate(individual):
    return ''.join(c if random.random() > MUTATION_RATE else random.choice(string.ascii_letters + string.digits + string.punctuation + ' ') for c in individual)

def genetic_algorithm():
    population = [random_string(len(TARGET)) for _ in range(POPULATION_SIZE)]

    for generation in range(GENERATIONS):
        fitness_scores = [fitness(ind) for ind in population]
        best_index = fitness_scores.index(min(fitness_scores))
        best_individual = population[best_index]

        print(f"Generation {generation + 1}: Best fitness = {fitness_scores[best_index]}")
        print(f"Best individual: {best_individual}")

        if fitness_scores[best_index] == 0:
            print("Target string reached!")
            break

        selected = [population[i] for i in sorted(range(len(fitness_scores)), key=lambda i: fitness_scores[i])[:int(0.3 * POPULATION_SIZE)]]
        population = [mutate(crossover(random.choice(selected), random.choice(selected))) for _ in range(POPULATION_SIZE)]

    print(f"Final best individual: {best_individual}")
    print(f"Final best fitness: {fitness_scores[best_index]}")

genetic_algorithm()

