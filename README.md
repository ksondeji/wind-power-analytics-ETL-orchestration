# Fabric Wind Power Analytics

Dans le cadre de ce projet, nous developerons une solutoion end-to-end à partir d'une capacité Microsoft Fabric en utilisant l'architecture Medallion classique (Bronze → Silver → Gold) avec des données réelles.
L'objectif est de s'exercer à mettre en œuvre des modèles courants et reproductibles et complètement automatisés de plateformes de données fréquemment utilisés en entreprise :
l'ingestion, la transformation, la modélisation, le reporting et l'orchestration.

Pipeline de données **production éolienne** sur Microsoft Fabric : ingestion quotidienne, medallion (Bronze/Silver/Gold), modèle sémantique et rapport BI.

## Réalisations

**Ingestion** — Données brutes (CSV) récupérées quotidiennement depuis un dataset public GitHub et chargées en append dans un Lakehouse Bronze (Delta). Le notebook détermine la dernière date présente, récupère le fichier du jour suivant et l’ajoute à la table `wind_power`.

**Transformation** — Nettoyage et enrichissement en Silver : arrondis (`wind_speed`, `energy_produced`), normalisation du champ `time`, création de colonnes calendrier (jour, mois, trimestre, année) et de créneaux (Morning / Afternoon / Evening / Night). En Gold : modélisation en star schema avec une table de faits (`FactWindPower`) et quatre dimensions (date, temps, turbine, statut opérationnel), prêtes pour l’analyse.

**Orchestration** — Pipeline Fabric enchaînant : ingestion → Bronze→Silver → Silver→Gold → refresh (actualisation) planifié du modèle sémantique pour mettre à jour le rapport BI tous les jours à une heure précise. En cas d’échec sur l’ingestion, une activité envoie un email de notification pour alerter l’équipe.

**Rapport BI** — Modèle sémantique Power BI en Direct Lake sur le Lakehouse Gold, avec relations entre la table de faits et les tables de dimensions. Rapport d’analyse de la production des éoliennes connecté à ce modèle.

**Variantes** — En complément du notebook PySpark principal, une version Spark SQL et un Dataflow Gen2 (Power Query) ont été réalisés pour l’étape Bronze→Silver, afin d’illustrer différentes options de transformation sur Fabric.

## Stack

Microsoft Fabric (Lakehouses, Pipelines, Notebooks PySpark, Semantic Model, Reports), Delta Lake, OneLake. Source des données : [wind-power-dataset](https://github.com/mikailaltundas/datasets-for-training/tree/main/wind-power-dataset).
