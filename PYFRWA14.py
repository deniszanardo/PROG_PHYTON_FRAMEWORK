# exemplo explicação


# class Dados:
#     def __init__(self):
#         self.nome = 'Ana' # publicp
#         self._cpf = '123146' # protegido
#         self.__conta = '1213' # privado


#     def display(self):
#         print(self.nome)
#         print(self._cpf)
#         print(self.__conta)


# class Dados2(Dados):
#     def __init__(self):
#         super().__init__()
#         self.x  =  10
        
#     def mostrar(self):
#         print(self._Dados__conta)



# # d = Dados()
# # d.display()
# # print(d._Dados__conta)        
# # print('cpf', d._cpf)


# d2  =  Dados2()
# d2.display()
# d2.mostrar()


# # ### **Exercício 1 – Livro**

# # Crie uma classe `Livro` com atributos de instância:
# #  `titulo`, `autor`, `ano`, `emprestado`
# #  (booleano, padrão `False`).

# # Métodos:

# # - `emprestar()` – se disponível, muda `emprestado` para `True`.
# # - `devolver()` – muda `emprestado` para `False`.
# # - `__str__()` – retorna uma string com as informações.
    
# #     Teste com dois livros.


# class Livro:
#     def __init__(self, titulo, autor, ano):
#         self.titulo = titulo
#         self.autor = autor
#         self.ano = ano
#         self.emprestado =  False
#     def emprestar(self):
#         if not self.emprestado:
#             self.emprestado = True 


#     def devolver(self):
#         self.emprestado = False


#     def __str__(self):
#         return f'NOME: {self.titulo} AUTOR:{self.autor} ANO:{self.ano}'


# livro = Livro('antifragil', 'taleb', 2015)


# livro.emprestar()
# livro.devolver()



# print(livro) 
 
 

# # ---

# # ### **Exercício 2 – Contador com Atributo de Classe**

# # Crie uma classe `Contador` que tenha um atributo de classe `total_contadores` que conta quantas instâncias foram criadas. 
# # Cada vez que um novo objeto é criado, esse contador deve ser incrementado. 
# # Adicione um método `exibir_total()` que exibe o total de contadores criados.


# class Contador:
#     total_contadores = 0
#     def __init__(self):
#        Contador.total_contadores += 1

#     def exibir_total(self): self é sobre a classe ter atributos que podem variar 
#         print(Contador.total_contadores)

# c = Contador()
# c1 = Contador()
# c2 = Contador ()

# c.exibir_total()



# # ### **Exercício 3 – Produto com Desconto**

# # Classe `Produto` com atributos privados `_nome`, `_preco`, `_quantidade`. 
# # Use propriedades (`@property`) para acessar esses atributos. 
# # Crie um método `aplicar_desconto(percentual)` que reduz o preço.
# # O preço não pode ficar negativo. Teste criando produtos e aplicando descontos.

# class Produto:
#     def __init__(self, nome, quantidade, preco):
#         self._nome = nome
#         self._quantidade = quantidade
#         self._preco = preco

#     @property
#     def nome(self):
#         return self._nome
    
#     @property
#     def quantidade(self):
#         return self._quantidade
    
#     @property
#     def preco(self):
#         return self._preco
    
#     def aplicar_desconto(self, percentual):
#         desconto = self._preco *(percentual / 100)
#         n_valor = self._preco - desconto
#         if n_valor < 1:
#             return 'nao pode ficar negativo'
#         else:
#             return n_valor
        
# p = Produto('x', 5, 100)
# print(p.aplicar_desconto(10))






# # ### **Exercício 4 – Banco com Saldo Privado**

# # Classe `ContaBancaria` com atributo privado `__saldo`. Métodos:

# # - `depositar(valor)` – aumenta saldo.
# # - `sacar(valor)` – reduz saldo se houver saldo suficiente; senão, exibe mensagem.
# # - `exibir_saldo()` – retorna o saldo (use propriedade `saldo` apenas para leitura).
    
# #     Crie uma conta, realize operações e exiba o saldo.

# class ContaBancaria:
#     def __init__(self):
#         self.__saldo = 100

#     def depositar(self, valor):
#         ContaBancaria.__saldo += valor
#         return ContaBancaria.__saldo
    
#     def depositar(self, valor):
#         ContaBancaria.__saldo -= valor
#         return ContaBancaria.__saldo

#     def exibir_saldo(self, valor):
#         return ContaBancaria.__saldo
    
    
# c = ContaBancaria()
# print(c.depositar(100))
# print(c.sacar(50))
# print(c.exibir_saldoaldo())




# ---

# # ### **Exercício 5 – Aluno com Notas**

