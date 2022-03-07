import numpy as np
# def solution(l):
# 	sep = [n.split(".") for n in l]
# 	sep = [s if len(s)==3 else (s+[""] if len(s)==2 else s+[""]+[""]) for s in sep]
# 	sorted_maj = sorted(sep,key=lambda x:x[0])
# 	unique_maj = list(set([s[0] for s in sorted_maj]))
# 	for val in sorted(unique_maj):
# 		print(val)
# 		rel = [x for x in sorted_maj if x[0]==val ]
# 		sorted_rel = sorted(rel, key= lambda x:x[1])
# 		print(sorted_rel)

def spec_sort(x):
	return [int(x[i]) for i in range(len(x))]

def solution(l):
	sep = [n.split(".") for n in l]
	sorted_sep = sorted(sep,key=spec_sort)
	return [".".join(x) for x in sorted_sep]

l = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
print(l)
print(solution(l))