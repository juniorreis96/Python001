nomeusuario = str(input('Olá, Qual seu nome? ')).strip()

# PROGRAMA QUE FAZ A CONTA DE ALUGUEL DO CARRO, POR KM SE PAGA R$0.15 centavos e por dia se paga R$300.00
print('Olá {}! Gostaria de simular a locação de um dos nossos carros?'.format(nomeusuario))
km = float(input('Quantos KM pretende percorrer?: '))
dias = int(input('Por quantos dias pretende manter a locação?: '))
print('A sua locação de {} dias com {:.2f} KMs rodados ficaria um total de: R${:.2f}. '
      .format(dias, km, (km * 0.15) + (dias * 300)))

# Ler a KM/h de um carro e caso seja maior que 80km/h ele emite uma multa e a multa custa R$7,00 por KM.
print('\033[1;31;40mCENTRAL DE TRÁFEGO\033[m')
km = float(input('Insira qual o KM registrado pelo veiculo: '))
if km <= 80:
    print('\033[1;34;40mPARABENS!\033[m Um veículo a {:.2f}KM/h está dentro do permitido.'
          '\nTenha uma ótima viagem!'.format(km))
else:
    print('Um veículo a {:.2f}KM/h está fora do permitido.'
          '\nPor isso receberá uma multa de: R${:.2f}! '.format(km, (km - 80) * 7))

# PROGRAMA QUE CONVERTE TEMPERATURAS
opiniao = str(input('Está com frio ou calor?')).upper().strip()
graus = float(input('Vamos converter temperaturas?'
                    '\nDigite uma temperatura em Celsius'
                    '\ne converteremos para Farenheit(F°) e Kelvin(K°): '))
if graus >= 25:
    print('Nossa, está calor!\n'
          '{:.2f}C° em Farenheit é: {:.2f}F° e em Kelvin seria: {:.2f}K°\n'
          '\033[1;31;40m BORA PASSAR O PROTETOR? ;)\033[m'.format(graus, graus * 1.8 + 32, graus + 273.15))
else:
    print('Nossa, por isso estou tremendo!\n'
          '{:.2f}C° em Farenheit é: {:.2f}F° e em Kelvin seria: {:.2f}K°\n'
          '\033[1;36;40m VÁ SE AGASALHAR!\033[m'.format(graus, graus * 1.8 + 32, graus + 273.15))

# LER UM NÚMERO E IDENTIFICAR SE ELE É PAR OU ÍMPAR
n = int(input('Está em dúvida se um número é par ou ímpar?\n'
              'Iremos te ajudar, digite o número aqui: '))
if n % 2 == 0:
    print('O número {}, é par!'.format(n))
else:
    print('O número {}, é impar!'.format(n))

# PROGRAMA QUE FAZ CALCULO DE AUMENTO DE SALARIO EM DIFERENTES % DEPENDENDO DO SALARIO ATUAL.
salario = float(input("""PARABÉNS! Você irá receber um aumento de salário!
Digite seu salario atual e mostraremos seu % de
aumento e seu novo salario!
       \033[1;33;40mDIGITE AQUI: R$\033[m"""))
if salario >= 2000.00:
    print('Seu salario atual de {:.2f} será reajustado em \033[4;31;40m15%\033[m para \033[4;34;40[mR${:.2f}\033[m!'
          .format(salario, salario * 0.15 + salario))
else:
    print('Seu salario atual de {:.2f} será reajustado em \033[4;31;40m20%\033[m para \033[4;34;40[mR${:.2f}\033[m!'
          .format(salario, salario * 0.2 + salario))
print('\033[4mAgradecemos muito pelo seu trabalho!\033[m')

# DIGITE O NOME DE UMA CIDADE E INDIQUE SE O A PRIMEIRA PALAVRA É OU NÃO "SANTO"
cidade = str(input('Digite o nome de uma cidade: ')).upper().strip().split()
if cidade[0] == "SANTO":
    print('A palavra que você escreveu tem "SANTO" como primeiro nome!')
else:
    print('A palavra que você escreveu \033[4mNÃO\033[m tem "SANTO" como primeiro nome!')

# TODOS MAIUSCULO, MINUSCULO, CONTAR QUANTAS LETRAS E QUANTAS LETRAS NO PRIMEIRO NOME.
nome = str(input("""Digite o seu nome completo e falaremos quantas letras ele possui,
quantas letras apenas no primeiro nome e escreveremos
em MAIUSCULO e minusculo.
        \033[;1;33;40mDIGITE AQUI: \033[m"""))
nome2 = nome.split()
nome3 = nome.replace(" ", "")
print('-=-' * 10)
print("""QTD letras: {}
QTD letras primeiro nome: {}
MAIÚSCULO: {}
MINÚSCULO: {}
""".format(len(nome3), len(nome2[0]), nome.upper(), nome.lower()))

