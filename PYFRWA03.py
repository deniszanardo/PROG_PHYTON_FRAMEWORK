# import statistics

# # sinais lógicos
# # sinais aritméticos
# # estruturas de dados
# # funções build
# # sinais aritmeticos
# # sinais lógicos
# # média 

# # Lógica de programação:

# # cadastrar o aluno
# # cadastrar as notas do aluno > ok
# # trazer média > nota
# # trazer a média da sala 
# # verificar qual a melhor média > media
# # verifica qual a pior média > todas as media
# # verificar de o aluno passou ou não >  medias

# dados_escola = {}

# nome_1 = input('Digite o nome: ')
# nome_2 = input('Digite o nome: ')
# nome_3 = input('Digite o nome: ')
# nome_4 = input('Digite o nome: ')

# dados_escola['alunos'] = []
# dados_escola['alunos'].extend([nome_1, nome_2, nome_3,nome_4])

# nota_aluno_1 = [float(input(f'Nota1 {nome_1}: ')), float(input(f'Nota2 {nome_1}: ')), float(input(f'Nota 3{nome_1}: '))]
# nota_aluno_2 = [float(input(f'Nota1 {nome_2}: ')), float(input(f'Nota2 {nome_2}: ')), float(input(f'Nota3 {nome_2}: '))]
# nota_aluno_3 = [float(input(f'Nota1 {nome_3}: ')), float(input(f'Nota2 {nome_3}: ')), float(input(f'Nota3 {nome_3}: '))]
# nota_aluno_4 = [float(input(f'Nota1 {nome_4}: ')), float(input(f'Nota2 {nome_4}: ')), float(input(f'Nota3 {nome_4}: '))]

# dados_escola['notas'] = []
# dados_escola['notas'].extend([nota_aluno_1,nota_aluno_2,nota_aluno_3, nota_aluno_4])

# media_aluno_1 = sum(dados_escola['notas'][0])/len(dados_escola['notas'][0])
# media_aluno_2 = sum(dados_escola['notas'][1])/len(dados_escola['notas'][1])
# media_aluno_3 = sum(dados_escola['notas'][2])/len(dados_escola['notas'][2])
# media_aluno_4 = sum(dados_escola['notas'][3])/len(dados_escola['notas'][3])

# n1 =  dados_escola['alunos'].index(nome_1)
# n2 =  dados_escola['alunos'].index(nome_2)
# n3 =  dados_escola['alunos'].index(nome_3)
# n4 =  dados_escola['alunos'].index(nome_4)

# print('-------------------------------------------')

# print('Media aluno',dados_escola['alunos'][n1], media_aluno_1)
# print('Media aluno',dados_escola['alunos'][n2], media_aluno_2)
# print('Media aluno',dados_escola['alunos'][n3], media_aluno_3)
# print('Media aluno',dados_escola['alunos'][n4], media_aluno_4)

# dados_escola['media_sala'] = []
# dados_escola['media_sala'].extend([media_aluno_1, media_aluno_2, media_aluno_3,media_aluno_4])

# print('-------------------------------------------')

# print('Medias da sala', dados_escola['media_sala'])

# maior = max(dados_escola['media_sala'])
# menor = min(dados_escola['media_sala'])

# i1 = dados_escola['media_sala'].index(maior)
# i2 =  dados_escola['media_sala'].index(menor)


# print('-------------------------------------------')

# print('Maior nota', maior, dados_escola['alunos'][i1])
# print('Menor nota', menor, dados_escola['alunos'][i2])


# print('-------------------------------------------')


# print('Aprovados: ')

# aprovado1 =  media_aluno_1 >= 7
# aprovado2 =  media_aluno_2 >= 7
# aprovado3 =  media_aluno_3 >= 7
# aprovado4 =  media_aluno_4 >= 7


# print('aluno situação', dados_escola['alunos'][0],'aprovado' ,aprovado1)
# print('aluno situação', dados_escola['alunos'][1],'aprovado' ,aprovado2)
# print('aluno situação', dados_escola['alunos'][2],'aprovado',aprovado3)
# print('aluno situação', dados_escola['alunos'][3],'aprovado' ,aprovado4)



