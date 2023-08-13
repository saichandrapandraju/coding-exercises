'''
Given an integer array, return the maximum product of any three numbers in the array. For example, for A = [1,2,3,4,5], you should return 60, while for B = [-2,-4,5,3] you should return 40.
'''
import heapq


# my implementation, manual
def max_prod_3(l:list):
    min_heap, max_heap = [], []
    heapq.heapify(min_heap)
    heapq.heapify(max_heap)
    for i in l:
        heapq.heappush(min_heap, i)
        heapq.heappush(max_heap, -i)
    min1, min2 = heapq.heappop(min_heap), heapq.heappop(min_heap)
    if min1<0 and min2<0:
        return min1*min2*(-heapq.heappop(max_heap))
    else:
        return (-heapq.heappop(max_heap))*(-heapq.heappop(max_heap))*(-heapq.heappop(max_heap))
    
# solution/suggested - use inbuilt functions
def max_prod_3_final(l:list):
    largest_3 = heapq.nlargest(3, l)
    smallest_2 = heapq.nsmallest(2, l)  # for -ve numbers
    
    return max(largest_3[0]*largest_3[1]*largest_3[2], smallest_2[0]*smallest_2[1]*largest_3[0])


# test
assert max_prod_3([1,2,3,4,5]) == 60
assert max_prod_3([-2,-4,5,3]) == 40

assert max_prod_3_final([1,2,3,4,5]) == 60
assert max_prod_3_final([-2,-4,5,3]) == 40