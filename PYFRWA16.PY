# import streamlit as st


# # herança e poliformismo ...


# class Linguagem:
#     def executar(self):
#         return 'Executando codigo ...'


# class Python(Linguagem):
#     def executar(self):
#         return 'Executar linguagem back e front'    


# class Go(Linguagem):
#     def executar(self):
#         return 'Linguagem de servidor e segurança ...'


# class JS(Linguagem):
#     def executar(self):
#         return 'Linguagem para web ...'      



# st.title('poo -  POLIFORMISMO')
# st.write('Escolha uma ...')


# opcao = st.selectbox(


#         'escolha a linguagem',
#         ['Python', 'Go', 'JS']


# )
# if opcao == 'Python':
#     linguagem = Python()
# elif opcao == 'Go':
#     linguagem = Go()
# elif opcao == 'JS':
#     linguagem = JS()



# st.subheader('RESULTADO')
# st.success(linguagem.executar())
# st.balloons()


# # st.camera_input()   


# enable = st.checkbox("Enable camera")
# picture = st.camera_input('teste',  label_visibility="visible" ,args=[])


# if picture:
#     st.image(picture)#
# # 
# #  import streamlit as st
# # from numpy.random import default_rng as rng
# # import pandas as pd


# # # herança e poliformismo ...

# # class Linguagem:
# #     def executar(self):
# #         return 'Executando codigo ...'

# # class Python(Linguagem):
# #     def executar(self):
# #         return 'Executar linguagem back e front'    

# # class Go(Linguagem):
# #     def executar(self):
# #         return 'Linguagem de servidor e segurança ...'

# # class JS(Linguagem):
# #     def executar(self):
# #         return 'Linguagem para web ...'      


# # st.title('poo -  POLIFORMISMO')
# # st.write('Escolha uma ...')

# # opcao = st.selectbox(

# #         'escolha a linguagem',
# #         ['Python', 'Go', 'JS']

# # )
# # if opcao == 'Python':
# #     linguagem = Python()
# # elif opcao == 'Go':
# #     linguagem = Go()
# # elif opcao == 'JS':
# #     linguagem = JS()


# # st.subheader('RESULTADO')
# # st.success(linguagem.executar())
# # st.balloons()

# # # st.camera_input()   

# # enable = st.checkbox("Enable camera")
# # # picture = st.camera_input('teste',  label_visibility="visible" ,args=[])

# # # d = {
# # # 'x' : [1,2,3,4,],
# # # 'z' :['']

# # # }

# # # picture = ''


# # # st.image('img.jpg')

# # # df = pd.DataFrame(
# # # rng(0).standard_normal((1000, 2)) / [50, 50] + [37.76, -122.4],
# # # columns=["lat", "lon"],

# # st.map()


# ## **Exercícios extra com Streamlit…**

# # # **Classe Livro** – crie uma classe com atributos título, autor, ano. 
# # # Adicione um método `__str__`. 
# # # Crie uma subclasse `LivroDigital` que 
# # adiciona atributo `formato` e sobrescreva `__str__`.

class Livro:
    def _init_(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def __str__adicione_metodo(self)
        
class LivroDigital:
    def 




# # **Classe Abstrata Veiculo** – defina uma classe abstrata com método
# #  `mover`. Implemente `Carro` e `Bicicleta` com 
# # comportamentos diferentes. 
# # Teste o polimorfismo.

# # **Sobrecarga de operador** – crie uma classe
# #  `Vetor` com atributos x, y e implemente
# #  `__add__`, `__sub__`, `__mul__` (escalar).

# # **Classe anônima** – use `type` para criar 
# # uma classe dinâmica com um método `saudacao`. 
# # Instancie-a.