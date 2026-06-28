# Projet Instit Watch

Agent de veille institutionnelle quotidienne basé sur LangGraph, FastAPI et OpenAI.

## Fonctionnalités MVP

- Collecte marchés via Yahoo Finance
- Collecte taux US via FRED
- Collecte communications Fed/BCE via RSS
- Génération d’un brief institutionnel avec OpenAI
- Exposition via API FastAPI
- Compatible n8n via endpoint `/brief/daily`

## Installation

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt