# Proyecto: Análisis de Fraude Financiero con Apache Spark

Este repositorio contiene el código en PySpark para el análisis batch del dataset "Synthetic Financial Datasets For Fraud Detection" de Kaggle.

## Instrucciones de ejecución
1. Descargar el dataset de Kaggle y renombrarlo como `transactions.csv`.
2. Ejecutar el script con el comando: `spark-submit batch_analysis.py`

## Resultados obtenidos
* Se procesaron **6.362.620** transacciones.
* Se identificaron **8.213** transacciones fraudulentas.
* Se calculó el monto total y promedio por cada tipo de transacción (TRANSFER, CASH_OUT, etc.).
