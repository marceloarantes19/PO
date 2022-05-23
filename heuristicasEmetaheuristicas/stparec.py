def spa(a1, r, n):
  if n == 1:
    return a1
  else:
    return spa(a1+r, r, n-1)+a1
  
print(spa(2,4,5))