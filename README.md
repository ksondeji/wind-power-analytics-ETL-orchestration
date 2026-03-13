# Fabric Wind Power Analytics

Pipeline de données **production éolienne** sur Microsoft Fabric : ingestion quotidienne, medallion (Bronze/Silver/Gold), modèle sémantique et rapport BI.

## Réalisations

**Ingestion** — Données brutes (CSV) récupérées quotidiennement depuis un dataset public GitHub et chargées en append dans un Lakehouse Bronze (Delta). Le notebook détermine la dernière date présente, récupère le fichier du jour suivant et l’ajoute à la table `wind_power`.

**Transformation** — Nettoyage et enrichissement en Silver : arrondis (`wind_speed`, `energy_produced`), normalisation du champ `time`, création de colonnes calendrier (jour, mois, trimestre, année) et de créneaux (Morning / Afternoon / Evening / Night). En Gold : modélisation en star schema avec une table de faits (`FactWindPower`) et quatre dimensions (date, temps, turbine, statut opérationnel), prêtes pour l’analyse.

**Orchestration** — Pipeline Fabric enchaînant : ingestion → Bronze→Silver → Silver→Gold → refresh du modèle sémantique. En cas d’échec sur l’ingestion, une activité envoie un email de notification pour alerter l’équipe.

**Consommation** — Modèle sémantique Power BI en Direct Lake sur le Lakehouse Gold, avec relations entre la table de faits et les dimensions. Rapport d’analyse de la production des éoliennes connecté à ce modèle.

**Variantes** — En complément du notebook PySpark principal, une version Spark SQL et un Dataflow Gen2 (Power Query) ont été réalisés pour l’étape Bronze→Silver, afin d’illustrer différentes options de transformation sur Fabric.

## Stack

Microsoft Fabric (Lakehouses, Pipelines, Notebooks PySpark, Semantic Model, Reports), Delta Lake, OneLake. Source des données : [wind-power-dataset](https://github.com/mikailaltundas/datasets-for-training/tree/main/wind-power-dataset).
