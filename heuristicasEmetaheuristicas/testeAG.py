import random
from biblioteca import Biblioteca as bb
from algoritmosGeneticos import AlgoritmoGenetico as AG
n, C, p, v = bb.sobeArquivo('arquivosKnapSack/low_dimensional/f10_l-d_kp_20_879')
a = AG()
tamanhoDaPopulacao = 200 
print("Tamanho da População:", tamanhoDaPopulacao)
m, valor = a.ag(v, p, C, 50, tamanhoDaPopulacao)
print(m, valor)
