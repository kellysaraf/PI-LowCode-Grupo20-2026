# PI - Low Code Grupo 20 - 2026

## Objetivo
Desenvolver um pipeline completo de ETL utilizando dados públicos do Kaggle, aplicando técnicas de tratamento de dados com Pandas e construção de um dashboard interativo com Streamlit para análise e visualização de informações.

---

## Problema do Projeto
O projeto tem como objetivo analisar dados para identificar padrões, tendências e insights relevantes que auxiliem na tomada de decisão.

A partir da base selecionada, buscamos responder perguntas como:
- Quais fatores influenciam os dados analisados?
- Quais são os principais padrões encontrados?
- Como os dados se comportam ao longo do tempo?

---

## Base de Dados

Fonte: Kaggle

Dataset utilizado: Brazilian E-Commerce Public Dataset by Olist

Link: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

Descrição:
Este dataset contém aproximadamente 100 mil pedidos realizados entre 2016 e 2018 em marketplaces brasileiros.

A base permite analisar pedidos sob diversas perspectivas, incluindo:
- Status do pedido
- Valores de compra e pagamento
- Frete e desempenho de entrega
- Localização dos clientes
- Avaliações dos clientes
- Informações dos produtos e vendedores

Os dados estão organizados em múltiplas tabelas (CSV), permitindo análises relacionais e construção de pipelines de dados mais completos.

---

## Pipeline de Dados (ETL)

O projeto segue a arquitetura de ETL (Extract, Transform, Load), organizada da seguinte forma:

### Extract
Nesta etapa, os arquivos CSV do dataset Brazilian E-Commerce Public Dataset by Olist são obtidos a partir do Kaggle e disponibilizados para processamento.

### Transform
Os dados são tratados com o uso da biblioteca Pandas, incluindo:
- leitura e integração das tabelas do dataset;
- remoção ou tratamento de valores nulos;
- padronização de nomes de colunas;
- conversão de tipos de dados;
- criação de variáveis derivadas para análise;
- agrupamentos e cálculos estatísticos.

### Load
Após o tratamento, os dados são preparados para análise e utilização no dashboard interativo desenvolvido em Streamlit.

---

## Análises e Métricas

Com base no dataset selecionado, o projeto busca analisar o desempenho do e-commerce sob diferentes perspectivas.

As principais métricas consideradas são:
- quantidade total de pedidos;
- valor médio dos pedidos;
- valor total de vendas;
- tempo médio de entrega;
- nota média de avaliação dos clientes.

Também são realizadas análises como:
- distribuição de pedidos por estado;
- comparação entre categorias de produtos;
- análise da satisfação dos clientes;
- avaliação do desempenho logístico das entregas;
- comportamento temporal das vendas.

---

## Dashboard

O dashboard foi desenvolvido utilizando Streamlit com o objetivo de apresentar os dados de forma visual, interativa e intuitiva.

A aplicação permite visualizar:
- indicadores principais do e-commerce;
- gráficos comparativos de vendas;
- distribuição geográfica de pedidos;
- métricas de entrega;
- análise das avaliações dos clientes.

O objetivo do dashboard é facilitar a interpretação dos dados e apoiar a identificação de padrões, tendências e oportunidades de melhoria no desempenho do e-commerce.

---

## Estrutura do Projeto

- `data/` → arquivos de dados utilizados no projeto
- `src/` → scripts relacionados ao processo de ETL
- `app/` → aplicação do dashboard
- `.gitignore` → arquivos e pastas ignorados pelo Git
- `requirements.txt` → bibliotecas necessárias para execução do projeto
- `README.md` → documentação principal do projeto


---

## Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- Streamlit
- Matplotlib
- Seaborn
- GitHub

---

## Como Executar o Projeto

1. Clonar este repositório.
2. Instalar as dependências com o comando:

pip install -r requirements.txt

3. Executar o script de ETL:

python src/etl.py

4. Executar o dashboard:

streamlit run app/dashboard.py

---

## Status do Projeto

- Estrutura inicial do repositório criada
- Dataset definido
- Processo de ETL estruturado
- Dashboard em desenvolvimento
- Documentação em atualização

---

## Integrantes

- Luan Belloti de Sousa
- Matheus Lucas da Silva
- Jorge Luiz Vieira Zorzetto de Oliveira
- Kelly Saraf
  
