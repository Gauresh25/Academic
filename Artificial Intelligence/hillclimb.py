import random
import matplotlib.pyplot as plt
import numpy as np


# Define the objective function (e.g., f(x) = -x^2 + 10x)
def objective_function(x):
    return -x ** 2 + 10 * x  # A simple quadratic function


# Hill Climbing Algorithm with path tracking
def hill_climb(start_x, step_size=1, max_iterations=1000):
    current_x = start_x
    current_value = objective_function(current_x)

    # Track the path of the algorithm
    path_x = [current_x]
    path_y = [current_value]

    for _ in range(max_iterations):
        # Generate a neighbor (small random step)
        neighbor_x = current_x + random.uniform(-step_size, step_size)
        neighbor_value = objective_function(neighbor_x)

        # If the neighbor has a better value, move to that point
        if neighbor_value > current_value:
            current_x = neighbor_x
            current_value = neighbor_value

            # Track the new position
            path_x.append(current_x)
            path_y.append(current_value)
        else:
            break  # Stop if no better neighbor is found

    return current_x, current_value, path_x, path_y


# Create a function to plot the objective function and hill climbing paths
def plot_hill_climbing(attempts=10):
    # Create x values for plotting the objective function
    x_vals = range(0, 10)
    y_vals = [objective_function(x) for x in x_vals]

    # Create the plot
    plt.figure(figsize=(12, 8))

    # Plot the objective function
    plt.plot(x_vals, y_vals, 'b-', label='Objective Function')

    # Mark the global maximum
    plt.plot(5, objective_function(5), 'r*', markersize=15, label='Global Maximum')

    # Colors for different attempts
    colors = ['g', 'r', 'c', 'm', 'y', 'k', 'orange', 'purple', 'brown', 'pink']

    # Run the algorithm multiple times and plot each path
    results = []
    for i in range(attempts):
        # Generate a random starting point
        start_x = random.uniform(0, 10)

        # Run hill climbing
        best_x, best_value, path_x, path_y = hill_climb(start_x)

        # Store results
        results.append({
            'start_x': start_x,
            'best_x': best_x,
            'best_value': best_value,
            'iterations': len(path_x) - 1
        })

        # Plot the starting point
        plt.plot(start_x, objective_function(start_x), 'o', color=colors[i],
                 markersize=10, label=f'Start {i + 1}: x={start_x:.2f}')

        # Plot the path taken
        plt.plot(path_x, path_y, color=colors[i], linestyle='-', linewidth=2)

        # Plot the final point
        plt.plot(best_x, best_value, 's', color=colors[i], markersize=8)

    # Add labels and title
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Hill Climbing Optimization')
    plt.grid(True)
    plt.legend(loc='lower right')

    # Print results
    print("Hill Climbing Results:")
    print(f"{'#':<3} {'Start x':<10} {'Best x':<10} {'Best Value':<15} {'Iterations':<10} {'Distance to Optimum':<20}")
    print('-' * 70)
    for i, result in enumerate(results):
        print(
            f"{i + 1:<3} {result['start_x']:<10.4f} {result['best_x']:<10.4f} {result['best_value']:<15.4f} {result['iterations']:<10} {abs(result['best_x'] - 5):<20.4f}")

    # Show the plot
    plt.tight_layout()
    plt.show()

    return results


# Run the visualization with 10 attempts
results = plot_hill_climbing(attempts=10)

# Print the overall best result
best_result = max(results, key=lambda x: x['best_value'])
print(f"\nOverall best solution found: x = {best_result['best_x']:.4f}, f(x) = {best_result['best_value']:.4f}")