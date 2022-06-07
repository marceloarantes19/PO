from copy import copy
import random
import math
from biblioteca import Biblioteca as bb
class AlgoritmoGenetico:
  # Ordena populacao pelo fitness 
  def ordenaPopulacaoPeloFitness(self, populacao, fitness):
    n = len(fitness)
    for i in range(1, n):
      k = fitness[i]
      kEst = populacao[i]
      j = i
      while j>=1 and fitness[j-1]<k:
        fitness[j] = fitness[j-1]
        populacao[j] = populacao[j-1]
        j = j - 1
      fitness[j] = k
      populacao[j] = kEst 
    return populacao, fitness 

  def calculaFitnessElemento(self, elemento, valores, restricoes, maxRestricao):
    somav = 0
    somap = 0
    for i in range(0, len(elemento)):
      somav = somav + (0 if elemento[i] == 0 else valores[i])
      somap = somap + (0 if elemento[i] == 0 else restricoes[i])
    return somav if somap <= maxRestricao else somav*(-1)

  def calculaFitness(self, populacao, valores, restricoes, maxRestricao):
    ret = []
    total = 0
    for i in populacao:
      sValor = 0
      sRestricao = 0
      for j in range(0, len(i)):
        if i[j] == 1:
          sValor = sValor + valores[j]
          sRestricao = sRestricao + restricoes[j]
      total = total + sValor
      ret.append(sValor*(-1 if sRestricao > maxRestricao else 1))
    return ret, total  

  def populacaoInicial(self, numeroDeBits, tamanhoDaPopulacao, val, rest, maxRest):
    ret = []
    for i in range(0, tamanhoDaPopulacao):
      fitElemento = 0
      elemento = []
      while fitElemento <= 0:
        elemento = []
        for j in range(0, numeroDeBits):
          elemento.append(random.randint(0,1))
        fitElemento = self.calculaFitnessElemento(elemento, val, rest, maxRest)
      ret.append(elemento)
    return ret
  
  # População ordenada do melhor para o pior em fitness
  def cruzamento(self, populacao, fitness, numeroDeBits, percentual): 
    ret = []
    pesoDosElementos = []
    totalDeCruzamentos = len(populacao)*percentual//100
    pontoDoCruzamento  = random.randint(1,(numeroDeBits-1))
    totalFitness = 0.0
    somaDosElementos = 0.0
    for i in fitness:
      totalFitness = totalFitness + i
    for i in fitness:
      somaDosElementos = somaDosElementos + i / totalFitness
      pesoDosElementos.append(somaDosElementos)
    
    for i in range(0,totalDeCruzamentos):
      elemento1 = []
      elemento2 = []
      valElemento1 = random.uniform(0,1)
      valElemento2 = random.uniform(0,1)
      indElemento1 = 0
      indElemento2 = 0
      for j in range(len(pesoDosElementos)-1, -1, -1):
        if pesoDosElementos[j] <= valElemento1:
          indElemento1 = j
          break
      for j in range(0, len(pesoDosElementos)):
        if pesoDosElementos[j] <= valElemento2:
          indElemento2 = j
          break
      elemento1 = populacao[indElemento1][:pontoDoCruzamento]+populacao[indElemento2][pontoDoCruzamento:]
      elemento2 = populacao[indElemento2][:pontoDoCruzamento]+populacao[indElemento1][pontoDoCruzamento:]
      ret.append(elemento1)
      ret.append(elemento2)
    return ret

  def mutacao(self, populacao, numeroDeBits, n):
    for i in range(0, n):
      indiceDeMutacao = random.randint(0, len(populacao) - 1)
      pontoDeMutacao = random.randint(0, numeroDeBits-1)
      populacao[indiceDeMutacao][pontoDeMutacao] = 0 if populacao[indiceDeMutacao][pontoDeMutacao] == 0 else 1
    return populacao
  
  def preselecao(self, populacao, fitness, restricao): # restrição é um valor real para o fitness
    ret = []
    retFit = [] 
    for i in range(0, len(populacao)):
      if fitness[i] >= restricao:
        ret.append(populacao[i])
        retFit.append(fitness[i])
    return ret, retFit 
  
  def selecao(self, populacao, fitness, novaPopulacao, novoFitness):
    n = len(populacao)
    ret = []
    retFit = []
    while len(ret)<n:
      ret.append(populacao.pop(0) if fitness[0]>novoFitness[0] else novaPopulacao.pop(0))
      retFit.append(fitness.pop(0) if fitness[0]>novoFitness[0] else novoFitness.pop(0)) 
    return ret, retFit

  def ag(self, valores, restricoes, maxRestricao, pCruzamento, tamanhoDaPopulacao):
    numeroDeBits = len(valores)
    populacao = self.populacaoInicial(len(valores), tamanhoDaPopulacao, valores, restricoes, maxRestricao)
    fitness, vFitness = self.calculaFitness(populacao, valores, restricoes, maxRestricao)
    self.ordenaPopulacaoPeloFitness(populacao, fitness)
    nv = 0
    while True:
      nv = nv + 1
      novaPopulacao = self.cruzamento(populacao, fitness, numeroDeBits, pCruzamento)
      novaPopulacao = self.mutacao(novaPopulacao, numeroDeBits, pCruzamento*10//100)
      novoFitness, novoVFitness = self.calculaFitness(novaPopulacao, valores, restricoes, maxRestricao)
      novaPopulacao, novoFitness = self.preselecao(novaPopulacao, novoFitness, 0)
      self.ordenaPopulacaoPeloFitness(novaPopulacao, novoFitness)
      novaPopulacao, novoFitness = self.selecao(populacao, fitness, novaPopulacao, novoFitness)
      novoFitness, novoVFitness = self.calculaFitness(novaPopulacao, valores, restricoes, maxRestricao)
      if novoVFitness > vFitness:
        populacao = copy(novaPopulacao)
        fitness = copy(novoFitness)
        vFitness = novoVFitness
      else:
        break
    print("Número Interações Genéticas:", nv)
    return populacao[0], fitness[0]
