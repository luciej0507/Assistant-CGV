# Projet Chatbot Conditions Générales de Ventes – Lexybot

**Entreprise :** Mon eshop (filiale de EcomLegal)  
**Secteur :** E-commerce  
**Auteurs :** Lucie & Cécile  
**Date :** Juillet 2025

---

## Présentation du projet

**Lexybot** est un assistant chatbot intelligent développé pour répondre aux questions des utilisateurs du site web Mon eshop concernant les **Conditions Générales de Vente (CGV)**. Ce chatbot vise à automatiser le support client sur des sujets clés tels que le paiement, la rétractation, la livraison, la garantie et la protection des données personnelles.

Lexybot utilise un modèle de langage avancé (LLM) d’OpenAI, le **gpt-4.1-nano-2025-04-14**, intégré via une interface simple sous forme de widget chat. La base documentaire des CGV est intégrée au format JSONL pour garantir une réponse précise et conforme à la documentation officielle.

---

## Objectifs

- **Automatiser les réponses** aux questions fréquentes des clients sur les CGV  
- **Fournir des réponses claires, fiables et conformes** à la documentation officielle  
- **Compréhension du langage naturel** pour s’adapter aux différentes formulations des utilisateurs  
- **Redirection vers un contact humain** lorsque la question dépasse le périmètre du chatbot  

---

## Fonctionnalités principales

- **Traitement du langage naturel (NLP)** grâce au modèle GPT-4.1-nano  
- **Base de connaissances CGV en JSONL** pour une intégration structurée et évolutive  
- **Widget chat intégré** sur le site Mon eshop pour une interaction fluide  
- **Escalade automatique** vers un support humain en cas de besoin  
- **Interface d’administration** via Adminer pour la gestion de la base MySQL  

---

## Architecture technique

| Composant             | Technologie / Outil              |
|----------------------|---------------------------------|
| Modèle IA            | OpenAI GPT-4.1-nano-2025-04-14  |
| Base de données      | MySQL (conteneur Docker)         |
| Outil d’administration | Adminer                         |
| Environnement de développement | VSCode                      |
| Conteneurisation     | Docker                          |
| Langage principal    | Python                         |
| Interface utilisateur | Widget chat simple intégré au site |

---

## Installation et déploiement

1. **Cloner le dépôt :**

2. **Lancer le conteneur MySQL via Docker :**

3. **Configurer la base de données MySQL** (via Adminer accessible sur `http://localhost:8080`) avec les données CGV au format JSONL.

4. **Installer les dépendances Python :**

5. **Configurer les variables d’environnement** (clé API OpenAI, accès base de données, paramètres du widget).

6. **Démarrer le serveur chatbot :**

7. **Intégrer le widget chat** dans le site Mon eshop via le script fourni.

---

## Utilisateurs cibles

- **Clients de Mon eshop** : pour obtenir rapidement des réponses fiables sur les CGV  
- **Support client** : pour évaluer la qualité des réponses du chatbot avant déploiement complet  

---

## Critères de succès

- **Pourcentage de réponses pertinentes** sur un jeu de questions test  
- **Temps moyen de réponse** rapide et fluide  
- **Satisfaction utilisateur** mesurée via feedbacks  

---

## Critères d’échec

- Retours négatifs fréquents sur la pertinence des réponses  
- Résultats négatifs lors des tests d’API (latence, erreurs)  

---

## Contribution

Les contributions sont les bienvenues ! Merci de consulter le fichier [CONTRIBUTING.md](CONTRIBUTING.md) pour les règles et processus.

---

## Licence

Ce projet est sous licence MIT.

---

## Contacts

Pour toute question ou demande d’assistance, contactez l’équipe projet Mon eshop via support@moneshop.com.

---

## Documentation complémentaire

- Exemplaier du fichier de fine-tuning (format JSONL)  
- Organigramme de l'algorithme
- Schéma de la base MySQL
---

