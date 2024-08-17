# Given a set of cities and distances between every pair of cities, the problem is to
# find the shortest possible route that visits every city exactly once and returns to the
# starting point. Like any problem, which can be optimized, there must be a cost
# function. In the context of TSP, total distance traveled must be reduced as much as possible.

# Consider the below matrix representing the distances (Cost) between the cities.
# Find theshortest possible route that visits every city exactly once and returns to the starting point.

import itertools

distances = {
    ('A', 'B'): 20,
    ('A', 'C'): 42,
    ('A', 'D'): 35,
    ('B', 'A'): 20,
    ('B', 'C'): 30,
    ('B', 'D'): 34,
    ('C', 'A'): 42,
    ('C', 'B'): 30,
    ('C', 'D'): 12,
    ('D', 'A'): 35,
    ('D', 'B'): 34,
    ('D', 'C'): 12,
}

city = ['A', 'B', 'C', 'D']

shortest_route = None
shortest_distance = float('inf')

# Generate all permutations of the points
permutations = itertools.permutations(city)

for perm in permutations:

    total_distance = 0

    for i in range(len(perm) - 1):
        total_distance += distances[(perm[i], perm[i + 1])]

    # Add the distance from the last point back to the starting point
    total_distance += distances[(perm[-1], perm[0])]

    if total_distance < shortest_distance:
        shortest_distance = total_distance
        shortest_route = perm

print("Shortest Route:", shortest_route)
print("Shortest Distance:", shortest_distance)

