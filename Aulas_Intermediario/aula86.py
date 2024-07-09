# Aula sobre yield from -- terminar

def generator():
    yield 1
    yield 2
    yield 3
    yield 4


def generator02():
    yield from generator()
    yield 'Mudando de generator'
    yield 5
    yield 6
    yield 7
    yield 8


def generator03(gen):
    yield from gen
    yield 10
    yield 11
    yield 12
    yield 13
    print('Acabou os geradores !')


ge = generator02()
ge02 = generator02(generator03())
for n in ge:
    print(n)

for n in ge02:
    print(n)
