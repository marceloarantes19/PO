from carregamento import Carregamento
def firstFit(m, v, p, C):
  pTotal = 0
  vTotal = 0
  for i in range(0, len(p)):
    if pTotal + p[i] <= C:
      pTotal = pTotal + p[i]
      vTotal = vTotal + v[i]
      m [i] = 1
  return pTotal, vTotal

arquivo = Carregamento()
n, C, p, v = arquivo.sobeArquivo('arquivos/low_dimensional/f1_l-d_kp_10_269')
m = [0 for _ in range(len(p))]

pMoch, vMoch = firstFit(m, p, v, C)
print("Mochila.........:", m)
print("Peso da Mochila.:", pMoch)
print("Valor da Mochila:", vMoch)


#print(n)
#print(C)
#print(p)
#print(v)
