# # def cpf2():


# #     cpf  =  input('CPF: ')
# #     soma  = 0


# #     for i in range(9):
# #         soma += int(cpf[i]) * (10 - i)
    
# #     nu1 = soma * 10
# #     x1 = nu1 % 11
# #     if x1 == 10:
# #         x1 = 0
# #     print(x1)



# #     soma = 0
# #     for i in range(10):
# #         soma += int(cpf[i]) * (11 - i)


# #     nu2 = soma * 10
# #     x2 = nu2 % 11
# #     if x2  == 10:
# #         x2  = 0
# #     print(x2)
   
   
    
# #     if x1 ==  int(cpf[-2] and x2 ==  int(cpf[-1])):
# #         print(True)
# #     else:
# #         print(False)    


# # cpf2()




# # tabuada 


# # def tabuada(numero, inicio=1, fim=10):
# #     for x in range(inicio,fim):
# #         c  = x * numero
# #         print( c)
     


# # def mostrar():
# #     tabuada(5,0,11)


# # mostrar()    



# #


# # def contar_palavras(palavras_texto):
# #     palavra = palavras_texto.split()
# #     d =  {}
# #     for i in palavra:
# #         if i in d:
# #             d[i] += 1
# #         else:
# #             d[i] = 1    
        
# #     print(d)


# # contar_palavras('olá olá bom dia')    


# # def ordenar_lista(lista):
# #     x = 0
# #     for i in range(len(lista)):
# #         for j in range(len(lista) - 1):
# #             if lista[i] > lista[j]:
# #                 x  = lista[j]
# #                 lista[j] = lista[j+1]
# #                 lista[j+1] = x
# #             # else:
# #             #     lista[j] = x 
# #             #     lista[j+1] =  lista[j]
# #             #     x = lista[j+1] 


# #         print(lista)        


# # ordenar_lista([10,15,61,2,1,35])

# # EX 2
# # n1 = int(input("Digite qualquer número de 1 a 9: "))

# # if n1 % 2 == 0: #se o n1 for divisivel por 2 e sobrar nada 
# #     print(f"{n1} é par") # então ele é par 
# # else: #se não 
# #     print(f"{n1} é ímpar")


# # 6. Maior de três
# # Dados três números, diga qual é o maior.

# # n1 = int(input("Digite qualquer número de 1 a 9: "))
# # n2 = int(input("Digite qualquer número de 1 a 9: "))
# # n3 = int(input("Digite qualquer número de 1 a 9: "))
 
# # if n1 > n2:
# # print(n1)

# # elif n1 > n3:
    
# #     if n2 > n1 or n2 >n3:
    
# # #     print(n2)
# # #     if n3 > n2 or n3 > n1:
# # #     print(n3)
# # else:

# # palavra = input( "Digite")
# # invertida = palavra [::-1]
# # print(f'Palavra invertida: {invertida}')

# # 4. FizzBuzz
# # Para números de 1 a 20:

# # Se divisível por 3, imprima "Fizz"
# # Se divisível por 5, imprima "Buzz"
# # Se divisível por ambos, imprima "FizzBuzz"
# # Caso contrário, imprima o número

# ### **4. Validação de Senha com Limite de Tentativas**>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # Defina uma senha fixa (ex: `"python123"`). Dê ao usuário 3 tentativas usando `while`. Se acertar, exiba `"Acesso liberado"` e encerre. Se errar todas, exiba `"Conta bloqueada"`.


# # ### **5. Números Primos*>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>*

# # Peça um número inteiro positivo e determine se ele é primo. Use `for` com `range` e `break` para otimizar.


# ### **6. Sequência de Fibonacci**>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # Gere os primeiros N termos da sequência de Fibonacci, onde N é informado pelo usuário. Use `for` ou `while` para iterar.

# # ### 



# # EX7. Soma de Dígitos**>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # Peça um número inteiro positivo e calcule a soma de seus dígitos. Use `while` para extrair os dígitos um a um.



