#Hacker rank Two strings problem using set()
#Given two strings, determine if they share a common substring. A substring may be as small as one character.
#For example, the words "a", "and", "art" share the common substring . The words "be" and "cat" do not share a substring.
#
#Function Description
#Complete the function twoStrings in the editor below. It should return a string, either  YES or NO based on whether the strings share a common substring.
#twoStrings has the following parameter(s):
#
#s1, s2: two strings to analyze .
#
#Input Format
#The first line contains a single integer 'q', the number of test cases.
#The following  pairs of lines are as follows:
#The first line contains string s1
#The second line contains string s2

#Note basically should match even if one character is present

#option1
def TwoStrings(s1,s2):
    ss1=set(s1)
    ss2=set(s2)
    print(s1 , ss1,s2 , ss2)
    if set.intersection(ss1,ss2):
        return "YES"
    return "NO"

if __name__=="__main__":
    #s1=input("enter the string1 : ")
    #s2=input("enter the string2 : ")
    #q=input("enter the string1 : ")
    s1="no is folse"
    s2="yes"
    q=1
    for i in range(q):
        print("Result :",TwoStrings(s1.replace(" ",""),s2.replace(" ","")))