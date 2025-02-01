# Praticando mais sobre funções recursivas

import sys

sys.setrecursionlimit(3000)

def fazerFatorial(numero):
    if numero <= 1:
        return 1
    else:
        return numero * fazerFatorial(numero - 1)
    
print(fazerFatorial(5))
print(fazerFatorial(10))
print(fazerFatorial(1000))