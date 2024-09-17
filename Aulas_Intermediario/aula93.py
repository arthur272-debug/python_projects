# aula sobre recarregando módulos, importlib e singleton
import importlib

import aula93_m

print(aula93_m.metro)

for i in range(10):
    importlib.reload(aula93_m)
    print(i)


print('Terminou')
