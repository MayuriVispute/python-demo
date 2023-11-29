n=121
num=n
sum=0
while n>0:
    res=n%10
    sum=sum*10+res
    n//=10
if num==sum:
    print("pallendrom")
