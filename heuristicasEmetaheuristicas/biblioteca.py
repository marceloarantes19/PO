import csv
class Biblioteca:
  def sobeArquivo(nome):
    peso = []
    valor = []
    with open(nome,'r') as a:
      l = csv.reader(a)
      for i in l:
        linha = []
        for j in i:
          linha.append(int(j))
        valor.append(linha.pop(0))
        peso.append(linha.pop(0))
    numeroDeElementos = valor.pop(0)
    capacidade = peso.pop(0)
    return numeroDeElementos, capacidade, peso, valor
  
  def calculaPeso(self, mAtual, p, n):
    ret = 0
    for i in range(0, n):
      ret = ret + (0 if mAtual[i] == 0 else p[i])
    return ret

  def calculaValor(self, mAtual, v, peso, n, C):
    ret = 0
    for i in range(0, n):
      ret = ret + (0 if mAtual[i] == 0 else v[i])
    return ret if peso <= C else ret * (-1) 

  def binParaVetor(self, n, binDoEstado):
    mat = [0 for _ in range(n)]
    j = 0
    for i in range(len(binDoEstado)-1, 1, -1):
      mat[j]=int(binDoEstado[i])
      j = j + 1
    return mat
