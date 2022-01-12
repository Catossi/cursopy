"""
funções  - DEF
"""

def saudacao(msg='Olá', nome='usuário'):
	nome = nome.replace('e', '3')
	msg = msg.replace('e', '3')
	print(msg, nome)
	return

saudacao(nome='zé', msg='Hello')
saudacao('oi', 'luiz')
saudacao('hello', 'Maria')
