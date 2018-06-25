#
#Length of longest sub string
#
def LongestSubString(s):
    start=maxlength=0
    for ch in s:
        if (ch!=" " and ch!=" "):
            start+=1
            #print(ch, start)
        else:
            maxlength=max(maxlength,start)
            start=0
            #print(ch, start, maxlength)
    maxlength = max(maxlength, start)
    return maxlength

#traditional brute force
#def LongestSubString(s):
#    list1=[]
#    list1=s.split()
#    SubString=list1[0]
#    for i in range(1,len(list1)):
#        if len(SubString)<len(list1[i]):
#            SubString = list1[i]
#    return len(SubString)

if __name__=="__main__":
    #s=input("enter the string")
    s="I am the rogue that everyone is lookinggggggg for!!!!!!!!!!!!!!!!"
    print("Length of Longest Substring is : ",LongestSubString(s))