def solution(m):
	w = len(m[0])
	h = len(m)
	return getSol(m,0,0,w-1,h-1,1)

def getNeighbours(m,i,j,dst_i,dst_j,budget):
	neighbours = []
	if (i>=0) and (i<dst_i): # can move east
		if m[j][i+1] == 0:
			neighbours.append((i+1,j,budget))
		elif budget>0:
			neighbours.append((i+1,j,budget-1))
	if i>=1: #can move west
		if m[j][i-1] == 0:
			neighbours.append((i-1,j,budget))
		elif budget>0:
			neighbours.append((i-1,j,budget-1))
	if (j>=0) and (j<dst_j): #can move south
		if m[j+1][i] == 0:
			neighbours.append((i,j+1,budget))
		elif budget>0:
			neighbours.append((i,j+1,budget-1))
	if j>=1:
		if m[j-1][i]==0:
			neighbours.append((i,j-1,budget))
		elif budget>0:
			neighbours.append((i,j-1,budget-1))
	return neighbours



def getSol(m,i,j,dst_i,dst_j,budget):
	memo = {}
	src = (i,j,budget)
	queue = [src]
	memo[src] = 1
	while len(queue)>0:
		curr = queue[0]
		queue = queue[1:]
		neighbours = getNeighbours(m,curr[0],curr[1],dst_i,dst_j,curr[2])
		for x,y,b in neighbours:
			if x==dst_i and y==dst_j:
				memo[(x,y,b)] = 1+memo[curr]
				return memo[(x,y,b)]
			if (x,y,b) not in memo.keys():
				queue.append((x,y,b))
				memo[(x,y,b)] = 1+memo[curr]
	return None

x = [[0, 1, 1, 0, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0]] 
x = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
x = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
print(solution(x))