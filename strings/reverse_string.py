'''
Reverse words in a String.
Input: Sky is blue in color
Output: color in blue is Sky
'''
#option 0: recursion
# def ReverseString(s):
#     if len(s)==0:
#         return s
#     else:
#         return (ReverseString(s[1:]) +s[0])

#option 1: using slice
# def ReverseString(s):
#     return s[::-1]

#option 2: reversed funtion
# def ReverseString(s):
#     return "".join(reversed(s))

#option 3: using stack
# from collections import deque
# def ReverseString(s):
#     stack=deque()
#     rev_str=""
#     for i in s:
#         stack.append(i)
#     for i in range(len(stack)):
#         rev_str+=stack.pop()
#     return rev_str

#option 4: using for loops
def ReverseString(s):
    new_str = ""
    for i in s:
        new_str = i + new_str
    return new_str

if __name__=="__main__":
    #s=input("enter the istring : ")
    s="Sky is blue in color"
    print("Reverse String:",ReverseString(s))