# print(dados_escola)

# Como Mudar os Atalhos no VS Code
# Para mudar os atalhos do VS Code, basta seguir os seguintes passo:

# Abra o Visual Studio Code e acesse o menu “Arquivo” na barra de menus superior.
# Selecione a opção “Preferências” e, em seguida, selecione “Atalhos de Teclado”. Isso abrirá o arquivo “keybindings.json” que contém todas as configurações de atalhos do VS Code.
# Na janela “Atalhos de Teclado”, você pode visualizar todos os atalhos existentes. Selecione o atalho que deseja mudar e clique em “Editar” ou simplesmente clique no ícone de lápis ao lado do atalho.
# Na janela de edição, você pode alterar a combinação de teclas que deseja usar para o atalho. Por exemplo, se você quiser mudar o atalho para salvar o arquivo de “Ctrl + S” para “Ctrl + Shift + S”, basta alterar o valor na coluna “Quando”.
# Depois de fazer as alterações, salve o arquivo “keybindings.json”. As novas configurações de atalhos serão aplicadas automaticamente.
# # Atalhos VS Code
# # Aqui estão alguns dos atalhos mais úteis do VS Code:

# # Ctrl + Shift + P: Abre a caixa de comando, onde é possível pesquisar por funcionalidades específicas.

# # Ctrl + D: Seleciona a próxima ocorrência da palavra selecionada.

# # Ctrl + Shift + D: Duplica a linha atual.

# # Ctrl + Shift + L: Seleciona todas as ocorrências da palavra selecionada.

# # Ctrl + Shift + O: Ordena as linhas selecionadas em ordem crescente.

# # Ctrl + Shift + F: Abre a ferramenta de busca global, que permite pesquisar por um termo em todos os arquivos do projeto.

# # Ctrl + Shift + X: Abre a barra de extensões, onde é possível instalar e gerenciar extensões do VS Code.

# # Ctrl + N – Abre um novo arquivo.

# # Ctrl + Shift + N – Abre uma nova janela do VS Code.

# # Ctrl + S – Salva o arquivo atual.

# # Ctrl + Shift + S – Salva todos os arquivos abertos.

# # Ctrl + X – Recorta a seleção atual.

# # Ctrl + C – Copia a seleção atual.

# # Ctrl + V – Cola a seleção atual.

# # Ctrl + Z – Desfaz a última ação.

# # Ctrl + Shift + Z – Refaz a última ação.

# # Ctrl + F – Abre a barra de pesquisa.

# # Ctrl + Shift + F – Abre a pesquisa em todos os arquivos.

# # Ctrl + G – Vai para uma linha específica do arquivo.

# # Ctrl + Shift + L – Seleciona todas as ocorrências da seleção atual.

# # Ctrl + / – Comenta ou descomenta a seleção atual.

# # Alt + Shift + seta para cima – Move a linha atual para cima.

# # Alt + Shift + seta para baixo – Move a linha atual para baixo.

# # F12 – Vai para a definição do símbolo.

# # Alt + F12 – Abre a definição do símbolo em uma nova janela.

# # Ctrl + Shift + O – Abre a lista de símbolos do arquivo atual.
# # #FERRAMENTA DE CONECTA O GITHUB, COM O GIT 
# # O GITHUB É UMA REDE SOCIAL, '
# # O GIT É UMA FERRAMENTA DE VERSIONAMENTO 
# # MUITO DIFUNIDADA PARA O AMBIENTE DO DESENVOLVIMENTO 
# # COMINT É UMA ALTERAÇÃO CONTRIBUIÇÕES
# # PROBLEMAS = ISSUES  

# # estruturas de dados- estruturas de dado é uma palavra seguido de igual = 
# se é uma palavra seguida de um parenteses, é uma ação 
# # lista = []

# # variaveis = "a"
# nome = input('nome:')



