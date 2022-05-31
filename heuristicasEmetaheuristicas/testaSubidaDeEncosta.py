import random
from biblioteca import Biblioteca as bb
from subidaDeEncosta import SubidaDeEncosta as subida
n, C, p, v = bb.sobeArquivo('arquivosKnapSack/low_dimensional/f1_l-d_kp_10_269')
m, valor, peso = subida.subidaDeEncosta(subida, v, p, C)
print("Capacidade:", C, "\n", m, valor, peso)
