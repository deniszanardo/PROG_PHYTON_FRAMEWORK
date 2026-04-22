#Crie um programa que:
#Peça ao usuário dois números.

#Mostre:
# soma 
# subtração
# multiplicação 
# divisão.


#Verifique:
#Se os números são iguais.
#Se o primeiro número é maior que o segundo.
#Se pelo menos um dos números é maior que 10.

#atividade:

n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))

print(n1 + n2)
print(n1 - n2)
print(n1 * n2)
print(n1 // n2)

print(n1 == n2)
print(n1 > n2)
print(n1 >10)
print(n2 > 10)


# 4  tipos
# str      int             float    bool
# textos numeros inteiros reais lógicos
# 'texto',  10 ,  5.2 ,  True , False
# 'Bom dia', 2026,1.80, 1 , 0
# 'Seu nome:',1, 60.200, 
# 'R$'


# ESTRUTURAS DE DADOS ****


# espaços na memória ram da maquina
# variar
# variaveis são dados únicos
# interpertador 
# meio termo linguagem 
# força indentação = organização
# OUTPUT - SAIDA - print()
# nomear de forma semantica  -  boa pratica


# regras para criar variáveis:
# _ ou letra
# não pode começar por números 
# não pode carcateres especiais 
# pode utilizar números(só não pode começar)
# palavra composta snake_case


# linguagem alto nivel
# interpretada
# dinamica - variáveis


print('CADASTRO DE USUÁRIOS:')


nome = 'Lucas Lima'
idade  =  25
email_usuario = 'lucas@gmail.com'
peso = 80.50
altura =  1.90
endereco = 'Rua 10, Jd X'
graduacao = 'ADS'
casado = False 


# SAÍDA
print(nome)
print(idade)
print(email_usuario)
print(endereco)
print(graduacao)
print(peso)
print(altura)
print(casado)

#se tem colchetes é lista não é variável, 
saldo = [1500.0]


extrato = []

adicionando a soma 
extrato.append(sum(saldo))


saque =  float(input('Digite o saque: '))


transacao =  sum(saldo) - saque


extrato.append(saque)


saldo = [transacao]

# concatenando um dado literal com um valor numerico 
print('Saldo R$', saldo)

# tenho uma input do tipo floar que adiciona ao extrato e vou concatenar a um valor numerico 
deposito =  float(input('Digite o Deposito R$: '))


extrato.append(deposito)


transacao =  sum(saldo) + deposito


saldo = [transacao]


print('Saldo R$', saldo)


print(extrato)



# # Peça o valor de um produto e:
# produto =  float(input('Digite o valor do produto: '))


# # Calcule um desconto de 10%.


# desconto = produto * 0.10


# # Mostre o valor final.


# valor_prod = produto - desconto
# print('Valor do produto R$', valor_prod)


# # Verifique se o valor final é maior que 100.


# print('Verifique se o valor final é maior que 100 - ', valor_prod > 100)


# # Verifique se o produto ficou barato (menor que 50).


# print('Verifique se o produto ficou barato (menor que 50) - ', valor_prod < 50)



# print('Concatenação: JUNTAR')

# pi = 3.14
# pi = 3,18
# # print('pi', pi)

# x = 10 

# print('--------------------')
# #estrutura composta 
 
# listas = [10,20,30,40,50]
# #          0 1  2  3  4  
# listas_texto = [a,b,c,d]

# listas_mista = []

# lista_boleano = []

# lista_real = [4.1, 5.2, 6.5]
#                 0   1    2


#adicionar um dado a lista
lista_vazia = []
lista_vazia.append(100)

lista_vazia.remove(0)
lista_vazia.append(a)
lista_vazia.append(200)
lista_vazia.count(150)

# espaços na memoria ram da maquina
# variar
# variáveis são dados únicos
# interpretador
# meio termo entre a linguagem humana e da máquina
# forçar a intenção = organização
# cidade = 'cidade' 
# cidade = 'são paulo'
# CIDADE = 'BH'
# Cidade = 'rj'

# nomear de forma semantica 
# semantica é dar o nome daquilo que ele é - boa prática 
  
# print(cidade)
# função de outpur, é uma saída de código, print()

# regras para criar variáveis:
# _ou letra #não pode começar por números 
# não pode conter caracteres especiais
# pode utilizar números, (só não pode começar pelo número)
# palavra composta snake_case

#linguagem de alto nível 
#
# aplicar o type, para chamar qual tipo de dado esta usando na variável
# CRTL : roda somente o que está selecionado 

# print('cadasro de usuários')
# nome = 'Denis Renan'
# idade = 37
# email = 'deniszanardo@gmail.com'
# peso = 80.50
# altura = 1.90
# endereco = 'rua maria marcolina, brás'
# graduacao = 'ads'
# casado = False

# print(nome)

# ENTRADA
# nome_2 = input('digite seu nome')
# print("nome2")

# numero = float(input('digite um numero: '))
# numero_2 = float(input('digite um numero: '))
# numero_3 = int(input('Digite o ano: '))

# soma = numero_1 + numero_2
# print(soma)


# print('IMC')


# peso =  float(input('Digite seu peso: '))
# altura  =  float(input('Digite sua altura: '))
# imc  =  peso/altura**2

# print('IMC', imc)

# print("sinais de calculo aritimetico")

# print(10+200) # soma
# print(10-200) # subtração 
# print(10*200) # multiplicação
# print(10/200) # divisão 
# print(10%200) # modulo 
# print(10**200) # potencia
# print(10//200) # divisão com duas barras

# variáveis - estruturas de dados 
# funcoes - print() input() float() int()
# sinais aritiméticos 

# sinais logicos

print(10 == 200) # comparar
print(10 > 200) # verifica se 1º número é maior  
print(10 < 200) # verifica se 1º número é menor
print(10 >=200) # maior ou igual
print(10 <= 200) # menor ou igual 
print(10 != 2) # diferente

#Crie um programa que:
#Peça ao usuário dois números.

#Mostre:
# soma 
# subtração
# multiplicação 
# divisão.


#Verifique:
#Se os números são iguais.
#Se o primeiro número é maior que o segundo.
#Se pelo menos um dos números é maior que 10.

#atividade:

n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))

print(n1 + n2)
print(n1 - n2)
print(n1 * n2)
print(n1 // n2)

print(n1 == n2)
print(n1 > n2)
print(n1 >10)
print(n2 > 10)
