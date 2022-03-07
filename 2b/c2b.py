import numpy as np

def solution(total_lambs):
	gen=1
	stingy = 1
	if (total_lambs>1):
	    gen = int(np.log2(total_lambs+1))
	    stingy = 2 #Assume more total_lambs>=2
	    fib = [1,1]
	    total_lambs-=2
	    while total_lambs>0:
			tmp = fib[0]+fib[1]
			fib[0] = fib[1]
			fib[1] = tmp
			total_lambs-=tmp
			if total_lambs<0:
				break
			stingy+=1
	
	return (stingy,gen)
print(solution(7))
print(solution(143))