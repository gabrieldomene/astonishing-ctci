"""
is unique: implement an algorithm to determine if a string has all unique characters. 
What if you cannot use additional data structures?
"""

def is_unique_set(string):
    """
    time: O(n)
    space: O(n)
    """
    s = set()
    for c in string:
        if c in s:
            return False
        s.add(c)
    return True

def is_unique_set_2(string):
    """
    time: O(n)
    space: O(n)
    """
    s = set(string)
    return len(s) == len(string)

def is_unique(string):
    """
    time: O(nlogn)
    space: O(1)
    """
    s_sorted = sorted(string)
    last_chart = None
    for c in s_sorted:
        if c == last_chart:
            return False
        last_chart = c
    return True

    
def is_unique_bit_vector(string):
    """
    bitwise operation
    time: O(n)
    space: O(1)
    """
    if len(string) > 128:
        return False
    checker = 0
    for c in string:
        val = ord(c)
        if checker & (1 << val) > 0:
            return False
        checker |= (1 << val)
    return True

def is_unique_ord(string):
    """
    time: O(n)
    space: O(n)
    """
    if len(string) > 128:
        return False

    chars = [False] * 128
    for c in string:
        val = ord(c)
        if chars[val]:
            return False
        chars[val] = True
    return True
    




assert is_unique_set("abcdefg") is True
assert is_unique_set("abcdefgg") is False

assert is_unique_set_2("abcdefg") is True
assert is_unique_set_2("abcdefgg") is False

assert is_unique("abcdefgg") is False
assert is_unique_bit_vector("abcdgefg") is False
assert is_unique_ord("abcdgefg") is False

