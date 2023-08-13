'''
Given a list of coordinates, write a function to find the k closest points (measured by euclidean distance) to the origin. For example, if k=3 and the points are [[2,-1], [3,2], [4,1], [-1,-1], [-2,2]] then return [[-1,-1], [2,-1], [-2,2]]
'''
import heapq

# optimal - O(N*log(k))
def k_closest_to_origin(coords:list, k:int):
    distances = []
    for coord in coords:
        distances.append(((coord[0]*coord[0])+(coord[1]*coord[1]), coord))
    heapq.heapify(distances)
    to_return = []
    for _ in range(k):
        to_return.append(heapq.heappop(distances)[1])
    return to_return


# test
assert k_closest_to_origin([[2,-1], [3,2], [4,1], [-1,-1], [-2,2]], 3) == [[-1,-1], [2,-1], [-2,2]]