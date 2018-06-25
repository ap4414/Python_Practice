#Python Interview Question FizzBuzz. Write a program that prints the numbers from 1 to 20.
# But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz”
#ONLY one return statement

#option 1: this returns index of first non repeating character - from leetcode
# def FizzBuzz():
#     for i in range(20):
#         if i%15==0:
#             print("FizzBuzz")
#         elif i%3==0:
#             print("Fizz")
#         elif i%5==0:
#             print("Buzz")
#         else:
#             print(i)
#
# if __name__=="__main__":
#    print("Result :",FizzBuzz())

#option 1:
def FizzBuzz(i):
    for j in range(i):
        if j%15==0:
            print("FizzBuzz")
        elif j%3==0:
            print("Fizz")
        elif j%5==0:
            print("Buzz")
        else:
            print(i)
if __name__=="__main__":
    #i=input("enter the i  : ")
    i=20
    print("Result :",FizzBuzz(i))