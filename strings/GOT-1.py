# Game of thrones - 1 from Hacker Rank
# Note : for a string to be a anagram, number of letters with odd frequency should be <=0
# Execution: A palindrome must by definition have an even number of letters. The only exception is a string of an odd length (‘aba’) that has exactly one odd letter count.

##Plaindrome
import timeit

def checkPal(s):
    output=False

    #option 1: trying with string reversal function
    #for i in range(0,int((len(s))/2)):
    ##    print(s[i], s[len(s)-1-i])
    #    if s[i]!=s[len(s)-1-i]:
    #        output=False
    #        break
    #    output=True

    #option 2: trying with string reversal function
    #print(s,s[::-1])
    #if s==s[::-1]:
    #    output=True

    #option 3: using reversed function
    #print(reversed(s))
    s_temp=""
    if s==s_temp.join(reversed(s)):
        output=True

    #option 4: calssic Algo- inplace swapping
    #“classic” textbook in-place string reversal algorithm, ported to
    #  Python. Because Python strings are immutable, you first need to
    #  convert the input string into a mutable list of characters, so
    # you can perform the in-place character swap

    return output

if __name__=="__main__":
    #s=input("enter the string :")
    s="malayalam"
    print(s)
    print("is Palindrome :", checkPal(s))
    print("execution time :", timeit.timeit(stmt="main"))