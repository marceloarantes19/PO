from cmath import exp
import random

k = 100
for i in range(k,0,-1):
  x = exp(i/k)
  #print(x)
kl = [10,5,3,2,2,1,1,1,1,1]
t = 0
kk = kl[2:]+kl[:2]
#print(kk)
for i in kl:
  t = t+i 
sp = 0.0
for i in kl:
  sp = sp + i / t
  print(i, ' --- ', sp)




