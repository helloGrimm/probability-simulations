import matplotlib.pyplot as plt
import numpy as np

def MC_simulation(n: int):
    global inside, outside

    while outside < n:
        # Generate random numbers in the range [0, 1)
        x = np.random.uniform(0.0, 1.0)
        y = np.random.uniform(0.0, 1.0)

        outside += 1  # Increment the count of points inside the square

        # Check the condition:
        # True: Add the coordinates to the circle
        # False: Add the coordinates to the square
        if (x**2 + y**2 < 1):
            x_circle.append(x)
            y_circle.append(y)

            inside += 1  # Increment the count of points inside the circle
        else: 
            x_square.append(x)
            y_square.append(y)

def graph(xC, yC, xS, yS, n):
    plt.title(f'Estimation of Pi using Monte Carlo Method, n = {n}')
    
    # Create a circle with a radius of r = 1
    ax = plt.subplot()

    # Set the boundary values for the plot
    ax.set_xlim((0, 1))
    ax.set_ylim((0, 1))
    
    # Create a scatter plot for points inside the circle
    plt.scatter(xC, yC, color='#3E8E9B', label='Points inside the circle')
    plt.scatter(xS, yS, color='#A9557E', label='Points outside the circle')
    circle = plt.Circle((0, 0), 1, fill=False, linestyle='dashed', color='#3D3939', label='Circle boundary')

    ax.add_artist(circle)

    # Automatically save the plot (optional)
    # plt.savefig('plot.png', dpi=1000, bbox_inches='tight')

    # Display the plot
    plt.legend()
    plt.show()
    

# Variables to store the number of points inside the circle {inside} and outside it {outside}
inside = 0
outside = 0

# Variables to store the x and y coordinates of points that satisfy the condition: x^2 + y^2 < 1
x_circle = []
y_circle = []

# Variables to store the x and y coordinates of points that do not satisfy the condition: x^2 + y^2 < 1
x_square = []
y_square = []

# n = 0 # Predefined value for n ~ bypass user input
n = int(input('Number of random pairs [n]: '))  # Number of random pairs ~ provided by the user

MC_simulation(n)
graph(x_circle, y_circle, x_square, y_square, n)
print(f'\nApproximation of PI: {4 * (inside / n)}\n')

# Comments in this code were generated by AI to help better understand the code.
