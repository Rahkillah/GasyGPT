# GasyGPT

## 🚀 Description
**GasyGPT** est un assistant de santé virtuel inspiré des remèdes traditionnels du foko malagasy. Grâce à l'intelligence artificielle, il permet de fournir des conseils de santé en utilisant des connaissances anciennes, tout en offrant une interface simple et interactive via **Streamlit**.

## 🏥 Fonctionnalités

- **Conseils de santé traditionnels** : Utilisation des remèdes anciens malgaches pour répondre à vos préoccupations de santé.
- **Réponses intelligentes** : Grâce à un modèle d'IA, le système comprend vos questions et fournit des réponses adaptées.
- **Interface simple et fluide** : Une interface web développée avec Streamlit pour faciliter l'interaction avec l'utilisateur.

## 🍏 Technologies utilisées
**Voici les technologies clés utilisées dans ce projet :**

1. **Streamlit** : Framework Python pour créer des applications web interactives.
2. **TensorFlow / Keras** : Pour l'apprentissage automatique et le modèle de classification des remèdes.
3. **NLTK** : Outil de traitement de langage naturel pour la gestion des textes.
4. **NumPy** : Pour les calculs et manipulations des données.
5. **random** : Génère des résultats aléatoires dans certains cas.
6. **data** : Contient les données sur les remèdes et les réponses possibles.
7. **string** : Pour manipuler les chaînes de caractères.

## 📦 Matériel et Logiciel requis

Avant de commencer, assurez-vous d'avoir les éléments suivants :

- **Python 3.x** installé sur votre machine.
- **Streamlit** installé via PIP pour exécuter l'interface.
- **TensorFlow** et autres dépendances installées.

## 💻 Installation et Configuration

1. **Clonez le dépôt** :  
   Clonez ce projet sur votre machine locale avec la commande suivante :
   ```bash
   git clone https://github.com/Rahkillah/GasyGPT/new/main

2. **Installez les dépendances** :
Accédez au dossier du projet et installez les bibliothèques nécessaires :
```bash
cd GasyGPT
pip install -r requirements.txt
```
## 🏃‍♂️ Lancer l'Application
1. **Lancer l'application** : Après avoir installé les dépendances et téléchargé les ressources, vous pouvez lancer l'application avec Streamlit :
```
bashstreamlit run app.py
```
2. **Accéder à l'application** : Une fois l'application lancée, elle s'ouvrira dans votre navigateur à l'adresse suivante :
```
http://localhost:8501
```

## 📝 Structure du projet
```
GasyGPT/
├── app.py               # Le fichier principal de l'application Streamlit
├── data/                # Dossier contenant les données de remèdes anciens
├── models/              # Dossier contenant les modèles de machine learning
├── requirements.txt     # Fichier contenant toutes les dépendances Python
└── README.md            # Ce fichier README
```
## License
© [RANDRIANAOVO Andrandraina](https://www.linkedin.com/in/andrandraina-randrianaivo-562aa3282/)
