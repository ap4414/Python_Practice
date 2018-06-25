#first non repeating Character

from collections import OrderedDict

#option 1: this returns index of first non repeating character - from leetcode
def firstNonRepeatingChar(s):
    alphabets='abcdefghijklmnopqrstuvwxyz' # can use sets and replace the whole thing with all the unique characters in the string
    indices=[]
    for ch in alphabets:
        print (ch, s.count(ch))
        if s.count(ch)==1:
            indices.append(s.index(ch))
            print (indices)
    if len(indices)>0:
        return (s[min(indices)])
    else:
        return None

#option 2: slight modification over opetion1
# def firstNonRepeatingChar(s):
#     dict=OrderedDict()
#     for ch in s:
#         if ch in dict:
#             dict[ch]+=1
#         else:
#             dict[ch]=1
#     for key,value in dict.items():
#         if value==1:
#             return key
#     return (None)


if __name__=="__main__":
    #s=input("enter the string1 : ")
    s="ABCEDABCABC"
    print("Result :",firstNonRepeatingChar(s))