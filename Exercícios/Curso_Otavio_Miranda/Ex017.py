def multiplicador(multiplicar_vezes):
    def numero(num):
        return f'{multiplicar_vezes} x {num} = {num*multiplicar_vezes}'
    return numero

duplicar = multiplicador(2)
triplicar = multiplicador(3)
quadruplicar = multiplicador(4)

print(duplicar(3))
print(triplicar(8))
print(quadruplicar(10))
