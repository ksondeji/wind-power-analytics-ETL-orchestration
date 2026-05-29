Projet orienté **Microsoft Fabric** : orchestration des flux, modélisation et restitution dans **Power BI** pour des utilisateurs métier.

# Fabric wind power analytics

## 1. Introduction

Dans le cadre de ce projet de data engineering, une plateforme de données end-to-end a été développée sur une capacité Microsoft Fabric afin de reproduire les principales étapes d’une architecture moderne de traitement de données utilisée en entreprise.


Le projet repose sur des données réelles de production éolienne et suit une architecture Medallion classique organisée en trois couches : Bronze, Silver et Gold. L’objectif était de concevoir une solution complète couvrant l’ensemble du cycle de vie de la donnée, depuis l’ingestion jusqu’au reporting décisionnel.

Cette plateforme permet d’automatiser quotidiennement l’ingestion, la transformation, la modélisation et la visualisation des données tout en garantissant la fiabilité et la maintenabilité des traitements. Le projet met également en avant les possibilités offertes par Microsoft Fabric pour centraliser les workloads data engineering, analytics et business intelligence au sein d’un même environnement.

## 2. Objectifs du projet

L’objectif principal du projet était de mettre en pratique les fondamentaux du data engineering à travers le développement d’une architecture moderne, reproductible et entièrement automatisée.

Plusieurs enjeux techniques ont été abordés :

- ingestion automatisée de données externes

- stockage et historisation dans un Data Lake

- transformation et nettoyage des données

- modélisation analytique

- création de rapports BI

- orchestration des pipelines

- supervision et gestion des erreurs

Le projet visait également à se familiariser avec les composants clés de Microsoft Fabric tels que les Lakehouses, les notebooks PySpark, les pipelines d’orchestration, les modèles sémantiques et les rapports Power BI.


## 3. Résultats

Ce projet a permis de mettre en pratique l’ensemble des étapes fondamentales d’une architecture moderne de data engineering.

La mise en oeuvre de l’architecture Medallion a permis de structurer efficacement les traitements et de séparer les différentes responsabilités entre données brutes, données transformées et données analytique

Durant ce projet j'ai pu automatiser des pipelines, superviser des traitements tout en m'assurant de la qualité et de la reproductibilité de ceux-ci, et enfin modéliser des données qui seront utilisées par des équipes métier.


## 4. Architecture

L’architecture mise en place repose sur une approche Medallion organisée en trois couches distinctes : Bronze, Silver et Gold.

La couche Bronze permet de stocker les données brutes ingérées quotidiennement depuis une source publique GitHub sous format CSV. Les données sont chargées en mode append dans un Lakehouse Delta afin de conserver l’historique des fichiers collectés.

La couche Silver est dédiée au nettoyage et à l’enrichissement des données. Les transformations appliquées permettent notamment de normaliser certains champs, créer des colonnes temporelles et préparer les données pour les usages analytiques.

Enfin, la couche Gold contient les données modélisées sous forme de schéma en étoile optimisé pour l’analyse décisionnelle. Cette couche est directement utilisée par le modèle sémantique et les rapports BI.

L’ensemble des données est centralisé dans OneLake avec stockage au format Delta Lake afin de garantir performance et compatibilité avec les workloads analytiques.

## 5. Ingestion et transformation

L’ingestion des données est réalisée à l’aide de notebooks PySpark exécutés dans Microsoft Fabric. Chaque jour, le pipeline détermine automatiquement la dernière date présente dans la table Bronze puis récupère le fichier correspondant au jour suivant depuis le dataset GitHub public.

Les données sont ensuite transformées dans la couche Silver. Plusieurs traitements ont été mis en oeuvre :

- nettoyage et standardisation des colonnes

- arrondis des valeurs numériques

- normalisation des formats temporels

- création de dimensions calendaires

- enrichissement avec des catégories horaires (Morning, Afternoon, Evening, Night)

Dans la couche Gold, les données sont modélisées sous forme de schéma décisionnel (schéma étoile) avec :

- une table de faits FactWindPower (avec les métriques analytiques)

- une dimension date

- une dimension temps

- une dimension turbine

- une dimension statut opérationnel

En complément des notebooks PySpark, une version Spark SQL ainsi qu’un Dataflow Gen2 utilisant Power Query ont également été développés afin d’illustrer différentes approches de transformation disponibles dans Fabric.


## 6. Modélisation et reporting BI

Les données Gold alimentent un modèle sémantique Power BI configuré en mode Direct Lake, permettant un accès performant aux données stockées dans le Lakehouse sans duplication supplémentaire.

Le modèle sémantique repose sur des relations entre la table de faits et les différentes dimensions afin de faciliter l’analyse multidimensionnelle de la production éolienne.

Un rapport BI interactif a ensuite été développé afin de suivre plusieurs indicateurs :

- volume de production énergétique

- performances des turbines

- évolution temporelle de la production

- répartition des statuts opérationnels

- analyses par période ou tranche horaire

## 7. Orchestration et automatisation

L’ensemble des traitements a été orchestré via des pipelines natifs Microsoft Fabric afin d’automatiser complètement le cycle de traitement des données.

Le pipeline principal exécute successivement :

- l’ingestion des données brutes

- les transformations Bronze vers Silver

- les transformations Silver vers Gold

- l’actualisation du modèle sémantique Power BI

Les traitements sont planifiés quotidiennement à une heure précise afin de garantir une mise à jour continue du rapport BI.

Un mécanisme de supervision a également été intégré. En cas d’échec lors de l’ingestion ou d’une étape critique du pipeline, une notification par email est automatiquement envoyée afin d’alerter l’équipe technique.

Cette orchestration permet d’assurer la fiabilité et l’autonomie de la plateforme sans intervention manuelle.

## Stack

Microsoft Fabric (Lakehouses, Pipelines, Notebooks PySpark, Semantic Model, Reports), Delta Lake, OneLake. Source des données : [wind-power-dataset](https://github.com/mikailaltundas/datasets-for-training/tree/main/wind-power-dataset).

## 8. Conclusion

Cette réalisation met en évidence l’intérêt des architectures Medallion pour structurer les pipelines de données et améliorer la maintenabilité des plateformes analytiques modernes. Elle démontre également l’importance de l’automatisation et de l’intégration des outils cloud dans les projets de data engineering actuels.

Ce projet constitue ainsi une expérience complète et concrète dans la conception de solutions data industrielles orientées analytics et business intelligence.