# PERGUNTAR A VIAGEM EM KM E CALCULAR O PREÇO DA PASSAGEM R$0.50 por km para até 200km ou R$0.45 para mais longas.
km = float(input("""Você gosta de viajar?
Vamos calcular quanto ficaria sua viagem conosco
Digite a distância em KM:  """))
if km <= 200:
    print('O sua viagem de {:1f}km custará: R${:.2f}'.format(km, km * 0.5))
else:
    print('Sua viagem de {:.1f}km custará: R${:.2f}'.format(km, km * 0.45))

# PROGRAMA QUE CALCULA O QUANDO DE ECONOMIA O CLIENTE PODERIA FAZER CASO COMPRASSE CONOSCO O MESMO PRODUTO.
nomecliente = str(input('Olá! Qual seu nome?: ')).upper().strip()
produto = str(input('{}, qual produto que você gostaria de avaliar? '.format(nomecliente))).strip().upper()
valor = float(input('Qual o valor que você paga em cada {}? R$ '.format(produto)))
quant = float(input('No valor de R${:.2f}, qual a quantidade mensal que é comprada? '.format(valor)))
desconto = (quant * valor) * 0.10
print('Você gasta o total de R$', quant * valor, '!')
print('{},O valor que você irá economizar será de: R${}'.format(nomecliente, desconto))

# DIGITAR UM ANO E IDENTIFICAR SE ELE É BISSEXTO
ano = int(input('Vamos descobrir se um ano é bissexto? Digite um ano e lhe falaremos'
                '                  DIGITE AQUI: '))
# PROGRAMA DA RITINHA
nomecliente2 = str(input('Qual seu nome?: ')).strip().upper()
pedido = str(input('Olá! Somos o "ritinhas bar"!\n'
                   'Gostaria de realizar um pedido?: ')).upper().strip()

print('-=-' * 10)
if pedido == "SIM":
    print('Ótimo! Preencha abaixo a quantidade de cada salgado:')
    print('\/ \/ \/ \/ \/ \/ \/ \/ \/')
    risole = int(input('Qual a quantidade de risoles?: '))
    coxinha = int(input('Qual a quantidade de coxinhas?: '))
    bolinhoqueijo = int(input('Qual a quantidade de bolinhos de queijo?: '))

    print('{}, seu pedido de {} risole(s),{} coxinha(s) e {} bolinhos de queijo ficará em {}: '.format(nomecliente2,
                                                                                                       risole, coxinha,
                                                                                                       bolinhoqueijo,
                                                                                                       risole * 0.6 + coxinha * 0.6 + bolinhoqueijo * 0.6))

if pedido == "NÃO":
    print('Tudo bem, volte assim que desejar fazer um pedido!')

# PROGRAMA QUE CALCULA QUANTO FICARIA PARA PINTAR UM COMODO DA CASA, MOSTRANDO QUANTAS LATAS NECESSÁRIAS E QUANTO FICARIA.
altura = float(input('Qual a altura total das paredes?: '))
largura = float(input('Qual a largura total das paredes?: '))
lata = int(input('Quantos m2 a uma lata pode pintar?: '))
valorlata = float(input('Qual o valor da lata de tinta?: '))
print("""Para pintarmos o comodo inteiro, de {:.1f} x {:.1f}, gastaremos
      um total de {} latas por R${:.2f}!"""
      .format(altura, largura, (altura * largura) / lata, ((altura * largura) / lata) * valorlata))

# PROGRAMA QUE FAZ CONVERSÃO DE DOLAR, EURO E LIBRA.
print("""Olá! Seja bem vindo ao conversor de moedas!
temos disponíveis conversor de moeda para as
seguinte cotações: LIBRA ESTERLINA, EURO E DOLLAR.""")
print('-=-' * 20)
print('-=-' * 20)
qtdreal = float(input('Quantos em R$ você deseja converter?: '))
moeda = str(input("""Para qual moeda que deseja converter?
        \033[4;33;40mDIGITE AQUI\033[m: """)).upper().strip()
if moeda == "LIBRA":
    print('R${:.2f} convertidos para LIBRA ESTERLINA lhe dará um total de: £{:.2f} '.format(qtdreal, qtdreal / 7))
elif moeda == "LIBRA ESTERLINA":
    print('R${:.2f} convertidos para LIBRA ESTERLINA lhe dará um total de: £{:.2f}'.format(qtdreal, qtdreal / 7))

if moeda == "EURO":
    print('R${:.2f} convertidos para EURO lhe dará um total de: €{:.2f}'.format(qtdreal, qtdreal / 6))

