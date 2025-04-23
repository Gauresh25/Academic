import random

# Function to optimize
def objective_function(x):
    return -(x - 3) ** 2 + 10  # Maximum at x = 3

# Genetic Algorithm with user input
def genetic_algorithm():
    population_size = int(input("Enter population size: "))
    generations = int(input("Enter number of generations: "))
    mutation_rate = float(input("Enter mutation rate (0-1): "))

    # Initialize population with random values
    population = [random.uniform(-10, 10) for _ in range(population_size)]

    for _ in range(generations):
        population.sort(key=objective_function, reverse=True)  # Sort by fitness
        new_population = population[:population_size // 2]     # Select top half

        # Crossover (generate offspring)
        for _ in range(population_size // 2):
            p1, p2 = random.sample(new_population, 2)
            offspring = (p1 + p2) / 2  # Simple average crossover
            if random.random() < mutation_rate:
                offspring += random.uniform(-0.5, 0.5)  # Mutation
            new_population.append(offspring)

        population = new_population  # Update population

    best_x = max(population, key=objective_function)
    print(f"Genetic Algorithm Best Solution: x = {best_x:.4f}, f(x) = {objective_function(best_x):.4f}")