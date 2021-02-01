import math
x,y=list(map(int,input().split()))
factotal=math.factorial(x+y)
fact_sum=math.factorial(x)*math.factorial(y)
print(int(factotal/fact_sum))
