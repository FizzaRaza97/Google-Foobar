import numpy as np

def euclidean(pt1,pt2):
    pt1 = np.array(pt1)
    pt2 = np.array(pt2)
    return np.linalg.norm(pt1-pt2)

def unitVec(vec,origin):
	if vec==origin:
		return[(0,0),0]
	vec = np.array(vec)-np.array(origin)
	dist = np.linalg.norm(vec)
	return (tuple(np.round(vec/dist,10)),dist)

def getReflections(dimensions,position,distance,origin):
	rows = distance / dimensions[1] + 3
	print rows
	cols = distance / dimensions[0] + 3
	print cols
	refs = {}
	for row in range(-rows, rows):
		for col in range(-cols, cols):
			# Guard
			coord1 = dimensions[0]*(col)+((dimensions[0]-position[0]) if col%2==1 else position[0])
			coord2 = dimensions[1]*(row)+((dimensions[1]-position[1]) if row%2==1 else position[1])
			point = [coord1, coord2]
			unit_point, dist = unitVec(point,origin) #unit vector, distance of vector from captain to guard (reflection)
			if unit_point in refs:
				if refs[unit_point]["dist"] > dist:
					refs[unit_point] = {"shoot":1, "vec": point, "dist":dist}
			else:
				if dist <= distance:
					refs[unit_point] = {"shoot":1, "vec": point, "dist":dist}

			coord1 = dimensions[0]*(col)+((dimensions[0]-origin[0]) if col%2==1 else origin[0])
			coord2 = dimensions[1]*(row)+((dimensions[1]-origin[1]) if row%2==1 else origin[1])
			point = [coord1, coord2]
			unit_point, dist = unitVec(point,origin) #unit vector, distance of vector from captain to own reflection
			if unit_point in refs:
				if refs[unit_point]["dist"] > dist:
					refs[unit_point] = {"shoot":0, "vec": point, "dist":dist}
			else:
				if dist <= distance:
					refs[unit_point] = {"shoot":0, "vec": point, "dist":dist}
	return(len([k for k in refs.keys() if refs[k]["shoot"]==1]))

  

def solution(dimensions, your_position, guard_position, distance):
	if euclidean(guard_position,your_position) > distance:
		return 0
	return getReflections(dimensions,guard_position,distance,your_position)

def main():

	# dimensions = [3,2]
	# captain_position=[1,1]
	# badguy_position = [2,1]
	# dist = 4

	# dimensions = [300,275]
	# captain_position = [150,150]
	# badguy_position = [185,100]
	# dist = 500

	# dimensions = [23,10]
	# captain_position = [6, 4]
	# badguy_position = [3,2]
	# dist = 23

	dimensions = [10,10]
	captain_position = [4, 4]
	badguy_position = [3,3]
	dist = 5000
	#ans == 739323

	# dimensions = [2,5]
	# captain_position = [1,2]
	# badguy_position = [1,4]
	# dist = 11

	print(solution(dimensions, captain_position, badguy_position, dist))


if __name__ == "__main__":
	main()