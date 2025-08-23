# Faça um programa que tenha a função notas() que pode receber várias notas de alunos
# e vai retornar um dicionário com as seguinte informações:
# Quantidade de notas | A maior nota | A menor nota | A média da turma | A situação(opcional)
# Adicione também as docstrings à função
def notas(* nums, situacao=False):
    """A função permite adiconar várias notas, e retornara os seguintes valores:
    • Número total de notas | • Maior nota | • Menor nota | • Média total | • Situação(opcional)
    :parameter nums: Parâmetro para adicionar as notas
    :parameter situacao: Parâmetro opcional para exibir a situação do aluno"""
    boletim = dict()
    boletim['Total'] = len(nums)
    boletim['Maior'] = max(nums)
    boletim['Menor'] = min(nums)
    boletim['Média'] = sum(nums) / len(nums)
    if situacao:
        if boletim['Média'] >= 7:
            boletim['Situação'] = 'APROVADO'
        elif 7 > boletim['Média'] >= 5:
            boletim['Situação'] = 'RECUPERÇÃO'
        else:
            boletim['Situação'] = 'REPROVADO'
    return boletim


notas(8, 10, 5, 7, situacao=True)
print(notas())
help(notas)
