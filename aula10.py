def soma():
    n1 = float(input('=='))
    n2 = float(input('=='))
    soma = n1 + n2
    print(soma)

def sub():
    n1 = float(input('=='))
    n2 = float(input('=='))
    sub = n1 - n2
    print(sub)

def mult():
    n1 = float(input('=='))
    n2 = float(input('=='))
    mult = n1 * n2
    print(mult)

def div():
    n1 = float(input('=='))
    n2 = float(input('=='))
    div = n1 / n2
    print(div)

def sair():
    print('voce saiu do sistema')


def calculadora():
    lista = ['+', '-', '*', '/']
    print('escolha uma operaçao ou sair')
    operacao = input('>>>')
    if operacao == '+':
        soma()
    elif operacao == '-':
        sub()
    elif operacao == '*':
        mult()
    elif operacao == '/':
        div()    
    else:
        sair()
while True:
    calculadora()
