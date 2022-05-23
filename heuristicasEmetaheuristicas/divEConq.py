from carregamento import Carregamento

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

arquivo = Carregamento()
n, C, p, v = arquivo.sobeArquivo('arquivos/low_dimensional/f1_l-d_kp_10_269')
m = [0 for _ in range(len(p))]

vet = divEConq(m, p, v, 0, C, [])
print(vet)
print("valor: ", calcV(m, p, v, C, vet))
for i in vet:
  m[i] = 1
print(m)