'''
Given two arrays, write a function to get the intersection of the two. For example, if A = [1,2,3,4,5] and B = [0,1,2,3,7] then you should return [1,3]
'''
# my implementation - O(M)
def get_intersection(l1:list, l2:list):
    mem = set(l1)
    result = []
    for j in l2:
        if j in mem and j not in result: result.append(j)
    return result

# solution/suggested - O(min(N,M))
def get_intersection_final(l1:list, l2:list):
    set_1 = set(l1)
    set_2 = set(l2)
    if len(set_1) < len(set_2):
        return [x for x in set_1 if x in set_2]
    else:
        return [x for x in set_2 if x in set_1]

# test

assert get_intersection([1,2,3,4,5], [0,1,3,7]) == [1,3] or get_intersection([1,2,3,4,5], [0,1,3,7]) == [3,1]
assert get_intersection_final([1,2,3,4,5], [0,1,3,7]) == [1,3] or get_intersection_final([1,2,3,4,5], [0,1,3,7]) == [3,1]