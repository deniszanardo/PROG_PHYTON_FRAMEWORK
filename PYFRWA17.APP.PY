#INTERFACE GRAFICA
import streamlit as st
#MODELAGEM
from sqlalchemy.ext.declarative import declarative_base
#DRIVE MOTOR - CONEXAO PATH
from sqlalchemy import create_engine, Column, Integer, String
#PERSSISTENCIA LER E SALVAR 
from sqlalchemy.orm import sessionmaker

#url - banco de dados
URL_NEON = 'postgresql://neondb_owner:***************@ep-old-star-a42ayjl7-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'

engine = create_engine(URL_NEON)
Session = sessionmaker(bind=engine)
Base = declarative_base()

#class base itinerario ORM MAPEAMENTO
class Itinerario (Base):
    __tablename__ = 'Itinerario de Aula'
    id = Column(Integer, primary_key=True , autoincrement=True)
    nome = Column(String)
    descricao = Column(String)

Base.metadata.creastrt_all(engine)

#FRAME STREAMLIT INTERFACE GRAFICA 
st.set_page_config(page_title= 'FORMULARIO DE ITINERARIO')
st.title('CADASTRO DE ITINERARIO 2026')
st.info('OS DADOS SERAO SALVOS DIRETAMENTE NO POSTGREESQL DA NUVEM NEON.TECH')

with st.form('formulario', clear_on_submit=True):
    nome_input = st.text.input('NOME DO ITINERARIO')
    desc_input = st.text_input('DESCRICAO')
    botao = st. form.submit.button('SALVAR DADOS')

if botao :
    if nome_input:
        session = Session()
        novo_registro = Itinerario(nome = nome_input, descricao = desc_input)
        session.add(novo_registro)
        session.comit()
        session.close()
        st.sucess(f'SUCESSO{nome_input} foi salvo com sucesso"')
    else:
        st.error('POR FAVOR, PREENCHA CORRETAMENTE')

#ATUALIZAÇÃO EM TEMPO REAL  
st.divider()
st.subheader('REGISTRO ATUAL')
session = Session()
dados = session.query(Itinerario).all()
session.close()

if dados:
    for item in dados:
        st.write(f'{item.nome}: {item.descricao}')