# # Classe `Aluno` com atributos: 
# # `nome`,
# #  `matricula` 
# # e uma lista privada `__notas`. 
# # Métodos:

# # - `adicionar_nota(nota)` – adiciona à lista (valida de 0 a 10).
# # - `calcular_media()` – retorna a média.
# # - `situacao()` – retorna "Aprovado" se média >= 7,
# # "Recuperação" se >= 5, "Reprovado" caso contrário.
    
# #     Teste com um aluno e algumas notas.
    
# class Aluno:
    

#     def __init__(self, nome, matricula, notas):
#         self.nome = nome
#         self.matricula = matricula
#         self.notas = notas
        
#     def adicionar_nota(self):
#         self.notas = [5, 4, 6]



#     def calcular_media (self):   
#         calcular_media = self.notas / 3
#         if calcular_media =>7 provado
#         else:
#             print("Reprovado")


#     def situacao(self):
#         return f'Aprovado: {self.media} "Reprovado   





# ---

# # ### **Exercício 6 – Data (validação)**

# # Crie uma classe `Data` com atributos `dia`, `mes`, `ano`. 
# # No `__init__`, 
# # valide se a data é válida (considere meses com 30/31 dias e ano bissexto para fevereiro). 
# # Use propriedades para garantir que alterações futuras também sejam validadas. 
# # Adicione um método `__str__` que retorna a data no formato `dd/mm/aaaa`.


# class Data:
#     def _init_(self, dia, mes, ano):
#         self.dia = dia
#         self.mes = mes
#         self.ano = ano

#     def validacao(self):
#         self.dia

     
            



# # ### **Exercício 7 – Funcionário com Aumento**

# # Classe `Funcionario` com atributos:
# #  `nome`, `cargo`, `salario_base` (privado). 
# # Métodos:

# # - `aumentar_salario(percentual)` – aumenta o salário.
# # - `calcular_bonus()` – retorna 10% do salário base.
# # - Propriedade `salario` para leitura.
    
# #     Teste criando um funcionário, aumente o salário e mostre o novo valor.
    
# class Funcionario:
#     def _init_(self, nome, cargo, salario_base):
#         self.nome = nome
#         self.cargo = cargo
#         self.__salario_base = salario_base

#     def aumentar_salario(self, aumento): 
#         aumento = int(input("Digite percentual de aumento"))
#         self.__salario_base += self.__salario_base * aumento
        

#     def calcular_bonus(self, bonus):
#         bonus = 0.10
#         self._calcular_bonus = self.__salario_base * bonus

# f1 = Funcionario("Joao")
# s1 









# ---

# # ### **Exercício 8 – Carro com Velocidade (Encapsulamento)**

# # Classe `Carro` com atributos `marca`, `modelo` e `__velocidade` (inicial 0). 
# # Métodos:
# # - `acelerar(valor)` – aumenta velocidade até no máximo 200.
# # - `frear(valor)` – reduz velocidade até no mínimo 0.
# # - Propriedade `velocidade` para leitura.
    
# #     Teste acelerando e freando.
    

# ---

# # ### **Exercício 9 – Estatísticas (Atributos de Classe)**

# # Classe `Estatistica` com atributos de classe `soma` e `contagem`. 
# # Métodos de classe:

# # - `adicionar(valor)` – atualiza soma e contagem.
# # - `calcular_media()` – retorna a média (ou 0 se nenhum valor adicionado).
    
# #     Use `@classmethod` e não crie instâncias.
# # Teste adicionando números e exibindo a média.


# # ### **Exercício 10 – Agenda com Contatos (Composição)**

# # Crie uma classe `Contato` com atributos `nome`, `telefone`, `email`. 
# # Crie uma classe `Agenda` que possui uma lista privada de contatos. Métodos:

# # - `adicionar_contato(contato)` – adiciona à lista.
# # - `listar_contatos()` – exibe todos os contatos.
# # - `buscar_contato(nome)` – exibe os dados do primeiro contato com aquele nome.
    
# #     Teste adicionando vários contatos e fazendo buscas.

# class Agenda:
    
#     def __init__(self, agenda):
#             agenda = []


# class Contato:
#     def __init__(self, nome, telefone, email):
#             self.nome = nome
#             self.telefone = telefone
#             self.email = email
                    
#     def adicionar_contato(self, agenda):
#             agenda = []
#             self.nome = str(input("Digite nome: "))
#             self.telefone = int(input("Digite seu telefone: "))
#             self.email = str(input("Digite seu email: "))

#     def buscar_contato(self, agenda):
#         agenda = []


# c1 = Contato()

# c1.append.adicionar_contato.agenda()
# c2.append.adicionar_contato.agenda()

