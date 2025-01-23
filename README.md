# Previsão de Vendas com Regressão Linear

Este projeto utiliza um modelo de **regressão linear** para prever as vendas de uma empresa com base nos **gastos com publicidade**. O modelo é treinado com dados simulados e avaliado com as métricas de **Erro Quadrático Médio (MSE)** e **Coeficiente de Determinação (R²)**.

## Funcionalidades

- Geração de dados simulados de vendas e gastos com publicidade.
- Implementação de um modelo de regressão linear para previsão de vendas.
- Avaliação do modelo utilizando **MSE** e **R²**.
- Visualização do gráfico comparando as vendas reais e previstas.

## Requisitos

- Python 3.x
- Bibliotecas: `pandas`, `scikit-learn`, `matplotlib`

## Como Usar

1. Clone o repositório:

```bash
   git clone https://github.com/LuiSilvak/sales_forecast.git
   cd sales_forecast
```

2. Instale as bibliotecas necessárias:

```bash
    pip install pandas scikit-learn matplotlib
```

3. Execute o programa:

```bash
    python sales_forecast.py
```

4. O programa irá gerar o gráfico e as métricas de avaliação.

## Exemplo de Execução
### Saída do terminal:

```bash
    Erro Quadrático Médio (MSE): 1181673.119842496
    Coeficiente de Determinação (R²): 0.9900564183833041
```

### Gráfico:

- O gráfico exibirá a comparação entre as vendas reais (pontos azuis) e as vendas previstas (linha vermelha).

## Melhorias Futuras

- Adicionar mais variáveis independentes para melhorar a precisão do modelo.
- Utilizar técnicas avançadas de previsão como regressão polinomial ou redes neurais.
- Integrar com dados reais de vendas e publicidade para previsões mais precisas.

## Licença

Este projeto está licenciado sob a MIT License.
