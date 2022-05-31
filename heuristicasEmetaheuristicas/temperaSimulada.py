from copy import copy
import random
import math
from biblioteca import Biblioteca as bb
class TemperaSimulada:
  def novoEstadoAleatorio(self, ma, tAtu, tIni):
    tb = len(ma)
    nb = tAtu * tb // tIni
    nea = ma.copy()
    for i in range(0, nb):
      pt = random.randint(0, (tb-1))
      nea[pt] = 0 if nea[pt] == 1 else 1
    return nea
  
  def geraAgenda(self, Ta, tb):
    Agenda = []
    for i in range(Ta, 0, -1):
      x = i*tb//Ta
      x = x if x > 0 else 1
      Agenda.append(x)
    Agenda.append(0)
    return Agenda
  
  def simula(self, v, p, C, Ta):
    n = len(v)
    T = self.geraAgenda(self, Ta, n)
    max = 2**n-1
    intDoEstadoAtual = random.randint(0, max)
    mAtual = bb.binParaVetor(bb, n, bin(intDoEstadoAtual))
    pAtual = bb.calculaPeso(bb, mAtual, p, n)
    vAtual = bb.calculaValor(bb, mAtual, v, pAtual, n, C)
    mMelhor, pMelhor, vMelhor = mAtual, pAtual, vAtual
    tMax = T[0]
    for t in T:
      if t == 0:
        break
      mProximo = self.novoEstadoAleatorio(self, mAtual, t, tMax)
      pProximo = bb.calculaPeso(bb, mProximo, p, n)
      vProximo = bb.calculaValor(bb, mProximo, v, pProximo, n, C)
      deltaE = vProximo - vAtual
      if deltaE > 0:
        mAtual, pAtual, vAtual = mProximo, pProximo, vProximo
        if vAtual > vMelhor:
          mMelhor, pMelhor, vMelhor = mAtual, pAtual, vAtual
      else:
        sort = random.uniform(0,1)
        if math.exp(deltaE/t)-int(math.exp(deltaE/t)) > sort:
          mAtual, pAtual, vAtual = mProximo, pProximo, vProximo

    return mMelhor, vMelhor, pMelhor


