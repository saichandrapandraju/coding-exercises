# URLify: Write a method to replace all spaces in a string with '%20'. 
# You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string. 
# (Note: if implementing in Java, please use a character array so that you can perform this operation in place.)

# EXAMPLE
# Input: "Mr John Smith    ", 13 Output: "Mr%20John%20Smith"

# space - O(n); time - O(n)
def urlify(inp: str, true_length:int):
    space_count = 0
    for i in range(true_length):
        if inp[i] == ' ':
            space_count+=1
    
    final_string_len = true_length + space_count*2
    out_string = ['']*final_string_len
    for i in range(true_length-1, -1, -1):
        if inp[i] != " ":
            out_string[final_string_len-1] = inp[i]
            final_string_len -= 1
        else:
            out_string[final_string_len-1] = '0'
            out_string[final_string_len-2] = '2'
            out_string[final_string_len-3] = '%'
            final_string_len -= 3

    return ''.join(out_string) 

if __name__ == "__main__":
    assert urlify("Mr John Smith    ", 13) == "Mr%20John%20Smith"
    assert urlify("Hi I'm Sai Chandra Pandraju        ", 27) == "Hi%20I'm%20Sai%20Chandra%20Pandraju"