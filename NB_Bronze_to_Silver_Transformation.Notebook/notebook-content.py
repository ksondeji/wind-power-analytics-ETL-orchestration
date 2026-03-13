# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "1e9070ef-5482-40a8-873d-e313bbb64f73",
# META       "default_lakehouse_name": "LH_Wind_Power_Bronze",
# META       "default_lakehouse_workspace_id": "9bbc69d7-19ab-4253-ab82-ab54001cef06",
# META       "known_lakehouses": [
# META         {
# META           "id": "1e9070ef-5482-40a8-873d-e313bbb64f73"
# META         },
# META         {
# META           "id": "a36e7b4b-5281-4a98-9543-8fd4578d8536"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Test

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Path to the wind_power table in the Bronze Lakehouse
bronze_table_path = "abfss://WindPowerAnalytics_KarlSONDEJI@onelake.dfs.fabric.microsoft.com/LH_Wind_Power_Bronze.Lakehouse/Tables/dbo/wind_power"
# Load the wind_power table into a DataFrame
df = spark.read.format("delta").load(bronze_table_path)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Display the Bronze data
# display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql.functions import (
col, round,
dayofmonth, month, quarter, year,
regexp_replace, substring, when
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Clean and enrich data
df_transformed = (df
.withColumn("wind_speed", round(col("wind_speed"), 2))
.withColumn("energy_produced", round(col("energy_produced"), 2))
.withColumn("day", dayofmonth(col("date")))
.withColumn("month", month(col("date")))
.withColumn("quarter", quarter(col("date")))
.withColumn("year", year(col("date")))
.withColumn("time", regexp_replace(col("time"), "-", ":"))
.withColumn("hour_of_day", substring(col("time"), 1, 2).cast("int"))
.withColumn("minute_of_hour", substring(col("time"), 4, 2).cast("int"))
.withColumn("second_of_minute", substring(col("time"), 7,
2).cast("int"))
.withColumn(
"time_period",
when((col("hour_of_day") >= 5) & (col("hour_of_day") < 12),
"Morning")
.when((col("hour_of_day") >= 12) & (col("hour_of_day") < 17),
"Afternoon")
.when((col("hour_of_day") >= 17) & (col("hour_of_day") < 21),
"Evening")
.otherwise("Night")
)
)
# Display the transformed data
display(df_transformed)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Path to the wind_power table in the Silver Lakehouse
silver_table_path = "abfss://WindPowerAnalytics_KarlSONDEJI@onelake.dfs.fabric.microsoft.com/LH_Wind_Power_Silver.Lakehouse/Tables/dbo/wind_power"

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Save the transformed table to the Silver Lakehouse
df_transformed.write.format("delta").mode("overwrite").save(silver_table_path)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Display the transformed data
display(df_transformed)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
