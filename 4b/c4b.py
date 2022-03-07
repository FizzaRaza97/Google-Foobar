import numpy as np

def bfs(src,dst,graph): 
	#returns if there is a path and if so, the nodes (indices) on that path, min flow on those nodes
	# graph is a numpy array now!
	src = src[0]
	dst = dst[0]
	path = []
	visited = [0 for i in range(len(graph))]
	queue = [(src,[])]
	visited[src] = 1
	res_path = []
	while len(queue)>0:
		curr = queue[0][0]
		curr_path = queue[0][1]+ [curr]
		if curr == dst:
			res_path = curr_path
		queue = queue[1:]
		
		for ind,node in enumerate(graph[curr]):
			if (not visited[ind]) and (node > 0):
				visited[ind] = 1
				queue.append((ind,curr_path))

	if visited[dst]:
		res_row = []
		res_col = []
		for i in range(len(res_path)-1):
			res_row.append(res_path[i])
			res_col.append(res_path[i+1])

		min_flow = np.min(graph[res_row,res_col])

		return visited[dst],[res_row,res_col],min_flow
	return 0,[[],[]],-1

def fordfulkerson(entrances,exits,path):
	max_flow = 0
	residual_graph = np.copy(path)
	search_path = bfs(entrances,exits,residual_graph)
	is_path = search_path[0]
	while is_path:
		min_flow = search_path[2]
		max_flow+=min_flow
		residual_graph[search_path[1][0],search_path[1][1]]-=min_flow
		residual_graph[search_path[1][1],search_path[1][0]]+=min_flow
		search_path = bfs(entrances,exits,residual_graph)
		is_path = search_path[0]
	return int(max_flow)


def solution(entrances, exits, path):
	INF = float("inf")
	if (len(entrances) > 1):
		new_src_row = [INF if node in entrances else 0 for node in range(len(path))]
		path.append(new_src_row)
		for row in range(len(path)):
			path[row].append(0)
		entrances = [len(path)-1]
	if (len(exits)>1):
		new_dst_row = [0 for node in range(len(path))]
		path.append(new_dst_row)
		for row in range(len(path)):
			if row in exits:
				path[row].append(INF)
			else:
				path[row].append(0)
		exits = [len(path)-1]
	return fordfulkerson(entrances,exits,path)

def main():
	entrances = [0, 1]
	exits = [4, 5]
	path = [
		  [0, 0, 4, 6, 0, 0],  # Room 0: Bunnies
		  [0, 0, 5, 2, 0, 0],  # Room 1: Bunnies
		  [0, 0, 0, 0, 4, 4],  # Room 2: Intermediate room
		  [0, 0, 0, 0, 6, 6],  # Room 3: Intermediate room
		  [0, 0, 0, 0, 0, 0],  # Room 4: Escape pods
		  [0, 0, 0, 0, 0, 0],  # Room 5: Escape pods
		]

	# entrances = [0]
	# exits = [3]
	# path = [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]

	print(solution(entrances,exits,path))

if __name__=="__main__":
	main()