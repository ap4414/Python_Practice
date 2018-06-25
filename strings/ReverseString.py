#
#Reverse string
#

#option 1: the old way
##strings are immutable cannot swap characters in a string
def ReverseString(s):
    inv_s=""
    SLength=len(s)
    for i in range(0, SLength):
        inv_s=inv_s+s[SLength-i-1]
    return inv_s

#option 2: slice
#def ReverseString(s):
#    return s[::-1]

#option 3: slice
#def ReverseString(s):
#    return "".join(reversed(s))


if __name__=="__main__":
    #s=input("enter the string : ")
    s="retaw evas reeb knird"
    print("reversed string is : ", ReverseString(s))