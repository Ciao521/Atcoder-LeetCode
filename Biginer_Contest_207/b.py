import math
a,b,c,d = map(int,input().split())
u = 0  #試行回数
if c*d - b == 0:
  u = -1
else:
  u = math.ceil(a/(c*d-b))
#(c*d -b) * u = a でc*d とbの差を回数を増やすことでaを超えれば条件達成
if u < 0:
  u = -1

print(u)