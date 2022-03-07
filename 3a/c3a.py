import numpy as np

def getCount(val,l):
	return [i for i in range(len(l)) if val%l[i]==0]


def solution(l):
    if len(l)==2:
    	return 0
    memo = {i:getCount(l[i],l[:i]) for i in range(len(l))}
    count = 0
    for i in range(len(l)-1,-1,-1):
    	count+=np.sum([len(memo[x]) for x in memo[i]])
    return int(count)

solution([1, 2, 3, 4, 5, 6])
solution([1,1,1])    