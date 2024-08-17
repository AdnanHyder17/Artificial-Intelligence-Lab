# Implement genetic algorithm to the Traveling Salesman Problem.
# We have a set of four cities A, B, C, and D. The distances
# between the cities are also given to us. Here (4-1)! That is 3!
# Route can be generated. The tour with A B C D A will be
# the optimal route for given problem.


import random

# Define the cities and their distances
cities = ['A', 'B', 'C', 'D']
distances = {
    ('A', 'B'): 3, ('A', 'C'): 6, ('A', 'D'): 2,
    ('B', 'A'): 3, ('B', 'C'): 4, ('B', 'D'): 7,
    ('C', 'A'): 6, ('C', 'B'): 4, ('C', 'D'): 4,
    ('D', 'A'): 2, ('D', 'B'): 3, ('D', 'C'): 4
}

# Initialize population of routes randomly
def generate_random_route():
    return random.sample(cities, len(cities))

def generate_initial_population(population_size):
    return [generate_random_route() for _ in range(population_size)]

# Calculate the fitness of a route (length of the route)
def calculate_fitness(route):
    total_distance = sum(distances[(route[i], route[i + 1])] for i in range(len(route) - 1))
    total_distance += distances[(route[-1], route[0])]  # Return to the starting city
    return total_distance

# Select two parent routes for reproduction
def select(population):
    return random.choices(population, k=2, weights=[1/calculate_fitness(route) for route in population])

# Perform crossover on parent routes
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child = parent1[:crossover_point]
    for city in parent2:
        if city not in child:
            child.append(city)
    return child

# Perform mutation on child routes
def mutate(route):
    mutation_point1 = random.randint(1, len(route) - 1)
    mutation_point2 = random.randint(1, len(route) - 1)
    route[mutation_point1], route[mutation_point2] = route[mutation_point2], route[mutation_point1]

# Genetic Algorithm
def genetic_algorithm(population_size, generations):
    population = generate_initial_population(population_size)
    for gen in range(generations):
        print("Generation", gen + 1)
        new_population = []
        for _ in range(population_size):
            parent1, parent2 = select(population)
            child = crossover(parent1, parent2)
            if random.random() < 0.1:  # Mutation rate
                mutate(child)
            new_population.append(child)
        population = new_population
        # Display the best route in this generation
        best_route = min(population, key=calculate_fitness)
        print("Best route:", best_route, "Distance:", calculate_fitness(best_route))
    return min(population, key=calculate_fitness)

# usage
if __name__ == "__main__":
    optimal_route = genetic_algorithm(population_size=6, generations=100)
    print("\nOptimal route:", optimal_route)
    print("Optimal distance:", calculate_fitness(optimal_route))
