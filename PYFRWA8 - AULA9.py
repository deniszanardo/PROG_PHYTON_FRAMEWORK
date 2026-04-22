# import random
# import time
# from itertools import chain


# # # loop finito
# # # z = random.randint(1,10)
# # l = [1,2,3]

# # for i in l:
# #     l.append(i)
# #     print(l)

# # lista  = [1,2,3,4,5,6]
# # for x in lista:
# #     print(x)

# # for  z in list(range(1,11)):
# #     print(z)

# # x  =  [x for x in range(1,12) if x % 2 == 0]
# # print(x)


# #  ---------------------------------------
# # enquanto 

# # x  =  10 > 2

# # while x:
# #     print('teste')


# # c  = 0
# # while c <= 10:
# #     print(c)
# #     c  =  c  + 1
# #     time.sleep(2)

# # print('isso esta fora')

# # percorriveis  = iterar 

# # lista
# # tuplas 
# # 'texto'
# # conjuntos = {1,2,3}
# # dic  =  {'a':10, 'b':150}

# # # dict compressions  dicionarios 
# # dicionario =  {x: x ** 2 for x in range(10)}
# # print(dicionario)

# # # set compressions conjuntos 
# # range(10)
# # range(1,10)
# # range(1,10,2)

# # se =  {x for x in range(11)}

# # print(se)


# # lista = [x for x in range(1,7)]
# # print(lista)

# x = []
# for i in range(1,7):
#     x.append(i)
# print(x)    

# # crie um form e digite o nome de 3  pessoas

# # ln = []

# # for i in range(10):
# #     nome = input('nome: ')
# #     ln.append(nome)
# # print(ln)    



# # pergunta =  input('Digite sim ou não')
# # while pergunta  == 'sim':
# #     print('comprar')
# #     pergunta = input('Deseja continuar? >>>')
# # else:
# #     print('obrigada volte sempre')    


# # break 


# # lista  =  [1,2,3]
# # x = int(input('>>>'))
# # while x in lista:
# #     print(x)
# #     if x  % 2 == 0:
# #         break
# #     x = int(input('>>>'))

# # lista  =  [1,2,3]
# # x = int(input('>>>'))
# # while x in lista:
# #     print(x)
# #     if x  % 2 == 0:
# #         continue
# #     x = int(input('>>>'))


# # encadeamento

# # l1 = [1,2,3]
# # l2 = [1,2,3]
# # l3 = [1,2,3]

# # for x in chain(l1,l2,l3):
# #     print(x)

# # l = [x for x in chain(l1,l2,l3)]
# # print(l)

# l1 = [1,2,3]
# l2 = [1,2,3]
# l3 = [1,2,3]

# for i, valor in enumerate(l1, start=1):
#     print(f'{i}, {valor}')

#-----------------------------------exercicio aula anterior 




# v = int(input('>>'))


# if v < 10 or v > 1000 or v % 5 != 0:
#     print('invalida')
# else:
#     p50 = v // 50
#     v  =  v % 50


#     p20 = v // 20
#     v  =  v % 20


#     p10 = v // 10
#     v  =  v % 10


#     p5 = v // 5
#     v  =  v % 5    


#     print('notas de 50', p50)
#     print('notas de 20', p20)
#     print('notas de 10', p10)
#     print('notas de 5', p5)


# # upper torna a lista toda em mairuscula 
# z = list(map(str.upper,["Julia, fernanda"]))
# print(z)
# # # loop finito
# # # z = random.randint(1,10)

# l = [1,2,3]
# for i in l:
#     l.append(i)
#     print(l)

# lista  = [1,2,3,4,5,6]
# for x in lista:
#     print(x)

# # for  z in list(range(1,11)):
# #     print(z)

# # x  =  [x for x in range(1,12) if x % 2 == 0]
# # print(x)

# ___________________________________________________________________________________________________________________________________________________________________________________
## **2  - Exercícios**

# ### **1. Tabuada Personalizada**

# Peça ao usuário um número inteiro positivo. 
# Use `for` para exibir a tabuada desse número de 1 a 10.

# **Exemplo:**

# `Digite um número: 7` → exibe 7 x 1 = 7, 7 x 2 = 14, ..., 7 x 10 = 70.

# tab = int(input("Digite n: "))
# for count in range(10):
#     c = count * tab
#     print(tab,"x", count, "=", c)



# contador = 0
# while contador < 15:
#     print(contador)
#     contador +=1




# x = []
# for i in range(1,7):
#     x.append(i)
# print(x)


# ---
# # ___________________________________________________________________________________________________________________________________________________________________________________

# ### **2. Contagem Regressiva com Pausa**

# Peça um número inteiro positivo. Use `while` para fazer 
# uma contagem regressiva até 0, exibindo cada número. 
# Após o término, exiba `"Fogo!"`.

# contador = 10
# while contador >0:
#     print(contador)
#     contador -=1
# print("fogo")


# ---

# ### **3. Média de Notas com `while`**

# Peça notas até que o usuário digite `-1`. 
# Calcule e exiba a média das notas válidas (0 a 10). 
# Ignore entradas inválidas e use `continue` quando necessário.

