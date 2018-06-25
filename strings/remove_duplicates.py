'''
Remove duplicate characters in a given string keeping only the first occurrences.
Example : if the input is ‘tree traversal’ the output will be ‘tre avsl’.
'''

#option 1:
def DelCopies(s):
    seen=[]
    new_str=""
    for i in s:
        if i not in seen:
            seen.append(i)
            new_str="".join((new_str,i))

    return new_str

if __name__=="__main__":
    #s=input("enter the istring : ")
    s="tree traversal"
    print("removing Dup characters :",DelCopies(s))