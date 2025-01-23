# Previsão de Vendas com Regressão Linear

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


# Função para gerar os dados simulados de vendas

def gerar_dados():
    np.random.seed(0)
    gastos_publicidade = np.random.randint(1000, 20000, 50)
    vendas = 3 * gastos_publicidade + np.random.normal(0, 1000, 50) # Relação linear com um pouco de ruido
    return pd.DataFrame({'Gastos_Publicidade': gastos_publicidade, 'Vendas': vendas})

class PrevisaoVendas:
    def __init__(self, dados):
        self.dados = dados
        self.modelo = LinearRegression()

    def treinar_modelo(self):
        """Treina o modelo de regressão linear com os dados fornecidos."""
        X = self.dados[['Gastos_Publicidade']]
        y = self.dados['Vendas']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Treinando o modelo
        self.modelo.fit(X_train, y_train)

        # Fazendo previsões
        y_pred = self.modelo.predict(X_test)

        # Avaliando o modelo
        self.mse = mean_squared_error(y_test, y_pred)
        self.r2 = r2_score(y_test, y_pred)

        print(f"Erro Quadrático Médio (MSE): {self.mse}")
        print(f"Coeficiente de Determinação (R²): {self.r2}")

        return X_test, y_test, y_pred

    def grafico_previsao(self, X_test, y_test, y_pred):
        """Plota o gráfico comparando os valores reais e previstos."""
        plt.figure(figsize=(10, 6))
        plt.scatter(X_test, y_test, color='blue', label='Real')
        plt.plot(X_test, y_pred, color='red', label='Previsto', linewidth=3)
        plt.xlabel('Gastos com Publicidade (R$)')
        plt.ylabel('Vendas (und)')
        plt.title('Previsão de Vendas com Regressão Linear')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

def main():
    # Gerando dados simulados de vendas
    dados = gerar_dados()

    # Criação do objeto de previsão de vendas
    previsao = PrevisaoVendas(dados)

    # Treinando o modelo e obtendo as previsões
    X_test, y_test, y_pred = previsao.treinar_modelo()

    # Exibindo o gráfico da previsão
    previsao.grafico_previsao(X_test, y_test, y_pred)

if __name__ == "__main__":
    main()