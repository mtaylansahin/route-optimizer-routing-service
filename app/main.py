import pathlib
from turtle import distance
from fastapi import FastAPI
from pydantic import BaseModel

from tsp_solver.greedy import solve_tsp
from tsp_solver.utils import path_cost
from tsp_solver.utils import create_distance_matrix
from tsp_solver.ga_solver import GeneticTSP
from typing import List, Dict

app = FastAPI()

BASE_DIR = pathlib.Path(__file__).resolve().parent




class Item(BaseModel):
    num_nodes: int
    coordinates: List[Dict[str, int]]

@app.on_event('startup')
def on_startup():
    pass

@app.post("/greedy")
def read_index(item: Item):
    distances = create_distance_matrix(item.coordinates)
    greedy_path = solve_tsp(distances)
    greedy_dist = path_cost(distances, greedy_path)
    return {'path':greedy_path, 'distance':greedy_dist}

@app.post("/genetic")
def read_index(item: Item):
    distances = create_distance_matrix(item.coordinates)
    ga = GeneticTSP(N=item.num_nodes, distances=distances)
    
    ga_path = [int(val) for val in ga.fittest]
    ga_dist = ga.best_fitness
    
    return {'path':ga_path, 'distance':ga_dist}