# DIGITAR 3 NÚMEROS E IDENTIFICAR QUAL O MAIOR E QUAL O MENOR
print('Vamos brincar!')
print('-=-' * 20)
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite o último número: '))
if (n1 > n2) and (n1 > n3):
    print('{} é o maior número!'.format(n1))
if (n2 > n1) and (n2 > n3):
    print('{} é o maior número!'.format(n2))
if (n3 > n1) and (n3 > n2):
    print('{} é o maior número!'.format(n3))

if (n1 < n2) and (n1 < n3):
    print('{} é o menor número!'.format(n1))
if (n2 < n1) and (n2 < n3):
    print('{} é o menor número!'.format(n2))
if (n3 < n1) and (n3 < n2):
    print('{} é o menor número!'.format(n3))

# SELECIONAR ORDEM DE ALUNOS DE 4 OPÇÕES
import random

al1 = str(input('Digite o nome do primeiro um aluno: ')).upper().strip()
al2 = str(input('Digite o nome do segundo aluno: ')).upper().strip()
al3 = str(input('Digite o nome do terceiro aluno: ')).upper().strip()
al4 = str(input('Digite o nome do quarto aluno: ')).upper().strip()
basealuno = [al1, al2, al3, al4]
escolhido = random.choice(basealuno)
print('-' * 20)
print('O aluno escolhido foi: \033[4;33;40m{}\033[m'.format(escolhido))

# CALCULANDO O VALOR DO PRODUTO COM DESCONTOS CASO COMPRE A PARTIR DE R$X.
desejo = str(input('Olá! Estamos com promoções especiais, '
                   'quer saber dos nossos descontos? ')).upper().strip()
if desejo == "NÃO":
    print('Tudo bem, agradecemos pela preferência!')
elif desejo == "NAO":
    print('Tudo bem, agradecemos pela preferência!')
elif desejo == "SIM":
    print('Ótimo!')
    produto = str(input('Qual produto você deseja consultar o desconto? '))
    qtd = int(input('Qual a quantidade que deseja comprar? '))
    valor = float(input('Qual o valor atual? R$ '))
    if qtd * valor <= 200:
        print("""Sua categoria de desconto ainda é a mais baixa, seu desconto é de 10%.
        Então seu total fica em: R${:.2f}! """.format((qtd * valor) - (qtd * valor * 0.1)))
    if (qtd * valor >= 201) and (qtd * valor <= 400):
        print("""Sua categoria de desconto é a segunda, seu desconto é de 15%.
        Então seu total fica em: R${:.2f}! """.format((qtd * valor) - (qtd * valor * 0.15)))
    if qtd * valor >= 401:
        print("""Sua categoria de desconto é a maior, seu desconto é de 20%.
        Então seu total fica em: R${:.2f}! """.format((qtd * valor) - (qtd * valor * 0.2)))
else:
    tentardnv = str(input('Você não indicou nenhuma opção válida!\n    \033[4;33;40mQuer tentar novamente?\033[m'))

# LEIA UMA FRASE E MOSTRE QUANTAS VEZES APARECE A LETRA "A", QUAL A PRIMEIRA E ÚLTIMA POSIÇÃO DELA.
print('Vamos brincar?')
digite = str(input('Digite uma frase: ')).strip().upper()
letra = str(input('Qual letra deseja procurar?: ')).upper().strip()
frase = digite.replace(" ", "")
contar = frase.count(letra)
primeirapos = frase.find(letra)
ultimapos = frase.rfind(letra)
print('A sua frase possui {} letras "{}"'.format(contar, letra))
print('A letra "{}" aparece pela primeira vez na {} posição.'.format(letra, primeirapos + 1))
print('A letra "{}" aparece pela primeira vez na {} posição.'.format(letra, ultimapos + 1))

# LER 3 COMPRIMENTOS DE RETAS E DIZER SE PODEM OU NÃO FORMAR UM TRIÂNGULO
print('Gostaria de entedner trinângulos?')
med1 = int(input('Digite a primeira reta: '))
med2 = int(input('Digite a segunda reta: '))
med3 = int(input('Digite a terceira reta: '))
if (med1 + med2 > med3) and (med2 + med3 > med1) and (med3 + med1 > med2):
    print('Com as retas {},{} e {} é possível formarmos um triângulo!'.format(med1, med2, med3))
else:
    print('Com as retas inseridas, não podemos criar um triângulo')

