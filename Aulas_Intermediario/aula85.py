# Aula sobre Generator functions

def generator(n=0):
    yield 1
    print('É suuuuper!!!')
    yield 2
    print('Moreeee')
    yield 3
    print('Acabou')
    return 'Finish'


def generator02(n=0, maximum=10):
    while True:
        yield n

        n += 1
        if n > maximum:
            return 'Acabou-se!!'


ge = generator(n=0)
# print(next(ge))
# print(next(ge))
# print(next(ge))

ge02 = generator02(n=8, maximum=12)

# for n in ge:
#     print(n)

for n in ge02:
    print(n)
