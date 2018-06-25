'''
From Cracking the coding Interview book,
A Program to check if strings are rotations of each other or not 2.6
Given a string s1 and a string s2, write a snippet to say whether s2 is a rotation of s1 using only one call to str routine?
(eg given s1 = ABCD and s2 = CDAB, return true, given s1 = ABCD, and s2 = ACBD , return false)
'''

#option1 Algorithm: areRotations(str1, str2)
#
#    1. Create a temp string and store concatenation of str1 to
#       str1 in temp.
#                          temp = str1.str1
#    2. If str2 is a substring of temp then str1 and str2 are
#       rotations of each other.
#
#Since str2 is a substring of temp, str1 and str2 are rotations of each other.
def TwoStringsRot(s1,s2):
    temp =s1+s1
    print(temp)
    if s2 in temp:
        return "True"
    return "False"

if __name__=="__main__":
    #s1=input("enter the string1 : ")
    #s2=input("enter the string2 : ")
    s1="ABCD"
    s2="CDAB"
    print("Result :",TwoStringsRot(s1.replace(" ",""),s2.replace(" ","")))