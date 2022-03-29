from greedy import solve_tsp
from ga_solver import GeneticTSP
from utils import initialize_problem_space, path_cost

N = 50
distances = initialize_problem_space(N)
print(distances)
greedy_path = solve_tsp(distances)
print(path_cost(distances, greedy_path))
print('*************************')
ga = GeneticTSP(N=N, distances=distances)
print(ga.best_fitness, ga.fittest)
'''
0   14  14  16  17
14  0   11  17  5
14  11  0   19  11   
16  17  19  0   4
17  5   11  4   0
'''
