'''
Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to
become 'A4B4C5D2E4'. For this problem, you can falsely "compress"
strings of single or double letters. For instance, it is okay
for 'AAB' to return 'A2B1' even though this technically takes more
space.
The function should also be case sensitive, so that a string 'AAAaaa'
returns 'A3a3'.
'''

#option1
def StringCompression(s):
    l=len(s)
    if l==0:
        return None
    if l==1:
        return (s+str(1))
    dic={}

    for char in s:
        if char in dic:
            dic[char]+=1
        else:
            dic[char]=1

    final=""

    for key,value in dic.items():
        final+=key+str(value)
    return final

##option2
#def StringCompression(s):
#    s_comp=""
#    comp=""
#    s_comp=s[0]
#    count=0
#    for i in range(0,len(s)):
#        if s[i]!=s_comp:
#            comp=comp+s_comp+str(count)
#            s_comp = s[i]
#            count=1
#        else:
#            count+=1
#        print(s_comp, comp, count)
#    comp = comp + s_comp + str(count)
#    return comp

if __name__=="__main__":
    #s=input("enter the string : ")
    s="AAAABBBBCCCCCDDEEEE"
    print("after compressing string : ",StringCompression(s))