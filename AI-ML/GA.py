import numpy as np
import random


def restrigian(x,y, A=10):
    return A*2 + (x**2 - A * np.cos(2 * np.pi * x))+(y**2 - A * np.cos(2 * np.pi * y))

def fitness(individual):
    return restrigian(individual[0], individual[1])

def initial_population(size):
    return [(random.uniform(-3,3),random.uniform(-3,3)) for _ in range(size)]

def selection(population):
    i1, i2 = random.sample(population,2)
    if fitness(i1) > fitness(i2): return i1 
    return i2


def mutation(individual, rate = 0.1):
    if rate > random.random():
        return (
            max(-3, min(3, individual[0] + random.uniform(-0.5, 0.5))),
            max(-3, min(3, individual[1] + random.uniform(-0.5, 0.5)))
        )
    return individual

def crossover(parent1, parent2):
    
    alpha = random.random()
    child_x = alpha * parent1[0] + (1 - alpha) * parent2[0]
    child_y = alpha * parent1[1] + (1 - alpha) * parent2[1]
    return (child_x, child_y)


def genetic_algorithm(pop_size):
    initial = initial_population(pop_size)
    best = min(initial, key=fitness)
    for _ in range(100):
        new_population = []
        for _ in range(pop_size):
            parent1 = selection(initial)
            parent2 = selection(initial)
            child = crossover(parent1, parent2)
            child = mutation(child)
            new_population.append(child)
        initial = new_population
        current_best = min(initial, key=fitness)
        if fitness(current_best) < fitness(best):
            best = current_best
    return best

if __name__ == "__main__":
    best_solution = genetic_algorithm(50)
    print("Best solution:", best_solution)
    print("Fitness:", fitness(best_solution))
    