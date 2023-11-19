# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

# Assumption - no space, and case sensitive
from collections import defaultdict

def is_permutation(inp1:str, inp2:str):
    if len(inp1) != len(inp2): return False
    mem = defaultdict(int)
    for i in inp1:
        mem[i]+=1
    for j in inp2:
        mem[j]-=1
        if mem[j]<0:
            return False
    return True


if __name__ == "__main__":
    assert is_permutation("god", "dog") == True
    assert is_permutation("tomelvisjedusor", "jesuisvoldemort") == True
    assert is_permutation("funny", "sunny") == False
    