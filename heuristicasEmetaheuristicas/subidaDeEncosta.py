from copy import copy
import random
from biblioteca import Biblioteca as bb
class SubidaDeEncosta:
  def melhorVizinho(self, mAtual, pAtual, vAtual, v, p, C, n):
    mMelhor = mAtual.copy()
    pMelhor = pAtual
    vMelhor = vAtual
    for i in range(0, n):
      mPrxV = mAtual.copy()
      mPrxV[i] = 1 if mAtual[i] == 0 else 1
      pPrxV = bb.calculaPeso(bb, mPrxV, p, n)
      vPrxV = bb.calculaValor(bb, mPrxV, v, pPrxV, n, C)
      if vPrxV > vMelhor:
        mMelhor = mPrxV.copy()
        pMelhor = pPrxV
        vMelhor = vPrxV
    return mMelhor, pMelhor, vMelhor

  def subidaDeEncosta(self, v, p, C):
    n = len(v)
    max = 2**n-1
    intDoEstadoAtual = random.randint(0, max)
    mAtual = bb.binParaVetor(bb, n, bin(intDoEstadoAtual))
    pAtual = bb.calculaPeso(bb, mAtual, p, n)
    vAtual = bb.calculaValor(bb, mAtual, v, pAtual, n, C)
    while True:
      mProximo, pProximo, vProximo = self.melhorVizinho(self, mAtual, pAtual, vAtual, v, p, C, n)
      if vProximo <= vAtual:
        break
      mAtual, pAtual, vAtual = mProximo, pProximo, vProximo
    return mAtual, vAtual, pAtual
