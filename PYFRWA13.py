# ### **1. Classe Livro**

# # Crie uma classe `Livro` com:

# # - Atributos: `titulo`, `autor`, `ano`, `disponivel` (booleano, padrão True)
# # - Métodos:
# #     - `emprestar()`: se disponível, marca como False e exibe `"Livro emprestado"`; 
# #           senão, exibe `"Indisponível"`
# #     - `devolver()`: marca como True e exibe `"Livro devolvido"`
# #     - `info()`: mostra todas as informações do livro
        
# #         Crie dois livros, faça empréstimos e devoluções.

# class Livro:
#     def __init__(self, titulo, autor, ano, disponivel=True):
#         self.titulo = titulo
#         self.autor = autor
#         self.ano = ano
#         self.disponivel = disponivel
    
#     def emprestar(self):
#         if self.disponivel:
#            self.disponivel = False
#            print(f'"{self.titulo}" "Livro emprestado")              
        
#         else:
          
#             print(f'"{self.titulo}" "Livro Indisponível)

    
#     def info(self, titulo, autor, ano, disponivel):   
#         print(f"{self.titulo} {self.autor} {self.ano} {self.disponivel}")



# #agora eu vou declarar os objetos 

# livro1 = Livro("Amadeu", "Fonseca", 2025)

# livro2 = Livro("Joaquina", "Antonieta", 2005,)

# emprestar = Livro()
# livro1.emprestar()
# livro2.emprestar()

# devolver = Livro()
# livro1.devolver
# livro2.devolver()

# info = Livro()
# livro1.info()
# livro2.info()



# # ---

# # ### **2. Classe Funcionário**

# # Crie uma classe `Funcionario` com:

# # - Atributos: `nome`, `cargo`, `salario_base`
# # - Métodos:
# #     - `aumentar_salario(percentual)`: aumenta o salário com base no percentual
# #     - `calcular_bonus()`: retorna 10% do salário base
# #     - `exibir_dados()`: exibe todas as informações
        
# #         Crie um funcionário, aumente o salário e mostre os dados atualizados.


# class Funcionario:
#     def __init__(self, nome, cargo, salario_base):
#         self.nome = nome
#         self.cargo = cargo
#         self.salario_base = salario_base

#     def aumentar_salario(self, percentual):
#         self.salario_base = self.salario_base * (percentual/100)
        
#     def calcular_bonus(sel):
#        return self.salario_base * 0.10
    
#     def exibir_dados(self):

#         print(f"Nome: {self.nome}")
#         print(f"Cargo: {self.cargo}")
#         print("Salario Base: R$ {self.salario_base:.2f}")
#         print(f"Bonus (10%): r$ {self.calcular_bonus():.2f}")

              
        
# f1 = Funcionario("Sebastiao", "Gerente", 2500)

# f1.exibir.dados()

# f1.aumentar_salario(15)

# f1.calcular_bonus()





# # ### **3./ Classe Calculadora (estática)**

# # Crie uma classe `Calculadora` que **não precisa de atributos**. 
# # Apenas métodos de classe (use `@classmethod` ou métodos estáticos) para:

# # - `somar(a, b)`
# # - `subtrair(a, b)`
# # - `multiplicar(a, b)`
# # - `dividir(a, b)`
    
# #     Teste os métodos sem criar objetos (chamando diretamente pela classe).
    

# # ---

# # ### **4. Classe Carro com Controle de Velocidade**

# # Crie uma classe `Carro` com:

# # - Atributos: `marca`, `modelo`, `velocidade` (inicial 0)
# # - Métodos:
# #     - `acelerar(valor)`: aumenta a velocidade (não pode ultrapassar 200 km/h)
# #     - `frear(valor)`: diminui a velocidade (não pode ficar negativa)
# #     - `velocidade_atual()`: exibe a velocidade
        
# #         Crie um carro, acelere e freie até parar.

# # ### **5. Classe Agenda**

# # Crie uma classe `Agenda` que armazena contatos. Cada contato é um objeto da classe `Contato` (crie-a separada), com `nome`, `telefone` e `email`. A classe `Agenda` deve ter:

# # - Atributo: `contatos` (lista)
# # - Métodos:
# #     - `adicionar_contato(contato)`: adiciona à lista
# #     - `listar_contatos()`: exibe todos os contatos
# #     - `buscar_contato(nome)`: exibe os dados do contato (se existir)
        
# #         Crie alguns contatos, adicione-os à agenda e faça buscas.

# import random 

# # PEDRA PAPEL E TESOURA COM POO
# # JOGADOR CLASS

# class Jogador:
#     def escolher(self):
#         escolha = input('Escolha Pedra, papel ou Tesoura') 
#         return escolha.lower()
    
# class Maquina:
#         def escolher_maqui(self):
#             escolha = ['pedra', 'papel','tesoura']
#             return random.choice(escolha)
        
# class Jogo:
#     def verifica_vitoria(self, jogador, maquina):
          
#           if jogador == maquina:
#                return 'EMPATE'
#           elif jogador == 'pedra' and maquina == 'tesoura':
#                return 'você ganhou'
#           elif jogador == 'papel' and maquina  == 'pedra':
#                return 'você ganhou'
#           elif jogador == 'tesoura' and maquina  == 'papel':
#                return 'você ganhou'
#           else:
#                return 'maquina venceu...'
    
#     def jogar(self):
              
#         jogador = Jogador() # jogador
#         maquina = Maquina() # maquina 

#         escolher_jogador = jogador.escolher() # atrib. à variável método da escolha
#         escolher_maquina = maquina.escolher_maqui() #''

#         print('jogador escolheu', escolher_jogador)
#         print('maquina escolheu', escolher_maquina)

#         resultado =  self.verifica_vitoria(escolher_jogador, escolher_maquina)
#         print('RESULTADO -> ', resultado)
                    


# jogo = Jogo()
# jogo.jogar()

# # def contar():
# #     nome = input("Nome do arquivo")
# #     palavra = input("palavra: ")
# #     c = 0
# #     linhas = open(nome,"r")
# #     for linha in linhas:
# #         linha = linha.lower()
# #         c = c + linha.count(palavra.lower())
# #     nome.close()
# #     print(c)

# # contar()


# def contar():


#     nome =  input('Nome do arquivo: ')
#     palavra  =  input('palavra: ')


#     c  =  0
#     linhas  = open(nome, 'r')


#     for linha in linhas:
#         # print(linha)
#         linha = linha.lower()
#         c  =  c + linha.count(palavra.lower())
#     linhas.close()
#     print(c) 


# contar()     





#   def ler_l():
#     arquivo = open("teste.txt", "r")
#     linhas = arquivo.readlines()
#     print(len(linhas))
#     # arquivo.close()


# ler_l()     
        
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        
# def leitura(o, d):
    
   
    
#     origem = open(o, 'w')
#     origem.write('teste 1\n')
#     origem.write('teste 2\n')
#     origem.close()
    
#     with open(o, 'r') as c :
#         conteudo = c.read() 


        
#         destino = open(d, 'w')
#         destino.write(conteudo)
#         destino.close()
  
    
    
     


# o = input('Origem:')
# d = input('destino:')


# leitura(o,d)



