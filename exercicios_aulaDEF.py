"""
1 - crie uma função que exibe saudação com os parametros saudacao e nome.
"""
'''
def saudacao(nome, idade):
	print('Olá', nome, 'sua idade é', idade)

name = input('digite seu nome')
age = input('digite sua idade')
saudacao(name, age)
'''

"""
1 - crie uma função que recebe 3 numeros como parametros e exiba a soma entre eles.
"""

'''
def soma(n1, n2, n3):
	total = (n1+n2+n3)
	print(total)

n1 = int(input('digite o primeiro número'))
n2 = int(input('digite o segundo número'))
n3 = int(input('digite o terceiro número'))
    
soma(n1, n2, n3)
'''


"""

3 - crie uma função que receba 2 numeros. o primeiro é um valor e o segundo um percentual (ex 10%), 
retorne (return) o valor do primeiro número somado do aumento do perce3ntual do mesmo.

n1 = int(input("digite umnúmero")) 
n2 = int(input('digite um percentual (ex: para 10% digite 10'))

def percentual(n1, n2):
  total = (n1+((n2/100)*n1))
  print(total)

percentual(n1, n2)
"""


"""
4 - Fizz Buzz -  se o parametro da função for divisível por 3, retorne fizz, se o parametro for divisível por 5 retorne buzz. 
se o parametro for divisível por 5 e 3 retorne fizzbuzz. Caso contrário retorne o número enviado.
"""


n1 = int(input('digite um número divisível por 3 e 5'))

resto1 = (n1 % 3)

def div(n1):
  if n1 % 3 == 0 and n1 % 5 ==0:
    return 'fizzbuzz'
  if n1 % 3 == 0:
    return 'fizz'
  if n1 % 5 == 0:
    return 'buzz'
  else:
    return n1

print(div(n1))