# tupla = () #imutável 
# tupla = 1,2,3,4,5
# tuplas = (1,2,3,5,6,8)
# t = tuple(range(1,200))
# tupla += (100,30)
# tupla = tupla()


# d= {}
# dicionario = {
#     'nome':'lucas,
#     'idade':10,
#     'email':lucas@gmail.com', 
#     'lista':[1.2.3],
#     'tupla':(456465,464646)
#     'd',
# }



# # estruturas de fluxo de controle 



# # # funcoes
# # print()
# # input()
# # len()
# # sum()



# # paradigma
# estrutural 


# banco_de_dados = {}



# id = input('Digite o ID: ')
# produto = input('Produto: ')
# preco = float(input('Preço: '))


# banco_de_dados['ID'] = id
# banco_de_dados['Produtos']  = produto
# banco_de_dados['Preço'] = preco
# banco_de_dados['cursos'] = ['ads','adm','ingles']



# print(banco_de_dados['Preço'])


# banco_de_dados['cursos'].append('espanhol')


# lista = [10,20,30]
# #        0   1  2



# print(banco_de_dados.keys())

# banco_de_dados = {}



# id = input('Digite o ID: ')
# produto = input('Produto: ')
# preco = float(input('Preço: '))


# banco_de_dados['ID'] = id
# banco_de_dados['Produtos']  = produto
# banco_de_dados['Preço'] = preco
# banco_de_dados['cursos'] = ['ads','adm','ingles']



# print(banco_de_dados['Preço'])


# banco_de_dados['cursos'].append('espanhol')


# lista = [10,20,30]
# #        0   1  2



# print(banco_de_dados.keys())banco_de_dados = {}



# id = input('Digite o ID: ')
# produto = input('Produto: ')
# preco = float(input('Preço: '))


# banco_de_dados['ID'] = id
# banco_de_dados['Produtos']  = produto
# banco_de_dados['Preço'] = preco
# banco_de_dados['cursos'] = ['ads','adm','ingles']



# print(banco_de_dados['Preço'])


# banco_de_dados['cursos'].append('espanhol')


# lista = [10,20,30]
# #        0   1  2



# print(banco_de_dados.keys())

# # Sistema Bancário Simples

# # Mostre: SE PEDE PRA MOSTRAR É PRINT()

# # Saldo atual
# # Lista de transações

# # Peça: SE PEDE É INPUT 
# # Valor da operação (positivo depósito, negativo saque)

# # Calcule:
# # Novo saldo

# # Peça:
# # Valor da operação (positivo depósito, negativo saque)
# # Calcule:
# # Novo saldo


# # Parte 3: Regras do Banco

# # Aplique regras usando apenas lógica:

# # Se saldo final < 0 - cobrar taxa de 20
# # Se depósito > 500 - bônus de 10
# # Se saque maior que saldo - taxa extra de 15


# # Sem if



# # ---------------------------------

# # banco = {
# #     "Joao": {
# #         "saldo": 1500,
# #         "transacoes": [200, -100, 50]
# #     },
# #     "Maria": {
# #         "saldo": 800,
# #         "transacoes": [-200, -50, 300]
# #     },
# #     "Carlos": {
# #         "saldo": 1200,
# #         "transacoes": [500, -300, -100]
# #     }
# # }

# #-----------------------------------------






# # Parte 1: Escolha do Destino

# # Peça ao usuário:

# # Nome do destino

# # Quantidade de pessoas

# # Parte 2: Cálculo do Valor

# # Calcule:

# # # Valor total da viagem (preço * pessoas)

# # Parte 3: Regras da Agência (SEM if, SEM loop)

# # Aplique:
# # Se pessoas > 3 → desconto de 10%

# # Se valor total > 10000 → desconto extra de 5%

# # Se não houver vagas suficientes → taxa de 500 (overbooking)

# # Se destino não existir → valor vira 0


# #-----------------------------------------------

# # # ---------------------------------------------------------
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

# destino = input('Digite seu destino: ')

# print(viagens[destino])

# quantidade = input('Digite a quantidade de pessoas: ')

# print(quantidade)

# preco_total = 











