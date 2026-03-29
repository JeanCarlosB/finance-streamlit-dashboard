'''Esse código é o app.py do projeto, ele é responsável por criar a interface visual do dashboard usando Streamlit. 
Ele carrega os dados do banco SQLite, exibe um gráfico interativo e permite que o usuário filtre os ativos financeiros. 
Se houver algum erro ao carregar os dados reais, ele exibe uma mensagem de aviso e carrega dados de demonstração para garantir que o 
dashboard funcione corretamente.'''

import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# Configurações iniciais da página

st.set_page_config(page_title="Dashboard Financeiro", layout="wide")
st.title("📊 Análise do Mercado Financeiro")
st.markdown("Interface visual do Pipeline ETL gerado em Python e SQLite.")

@st.cache_data 
def carregar_dados():
    # Caminho do banco
    conn = sqlite3.connect('') 
    # AQUI VOCÊ DEVE COLOCAR O CAMINHO DO SEU BANCO DE DADOS SQLite 
    
    # Se o nome da tabela no seu banco não for 'tabela_financeira', o erro vai aparecer!
    query = "SELECT data_pregao AS data, codigo_ativo AS ticker, preco_fechamento FROM historico_acoes"
    df = pd.read_sql(query, conn)
    conn.close()
    
    df['data'] = pd.to_datetime(df['data'])
    return df

try:
    df = carregar_dados()
    st.success("Dados reais carregados com sucesso do SQLite!")
except Exception as e:
    # AQUI ESTÁ O DEDO-DURO: Ele vai imprimir o erro real do banco na tela
    st.warning(f"Atenção: Carregando dados de demonstração. Erro detalhado: {e}")
    datas = pd.date_range(start="2026-01-01", periods=30)
    df = pd.DataFrame({
        'data': datas,
        'ticker': ['PETR4'] * 30,
        'preco_fechamento': [30 + (i * 0.5) for i in range(30)]
    })

st.sidebar.header("Filtros")
ativos_selecionados = st.sidebar.multiselect(
    "Selecione os Ativos:",
    options=df['ticker'].unique(),
    default=df['ticker'].unique()
)

df_filtrado = df[df['ticker'].isin(ativos_selecionados)]

st.subheader("Evolução do Preço de Fechamento")
fig = px.line(df_filtrado, x='data', y='preco_fechamento', color='ticker', markers=True)
st.plotly_chart(fig, width='stretch')

if st.checkbox("Mostrar Dados Brutos (Tabela SQLite)"):
    st.dataframe(df_filtrado)