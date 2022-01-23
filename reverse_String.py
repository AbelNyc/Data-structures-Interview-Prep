'''
Write a function that reverses a string.

Example:
Input: "hello"
Output: "olleh"

Input: "REVERSE" 
Output: "ESREVER" 

Input: "42 Wallaby Way, Sydney" 
Output: "yendyS ,yaW yballaW 24"

Input: ""
Output: ""

no minimum or maximum length
return string, don't print
could get numbers/spaces/punctuation

(1) Reverse String by indexing it
 - Base Case: if len(0): return ""
 - Base Case: if len(1): return input_char
 
 split string into separate char.s (slicing)
 set up two pointers, one at first char, other at last 
 iterate, compare left and right pointers
 exchange value of pointers
 move left pointer to right, right pointer to left 
 keep doing this until pointers coincide, at that point return
 
'''
def solution(s):
    result = list(s)    
    first = 0
    last = len(s)-1
    while first < last:
        result[first], result[last] = result[last],result[first]
        first, last = first + 1, last-1
    return ''.join(result)
    
    
