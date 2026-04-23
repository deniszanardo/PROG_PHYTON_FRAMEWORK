


# # POO DEFINICÇÃO 

# # class Aluno: #CLASSE É UMA DEFINIÇÃO QUE NÃO OCUPA ESPAÇO NA MEMÓRIA, É UM MODELO UM PADRÃO, QUE DEFINE QUAIS ATRIBUTOS E METODOS UM OBJETO TERÁ 
# #     def __init__(self, nome, nota):
# #         self.nome = nome #ATRIBUTO 1 "NOME" DO OBJETO "ALUNO" 
# #         #O OBJETO É A CONCRETIZAÇÃO DA CLASSE
# #         self.nota = nota #ATRIBUTO  2 NOTA DO OBJETO "ALUNO" 
# #         #ATRIBUTOS SÃO AS CARACTERISTICAS DO OBJETO, DEFINIDAS DENTRO DA CLASSE, NO EXEMPLO DO ALUNO, OS ATRIBUTOS SÃO NOME E NOTA 

# #     def exibir(self): #METODOS SÃO AS FUNÇÕES QUE PERTECEM AO OBJETO, O PRIMEIRO PARAMETRO DE UM MÉTODO É SEMPRE O "SELF", QUE REPRESENTA O PROPRIO OBJETO
# #         print(f"{self.nome} tirou{self.nota}")

# # # Criando um objeto aluno
# # aluno1 = Aluno("João", 8.5)
# # aluno1.exibir()


# # COMO CRIAR UMA CLASSE EM PYTHON, 

# # class Teste:
# #     def_init_(self, parametro) #o metodo init é o construtor, ele é automaticamente executado, quando voce cria um objeto, 
# #     serve para configurar os valores iniciais dos atributos
# #     o parametro self é uma referencia para o proprio objeto, ex: self.nome, eu estou dizendo, dentro deste objeto, guarde um valor chamado nome 

# # exemplo 

# # # class carro: #criação da classe 
# # #     def_init_(self, marca, modelo, ano): #criação do objeto
# # #     self.marca = marca #atributos que são as caracteristicas do objeto 
# # #     self.modelo = modelo #atributos que são as caracteristicas do objeto 
# # #     self.ano = ano #atributos que são as caracteristicas do objeto 


# # #     MÉTODO É UM CONJUNTO DE PARAMETROS 
    
# # #     def ligar(self): # PARAMETRO 1 LIGADO 
# # #         self.ligado = True = #SE SIM, 
# # #         print(f"{self.modelo} esta ligado.") 

# # #     def desligar(self): # PARAMETRO 2 DESLIGADO
# # #         self.desligado = False #SE NÃO, 
# # #         print(f"{self.modelo} esta desligado.")

# # #     def status(self): # PARAMETRO 3 CRIA UMA VARIAVEL "ESTADO" CHAMA OS DOIS PARAMETROS SUPERIORES  
# # #         estado = "ligado" if self.ligado else "desligado" # SE SELF.LIGADO FOR VERDADEIRO PRINTA "ligado" se sel.ligadodo for falso, "printa" "delisgado"

# # #         print(f"{self.modelo} ({self.marca}, {self.ano}) está{estado}.")

# # # carro1 = Carro("Fiat", "Uno", 2020)
# # # carro = Carro("Volkswagen", "Gol", "2022" ) 

# # # #objetos
# # # carro1.status


# # # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>EXERCICIO>>>>>>>>>>>>>>>>>>>>>>>>>>> DA AULA 11>>>>>>>>>


# # ### **1- Classe Pessoa**

# # # Crie uma classe `Pessoa` com os atributos `nome` e `idade`. 
# # # Adicione um método `apresentar()` que exiba `"Olá, meu nome é [nome] e tenho [idade] anos."` 

# # # Crie duas pessoas diferentes e chame o método.

# # class Pessoa:
# #     def_init_(self):

# #         self.nome = "nome"
# #     self.idade ="idade"

# #     def apresentar(self):
# #         print("nome", self.nome "idade", self.idade)

# # nome1 = "joana", 22
# # nome 2 = "gustavo", 44        



# # ---

# # # ### **2.Classe Retângulo**

# # # Crie uma classe `Retangulo` com os atributos `largura` e `altura`. Adicione métodos:

# # # - `calcular_area()` – retorna a área
# # # - `calcular_perimetro()` – retorna o perímetro
    
# # #     Crie um retângulo com largura 5 e altura 3 e exiba sua área e perímetro.
    

# # # ---

# # # ### **3.   Classe Conta Bancária**

# # # Crie uma classe `ContaBancaria` com:

# # # - Atributos: `titular`, `saldo` (inicial 0)
# # # - Métodos:
# # #     - `depositar(valor)`: acrescenta ao saldo
# # #     - `sacar(valor)`: se houver saldo suficiente, subtrai; senão, exibe `"Saldo insuficiente"`
# # #     - `exibir_saldo()`: mostra o saldo formatado
        
# # #         Crie uma conta, faça depósitos e saques e exiba o saldo.
        

# # # ---

# # # ### **4. Classe Produto**

# # # Crie uma classe `Produto` com:

# # # - Atributos: `nome`, `preco`, `quantidade_estoque`
# # # - Métodos:
# # #     - `total_estoque()`: retorna `preco * quantidade_estoque`
# # #     - `adicionar_estoque(quantidade)`: aumenta a quantidade
# # #     - `remover_estoque(quantidade)`: diminui, mas não permite ficar negativo
        
# # #         Crie um produto, altere o estoque e exiba o valor total.
# # # ### **5. Classe Aluno**

# # Crie uma classe `Aluno` com:

# # - Atributos: `nome`, `matricula`, `notas` (lista de floats)
# # - Métodos:
# #     - `adicionar_nota(nota)`: adiciona à lista
# #     - `calcular_media()`: retorna a média das notas
# #     - `situacao()`: retorna `"Aprovado"` se média >= 7, `"Recuperação"` se >= 5, `"Reprovado"` caso contrário
        
# #         Crie um aluno, adicione 3 notas e exiba sua situação.

# class Aluno:
#     def __init__(self, nome, matricula, notas):
#         self.nome = nome
#         self.matricula = matricula
#         self.nota = notas
        
#     def adicionar_nota(self):

#     def calcular_media(self):

#     def situacao(self):
        


# lista =[]
        