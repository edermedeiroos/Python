# FUNÇÕES RECURSIVAS E RECURSIVIDADE
# São funções que retornam si mesmas 
# Podem dar StackOverflor caso a recursão seja muito grande | RecursionError

def func_recursiva(inicio= 0, fim=10):
    print(inicio, fim)
    if inicio >= fim:
        return fim
    inicio += 1
    return func_recursiva(inicio)

print(func_recursiva())