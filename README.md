# Projet IA – File Rouge PSTB 🤖

> **Application web de chat IA** intégrant l'API Google Gemini — Projet File Rouge Bachelor Cybersécurité @ PSTB

---

## 🚀 Présentation

Application web permettant d'interagir avec un modèle d'intelligence artificielle (Google Gemini) via une interface conversationnelle intuitive. Le projet couvre l'ensemble de la stack : backend Python pour les appels API et frontend HTML/JS pour l'affichage dynamique des réponses.

---

## ⚙️ Stack technique

| Couche | Technologie |
|---|---|
| Frontend | HTML5, CSS3, JavaScript (Vanilla) |
| Backend | Python 3 |
| IA | Google Gemini API |
| Communication | Fetch API (REST) |

---

## ✨ Fonctionnalités

- 💬 **Interface de chat** — Envoi de messages et affichage dynamique des réponses IA
- 🤖 **Intégration Gemini** — Appels à l'API Google Gemini depuis le backend Python
- ⚡ **Affichage temps réel** — Mise à jour dynamique de l'interface sans rechargement
- 🔄 **Architecture client/serveur** — Séparation claire frontend (HTML/JS) et backend (Python)

---

## 🏗️ Structure du projet

```
projet-ia-file-rouge/
├── index.html              # Interface principale
├── frontend-updates.js     # Logique frontend & appels API
├── backend-gemini.py       # Backend Python — appels Gemini API
├── nv.py                   # Script utilitaire
└── votre_script.py         # Script de traitement
```

---

## 🚀 Lancer le projet en local

### Prérequis
- Python 3.x
- Une clé API Google Gemini ([obtenir ici](https://aistudio.google.com/))

```bash
# Cloner le repo
git clone https://github.com/PayzzTTV/projet-ia-file-rouge.git
cd projet-ia-file-rouge

# Installer les dépendances Python
pip install google-generativeai

# Configurer la clé API
export GEMINI_API_KEY="votre_clé_ici"

# Lancer le backend
python backend-gemini.py

# Ouvrir index.html dans le navigateur
```

---

## 📚 Contexte

Projet réalisé dans le cadre du **Bachelor Cybersécurité – Projet File Rouge** à la PSTB (Paris School of Technology & Business), visant à concevoir une application intégrant des technologies IA modernes.

---

## 👤 Auteur

**Alexis Delburg** — Étudiant Bachelor Cybersécurité @ PSTB
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Alexis_Delburg-blue)](https://linkedin.com/in/AlexisDelburg)
[![GitHub](https://img.shields.io/badge/GitHub-PayzzTTV-black)](https://github.com/PayzzTTV)
