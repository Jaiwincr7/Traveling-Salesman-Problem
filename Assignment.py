from sys import maxsize
from itertools import permutations
V = 4 

def travellingSalesmanProblem(time, s):
	v = []  
	for i in range(V):
		if i != s:
			v.append(i)

	min_path = maxsize
	next_permutation=permutations(v)
	for i in next_permutation:
		current_pathweight = 0
		k = s
		for j in i:
			current_pathweight += time[k][j]
			k = j
		current_pathweight += time[k][s]
		min_path = min(min_path, current_pathweight)

	return min_path
	
def travellingSalesmanProblem(distance, s):
	v = []  
	for i in range(V):
		if i != s:
			v.append(i)

	min_path = maxsize
	next_permutation=permutations(v)
	for i in next_permutation:
		current_pathweight = 0
		k = s
		for j in i:
			current_pathweight += distance[k][j]
			k = j
		current_pathweight += distance[k][s]
		min_path = min(min_path, current_pathweight)
		
	return min_path
	
def travellingSalesmanProblem(distance, s):
	v = []  
	for i in range(V):
		if i != s:
			v.append(i)

	min_path = maxsize
	next_permutation=permutations(v)
	for i in next_permutation:
		current_pathweight = 0
		k = s
		for j in i:
			current_pathweight += distance[k][j]
			k = j
		current_pathweight += distance[k][s]
		min_path = min(min_path, current_pathweight)
		
	return min_path

if __name__ == "__main__":
	time = [[17, 12, 15, 20], [5,0,13,10],
			[11,12,10,12], [17,5,19,6]]
	distance=[[10, 10, 1, 20], [10, 30, 5, 25],
			[17, 33, 0, 30], [1, 20, 30, 10]]
	s = 0
	print("Minimum time travelled by the salemans is ")
	print(travellingSalesmanProblem(time, s))
	print("Distance travelled by the salemans is ")
	print(travellingSalesmanProblem(distance, s))