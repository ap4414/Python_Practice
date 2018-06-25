"""Find if two strings are anagrams of each other."""

#best appoach using ascii/unicode values
def anagram(s1,s2):
    result=False
    s1=s1.replace(" ","")
    s2=s2.replace(" ","")
    a1=[0]*26
    a2=[0]*26

    for i in range(len(s1)):
        CharCase=ord(s1[i])
        if CharCase<97:
            ordSel=ord('A')
        else:
            ordSel=ord('a')
        pos= CharCase-ordSel
        a1[pos]=a1[pos]+1

    for i in range(len(s2)):
        CharCase = ord(s2[i])
        if CharCase<97:
            ordSel=ord('A')
        else:
            ordSel=ord('a')
        pos= CharCase-ordSel
        a2[pos]=a2[pos]+1

    if(a2==a1):
        result=True
    return result

#using lists
#def anagram(s1,s2):
#    result=False
#    l1=s1.split()
#    l2=s2.split()
#    if(set(l1)==set(l2)):
#        result=True
#    return result

s1="sh ee ter"
s2="seEther"
print(anagram(s1,s2))

