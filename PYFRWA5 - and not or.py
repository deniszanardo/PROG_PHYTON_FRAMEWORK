# 1. Verificação de maioridade e permissão
# Enunciado:
# Crie um programa que leia a idade do usuário e se ele possui autorização dos pais (responda True ou False).
# O usuário pode participar da atividade se tiver 18 anos ou mais ou tiver autorização dos pais.
# Use and / or para verificar e exiba "Pode participar" ou "Não pode participar".

# idade = int(input('Idade'))
# autorizacao = input('Possui autorização: ')
# pode = (idade >=18) and (autorizacao)

# print('Pode participar? - ', pode)

# -------------------------------------------->
# 2. Classificação de peso ideal
# Enunciado:
# Leia o peso (kg) e a altura (m) de uma pessoa. Calcule o IMC (peso / altura**2).
# Uma pessoa está com peso normal se o IMC estiver entre 18.5 e 24.9 (inclusive).
# Use operadores lógicos para verificar se o IMC está nessa faixa e exiba "Peso normal" ou "Fora da faixa".

# peso = float(input('Digite seu peso:  '))

# altura = float(input('Digite sua altura: '))

# imc = peso/altura**2
# print(imc)

# peso_normal = imc >= 18.5 and imc<= 24.9

# v = peso_normal and 'Peso Normal' or 'Fora '
# print(v)

#------------------------------------------------


# 3. Acesso ao sistema
# Enunciado:
# Leia o nome de usuário e a senha. O acesso é permitido apenas se o usuário for "admin" e a senha for "1234".
# Use and para verificar as duas condições e exiba "Acesso liberado" ou "Acesso negado".

# nome = str(input("Digite seu nome: "))
# senha = int(input("Digite sua senha: "))

# admin = nome == "admin" and senha ==1234

# v = admin and 'Acesso Liberado' or 'Acesso Negado'
# print(v)

#-------------------------------------------------

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# 4. Compra com desconto
# Enunciado:
# Leia o valor da compra e se o cliente é VIP (True ou False).
# O cliente ganha 10% de desconto se o valor for maior que R$ 100 ou ele for VIP.
# Exiba o valor final com desconto (se aplicável) ou o valor original.

# valor = float(input("Digite o valor da compra: "))
# vip = str(input('Você é vip? '))

# descontovip = valor >=100 or vip == "sim"

# desconto = valor * 0.10

# valortotal = valor - d 

# valorfinal = valortotal == "valor final com desconto" or valor == "valor original"

# print(valortotal)


# v = valortotal and print(valortotal) or valor print(valor)

# print(v)

# admin = nome == "admin" and senha ==1234

# v = admin and 'Acesso Liberado' or 'Acesso Negado'
# print(v)

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# 5. Elegibilidade para doação de sangue
# Enunciado:
# Leia a idade e o peso.
# Para doar sangue, a pessoa deve ter entre 16 e 69 anos (inclusive) e pesar pelo menos 50 kg.
# Use and para verificar ambos os critérios e informe se a pessoa pode doar.


idade = int(input("Digite seu idade: "))

peso = float(input('Digite seu peso: '))

pode = idade >=16 or idade <=69 and peso >=50 
npode = idade <16 or idade >69 and peso <50

print('Você pode doar', pode or 'Você não pode doar', npode)

print(pode == 'Vc pode doar' or  npode == 'Não pode'  )


#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# 6. Validação de horário de funcionamento
# Enunciado:
# Uma loja funciona de segunda a sexta, das 9h às 18h.
# Leia o dia da semana (1=segunda, 7=domingo) e a hora (0 a 23).
# Determine se a loja está aberta.
# Dica: use and para combinar dia útil com horário, e or se quiser tratar sábado/domingo como fechado.



# 7. Aprovação em duas disciplinas
# Enunciado:
# Leia as notas de Matemática e Português.
# O aluno é aprovado se ambas as notas forem maiores ou iguais a 6.
# Use and para verificar e exiba "Aprovado" ou "Reprovado".



# 8. Identificação de ano bissexto
# Enunciado:
# Um ano é bissexto se for divisível por 4, mas não por 100, a menos que também seja divisível por 400.
# Leia um ano e use and e or para determinar se ele é bissexto.
# Exiba "Ano bissexto" ou "Ano não bissexto".


# ano = int(input('Digite um ano: '))


# Ano_bissexto = ano // (4 and 400)

# Ano_nao_bissexto = ano 

# print(Ano_bissexto and Ano_nao_bissexto)




# print(ano)  == True, 'Ano Bissexto' or ==False, 'Ano não bissexto')





# 9. Faixa etária
# Enunciado:
# Leia a idade e classifique:

# "Criança" se idade < 12

# "Adolescente" se 12 ≤ idade ≤ 17

# "Adulto" se idade ≥ 18
# Use and e or para definir os intervalos e exiba a classificação.



# 10. Sistema de alerta de temperatura e umidade
# Enunciado:
# Leia a temperatura (°C) e a umidade (%).
# Dispare um alerta se temperatura > 35 ou umidade > 70.
# Caso contrário, exiba "Condições normais".
# Use or para combinar as condições.





