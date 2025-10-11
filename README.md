# FakeNewsDetector
Détection automatique de Fake News à partir de texte en utilisant **Natural Language Processing (NLP)** et **Machine Learning**.

---

##  Objectif
Ce projet a pour objectif de classifier automatiquement les articles de presse en **vraies news** ou **fake news**.  
Il utilise un pipeline complet : **prétraitement du texte, vectorisation TF-IDF, entraînement de modèles ML**, et une **interface Streamlit** pour tester de nouveaux textes.

---

##  Technologies utilisées
- **Python 3**
- **Pandas, NumPy** – manipulation des données
- **Scikit-learn** – modèles ML (Logistic Regression, Naive Bayes)
- **NLTK** – nettoyage et prétraitement des textes (stopwords, lemmatisation)
- **Matplotlib / Seaborn** – visualisation des résultats
- **Streamlit** – application web interactive
- **Joblib** – sauvegarde des modèles et vectorizers

---
## Prétraitement du texte
- Texte converti en **minuscules**
- Suppression de la **ponctuation**
- Suppression des **stopwords**
- **Lemmatisation** des mots (réduction à la racine)

##  Vectorisation
- Utilisation de **TF-IDF** (`TfidfVectorizer`) pour transformer le texte en vecteurs numériques exploitables par les modèles ML.
- `max_features=5000` pour limiter la dimension du vecteur.

---

##  Modèles ML
1. **Logistic Regression**
2. **Naive Bayes (MultinomialNB)** – meilleur résultat pour ce dataset
