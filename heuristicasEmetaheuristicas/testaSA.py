import random
from biblioteca import Biblioteca as bb
from temperaSimulada import TemperaSimulada as ts
n, C, p, v = bb.sobeArquivo('arquivosKnapSack/low_dimensional/f1_l-d_kp_10_269')
m, valor, peso = ts.simula(ts, v, p, C, 100)
print("Capacidade:", C)
print("Mochila:", m)
print("Valor: ", valor)
print("Peso: ", peso)
