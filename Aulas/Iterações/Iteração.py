# Iterável -> str, range, etc (__iter__)
# Iterador -> quem sabe entregar um valor por vez
# next -> me entregue o próximo valor
# iter -> me entregue seu iterador

texto = 'Eder'  # iterável

iterador = iter(texto)  # iterator

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration as e:
        print(e.__class__.__name__)
        break

for letra in texto:
    print(letra)