# ---
# # ___________________________________________________________________________________________________________________________________________________________________________________

# ### **4. Validação de Senha com Limite de Tentativas**

# Defina uma senha fixa (ex: `"python123"`). 
# Dê ao usuário 3 tentativas usando `while`. 
# Se acertar, exiba `"Acesso liberado"` e encerre. 
# Se errar todas, exiba `"Conta bloqueada"`.


# contador = 3
# while contador > 0:
#     print(contador)
#     contador -=1
#     print("acesso negado")






# ---
# # ___________________________________________________________________________________________________________________________________________________________________________________

# ### **5. Números Primos**

# Peça um número inteiro positivo e determine se ele é primo. Use `for` com `range` e `break` para otimizar.

# ---
# # ___________________________________________________________________________________________________________________________________________________________________________________

# ### **6. Sequência de Fibonacci**

# Gere os primeiros N termos da sequência de Fibonacci, onde N é informado pelo usuário. Use `for` ou `while` para iterar.

# ---
# # ___________________________________________________________________________________________________________________________________________________________________________________

# ### **7. Soma de Dígitos**

# Peça um número inteiro positivo e calcule a soma de seus dígitos. 
# Use `while` para extrair os dígitos um a um.

# ---
# # ___________________________________________________________________________________________________________________________________________________________________________________

# ### **8 Menu Interativo**

# Crie um menu que permaneça ativo até que o usuário escolha a opção `"Sair"`. As opções podem ser:

# - `1` – Exibir mensagem "Olá!"
# - `2` – Exibir a data/hora atual (use `import datetime`)
# - `3` – Sair

# Use `while True` e `break` para sair.

# ---

# ### **9 Simulador de Lançamento de Dados**

# Simule 100 lançamentos de um dado de 6 faces.
# Conte quantas vezes cada face foi sorteada e exiba o resultado. 
# Use `for` e `random.randint(1,6)`. (Importe `random`.)

# for and `random.randint(1,6)`. (Importe `random`.)


import random

# Crie um programa que leia 
# a nota de um aluno (0 a 10) e exiba 
# a menção correspondente:

# nota  =  float(input('>>>  '))
# if nota  >= 9:
#     print('Excelente')
# elif nota >= 7 and nota <9:
#     print('Bom')
# elif nota >=5  and nota <9:
#     print('Regular')
# else:
#     print('insuficiente...')    



# # - `"Excelente"` se nota >= 9
# # - `"Bom"` se nota >= 7 e < 9
# # - `"Regular"` se nota >= 5 e < 7
# # - `"Insuficiente"` se nota < 5



# # # 2

# l1  =  float(input('lado 1 '))
# l2  =  float(input('lado 2 '))
# l3  =  float(input('lado 3 '))

# if l1 == l2 == l3 == l1:
#     print('equilatero')
# elif l1 != l2 != l3 != l1:
#     print('escaleno')
# else:
#     print('Isosceles')        

# 3

# peso =  float(input('Peso: '))
# altura  =  float(input('Altura: '))

# imc  = peso/(altura ** 2)
# print(imc)

# if imc < 18: print('abaixo do peso')
# elif imc>= 18 and imc <25:print('Peso normal')
# elif imc >=25 and imc <30:print('Sobrepeso')
# else:print('Obesidade') 

# try:
#     salario = float(input('Salário: '))

#     if salario >= 1501.00 and salario <= 2500.0:
#         if salario <= 1500.0:
#            print('Insento.. R$', salario )
#         sal =  salario
#         desconto_i = salario * 0.11
        
#         print('desconto INSS:', desconto_i )
#         print('Liquido ', sal - desconto_i )   
#     elif salario > 2500.0 and salario <= 3500.0:
#         sal =  salario
#         desconto =  salario * 0.075
#         inss =  salario * 0.11
#         print('desconto', desconto)
#         print('liquido', sal - desconto  + inss)  
#     elif salario > 3500.0 and salario <= 5000.0:
#         sal =  salario
#         desconto =  salario * 0.15
#         inss =  salario * 0.11
#         print('desconto', desconto)
#         print('liquido', sal - desconto  + inss )        
#     elif salario > 5000.0:
#         sal =  salario
#         desconto =  salario * 0.275
#         inss =  salario * 0.11
#         print('INSS', inss)
#         print('desconto', desconto)
#         print('liquido', sal - desconto + inss ) 
# except ValueError:
#        print('Digite algo válido')        


# 5 


# lista_opcoes  =  ['Pedra', 'Papel', 'Tesoura']
# aleatorio =  random.choice(lista_opcoes)
# escolha = input(f'Escolha: {lista_opcoes}')

# if aleatorio == escolha:
#     print('Empate')
# elif aleatorio == 'Pedra' and escolha == 'Tesoura':
#     print('Maquina ganhou!')
# elif aleatorio == 'Tesoura' and escolha == 'Papel':
#     print('Maquina ganhou!')
# elif aleatorio == 'Papel' and escolha == 'Pedra':
#     print('Maquina ganhou')  
# else:
#     print('Voc ganhou! ')     

