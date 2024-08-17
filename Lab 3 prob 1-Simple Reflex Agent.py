# Consider an interactive and cognitive environment (ICE) in which a smart camera is
# monitoring robot movement from one location to another. Let a robot be at location A for
# some time instant and then moves to point B and eventually reaches at point C and so on
# and so forth shown in the Fig. Develop a Python code to calculate a distance between
# reference point R (4, 0) of a camera and A, B, and C and N number of locations.

import numpy as np
import random as r
import math

def distance(pos, x2, y2):
    """Calculate Euclidean distance between a reference point and another point."""
    return math.sqrt((pos[0] - x2)**2 + (pos[1] - y2)**2)

def main():
    n = int(input("Enter the number of locations: "))
    if n > 16 or n < 5:
        print("Number of locations must be at least 5 and not greater than 16.")
        return

    # Initialize the environment with empty strings
    env = np.full((n, n), '', dtype=str)
    
    # Place the reference point R
    env[4][0] = 'R'
    
    robo_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
    
    # Randomly place robots
    j = 0
    while j < n:
        x = r.randint(0, n-1)
        y = r.randint(0, n-1)
        if env[x][y] == '':
            env[x][y] = robo_names[j]
            j += 1

    print(env)
    
    r_position = [4, 0]
    res = []
    
    # Calculate distances
    for i in range(n):
        for j in range(n):
            if env[i][j] in robo_names:
                res.append(distance(r_position, i, j))
    
    print("\nEuclidean Distance from reference point R to all given robots: ", res)

if __name__ == "__main__":
    main()
