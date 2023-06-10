"""
LeetCode link: https://leetcode.com/problems/k-closest-points-to-origin/

Problem description:
--------------------
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)^2 + (y1 - y2)^2).

You may return the answer in "any order". The answer is "guaranteed" to be "unique" (except for the order that it is in).

example - 1:
    Input: points = [[1,3],[-2,2]], k = 1
    Output: [[-2,2]]
    Explanation:
    The distance between (1, 3) and the origin is sqrt(10).
    The distance between (-2, 2) and the origin is sqrt(8).
    Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
    We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

example - 2:
    Input: points = [[3,3],[5,-1],[-2,4]], k = 2
    Output: [[3,3],[-2,4]]
    Explanation: The answer [[-2,4],[3,3]] would also be accepted.

Constraints:
    1 <= k <= points.length <= 104
    -104 < xi, yi < 104
"""

from heapq import heappop, heappush
from typing import List

def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    to_return, heap = [], []
    for point in points:
        dist = (point[0]*point[0]) + (point[1]*point[1])
        heappush(heap,(-dist,point))            # build max heap 
        if len(heap)>k:                         # if heap size is more than k, pop the point with max dist , b/c we need k closest 
            heappop(heap)
    for _ in range(k):
        to_return.append(heappop(heap)[1])
    return to_return
    

# test
def test_equals(expected, actual):
    for i in expected:
        if i not in actual: return False
    return len(actual) == len(expected)

assert test_equals([[-2,2]], kClosest([[1,3],[-2,2]], 1)) == True
assert test_equals([[3,3],[-2,4]] , kClosest([[3,3],[5,-1],[-2,4]], 2)) == True
assert test_equals([[-2,4],[3,3]] , kClosest([[3,3],[5,-1],[-2,4]], 2)) == True
assert test_equals([[5,-1],[3,3]] , kClosest([[3,3],[5,-1],[-2,4]], 2)) == False