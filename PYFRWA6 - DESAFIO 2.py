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

UTILIZE APENAS SINAIS LÓGICOS
 -  VARIAVEIS
   -  LISTAS
     -  I/O
      -  NÃO UTILIZE CONDICIONAIS OU LOOPS



#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#SOLUÇÃO
#  

risco = {
    Crítico: (T > 40 ou U > 80) e G == 1
    
    Alto: (T > 40 ou U > 80) e G == 0
    
    Médio: (T entre 25 e 40) e (U entre 50 e 80)
# risco = {
#     "Critico": {
#         "T": > 40,
#         "U": > 80,
#         "G": == 1
#     },
#     "Alto": {
#         "T": > 40,
#         "U": > 80,
#         "G": == 0
#     },
#     "Médio": {
#         "T": > = 25 <=40,
#         "U": > =50 <=80,
#         "G": não especificado
#     }
# }







}
# Contexto
# Uma loja oferece um cupom especial. O cliente ganha o cupom se atender a pelo menos 1 das seguintes condições:
#  (responde "sim" ou "não")
#  (responde "sim" ou "não")

# Além disso, o cupom  pode ser aplicado se o cliente tiver no histórico (número inteiro).Tarefa

# Receba:

# vip (string "sim" ou "nao")

# valor (float)

# primeira_compra (string "sim" ou "nao")

# itens_defeito (int)

# Determine se o cliente  ("Cupom liberado") ou  ("Sem cupom"),  (SEM IF , SEM LOOP, SEM FUNÇÃO)

# idade = int(input('Idade'))

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

sorteio = (input("Digite: sim ou não "))