# instrucoes


# # AND -  E xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# x  =  10

# y  =  10

# carteira_motorista = 'sim'

# idade  = 25

# print(carteira_motorista == 'sim' and idade < 17)



# # OR - OU  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# tempo  =  input('Digite o tempo: ')

# print(tempo == 'calor' or  tempo == 'frio'  )

# # ambas verdadeiras ou ao menos uma expressão true



# # not não  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# # é veridadeiro quando ao contrário,

# salario =  input('O salario caiu? ')

# print(not tempo  == 'calor' and  not  salario == 'não') 


# # in -  dentro xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# lista  =  [1,2,3]

# print(1 in lista or not 2 in lista)


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
Contexto:
Uma indústria monitora temperatura (T), umidade (U) e presença de gás inflamável (G, 0 ou 1).
O nível de risco é dado por:

Crítico: (T > 40 ou U > 80) e G == 1

Alto: (T > 40 ou U > 80) e G == 0

Médio: (T entre 25 e 40) e (U entre 50 e 80)

Baixo: qualquer outra situação

Tarefa:
Receba T (float), U (float), G (0 ou 1).
Classifique o risco em "Crítico", "Alto", "Médio" ou "Baixo" sem usar if/elif.
Use apenas dicionários com chaves booleanas e operadores lógico

UTILIZE APENAS SINAIS LÓGICOS -  VARIAVEIS  -  LISTAS  -  I/O -  NÃO UTILIZE CONDICIONAIS OU LOOPS
Contexto
Uma loja oferece um cupom especial. O cliente ganha o cupom se atender a pelo menos  das seguintes condições:
 (responde "sim" ou "não")
 (responde "sim" ou "não")
Além disso, o cupom  pode ser aplicado se o cliente tiver  no histórico (número inteiro).Tarefa
Receba:
vip (string "sim" ou "nao")
valor (float)
primeira_compra (string "sim" ou "nao")
itens_defeito (int)
Determine se o cliente  ("Cupom liberado") ou  ("Sem cupom"),  (SEM IF , SEM LOOP, SEM FUNÇÃO)


idade = int(input('Idade'))
# 4 tipos dados
# variáveis 
# listas 
# tuplas 
# dicionarios 
# I/O 
# sinais lógicos 
# sinais Aritméticos
# concatenação



# expressões lógicas 


# and, or ,not, in




# AND -  E
x  =  10
y  =  10
carteira_motorista = 'sim'
idade  = 25
print(carteira_motorista == 'sim' and idade < 17)



# OR - OU 
tempo  =  input('Digite o tempo: ')
print(tempo == 'calor' or  tempo == 'frio'  )

# ambas verdadeiras ou ao menos uma expressão true



# not não 
# é veridadeiro quando ao contrário
salario =  input('O salario caiu? ')


print(not tempo  == 'calor' and  not  salario == 'não') 


# in -  dentro


lista  =  [1,2,3]


print(1 in lista or not 2 in lista)


viagens = {
    "Paris": {
        "preco": 5000,
        "vagas": 5
    },
    "Nova York": {
        "preco": 4000,
        "vagas": 3
    },
    "Tokyo": {
        "preco": 6000,
        "vagas": 2
    }
}




# Parte 1: Escolha do Destino
# Peça ao usuário:
# Nome do destino
# Quantidade de pessoas


destino =  input('Destino: ')
quantidade = int(input('Quantida de pessoas: '))






# Parte 2: Cálculo do Valor
# Calcule:
# Valor total da viagem (preço * pessoas)


calculo =  viagens[destino]['preco'] * quantidade
print('Calculo da viagem R$', calculo)




# Parte 3: Regras da Agência (SEM if, SEM loop)


# Aplique:
# Se pessoas > 3 → desconto de 10%
desconto_1 = (quantidade > 3) * calculo * 0.10
print('Desconto de 10%', desconto_1)



# Se valor total > 10000 → desconto extra de 5%
total =  (calculo > 10000 ) * calculo * 0.05
print('desconto de 5%',  calculo - total)


# Se não houver vagas suficientes → taxa de 500 (overbooking)
vagas_s =  (calculo + 500.0) * (viagens[destino]['vagas'] < quantidade ) 
print('Overbooking', vagas_s)



# Se destino não existir → valor vira 0
destino_ex = (input('Digite o destino> ') in viagens  ) * calculo  
print('Valor total R$ ', destino_ex)


# instrucoes


# # AND -  E xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# x  =  10

# y  =  10

# carteira_motorista = 'sim'

# idade  = 25

# print(carteira_motorista == 'sim' and idade < 17)



# # OR - OU  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

tempo  =  input('Digite o tempo: ')

print(tempo == 'calor' or  tempo == 'frio'  )


# # ambas verdadeiras ou ao menos uma expressão true



# # not não  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# # é veridadeiro quando ao contrário,

# salario =  input('O salario caiu? ')

# print(not tempo  == 'calor' and  not  salario == 'não') 


# # in -  dentro xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# lista  =  [1,2,3]

# print(1 in lista or not 2 in lista)



