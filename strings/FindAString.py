'''
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
Sample Input:
ABCDCDC
CDC
Sample Output:
2
'''
#len of search string
#make a queue of that len
#keep popping in char and each time check if queue i substring


import timeit
#using loops
def findSubString(sSub, s):
    count=0
    for i in range(0,len(s)-len(sSub)+1):
#        print("start", i, s[i])
        if s[i]==sSub[0]:
            flag=1
            for j in range(0,len(sSub)):
#                print("inside")
#                print (s[i + j] , sSub[j])
                if s[i+j]!=sSub[j]:
                    flag=0
                    break
            count+=flag
#            print("count : ",count)
    return count

#using lists
#def findSubString(sSub, s):
#    output=0
#    pattern=list(sSub)
#    buffer=[]
#    counter=0
#    for i in range(len(s)):
#        if (len(pattern)==len(buffer)):
#            buffer.pop(0)
#        buffer.append(s[i])
#        counter+=1
#        print (buffer)
#        if buffer==pattern:
#            output+=1
#
#    return output

if __name__=="__main__":
    theString="ACCCACACA ACA"
    theSubString="ACA"
    print(findSubString(theSubString, theString))
    print("execution time is :",timeit.timeit(stmt="main"))
