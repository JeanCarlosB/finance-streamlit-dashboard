# 📊 Dashboard Interativo de Ativos Financeiros

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/Plotly-239120?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly">
</p>

## 🎯 Visão de Negócios e Objetivo
O objetivo desta aplicação é transformar dados brutos do mercado financeiro em informações visuais e acionáveis. Através de uma interface web interativa, gestores e analistas podem acompanhar a evolução do preço de fechamento de diversos ativos em tempo real, facilitando a tomada de decisão.

## 🗄️ Origem dos Dados (Pipeline ETL)
Os dados consumidos por este dashboard (armazenados no banco SQLite) são extraídos, tratados e atualizados de forma automatizada pelo meu script de Engenharia de Dados. Você pode conferir a arquitetura completa do pipeline de extração acessando o repositório base abaixo:

<a href="https://github.com/JeanCarlosB/pipeline-etl-acoes">Repositório: Pipeline ETL de Ações</a>

## ⚙️ Funcionalidades
* **Filtros Dinâmicos:** Seleção múltipla de ativos financeiros diretamente na barra lateral.
* **Gráficos Interativos:** Visualização da evolução temporal dos preços com zoom e detalhamento ao passar o mouse.
* **Acesso aos Dados Brutos:** Opção de visualizar a tabela completa gerada pelas consultas SQL para auditoria rápida.

## 🚀 Como executar o projeto na sua máquina
Certifique-se de ter o Python instalado e siga os passos abaixo no seu terminal:

1. Clone este repositório para o seu computador.
2. Instale as bibliotecas necessárias executando: pip install -r requirements.txt
3. Inicie o servidor web da aplicação: streamlit run app.py
4. O painel abrirá automaticamente no seu navegador padrão.

---

## 📚 Outros Projetos Acadêmicos
Caso queira conhecer mais do meu histórico, desenvolvi também um projeto colaborativo focado puramente em modelagem e ciência de dados sobre ações e obtive ótimos resultados. Você pode conferir a pesquisa completa acessando o link abaixo:

<a href="https://github.com/Juliana001/Datascience-para-Mercado-Financeiro---Projeto-final">Ciência de Dados para Mercado Financeiro - Projeto Final</a>
