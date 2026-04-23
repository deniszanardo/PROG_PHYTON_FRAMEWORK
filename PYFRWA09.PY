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

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # ### **1. Tabuada Personalizada**

# # Peça ao usuário um número inteiro positivo. Use `for` para exibir a tabuada desse número de 1 a 10.

# # **Exemplo:**

# # `Digite um número: 7` → exibe 7 x 1 = 7, 7 x 2 = 14, ..., 7 x 10 = 70.

# # ---

# # ### **2. Contagem Regressiva com Pausa**

# # Peça um número inteiro positivo. Use `while` para fazer uma contagem regressiva até 0, exibindo cada número. Após o término, exiba `"Fogo!"`.

# # ---

# # ### **3. Média de Notas com `while`**

# # Peça notas até que o usuário digite `-1`. Calcule e exiba a média das notas válidas (0 a 10). Ignore entradas inválidas e use `continue` quando necessário.

# # ---

# # ### **4. Validação de Senha com Limite de Tentativas**

# # Defina uma senha fixa (ex: `"python123"`). Dê ao usuário 3 tentativas usando `while`. Se acertar, exiba `"Acesso liberado"` e encerre. Se errar todas, exiba `"Conta bloqueada"`.

# # ---

# # ### **5. Números Primos**

# # Peça um número inteiro positivo e determine se ele é primo. Use `for` com `range` e `break` para otimizar.

# # ---

# # ### **6. Sequência de Fibonacci**

# # Gere os primeiros N termos da sequência de Fibonacci, onde N é informado pelo usuário. Use `for` ou `while` para iterar.

# # ---

# # ### **7. Soma de Dígitos**

# # Peça um número inteiro positivo e calcule a soma de seus dígitos. Use `while` para extrair os dígitos um a um.

# # ---

# # EX8
# # ### **8 Menu Interativo** Crie um menu que permaneça ativo até que o usuário escolha a opção `"Sair"`. 
# # As opções podem ser: 
# # - `1` – Exibir mensagem "Olá!" -
# #  `2` – Exibir a data/hora atual (use `import datetime`) - 
# # `3` – Sair Use `while True` e `break` para sair.

# import datetime
# data = datetime.datetime.now()

# print(data)
# while True:
#     print("\n========MENu=========")
#     print("1 - Dizer olá")
#     print("1- ver data /hora atual")
#     print("3 - Sair")

#     opcao = input("\nEscolha uma opcao ")
#     if opcao == "1":
#         print("Olá seja bem vindo")
#     elif opcao =="2":
#         now = datetime.datetime.now()
#         print(f"opcao,Data e hora atual: {now}")
#     elif opcao == "3":
#         print("Saindo...Até logo")
#         break
#     else:
#         print("Opcao invalida ! Tente novamente")
                           
# # #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                               

# # ---

# # ### **9 Simulador de Lançamento de Dados**

# # Simule 100 lançamentos de um dado de 6 faces. Conte quantas vezes cada face foi sorteada e exiba o resultado. Use `for` e `random.randint(1,6)`. (Importe `random`.)

# # def teste():
# #     print('teste')


# # print('teste2')
# # teste()



# # variáveis global


# # a = 'teste 1'
# # def x():
# #     a = 'teste 2'
# #     print(a)
# # x()
# # print(a)    


# # # variáveis locais 


# # def y():
# #     nome = 'Paulo'
# # #     idade = 12
# # #     print(nome, idade)


# # # y()


# # # # globais

# # # nome = 'teste'
# # # def z():
# # #     global nome, idade, endereco
    
# # #     nome = 'Marcos'
# # #     idade  =  25
# # #     endereco = 'rua 10'



# # # # z()


# # # # print(nome)
# # # # # print(idade)
# # # # # print(endereco)


# # # def x(a=5,b=0,c =5):
# # #     print(a+b)


# # # x(10,200)
# # # x(110,20)
# # # x() 



# # # def mostra ():
# # #     return 'teste'

# # # print(mostra)



# # def soma(x,y):
# #     return x + y


# # def subtrair(x,y):
# #     return x - y


# # def multiplicar(x,y):
# #     return x * y


# # def dividir(x,y):
# #     try:
# #         return x / y
            
# #     except ZeroDivisionError as erro:
# #         return erro



# # def operacoes():


# #     op =  input(':>>>')
# #     x = int(input('>>>'))
# #     y = int(input('>>>'))
# #     if op == '+':
# #        s  =  str(soma(x,y))
# #        print(s) 
# #        print(type(s))
# #     elif op == '-':
# #        s  =  str(subtrair(x,y))
# #        print(s) 
# #        print(type(s))


# #     elif op == '*':
# #        s  =  str(multiplicar(x,y))
# #        print(s) 
# #        print(type(s))   
# #     elif op == '/':
# #        s  =  str(dividir(x,y))
# #        print(s) 
# #        print(type(s))   
# #     else:
# #         print('Digite algo válido')           
# # operacoes()
    