# # elif aleatorio == 'Tesoura' and escolha == 'Pedra':
# #     print('Você ganhou!')
# # elif aleatorio == 'Papel' and escolha == 'Tesoura':
# #     print('Você ganhou!')
# # elif aleatorio == 'Pedra' and escolha == 'Papel':
# #     print('Você ganhou!')   

# print('escolha da maquina -- ', aleatorio)
# print('Minha escolha -- ', escolha)

# 7


# ano = int(input('Ano: '))
# sexo =  input('f ou m')
# deficiencia = input('sim ou não')

# idade  =  2026 - ano


    
# if sexo == 'f':
#     print('Não obrigatório')
# elif sexo == 'm' and  idade == 18 and deficiencia == 'não':
#     print('Aliste-se imediatamente') 
# elif sexo == 'm' and  idade >= 18 and deficiencia == 'sim':
#     print('Dispensado por saúde')
# elif sexo == 'm' and  idade < 18 and deficiencia == 'não':
#     mes = int(input('Mês: '))
#     print('Idade: ', idade)
#     print('Faltam : ',18 -  idade, 'anos... e', 8 - mes, 'meses' )
# elif idade > 18   and idade <=45:
#     print('Já passou do prazo')
# elif idade > 45:
#     print('Dispensado por idade')     
             
# 8

# idade =  int(input('Idade: '))
# plano =  input('b, s, p')

# if plano == 'b' and idade <= 60:
#     valor  =  (idade * 2) + 100
#     print('R$', valor)
# elif plano == 's' and idade <= 60:
#     valor  =  (idade * 3) + 150
#     print('R$', valor)    

# elif plano == 'p' and idade <= 60:
#     valor  =  (idade * 5) + 200
#     print('R$', valor)  

# else:
#     valor  =  (idade * 5) + 200
# #     print(valor) 
# #     acrescimo =  valor * 0.10
# #     print(acrescimo)
# #     print('R$', valor +acrescimo)   


# ano = int(input('Ano: '))
# dia = int(input('Dia: '))
# mes = int(input('mes: '))

# meses = [1,2,3,4,5,6,7,8,9,10,11,12]
# bissexto = (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)
# print('Ano bissexto: ', ano and bissexto and 'é bissexto' or 'não é bissexto' )

# dias_meses = [
#     list(range(1,31)),  # 1
#     list(range(1,28)) if bissexto else list(range(1,29)),
#     list(range(1,31)), # 3
#     list(range(1,30)),  # 4
#     list(range(1,31)),  # 5
#     list(range(1,30)),  # 6
#     list(range(1,31)),  # 7
#     list(range(1,31)),  # 8
#     list(range(1,30)),  # 9
#     list(range(1,31)), # 10 
#     list(range(1,30)),  # 11
#     list(range(1,31))   # 12
# ]

# if mes in meses:
#     posicao = meses.index(mes)
#     if dia in dias_meses[posicao]:
#         print('Data válida')
#     else:
#         print('Dia inválido no mês...')
# else:
#     print('nao existe ')




# 10
valor  =  int(input('R$: '))

# valor entre 10 e 1000
# # 50, 20, 10, 5


l = [5,10,20,50]

if valor % 5 == 0:

    if valor == 10:
        quatidade_notas =  1
        print('R$', quatidade_notas)   
    elif valor  == 20 :
        quatidade_notas =  1
        print('R$', quatidade_notas)   
    elif valor == 50:
        quatidade_notas =  1
        print('R$', quatidade_notas)
    elif valor > 50:
         quantidade_notas_50 = valor // 50
         print(quantidade_notas_50,'notas de R$ 50')
         if quantidade_notas_50 * valor < valor:
             resto = quantidade_notas_50 -  valor
             print(resto)       
        
#          print(quantidade_notas_50)
#          quantidade_notas_20 = valor//20
#          print(quantidade_notas_20)
#          quantidade_notas_10 =  valor // 10
#          print(quantidade_notas_10)
#          quantidade_notas_5 =  valor // 5
#          print(quantidade_notas_5)

#          if quantidade_notas_50 * valor + quantidade_notas_20 * valor == valor:
#              print('Quantidade de notas 20 - ', quantidade_notas_20, '50')
#              print('Quantidade de notas 50 - ', quantidade_notas_50, '20')
#          elif quantidade_notas_50 * valor + quantidade_notas_20 * valor + quantidade_notas_10 * valor == valor:    
#              print('Quantidade de notas 20 - ', quantidade_notas_20)
#              print('Quantidade de notas 50 - ', quantidade_notas_50)
#          elif quantidade_notas_50 * valor + quantidade_notas_20 * valor + quantidade_notas_10 * valor + quantidade_notas_5 *5 == valor :   
#              print('Quantidade de notas 20 - ', quantidade_notas_20)
#              print('Quantidade de notas 50 - ', quantidade_notas_50)         
#              print('Quantidade de notas 20 - ', quantidade_notas_10)
#              print('Quantidade de notas 5 - ', quantidade_notas_5)
         
     


         
        
else:
    print('Erro ...')        



# # if valor % 10 and valor % 5 and valor % 50 and valor % 10:
# #     quantidade =  
# #     print()



    