# FAZ A CALCULADORA
numerocalc = int(input('Qual o número que deseja saber a calculadora?: '))
print("""
O resultado para a tabuada do {} é de:
{} x 1  = {}
{} x 2  = {}
{} x 3  = {}
{} x 4  = {}
{} x 5  = {}
{} x 6  = {}
{} x 7  = {}
{} x 8  = {}
{} x 9  = {}
{} x 10 = {}""".format(numerocalc, numerocalc, numerocalc * 1, numerocalc, numerocalc * 2, numerocalc, numerocalc * 3,
                       numerocalc, numerocalc * 4, numerocalc, numerocalc * 5, numerocalc, numerocalc * 6, numerocalc,
                       numerocalc * 7, numerocalc, numerocalc * 8, numerocalc, numerocalc * 9, numerocalc,
                       numerocalc * 10))

# LER NOME COMPLETO E MOSTRA O PRIMEIRO E ÚLTIMO NOME, SEPARADAMENTE.
nome = str(input('Qual seu nome completo?: ')).strip()
print('Seu nome completo é: {}'.format(nome.upper()))
nome1 = nome.split()
print('Sendo primeiro nome: {}'.format(nome1[0]).upper())
print('E seu segundo nome: {}'.format(nome1[-1]).upper())

# CALCULAR HIPOTENUSA
import math

caoposto = float(input('Qual a medida do cateto oposto?: '))
caadjacente = float(input('Qual a medida do cateto adjacente?: '))
hipotenusa = math.hypot(caoposto ** 2 + caadjacente ** 2) ** (1 / 2)
print('A hipotenusa é: {}'.format(hipotenusa))

# DIGITE UM NÚMERO E RETORNAREMOS APENAS O NUMERO INTEIRO
import math

n1 = float(input('Digite um número e retornaremos apenas sua parte inteira!'
                 '             \nDIGITE AQUI: '))
print('A parte inteira de {:.2f} é {}'.format(n1, math.trunc(n1)))

# CONVERTE MEDIDAS (CM PARA M, MM)
import math

n1 = float(input("""
Digite um número (em M) e além de dar seu valor inteiro, converteremos para cm, mm, dc e km
  \033[4;34;40mDIGITE AQUI:\033[m """))
print("""
O valor que você digitou ({}) é convertido da seguinte forma: 
VALOR INTEIRO (em M): {}
M p/ KM : {:.2f}
M p/ DM : {:.2f}
M p/ CM : {:.2f}
M p/ MM : {:.2f}
""".format(n1, math.trunc(n1), n1 / 1000, n1 * 10, n1 * 1000, n1 * 100))

# RESOLVER SENO, COSSENO E TANGENTE
import math

medida = int(input('Qual o ângulo?: '))
mseno = math.sin(math.radians(medida))
mcos = math.cos(math.radians(medida))
mtang = math.tan(math.radians(medida))

print("""
Com o ângulo {:.2f}°, obtemos os seguintes resultados:
seno: {:.2f}
cosseno: {:.2f}
tangente: {:.2f}
      """.format(medida, mseno, mcos, mtang))

# SELECIONAR UM ALUNO DE 4 OPÇÕES
import random, time

a1 = str(input('Digite o primeiro aluno: ')).upper().strip()
a2 = str(input('Digite o segundo aluno: ')).upper().strip()
a3 = str(input('Digite o terceiro aluno: ')).upper().strip()
a4 = str(input('Digite o quarto aluno: ')).upper().strip()
listalunos = [a1, a2, a3, a4]
escolhido = random.choice(listalunos)
print('O aluno escolhido foi...')
time.sleep(4)
print('\033[4;33;40mPARABÉNS, {}!\033[m'.format(escolhido))

# CALCULA A MÉDIA DE UM ALUNO
nomealuno = str(input('Digite o nome do aluno: '))
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
n3 = float(input('Digite a terceira nota do aluno: '))
media = (n1 * 0.3) + (n2 * 0.4) + (n3 * 0.3)
print('Para o aluno {}, a média fica em {:.2f}! '.format(nomealuno, media))
if media >= 7:
    print('PARABÉNS! Sua média foi o suficiente para ser aprovado!')
if media < 7:
    print('VOCÊ FOI REPROVADO!')

# DIGITE UM NOME E INDIQUE SE TEM "SILVA" NO NOME
nome = str(input('Digite seu nome: ')).upper().strip()
nomeprocura = nome.find("SILVA")
if nomeprocura >= 0:
    print('O nome digitado possui "SILVA"!')
if nomeprocura < 0:
    print('O nome digitado \033[4;33;40mNÃO\033[m possui "SILVA"!')

# LER NÚMERO E MOSTRE CADA DIGITO SEPARADO. (UNIDADE, CENTENA E MILHAR)
numero = int(input('Olá, tudo bem? Digite um número de 0 até 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 100 % 10
print('A unidade: {}'.format(u))
print('A dezena: {}'.format(d))
print('A centena: {}'.format(c))
print('A milhar: {}'.format(m))