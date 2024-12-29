#!/usr/bin/env python
# coding: utf-8

# # Exemplo trabalho econometria - Análise exploratória de dados

# In[41]:


# Importando bibliotecas e módulos

import pandas as pd # Para manipulação e análise de dados
import numpy as np # Para computação numérica
import matplotlib.pyplot as plt # Para vizualização de dados
import seaborn as sns # Para vizualização de dados


# In[23]:


# Importando o dataframe (utilizando a função pd.read_excel(), de pd)

dados = pd.read_excel(r'C:\users\joaos\downloads\exercício multi py.xlsx')


# In[25]:


# Exibindo as dimensões do dataframe (utilizando o comando dados.shape, de pd)

dados.shape


# In[19]:


# Exibindo as primeiras observações do dataframe (utilizando o comando dados.head(), de pd)

dados.head()


# In[20]:


# Exibindo as últimas observações do dataframe(utilizando o comando dados.tail(), de pd)

dados.tail()


# In[26]:


# Verifcando se há dados faltantes no dataframe (utilizando o comando dados.isna().sum(), de pd)

dados.isna().sum()


# In[29]:


# Exibindo uma tabela descritiva do dataframe e formatando os números com duas casas decimais (utilizando o comando dados.describe().applymap() e a função lambda x: f"{x:.2f}", ambos de pd)

dados.describe().applymap(lambda x: f"{x:.2f}") 


# In[45]:


# Criando gráficos de dispersão que relacionam os respectivos regressores com o regressando (utilizando as bibliotecas matplotlib e seaborn)

# Criando uma figura de grade com subgráficos dispostos em 2 linhas e 3 colunas e ajustando seu tamanho (utilizando o comando fig, ax = plt.subplots(2, 3, figsize=(15, 10)), de plt)
fig, ax = plt.subplots(2, 3, figsize=(15, 10))

## 2, 3 determina que grade de subgráficos tenha 2 linhas e 3 colunas
## figsize=(15, 10) determina o tamanho da fgura


# Plotando os gráficos de dispersão com linhas de tendência (utilizando o comando sns.regplot(), de sns)
sns.regplot(x='Deflator implícito dos preços no PNB', y='Empregados (K)', data=dados, ax=ax[0][0], scatter_kws={'s': 50}, line_kws={'color': 'blue'})
sns.regplot(x='PNB (M de US$)', y='Empregados (K)', data=dados, ax=ax[0][1], scatter_kws={'s': 50}, line_kws={'color': 'blue'})
sns.regplot(x='Desempregados (K)', y='Empregados (K)', data=dados, ax=ax[0][2], scatter_kws={'s': 50}, line_kws={'color': 'blue'})
sns.regplot(x='Empregados nas forças armadas (K)', y='Empregados (K)', data=dados, ax=ax[1][0], scatter_kws={'s': 50}, line_kws={'color': 'blue'})
sns.regplot(x='Não institucionalizados com mais de 14 anos (K)', y='Empregados (K)', data=dados, ax=ax[1][1], scatter_kws={'s': 50}, line_kws={'color': 'blue'})
sns.regplot(x='Tendência', y='Empregados (K)', data=dados, ax=ax[1][2], scatter_kws={'s': 50}, line_kws={'color': 'blue'})

## x='_____' especifica a coluna do dataframe que será disposta no eixo x
## y='_____' especifica a coluna do dataframe que será disposta no eixo y
## ax=ax[0][0] especifica em quais locais da grade os respectivos subgráficos localizar-se-ão
## scatter_kws={'s': 50} define, em 50, o tamanho dos pontos
## line_kws={'color': 'blue'} define, como azul, a cor da linha de tendência

        
# Ajustando o tamanho dos rótulos dos eixos (utilizando loops)
for i in range(2):
    for j in range(3):
        ax[i, j].set_xlabel(ax[i, j].get_xlabel(), fontsize=14)
        ax[i, j].set_ylabel(ax[i, j].get_ylabel(), fontsize=14)
        
        
# Ajustando o tamanho dos valores dos eixos (utilizando loops)
for i in range(2):
    for j in range(3):
        ax[i, j].tick_params(axis='x', labelsize=13)
        ax[i, j].tick_params(axis='y', labelsize=13)
        
        
# Ajustando o layout para evitar sobreposição (utilizando o comando plt.tight_layout(), de plt)        
plt.tight_layout()


# In[ ]:




