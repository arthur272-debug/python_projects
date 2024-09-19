from sys import path

from package import package_aula  # outra forma de importar
import package.package_aula  # outra forma de importar
# outra forma de importar(abaixo) --> não muito recomendável
from package.package_aula import *

print(package_aula.soma(1, 2))
print(package.package_aula.aleatorio)
print(soma(10, 2))
package_aula.aleatorio = 'Novo'
print(package_aula.aleatorio)