# # ### **1. Tabuada Personalizada**>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # Peça ao usuário um número inteiro positivo. Use `for` para exibir a tabuada desse número de 1 a 10.

# # **Exemplo:**

# # `Digite um número: 7` → exibe 7 x 1 = 7, 7 x 2 = 14, ..., 7 x 10 = 70.

# # ---

# # ### **2. Contagem Regressiva com Pausa**>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # Peça um número inteiro positivo. Use `while` para fazer uma contagem regressiva até 0, exibindo cada número. Após o término, exiba `"Fogo!"`.

# # ---

# # ### **3. Média de Notas com `while`**>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # Peça notas até que o usuário digite `-1`. Calcule e exiba a média das notas válidas (0 a 10). Ignore entradas inválidas e use `continue` quando necessário.

# # ---

# # ### **4. Validação de Senha com Limite de Tentativas**>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # Defina uma senha fixa (ex: `"python123"`). Dê ao usuário 3 tentativas usando `while`. Se acertar, exiba `"Acesso liberado"` e encerre. Se errar todas, exiba `"Conta bloqueada"`.

# # ---

# # ### **5. Números Primos**>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # Peça um número inteiro positivo e determine se ele é primo. Use `for` com `range` e `break` para otimizar.

# # ---

# # ### **6. Sequência de Fibonacci**>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # Gere os primeiros N termos da sequência de Fibonacci, onde N é informado pelo usuário. Use `for` ou `while` para iterar.

# # ---

# # # ### **7. Soma de Dígitos**>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # # Peça um número inteiro positivo e calcule a soma de seus dígitos. Use `while` para extrair os dígitos um a um.

# # # ---

# # # EX8 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# # # ### **8 Menu Interativo** Crie um menu que permaneça ativo até que o usuário escolha a opção `"Sair"`. 
# # # As opções podem ser: 
# # # - `1` – Exibir mensagem "Olá!" -
# # #  `2` – Exibir a data/hora atual (use `import datetime`) - 
# # # `3` – Sair Use `while True` e `break` para sair.

# # import datetime
# # data = datetime.datetime.now()

# # print(data)
# # while True:
# #     print("\n========MENu=========")
# #     print("1 - Dizer olá")
# #     print("1- ver data /hora atual")
# #     print("3 - Sair")

# #     opcao = input("\nEscolha uma opcao ")
# #     if opcao == "1":
# #         print("Olá seja bem vindo")
# #     elif opcao =="2":
# #         now = datetime.datetime.now()
# #         print(f"opcao,Data e hora atual: {now}")
# #     elif opcao == "3":
# #         print("Saindo...Até logo")
# #         break
# #     else:
# #         print("Opcao invalida ! Tente novamente")
                           
# # #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                               
# # ---
# # ### **9 Simulador de Lançamento de Dados**
# # Simule 100 lançamentos de um dado de 6 faces. Conte quantas vezes cada face foi sorteada e exiba o resultado. Use `for` e `random.randint(1,6)`. (Importe `random`.)


# # def saudacao(nome):          # nome é um parâmetro
# #     print(f"Olá,{nome}")

# # saudacao("Maria") 


# # def adeus(nome):
# #     print(f"Foi bom te conhecer,{Juan}")
    

# # # print("A" \
# # # "deus")

# # x = 10      # global

# # def alterar():
# #     global x
# #     x = 20   # modifica a global

# # alterar()
# # print(x)    # 20
# # #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # ## **Exercícios de Nível Médio**

# # ### **1. Calculadora com Funções**

# # Crie funções separadas para as quatro operações básicas 
# # (`somar`, `subtrair`, `multiplicar`, `dividir`). 
# # Em seguida, 
# # escreva um programa que leia dois números e a operação desejada (como string) e chame a função correspondente. 
# # A divisão deve tratar divisão por zero.


# # def soma(a , b):
# #     return( a + b)

# # def subtracao(a , b):
# #     return(a - b)

