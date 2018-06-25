##Reverse characters of each word in a sentence(whitespace separated)

#option 1:
def RevChar(s):
    list=s.split()
    new_str=""
    print(list)
    for i in list:
        new_str=new_str+"".join((" ",i[::-1]))
    return new_str

if __name__=="__main__":
    #s=input("enter the istring : ")
    s="tree traversal in motion"
    print("#Reverse characters of each word  :",RevChar(s))