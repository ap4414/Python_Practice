#palindrome check - Queue.py
import queue
from collections import deque

#option 1: queue module
# def plaindrome(s):
#     q=queue.Queue(maxsize=0) #inifitie queue maxsize=0
#     for i in s:
#         q.put(i)
#     print(q.qsize())
#     for i in s[::-1]:
#         if q.get()!= i:
#             return "No"
#     return "Yes"

#option 2: deque module
def plaindrome(s):
    q=deque()
    for i in s:
        q.append(i)
    print(q)
    for i in s:
        if q.pop()!= i: #use popleft to pop from th otherside
            return "No"
    return "Yes"

if __name__=="__main__":
    #s=input("enter the istring : ")
    s="malayalam"
    print("Is it a Plaindrome? :",plaindrome(s))