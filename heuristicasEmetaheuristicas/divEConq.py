def calcV(x, p, v, C, vet):
  valor = 0
  peso = 0
  for i in vet:
    valor = valor + v[i]
    peso = peso + p[i]
  return valor if peso <= C else valor * (-1)

def divEConq(x, p, v, a, C, vet):
  if a == len(x):
    return vet 
  else:
    l = vet[:a]
    r = vet[:a]
    r.append(a)
    vetl = divEConq(x, p, v, a+1, C, l) 
    vetr = divEConq(x, p, v, a+1, C, r)
    vl = calcV(x, p, v, C, vetl)
    vr = calcV(x, p, v, C, vetr)
    return vetl if vl > vr else vetr

C = 12
x = [0, 0, 0, 0]
p = [4, 6, 3, 2]
v = [5, 7, 9, 6]
vet = divEConq(x, p, v, 0, C, [])
print(vet)
print("valor: ", calcV(x, p, v, C, vet))
for i in vet:
  x[i] = 1
print(x)