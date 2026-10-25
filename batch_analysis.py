from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, count, sum

# 1. Iniciar la sesión de Spark
spark = SparkSession.builder \
    .appName("BatchAnalysis_Fraude") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# 2. Cargar el dataset
print("=== CARGANDO DATASET ===")
df = spark.read.csv("transactions.csv", header=True, inferSchema=True)

# 3. Mostrar el esquema
print("=== ESQUEMA DEL DATASET ===")
df.printSchema()

# 4. Contar filas totales
total_filas = df.count()
print(f"=== TOTAL DE REGISTROS: {total_filas} ===")

# 5. Limpieza: Eliminar filas nulas
df_clean = df.dropna(subset=["amount", "type", "isFraud"])
print(f"=== REGISTROS DESPUÉS DE LIMPIEZA: {df_clean.count()} ===")

# 6. Análisis Exploratorio (EDA)
print("=== ANÁLISIS POR TIPO DE TRANSACCIÓN ===")
analisis = df_clean.groupBy("type") \
    .agg(
        count("amount").alias("cantidad_transacciones"),
        sum("amount").alias("monto_total"),
        avg("amount").alias("monto_promedio")
    ) \
    .orderBy(col("monto_total").desc())

analisis.show()

# 7. Análisis de Fraudes
print("=== ANÁLISIS DE FRAUDES ===")
fraudes = df_clean.groupBy("isFraud") \
    .agg(
        count("amount").alias("cantidad"),
        sum("amount").alias("monto_total")
    )
fraudes.show()

spark.stop()
