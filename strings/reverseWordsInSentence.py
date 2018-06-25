'''
Reverse words in a String.
Input: Sky is blue in color
Output: color in blue is Sky
'''

#option 1:
def ReadWordsInReverse(s):
    list=s.split()
    new_str=""
    print(list)
    for i in list[::-1]:
        new_str=new_str+"".join((i," "))
    return new_str

if __name__=="__main__":
    #s=input("enter the istring : ")
    s="Sky is blue in color"
    print("Reading Words In Reverse :",ReadWordsInReverse(s))