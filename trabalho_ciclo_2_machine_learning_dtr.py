# -*- coding: utf-8 -*-
"""trabalho_ciclo_2_machine_learning_dtr.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J3Tke9US6T3_lb6nnFgIpjfqzux2-P-x

Trabalho da disciplina de Machine Learning

Nome: Diones Rossetto

Data: 24/09/2021
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.tree import DecisionTreeRegressor
from sklearn import datasets
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.externals.six import StringIO  
from IPython.display import Image  
from sklearn.tree import export_graphviz
import pydotplus
import graphviz
import os

# carregar os dados em separar em dados (x) e resultado (y)
dados, resultados = datasets.load_diabetes(return_X_y=True)
df = pd.DataFrame(dados, columns=["age", "sex", "bmi", "bp", "tc", "ldl", "hdl","tch", "ltg", "glu"])
df.head()

# separar os dados em treinamento e teste (em 392 registros para treinamento e 50 para testes)
dados_treinamento = dados[:-50]
dados_teste = dados[-50:]
dados.shape

# separar os resultados em treinamento e teste (em 392 registros para treinamento e 50 para testes)
resultados_treinamento = resultados[:-50]
resultados_teste = resultados[-50:]

# carregar o objeto de decision tree regression
dtr = DecisionTreeRegressor(max_depth=2)

# treinar o modelo usando os dados de treinamento
dtr.fit(dados_treinamento, resultados_treinamento)

# obter predicoes com os dados de teste
predicoes = dtr.predict(dados_teste)

predicoes

# gerar grafico com as informacoes retornadas pelo dtr
print("#### grafico de resultados ####")
plt.plot(range(len(predicoes)), predicoes,color="brown")
plt.scatter(range(len(predicoes)), resultados_teste)
plt.title("Decision Tree Regression")
plt.legend(["Predições","Valor Real"], loc='best',fancybox=True, shadow=True)
plt.grid(True)
plt.show()

print("#### metricas dos resultados ####")
score = dtr.score(dados_treinamento, resultados_treinamento)
print("R²:", score) 
mse = mean_squared_error(resultados_teste, predicoes)
print("MSE: ", mse)
mae = mean_absolute_error(resultados_teste, predicoes)
print("MAE: ", mae)

print("#### arvore de decisao ####")
dot_data = StringIO()
export_graphviz(dtr, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
Image(graph.create_png())