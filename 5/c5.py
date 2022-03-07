import math # for factorial
import numpy as np # for np.lcm
from collections import Counter
from fractions import Fraction

# http://jeromekelleher.net/generating-integer-partitions.html
def accel_asc(n):
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1]   


def getCycleIndices(n):
	J = accel_asc(n)
	cycles = []
	for part in J:
		comps = {"sub":[],"super":[]}
		j = Counter(part)
		coef = 1
		for key in j:
			comps["sub"].append(key)
			comps["super"].append(j[key])
			coef *= (key**j[key])*(math.factorial(j[key]))
		comps["coef"] = Fraction(1,coef)
		cycles.append(comps)
	return cycles


def combineCycles(row,col):
	subs_r = row["sub"]
	sups_r = row["super"]
	subs_c = col["sub"]
	sups_c = col["super"]
	res = []
	for i in range(len(subs_r)):
		for j in range(len(subs_c)):
			sub = np.lcm.reduce([subs_r[i],subs_c[j]])
			sup = int(subs_r[i]*sups_r[i]*subs_c[j]*sups_c[j]/sub)
			res.append((sub,sup))
	return sorted(res)

def printArray(x):
	x = sorted(x)
	for x_i in x:
		print(x_i)

def solution(w, h, s):
	row_cycle_index = getCycleIndices(h) #return list of dictionaries of the type: {coef:.., subs:[..], supers:[..]}
	#print(row_cycle_index)
	col_cycle_index = getCycleIndices(w)
	all_cycs = []
	num_unique = 0
	for row_cycle in row_cycle_index:
		for col_cycle in col_cycle_index:
			coef_comb = row_cycle["coef"]*col_cycle["coef"]
			cycle_index_comb = combineCycles(row_cycle,col_cycle) # returns [(sub,super),..]
			all_cycs.append(cycle_index_comb+[coef_comb])
			#print(cycle_index_comb)
			value = 1
			for _, power in cycle_index_comb:
				value *= s ** power
			num_unique+=coef_comb*value #prod_comb
	#printArray(all_cycs)
	return str(int(num_unique))


if __name__ == '__main__':
	#1,5624,64796982,79846389608,20834113243925,1979525296377132,93242242505023122,2625154125717590496,
	w = 5
	h = 7
	s = 8
	print(solution(w,h,s))