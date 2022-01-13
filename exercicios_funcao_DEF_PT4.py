"""

crie uma função 1 que recebe uma função 2 como parametro e retorne o valor da função 2 executada.


def f1():
    f2()

def f2(outravar=None):
    outravar = int(4+4)
    print(outravar, 'deu certo')
    return

f1()

"""

"""
crie uma função 1 que recebe uma função 2 como parametro e retorne o valor da função 2 executada. 
Faça a função 1 executar duas funções que recebam um número diferente de argumentos. 
"""


def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def falaoi(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

executando1 = mestre(falaoi, 'Luiz')
executando2 = mestre(saudacao, 'Luiz', saudacao='Bom dia!!!')
print(executando1)
print(executando2)