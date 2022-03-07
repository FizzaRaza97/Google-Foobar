import numpy as np
from fractions import Fraction
def correct(x):
	x = np.array(x)
	for j in range(len(x)):
		for i in range(len(x)-1,0,-1):
			if (~x[i-1].any()) and (x[i].any()):
				x[[i-1, i], :] = x[[i, i-1], :]
				x[:, [i-1, i]] = x[:, [i, i-1]] 
	return x

def solution(m):
	fnl= ~np.array(m[0]).any() #Start at terminal?
	
	m = correct(m)
	is_zero = np.array(m).any(axis=1)
	count_nonterm = np.sum(is_zero)
	term = [ i for i,b in enumerate(is_zero) if b==False]
    
	if fnl: 
		term[0] = 1
		term[1:] = [0]*(len(term)-1)
		term.append(1)
		return term

	for t in term:
		m[t][t] = 1

	m = np.array([[float(i) for i in x] for x in m])
	row_sums = m.sum(axis=1)
	m = m/np.array(row_sums[:,np.newaxis])

	Q = m[:term[0],:term[0]]
	R = m[:term[0],term[0]:]
	I_Q = np.eye(term[0])-Q
	N = np.linalg.inv(I_Q)
	B = np.dot(N,R)[0]
	#total = B.sum()
	nums = [Fraction(b).limit_denominator().numerator for b in B]
	dens = [Fraction(b).limit_denominator().denominator for b in B]
	den = np.lcm.reduce(dens)
	nums = [int((n*den)/dens[i]) for i,n in enumerate(nums)]
	nums.append(den)
	return nums



# x = [
#   [0,1,0,0,0,1,0,0,0,0],  # s0, the initial state, goes to s1 and s5 with equal probability
#   [4,0,0,3,2,0,0,0,0,0],  # s1 can become s0, s3, or s4, but with different probabilities
#   [0,0,0,0,0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
#   [0,0,0,0,0,0,0,0,0,0],  # s3 is terminal
#   [0,0,0,0,0,0,0,0,0,0],  # s4 is terminal
#   [0,0,0,0,0,0,0,0,0,0],  # s5 is terminal
#   [0,0,0,0,0,0,0,0,0,0],
#   [0,0,0,0,0,0,0,0,0,0],
#   [0,0,0,0,0,0,0,0,0,0],
#   [0,0,0,0,0,0,0,0,0,0]
# ]
#x = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]
#x = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]
#x = [[0, 2, 1], [0, 3, 4], [0, 0, 0]]
#x = [[0]]
#print(correct(x))
x = [[0, 0, 4, 5, 0, 1], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],  [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
# x =  [
#             [0, 1, 0, 0, 0, 1],
#             [4, 0, 0, 3, 2, 0],
#             [0, 0, 0, 0, 0, 0],
#             [1, 2, 0, 4, 0, 6],
#             [0, 0, 2, 0, 0, 3],
#             [0, 0, 1, 0, 0, 0]
#         ]

# x = [
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     ]
# ans = [1, 1, 1, 1, 1, 5]

# print(correct(x))
# print(ans)
x = [
        [1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
print(solution(x))

# assert (
#     solution([
#         [1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     ]) == [2, 1, 1, 1, 1, 6]
# )
# print("Assertion 8 passed")
