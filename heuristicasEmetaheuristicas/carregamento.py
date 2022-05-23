import csv
class Carregamento:
  def sobeArquivo(self, nome):
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