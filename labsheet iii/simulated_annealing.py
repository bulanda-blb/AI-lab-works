import math
import random

class SimulatedAnnealing:
    def __init__(self, initial_temperature, cooling_rate):
        self.temperature = initial_temperature
        self.cooling_rate = cooling_rate

    def probability_of_acceptance(self, delta_energy):
        # Calculate the probability of accepting a worse solution
        if delta_energy < 0:
            return 1.0  # Always accept if the new solution is better
        return math.exp(-delta_energy / self.temperature)

    def anneal(self, initial_state, cost_function, neighbor_function):
        current_state = initial_state
        current_cost = cost_function(current_state)

        while self.temperature > 1e-3:  # Stop when temperature is close to zero
            # Generate a neighbor state
            new_state = neighbor_function(current_state)
            new_cost = cost_function(new_state)
            delta_energy = new_cost - current_cost

            # Accept or reject the new state
            if random.random() < self.probability_of_acceptance(delta_energy):
                current_state = new_state
                current_cost = new_cost

            # Reduce the temperature
            self.temperature *= self.cooling_rate

        return current_state, current_cost

# Example: Optimization of a simple function
def cost_function(x):
    # A simple quadratic function with a global minimum at x = 0
    return x**2

def neighbor_function(x):
    # Generate a new state by adding a small random value
    return x + random.uniform(-1, 1)

# Initial parameters
initial_temperature = 100
cooling_rate = 0.95
initial_state = 10  # Start far from the minimum

# Run Simulated Annealing
sa = SimulatedAnnealing(initial_temperature, cooling_rate)
final_state, final_cost = sa.anneal(initial_state, cost_function, neighbor_function)

# Print results
print(f"Final State: {final_state}")
print(f"Final Cost: {final_cost}")
