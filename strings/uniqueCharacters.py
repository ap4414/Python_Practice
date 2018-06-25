#
#Check if the string has all unique characters
#option 1
def UniqueCh(s):
    #set command omits duplicates
    print(set(s),"vs", list(s))
    if len(list(set(s)))== len(s):
        return True
    else:
        return False

#option 2
#def UniqueCh(s):
#    s=s.replace(" ","")
#    #print(s)
#    ChUnique=[None]*26
#    IsUnique=True
#    for i in s:
#        pos=ord(i)-ord('a')
#        if ChUnique[pos]==None:
#            ChUnique[pos]=i
#        else:
#            IsUnique=False
#            break
#    return IsUnique

#return all characters that are Unique
#def UniqueCh(s):
#    s=s.replace(" ","")
#    seen=[]
#    for i in s:
#        print(seen)
#        if i not in seen:
#            seen.append(i)
#    return seen


if __name__=="__main__":
    #s=input("enter the string : ")
    s="abc zdefz"
    print(UniqueCh(s))