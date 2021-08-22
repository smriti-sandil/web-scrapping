# c=int(input())
# def add(rng):
#     addition=0
#     for i in range(1,rng+1):
#         st=int(bin(i).replace("0b"," "))
#         addition+=st
#     print(addition)
# for i in range(c):
#     a=int(input())
#     add(a)

N,K,Q=map(int,input().split())
# print(N,Q,K)
# for i in range(Q):
#     a=int(input())
#     if N%K==a:
#         print("YES")
#     elif N%K!=a:
#         print("NO")
# for i in range(Q):

#     val=N//K
#     a=int(input())
#     if val==a:
#         print("YES")
#     else:
#         print("NO")
#     N=val
def findSubSequence(s, num):
 
    # Initialize the result
    res = 0
  
    # till n!=0
    i = 0
    while (num) :
          
        # if i-th bit is set
        # then add this number
        if (num & 1):
            res += ord(s[i]) - ord('0')
        i+=1
          
        # right shift i
        num = num >> 1
  
    return res

print(findSubSequence("174",3))