vipsorteio = (str(input("Digite: sim ou não "))

valorsorteio = bool(int(input("Digite um número:  "))

primeiracompra = bool(str(input("Digite: sim ou não ")

ganha = sorteio == true or vipsorteio == True or valorsorteio == True or primeiracompra == True  


#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# 5. Elegibilidade para doação de sangue
# Enunciado:
# Leia a idade = #idade = int(input("Digite seu idade: "))
# leia o peso = #peso = float(input('Digite seu peso: '))
# Para doar sangue, 
# a pessoa deve ter entre 16 e 69 anos ------xxxxxx  pode = idade >=16 or idade <=69 and peso >=50 
# (inclusive)
# e pesar pelo menos 50 kg.--------------xxxxxxxxxx npode = idade <16 or idade >69 and peso <50 

# Use and para verificar ambos os critérios e informe se a pessoa pode doar.

#print('Você pode doar', pode or 'Você não pode doar', npode)

#print(pode == 'Vc pode doar' or  npode == 'Não pode'  )

#SOLUÇÃO

idade = bool(int(input("Digite seu idade: "))) 

peso = bool(float(input('Digite seu peso: ')))


pode = idade >=16 or idade <=69 and peso >=50 
npode = idade <16 or idade >69 and peso <50 

print('Você pode doar', pode or 'Você não pode doar', npode)

#nao funcoionou print(pode == 'Vc pode doar' or  npode == 'Não pode'  )

# print(1 in lista or not 2 in lista)

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# 10. Sistema de alerta de temperatura e umidade
# Enunciado:
# Use or para combinar as condições.



# Leia a temperatura (°C) e a umidade (%).
t = float(input("Digite temperatura em Cº: "))
u = float(input('Digite umidade em %: '))

# Dispare um alerta se temperatura > 35 ou umidade > 70.
ruim = t > 35 or u > 70 == True

# Caso contrário, exiba "Condições normais".
alerta = ruim or "alerta" or 'Condicoes normais '

print(alerta)


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


# idade = int(input("Digite seu idade: "))

# peso = float(input('Digite seu peso: '))

# pode = idade >=16 or idade <=69 and peso >=50 
# npode = idade <16 or idade >69 and peso <50

# print('Você pode doar', pode or 'Você não pode doar', npode)

# print(pode == 'Vc pode doar' or  npode == 'Não pode'  )


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

x  =  10

y  =  10


i = int(input("Digite idade: "))

carteira = bool(input("Digite : "))

carteira_motorista = 'sim'

idade  = 25

print(carteira_motorista == 'sim' and idade < 17)



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



# COMENTARIOS ANTES DE RESOLVER O EXERICIO, 
# 27/03/2026
# FATIAR O PROBLEMA, 

# DESTINO É UM INPUT DO TIPO TEXTO, 
# VOU PEGARO DICIONARIO E VOU COLOCAR LÁ EM CIMA 
# DEPOIS VOU PEDIR PRO USUARIO DIGITAR A QUANTIDADE DE PESSOAS 

# # Parte 1: Escolha do Destino

# # Peça ao usuário:

# # Nome do destino

# # Quantidade de pessoas


# Parte 2: Cálculo do Valor
# Calcule:

# Valor total da viagem (preço * pessoas)
# Parte 3: Regras da Agência (SEM if, SEM loop)

# Aplique:
# Se pessoas > 3 → desconto de 10%

# Se valor total > 10000 → desconto extra de 5%
# Se não houver vagas suficientes → taxa de 500 (overbooking)
# Se destino não existir → valor vira 0

# viagens = {
#     "Paris": {
#         "preco": 5000,
#         "vagas": 5
#     },
#     "Nova York": {
#         "preco": 4000,
#         "vagas": 3
#     },
#     "Tokyo": {
#         "preco": 6000,
#         "vagas": 2
#     }
# }




# # ---------------------------------------------------------
# INÍCIO DA RESOLUÇÃO DO EXERCÍCIO 

# O preço para paris é 5000 e a quantidade de vagas são 5 
# O preço para Nova York e 4000 e a quantidade de vagas sao 3
# O preco para Tokyo é 6000 e a quantidade de vagas são 2 

# PREMISSAS 
# # Se pessoas > 3 → desconto de 10%
# SE A QUANTIDADE DE PESSOAS FORAM SUPERIOR A 3 TERÁ DESCONTO DE 10%

# # Se valor total > 10000 → desconto extra de 5%
# SE O VALOR TOTAL FOR SUPERIOR A 10000 TERÁ DESCONTO EXTRA DE 5% ALÉM DOS 10%

# # Se não houver vagas suficientes → taxa de 500 (overbooking)
# SE NÃO TIVER VAGAS SUFICIENTES, ACRESCIMO DE 500 

# # Se destino não existir → valor vira 0


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
# -----------------------------------------------------------

destino = input('Digite o Destino - ')

quantidade = int(input('Quantidade de Pessoas: '))

total = viagens[destino]["preco"]*quantidade
print('Valor Viagem',total)

desconto_sup3 = float(total * 0.1) * (quantidade > 3)
print('Desconto Extra', desconto_sup3)

desconto10 = float(total * 0.05) * (total > 10000)
print('Desconto acima' , desconto10)



# estrutura de dados -  espaço na memória

lista =  [
{
'nome': 'lucas',
'idade':25,
'e-mail':'lucas@gmail.com'
},

{
'nome': 'lucas',
'idade':25,
'e-mail':'lucas@gmail.com'
},

{
'nome': 'lucas',
'idade':25,
'e-mail':'lucas@gmail.com'
},

]



# mutavel #array
l = list(range(1,1000))
lista.append(100)

variaveis  =  'a' # mutavel

tupla = () # imutavel
tupla =  1,2,3,6,10
tuplas = (1,2,3,6,9)

print(tuplas[0])
t = tuple(range(1,200))


d = { 'a':10,'b':20},c = { 'a':10,'b':20}

dicionario = {

'nome':'lucas',
'idade':10,
'e-mail':'lucas@gmail.com',
'lista':[1,2,30],
'tupla':(456465,465465),
'd':{


}


}


 

# estruturas de fluxo de controle

# funções
print()
input()
len()
sum()

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx CORRETOOOOOOOOOOOOOOOOOOOOOOOOOOOO
# 1. Verificação de maioridade e permissão
# Enunciado:
# Crie um programa que leia a idade do usuário e se ele possui autorização dos pais (responda True ou False).
# O usuário pode participar da atividade se tiver 18 anos ou mais ou tiver autorização dos pais.
# Use and / or para verificar e exiba "Pode participar" ou "Não pode participar".
#SOLUÇÃO

# idade = int(input('Idade: '))
# autorizacao = input('Possui autorização: ')
# pode = (idade >=18) and (autorizacao)

# print('Pode participar? - ', pode)

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx CORRETOOOOOOOOOOOOOOOOOOOOOOOOOOOO 
# 2. Classificação de peso ideal
# Enunciado:
# Leia o peso (kg) e a altura (m) de uma pessoa. Calcule o IMC (peso / altura**2).
# Uma pessoa está com peso normal se o IMC estiver entre 18.5 e 24.9 (inclusive).
# Use operadores lógicos para verificar se o IMC está nessa faixa e exiba "Peso normal" ou "Fora da faixa".
#SOLUÇÃO


# peso = float(input('Digite seu peso:  '))

# altura = float(input('Digite sua altura: '))

# imc = peso/altura**2
# print(imc)

# peso_normal = imc >= 18.5 and imc<= 24.9

# v = peso_normal and 'Peso Normal' or 'Fora '
# print(v)



#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx CORRETOOOOOOOOOOOOOOOOOO
# 3. Acesso ao sistema
# Enunciado:
# Leia o nome de usuário e a senha. O acesso é permitido apenas se o usuário for "admin" e a senha for "1234".
# Use and para verificar as duas condições e exiba "Acesso liberado" ou "Acesso negado".
#SOLUÇÃO


# nome = str(input("Digite seu nome: "))
# senha = int(input("Digite sua senha: "))

# admin = nome == "admin" and senha ==1234

# v = admin and 'Acesso Liberado' or 'Acesso Negado'
# print(v)



#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# 4. Compra com desconto
# Enunciado:
# # Leia o valor da compra e
# compra = float(input("Digite o valor da compra: "))

# # E se o cliente é VIP (True ou False).
# vip = (input('é vip? '))

# maior100 = True
# menor100 = False
# vip = True
# nvip = False

# # O cliente ganha 10% de desconto se o valor for maior que R$ 100 ou ele for VIP.

# ganha = maior100 or vip

# # Exiba o valor final com desconto (se aplicável) ou o valor original.


# print desc * (ganha)
 
# desc = compra - compra * 0.1
# print(ganha)


# sim = compra 
# print(desc)

# vd = compra * 0.10 + compra

# vf = des and print(vd) or print(compra) 
# print(vf)
#SOLUÇÃO











#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# 5. Elegibilidade para doação de sangue
# Enunciado:
# Leia a idade = #idade = int(input("Digite seu idade: "))
# leia o peso = #peso = float(input('Digite seu peso: '))
# Para doar sangue, 
# a pessoa deve ter entre 16 e 69 anos ------xxxxxx  pode = idade >=16 or idade <=69 and peso >=50 
# (inclusive)
# e pesar pelo menos 50 kg.--------------xxxxxxxxxx npode = idade <16 or idade >69 and peso <50 

# Use and para verificar ambos os critérios e informe se a pessoa pode doar.

#print('Você pode doar', pode or 'Você não pode doar', npode)

#print(pode == 'Vc pode doar' or  npode == 'Não pode'  )

#SOLUÇÃO

# idade = int(input("Digite seu idade: "))

# peso = float(input('Digite seu peso: '))

# pode = idade >=16 or idade <=69 and peso >=50 
# npode = idade <16 or idade >69 and peso <50

# resu1 = ('Você pode doar', pode or 'Você não pode doar', npode)

# resu2 = print(re == 'Vc pode doar' or  npode == 'Não pode'  )

# print(resu1)


#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# 6. Validação de horário de funcionamento
# Enunciado:
# Uma loja funciona de segunda a sexta, das 9h às 18h.
# Leia o dia da semana (1=segunda, 7=domingo) e a hora (0 a 23).
# Determine se a loja está aberta.
# Dica: use and para combinar dia útil com horário, e or se quiser tratar sábado/domingo como fechado.
#SOLUÇÃO
# dia = int(input("Digite o dia: "))
# hora = float(input('Digite o horário: '))
# funcd = dia == 1,2,3,4,5
# funch = hora == 9,10,11,12,13,14,15,16,17,18

# #só estará aberta de segunda a sexta, 1 até 5, das 9 as 18 

# aberta = funcd == True and funch == True or "Fechada" 
# print(aberta)

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx CORRETOOOOOOOOOOOOOOOOOOOOOOOOO
# 7. Aprovação em duas disciplinas 
# Enunciado:
# Leia as notas de Matemática e Português.
# mat = float(input("Digite nota: "))
# port = float(input('Digite nota: '))

# # O aluno é aprovado se ambas as notas forem maiores ou iguais a 6.

# apro = mat >= 6 and port >= 6

# # Use and para verificar e exiba "Aprovado" ou "Reprovado".

# resu = apro and "Aprovado" or "Reprovado"
# print(resu)

#SOLUÇÃO


#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# 8. Identificação de ano bissexto
# Enunciado:
# Um ano é bissexto se for divisível por 4, mas não por 100, a menos que também seja divisível por 400.
# Leia um ano e use and e or para determinar se ele é bissexto.
# Exiba "Ano bissexto" ou "Ano não bissexto".
#SOLUÇÃO

# ano = int(input("Digite ano: "))

# ________ = ano == // (4) or //(400) not ano // (100)

# print(_______"Ano Bissexto" or "Ano não Bissexto")




#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# 9. Faixa etária
# Enunciado:
# Leia a idade e classifique:
# "Criança" se idade < 12
# "Adolescente" se 12 ≤ idade ≤ 17
# "Adulto" se idade ≥ 18
# Use and e or para definir os intervalos e exiba a classificação.

#SOLUÇÃO

idade = int(input("Digite idade: "))

crianca = idade <=12

# icria = icria <= 12
# iado = iado <=12 and < 17
# iadu = iadu >= 18


print("Você é criança" and crianca)



# classif = cria <12 "Criança" or ado > 12 and ado < 17 "Adolescente" or adu >= 18 "Adulto"
# print(classif)


# apro = mat >= 6 and port >= 6

# # Use and para verificar e exiba "Aprovado" ou "Reprovado".

# resu = apro and "Aprovado" or "Reprovado"







#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# 10. Sistema de alerta de temperatura e umidade
# Enunciado:
# Leia a temperatura (°C) e a umidade (%).
# Dispare um alerta se temperatura > 35 ou umidade > 70.
# Caso contrário, exiba "Condições normais".
# Use or para combinar as condições.

# t = float(input("Digite temperatura em Cº: "))
# u = float(input('Digite umidade em %: '))

# alerta = t > 35 and u > 70 == True
# print( alerta * 1 or alerta 'Condicoes normais ')









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







