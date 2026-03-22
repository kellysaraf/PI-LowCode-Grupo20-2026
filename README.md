# PI - Low Code Grupo 20 - 2026

## 🎯 Objetivo
Desenvolver um pipeline completo de ETL utilizando dados públicos do Kaggle, aplicando técnicas de tratamento de dados com Pandas e construção de um dashboard interativo com Streamlit para análise e visualização de informações.

---

## 📊 Problema do Projeto
O projeto tem como objetivo analisar dados para identificar padrões, tendências e insights relevantes que auxiliem na tomada de decisão.

A partir da base selecionada, buscamos responder perguntas como:
- Quais fatores influenciam os dados analisados?
- Quais são os principais padrões encontrados?
- Como os dados se comportam ao longo do tempo?

---

## 📁 Base de Dados
Fonte: Kaggle

Dataset utilizado: **[INSERIR NOME DA BASE]**  
Link: **[INSERIR LINK DO KAGGLE]**

Descrição:
Breve explicação sobre o que contém a base (ex: dados de vendas, saúde, imóveis, etc.)

---

## 🔄 Pipeline de Dados (ETL)

O projeto segue a arquitetura de ETL:

### Extract
Coleta dos dados a partir de arquivos CSV obtidos no Kaggle.

### Transform
Tratamento e preparação dos dados utilizando Pandas:
- Remoção de valores nulos
- Padronização de colunas
- Criação de novas variáveis
- Agrupamentos e cálculos estatísticos

### Load
Os dados tratados são armazenados para utilização no dashboard.

---

## 📊 Análises e Métricas

Durante o projeto foram definidas métricas para análise, como:

- KPI 1: [ex: total de registros]
- KPI 2: [ex: média]
- KPI 3: [ex: valor máximo/mínimo]

Também foram realizadas análises como:
- Comparação entre categorias
- Evolução temporal
- Distribuição dos dados

---

## 📈 Dashboard

O dashboard foi desenvolvido utilizando Streamlit e apresenta:

- Indicadores principais (KPIs)
- Gráficos interativos
- Filtros para exploração dos dados

O objetivo é permitir uma análise visual e intuitiva das informações.

---

## 🧱 Estrutura do Projeto
data/ → Dados brutos e tratados
notebooks/ → Análises exploratórias
src/ → Scripts de ETL
dashboard/ → Aplicação Streamlit
docs/ → Documentação do projeto


---

## 🛠 Tecnologias Utilizadas

- Python
- Pandas
- Streamlit
- NumPy
- Matplotlib
- Seaborn
- GitHub


