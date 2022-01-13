

def func(*args, **kwargs):
    print(args)

    idade = kwargs['idade']
    print(idade)


lista = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 0]

func(*lista, *lista2, Nome='Luiz', Sobrenome='Miranda', idade=30)
