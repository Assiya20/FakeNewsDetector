{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f42ac456-310a-4558-a44f-5ad4aa74db16",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-10-11 21:15:19.290 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\belkheiri\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-10-11 21:15:19.290 Session state does not function when running a script without `streamlit run`\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import joblib\n",
    "\n",
    "# Charger les objets\n",
    "model = joblib.load(\"models1/fake_news_nb.pkl\")\n",
    "tfidf = joblib.load(\"models1/tfidf_vectorizer.pkl\")\n",
    "\n",
    "# Interface utilisateur\n",
    "st.title(\" Fake News Detector\")\n",
    "st.write(\"Entrez un texte d'article pour vérifier s'il est FAKE ou RÉEL.\")\n",
    "\n",
    "# Champ de saisie\n",
    "user_input = st.text_area(\"Texte de l'article :\", height=200)\n",
    "\n",
    "if st.button(\"Vérifier\"):\n",
    "    if user_input.strip() == \"\":\n",
    "        st.warning(\" Merci d'entrer un texte avant de vérifier.\")\n",
    "    else:\n",
    "        # Transformer le texte\n",
    "        text_tfidf = tfidf.transform([user_input])\n",
    "        prediction = model.predict(text_tfidf)[0]\n",
    "        \n",
    "        # Résultat\n",
    "        if prediction == 1:\n",
    "            st.error(\" FAKE NEWS détectée !\")\n",
    "        else:\n",
    "            st.success(\" Cette news semble RÉELLE.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eed840ce-a37d-45cf-893c-5ade2c01a801",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
