# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

# space=O(n); time=o(n);
def isUnique(inp:str):
    mem = set()
    for i in inp:
        if i in mem:
            return False
        mem.add(i)
    return True

# if no additional ds, then time=O(n^2)
def isUnique2(inp:str):
    for i in range(len(inp)):
        for j in range(i+1, len(inp)):
            if inp[i]==inp[j]:
                return False
    return True


if __name__ == "__main__":
    assert isUnique("saichandrapandraju") == False
    assert isUnique("thisnodupl") == True
    
    assert isUnique2("saichandrapandraju") == False
    assert isUnique2("thisnodupl") == True