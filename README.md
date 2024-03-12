# Projet_CAP
Projet final de la formation de développeurs applicatifs sous Django et Docker.

Ce projet consiste en un bot Discord qui fournit des informations sur des données de vaccination. Il utilise Discord.py pour l'interaction avec l'API Discord.

## Configuration

### Django Settings

Assurez-vous de configurer les clés secrètes dans les paramètres Django, en les renseignant dans un fichier `.env` :

```python
SECRET_KEY = 'your_secret_key'
API_KEY = 'your_api_key'
DISCORD_TOKEN = 'your_discord_token'
```

### Base de données

Le projet utilise une base de données SQLite par défaut. Vous pouvez ajuster les paramètres de la base de données dans `settings.py`.

Le projet comprend des scripts pour peupler la base de données opérationnelle (ODS) et le data warehouse (DWH) à partir des données fournies dans le data. Voici comment les utiliser :

*Pour la table ODS :*
```
python manage.py runscript VAC_ODS   
```

*Pour les tables du DWH :*
```
python manage.py runscript D_Date_DWH   
```
```
python manage.py runscript D_Type_DWH   
```
```
python manage.py runscript D_Localisation_DWH   
```
```
python manage.py runscript F_Vaccin_DWH   
```

### Installation des dépendances

Avant de lancer le projet, assurez-vous d'installer les dépendances requises. Vous pouvez le faire en exécutant :

```
pip install -r requirements.txt
```

## Utilisation

### Lancement du Bot Discord

Pour lancer le bot Discord que vous aurez créé sur le site dev de Discord, exécutez le script `runscript main_bot` :

```
python manage.py runscript main_bot
```

Le bot se connectera à Discord en utilisant le jeton spécifié dans les paramètres Django.

### API REST

Le projet expose également une API REST pour accéder aux données sur la vaccination. Vous pouvez accéder aux différentes ressources via les endpoints correspondants :

- `/vaccins/`: Ressource pour accéder aux données sur les vaccins administrés.
- `/localisations/`: Ressource pour accéder aux données sur les localisations de vaccination.
- `/dates/`: Ressource pour accéder aux données sur les dates de vaccination.
- `/types/`: Ressource pour accéder aux données sur les types de vaccins.

Assurez-vous d'inclure le jeton d'authentification dans les en-têtes de vos requêtes Postman et d'etre connecté à l'admin pour pouvoir accéder à ces données via URL.

## Tests

Le projet inclut des tests unitaires pour les différentes fonctionnalités. Vous pouvez exécuter les tests en utilisant la commande :

```
python manage.py test api.tests    
```

Assurez-vous que votre environnement est configuré correctement pour exécuter les tests Django.
