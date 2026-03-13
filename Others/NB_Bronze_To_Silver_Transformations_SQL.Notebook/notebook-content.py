# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "a36e7b4b-5281-4a98-9543-8fd4578d8536",
# META       "default_lakehouse_name": "LH_Wind_Power_Silver",
# META       "default_lakehouse_workspace_id": "9bbc69d7-19ab-4253-ab82-ab54001cef06",
# META       "known_lakehouses": [
# META         {
# META           "id": "a36e7b4b-5281-4a98-9543-8fd4578d8536"
# META         },
# META         {
# META           "id": "1e9070ef-5482-40a8-873d-e313bbb64f73"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC -- Create a temporary view of the Bronze wind_power table
# MAGIC CREATE OR REPLACE TEMP VIEW bronze_wind_power AS
# MAGIC SELECT *
# MAGIC FROM `WindPowerAnalytics_KarlSONDEJI`.LH_Wind_Power_Bronze.dbo.wind_power;

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC -- Clean and enrich data
# MAGIC CREATE OR REPLACE TEMP VIEW transformed_wind_power AS
# MAGIC SELECT
# MAGIC production_id,
# MAGIC date,
# MAGIC turbine_name,
# MAGIC capacity,
# MAGIC location_name,
# MAGIC latitude,
# MAGIC longitude,
# MAGIC region,
# MAGIC status,
# MAGIC responsible_department,
# MAGIC wind_direction,
# MAGIC ROUND(wind_speed, 2) AS wind_speed,
# MAGIC ROUND(energy_produced, 2) AS energy_produced,
# MAGIC DAY(date) AS day,
# MAGIC MONTH(date) AS month,
# MAGIC QUARTER(date) AS quarter,
# MAGIC YEAR(date) AS year,
# MAGIC REGEXP_REPLACE(time, '-', ':') AS time,
# MAGIC CAST(SUBSTRING(time, 1, 2) AS INT) AS hour_of_day,
# MAGIC CAST(SUBSTRING(time, 4, 2) AS INT) AS minute_of_hour,
# MAGIC CAST(SUBSTRING(time, 7, 2) AS INT) AS second_of_minute,
# MAGIC CASE
# MAGIC WHEN CAST(SUBSTRING(time, 1, 2) AS INT) BETWEEN 5 AND 11 THEN
# MAGIC 'Morning'
# MAGIC WHEN CAST(SUBSTRING(time, 1, 2) AS INT) BETWEEN 12 AND 16 THEN
# MAGIC 'Afternoon'
# MAGIC WHEN CAST(SUBSTRING(time, 1, 2) AS INT) BETWEEN 17 AND 20 THEN
# MAGIC 'Evening'
# MAGIC ELSE 'Night'
# MAGIC END AS time_period
# MAGIC FROM bronze_wind_power;

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC -- Drop the wind_power table in the Silver Lakehouse if it exists
# MAGIC DROP TABLE IF EXISTS
# MAGIC `WindPowerAnalytics_KarlSONDEJI`.LH_Wind_Power_Silver.dbo.wind_power;

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC -- Create the new wind_power table in the Silver Lakehouse
# MAGIC CREATE TABLE
# MAGIC `WindPowerAnalytics_KarlSONDEJI`.LH_Wind_Power_Silver.dbo.wind_power
# MAGIC USING delta
# MAGIC AS
# MAGIC SELECT *
# MAGIC FROM transformed_wind_power;

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT *
# MAGIC FROM `WindPowerAnalytics_KarlSONDEJI`.LH_Wind_Power_Silver.dbo.wind_power;

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }
