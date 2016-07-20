import time
from copy import deepcopy
def generate_univers(alive_cells):
	uni = [[0] * size for i in range(size)]
	for i in range(size):
		for j in range(size):
			if (i,j) in alive_cells: uni[i][j] = 1
			else: uni[i][j] = 0
	return uni

def get_univers(step):
	for i in range(size):
		print(step[i])

def get_neighbors(cell):
	neigh_for_cells = set()
	for neighor in neighors:
		x = (size + int(neighor[0]) + int(cell[0]))%size
		y = (size + int(neighor[1]) + int(cell[1]))%size
		neigh_for_cells.add((x,y))	
	return neigh_for_cells

def col_alive_neighbors(cell, alive_cells):
	return len(alive_cells.intersection(get_neighbors(cell)))

def get_new_alive_cells(alive_cells):
	alive_list = list(alive_cells)
	new_alive_cells = set()
	for i in range(len(alive_cells)):
		for j in range(i+1, len(alive_cells)):
			for k in range(j+1, len(alive_cells)):
				ineib = get_neighbors(alive_list[i])
				new_alive_cells = new_alive_cells.union(ineib.intersection(get_neighbors(alive_list[j]), get_neighbors(alive_list[k])))
	return new_alive_cells
					
def alive_rules(alive_cells):
	next_alive_cells = deepcopy(alive_cells)
	next_alive_cells = next_alive_cells.union(get_new_alive_cells(alive_cells))
	for cell in set(next_alive_cells):
		if col_alive_neighbors(cell,alive_cells) < 2 or col_alive_neighbors(cell, alive_cells) > 3: next_alive_cells.discard(cell)	
	return next_alive_cells	

def univers_simulation(generation, col_iter):
	for i in range(col_iter):
		print('\n')
		get_univers(generate_univers(generation))
		generation = alive_rules(generation)		
		time.sleep(1)

size = 10
neighors = set([(-1, -1),(-1, 0),(-1, 1),(0,1),(1, 0),(1, 1),(0, -1),(1, -1)])
first_generation = set([(0, 2),(1, 2),(2, 2),(1, 0),(2, 1)])
col_iter = 3
univers_simulation(first_generation, col_iter)





	










