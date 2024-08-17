# Implement genetic algorithm to the Traveling Salesman Problem.
# We have a set of four cities A, B, C, and D. The distances
# between the cities are also given to us. Here (4-1)! That is 3!
# Route can be generated. The tour with A B C D A will be
# the optimal route for given problem.

# cities = ['A', 'B', 'C', 'D']
# distances = {
#     ('A', 'B'): 3, ('A', 'C'): 6, ('A', 'D'): 2,
#     ('B', 'A'): 3, ('B', 'C'): 4, ('B', 'D'): 7,
#     ('C', 'A'): 6, ('C', 'B'): 4, ('C', 'D'): 4,
#     ('D', 'A'): 2, ('D', 'B'): 3, ('D', 'C'): 4
# }

# Pseudo code
# Initial Population (set of solutions) = 6
# Fitness (Quality of solution) = each solution is generally represented as a string of binary
# numbers, known as a chromosome. The most common fitness function for Travel Salesman Problem is the lengthnof the route. However, the 'shorter' the route is - the better.
# Crossover point, exchange data after ‘1’ instances of the list. Mutation point perform between 2nd and 4th item.
# The pseudo code for genetic algorithm for implementing the Traveling salesman problem:

# GeneticAlgorithm ( )
# {
#   Initialize population of routes of cities randomly with a function Random ( ) Evaluate the
#   fitness of each individual route using function Fitness ( )
#   While the fitness criteria is not satisfied do
#   {
#      Selection of two routes for reproduction using select function (Select (parent_route1, parent_route2))
#      Perform crossover on the selected parent routes with crossover function (child_route = Crossover (parent_route1, parent_route2))
#      Perform mutation on the newly generated child routes with mutation function (Mutation(child_route))
#      Evaluate the fitness of child_route and replace the parent population with child_route
#    }
# }


import random

# Cities and distances
cities = ['A', 'B', 'C', 'D']
distances = {
    ('A', 'B'): 3, ('A', 'C'): 6, ('A', 'D'): 2,
    ('B', 'A'): 3, ('B', 'C'): 4, ('B', 'D'): 7,
    ('C', 'A'): 6, ('C', 'B'): 4, ('C', 'D'): 4,
    ('D', 'A'): 2, ('D', 'B'): 3, ('D', 'C'): 4
}

# Function to calculate the total distance of a route
def calculate_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distances[(route[i], route[i + 1])]
    total_distance += distances[(route[-1], route[0])]  # Return to start
    return total_distance

# Generate a population (a list of routes)
def generate_population(size):
    population = []
    for _ in range(size):
        route = cities[:]  # Copy the cities list
        random.shuffle(route)  # Shuffle to create a random route
        population.append(route)
    return population

# Evaluate fitness of a route (shorter distance is better)
def evaluate_fitness(route):
    return 1 / calculate_distance(route)

# Select a route based on fitness (Roulette-wheel selection)
def select_route(population, fitness_scores):
    total_fitness = sum(fitness_scores)
    pick = random.uniform(0, total_fitness)
    current = 0
    for i, fitness in enumerate(fitness_scores):
        current += fitness
        if current > pick:
            return population[i]

# Perform crossover between two parent routes
def crossover(parent1, parent2):
    crossover_point = 1  # Fixed crossover point (after the first city)
    child = parent1[:crossover_point]
    for city in parent2:
        if city not in child:
            child.append(city)
    return child

# Perform mutation by swapping two cities
def mutate(route):
    idx1, idx2 = random.sample(range(1, len(route)), 2)
    route[idx1], route[idx2] = route[idx2], route[idx1]
    return route

# Main function to run the Genetic Algorithm
def genetic_algorithm(pop_size=6, generations=100):
    population = generate_population(pop_size)
    
    for generation in range(generations):
        # Step 1: Calculate fitness of each route
        fitness_scores = [evaluate_fitness(route) for route in population]
        
        # Get the best route in the current generation
        best_route = population[fitness_scores.index(max(fitness_scores))]
        best_distance = calculate_distance(best_route)
        
        # Print the generation, best route, and its distance
        print(f"Generation {generation + 1}: Best Route = {best_route}, Distance = {best_distance}")
        
        # Check if we've found the optimal solution
        if best_distance == 14:  # Optimal distance for this problem is 14
            break
        
        # Step 2: Create a new population
        new_population = []
        for _ in range(pop_size // 2):
            parent1 = select_route(population, fitness_scores)
            parent2 = select_route(population, fitness_scores)
            child1 = mutate(crossover(parent1, parent2))
            child2 = mutate(crossover(parent2, parent1))
            new_population.extend([child1, child2])
        
        # Replace old population with new one
        population = new_population

    # Return the best route found
    return best_route, best_distance

# Run the algorithm and output all generations
best_route, best_distance = genetic_algorithm()
print("\nFinal Optimal Route:", best_route)
print("Final Optimal Distance:", best_distance)
