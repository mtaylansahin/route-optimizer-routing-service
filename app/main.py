import pathlib
from fastapi import FastAPI
from pydantic import BaseModel

from tsp_solver.greedy import solve_tsp
from tsp_solver.utils import path_cost
from tsp_solver.ga_solver import GeneticTSP
from typing import List

app = FastAPI()

BASE_DIR = pathlib.Path(__file__).resolve().parent




class Item(BaseModel):
    num_nodes: int
    distances: List[List[int]]

@app.on_event('startup')
def on_startup():
    pass

@app.post("/greedy")
def read_index(item: Item):
    greedy_path = solve_tsp(item.distances)
    greedy_dist = path_cost(item.distances, greedy_path)
    return {'path':greedy_path, 'distance':greedy_dist}

@app.post("/genetic")
def read_index(item: Item):
    ga = GeneticTSP(N=item.num_nodes, distances=item.distances)
    
    ga_path = [int(val) for val in ga.fittest]
    ga_dist = ga.best_fitness
    
    return {'path':ga_path, 'distance':ga_dist}