# # def multiplicacao(a , b):
# #     return(a * b)

# # def divisao(a , b):
# #     if b == 0:
# #         return "Erro"
# #     return a / b

# # def calculadora( a, b, operacao):
# #     operacoes = {
# #         "somar"        somar, 
# #         "subtrair"     subtrair,
# #         "multiplica"   multiplicação,
# #         "dividir"      dividir, 
# #     }

# #     operacao = operacao.strip().lower

# # #     if operacao not in operacoes:
# # #         return f"Erro: operacao '{operacao}'


# # # ### **2. Validador de CPF (simplificado)**>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # # Crie uma função `validar_cpf(cpf)` que recebe uma string com 11 
# # # dígitos e retorna `True` se for válido
# # #  (use o algoritmo básico de validação de CPF).
# # #  Em seguida, teste a função com alguns CPFs.

# validar_cpf = int(input("Digite CPF: "))

# qtde = len(str(validar_cpf))
# if qtde == 11:
#     print("Passou na verificação de 11 digitos")
# else:
#     print("Digite novamente o cpf")


# def validar_cpf1(a,b,c,d,e,f,g,h,i):
#     return(a * 10, b * 9, c * 8, d * 7, e * 6, f * 5, g * 4, h * 3, i * 2)
#     return(validar_cpf1 * 10 / 11)
# if validar_cpf1 == 2:
#     print("PASSOU NA VERIFICAÇÃO 1")
# else:
#     print("PASSOU NA VERIFICAÇÃO 1")
        

# def validar_cpf2(a,b,c,d,e,f,g,h,i,j):
#     print(a * 11, b * 10, c * 9, d * 8, e * 7, f * 6, g * 5, h * 4, i * 3, j * 2)
#     print(validar_cpf2 * 10 / 11)
# if validar_cpf2 == 2:
#     print("PASSOU NA VERIFICAÇÃO 1")
# else:
#     print("PASSOU NA VERIFICAÇÃO 2")


# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>







# # cpf = int(input("Digite CPF"))

# # def validar_cpf(cpf):
# # # Verifica se tem 11 dígitos e se são todos numéricos
# #     if len(cpf) != 11 or not cpf.isdigit():
# #         return False

# #     # --- Validação do 1º dígito verificador ---
# #     soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
# #     resto = (soma * 10) % 11
# #     if resto == 10 or resto == 11:
# #         resto = 0
# #     if resto != int(cpf[9]):
# #         return False

# #     # --- Validação do 2º dígito verificador ---
# #     soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
# #     resto = (soma * 10) % 11
# #     if resto == 10 or resto == 11:
# #         resto = 0
# #     if resto != int(cpf[10]):
# #         return False

# #         return True















# # ### **3. Gerador de Tabuada**

# # Escreva uma função `tabuada(numero, inicio=1, fim=10)` que exibe a tabuada do `numero` no intervalo `[inicio, fim]`. Se os argumentos `inicio` e `fim` não forem fornecidos, use 1 e 10.

# # ### **4. Contador de Palavras**

# # Crie uma função `contar_palavras(texto)` que retorna um dicionário com a contagem de cada palavra no texto (considere palavras separadas por espaços). O programa principal deve ler uma frase e exibir o resultado.

# # ### **5. Ordenação Personalizada**

# # Implemente uma função `ordenar_lista(lista, crescente=True)` que retorna uma nova lista ordenada. Se `crescente=True`, ordena em ordem crescente; caso contrário, decrescente. Não use `sorted()` ou `list.sort()` (implemente o algoritmo de ordenação de sua escolha, como bolha).

# # ### **6. Jogo de Adivinhação**

# # Crie uma função `jogar()` que sorteia um número entre 1 e 100 e dá dicas ("maior", "menor") até o usuário acertar. Use `random.randint()`. A função deve retornar o número de tentativas. No programa principal, chame a função e exiba quantas tentativas foram necessárias.