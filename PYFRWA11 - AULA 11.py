# # ### **6. Jogo de Adivinhação**


# # Crie uma função `jogar()` que sorteia um número entre 1 e 100 e dá dicas ("maior", "menor") até o usuário acertar. Use `random.randint()`. A função deve retornar o número de tentativas. No programa principal, chame a função e exiba quantas tentativas foram necessárias.



# import random

# 

# def jogar():
#     n_a = random.randint(1,10)
    
    
#     c = 0
#     while c <= 100: 
#         escolha  =  int(input('1 à  100 >>> '))
#         if escolha  == n_a:
#             print('acertou!')
#             c = c + 1
#             print('Tentativas - ', c )
#             break
#         elif escolha > n_a:
#             print('É menor...')
#             c = c + 1
#             print('Tentativas - ', c )
#         elif escolha < n_a:
#             print('É maior... ')        
#             c = c + 1
#             print('Tentativas - ', c )
#         else:
#             print('Digite algo válido...')    
# jogar()

def sacar(valor):



    l =  [100,50,20,10,5,2]
    d  =  {}


    
    if valor % 2 != 0 or valor <= 0:
        return None
    
    for x in l:
        q  =  valor //  x
        d[x] = q  
        valor %= x
    return d


# print(sacar(350))

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def analisar_lista(lista):
    
    # menor
    menor  =  min(lista)
    # maior
    maior = max(lista)
    # soma 
    soma  =  sum(lista)
    # media 
    media  =  soma / len(lista)
    
    l =  []


    l.extend([menor, maior, soma, media])


    a,b,c,d = l


    print(a,b,c,d)
       


    return [menor, maior, soma , media]


analise  =  analisar_lista([1,2,3,20,3040,150,0,66,99,10])


print(analise)



estoque  =  []


def adicionar_produto(nome, quantidade):
    estoque.append([{nome:quantidade}])
  
    return estoque 


# print(adicionar_produto('x', 2))


def remover_produto(i):
    estoque.pop(i)
    return estoque
   



def listar_estoque():
    return estoque


def main():
  adicionar_produto('x', '0')
  while True:  
    menu =  int(input('''


                1 - add
                2 - remover
                3 - listar            



                '''))


    if menu == 1:
       prod = input('Nome produto: ')
       q  =  int(input('Quantidade: '))
       print(adicionar_produto(prod, q))


    elif menu == 2:
        print(listar_estoque())
        prod = int(input('Nome produto: '))
        remover_produto(prod)
        
    elif menu == 3:
        print(listar_estoque())





main()

# 1. **Criar e escrever**
    
#     Crie um programa que peça ao usuário um nome e uma idade, 
# e grave essas informações em um arquivo chamado `cadastro.txt`, 
# uma pessoa por linha no formato `"nome,idade"`. O programa deve permitir adicionar várias pessoas até que o usuário digite `"sair"`.



def escrever_mostrar(): #define a funcção escrever
    c = input('Deseja cadastra? sim ou sair') #cria a variavel para perguntar se deseja sim ou sair
    while c == 'sim': # cria o looping enquanto o usuario digitar "sim" ele repete a sequencia
        nome =  input('nome: ') # define a variavel do tipo texto, 
        idade =  int(input('Idade:  ')) #define a variavel do tipo idade, usando o int, numero inteiro 
        arquivo = open("cadastro.txt", "a") # cria o arquivo dentro do vs, com o nome desejado, e usa o tipo "A", que é append, acrescentar, 
        arquivo.write(f"nome - {nome} idade - {idade}\n") # escreve os dados das duas pessoas no arquivo, pulando linha com a inclusão do \n no final, esse f é fstring que permite inserir variaveis dentro do texto, tipo o resultado inserido e o \n quebra a linha, que quer dizer que pula para a proxima linha 
        nome2 =  input('nome: ') #define a variavel nome2 do tipo texto
        idade2 =  int(input('Idade:  ')) #define a variavel do tipo inteira 
        arquivo.write(f"nome - {nome2} idade - {idade2}\n") #
        c = input('Deseja cadastra? sim ou sair')
        
    else:
        arquivo.close()
        print('Saiu...')
escrever_mostrar()

# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# # 2. **Ler e exibir**
    
# #     Escreva um programa que leia o arquivo `cadastro.txt` criado no exercício anterior 
# # e exiba na tela cada pessoa no formato `"Nome: [nome], Idade: [idade]"`.
    


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# # 3. **Contar linhas**
    
# #     Crie uma função `contar_linhas(nome_arquivo)` que retorna o número de linhas do arquivo. 
# # Teste com o arquivo `cadastro.txt`.




# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# # 4. **Procurar palavra**
    
# #     Peça ao usuário uma palavra e um nome de arquivo. Conte quantas vezes essa palavra aparece no arquivo
# # (ignorando maiúsculas/minúsculas). Exiba o resultado.

# funcao para localizar maiusucula e minuscula
# upper()
# lower()


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# # 5. **Copiar arquivo**
    
# #     Peça ao usuário o nome de um arquivo de origem e um arquivo de destino. 
# # Copie o conteúdo do arquivo de origem para o destino, mantendo as linhas.


