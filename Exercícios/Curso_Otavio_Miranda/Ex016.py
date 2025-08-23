from random import randint

def multiplica(* nums):
    resultado = 1
    for n in nums:
        resultado *= n
    return resultado


nums = 5, 4, 3, 2, 1
resultado = multiplica(* nums)
print(resultado)


def parOuImpar(num):
    if num % 2 == 0:
        return f'O número {num} é par!'
    else:
        return f'O número {num} é ímpar!'


print(parOuImpar(randint(0, 100)))