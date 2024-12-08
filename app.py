import streamlit as st
import numpy as np
import random
import nltk
from nltk.stem import WordNetLemmatizer
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
import string
import data
import time

# Configuration de la page
st.set_page_config(page_title="GasyGPT", page_icon="💬")

# Charger le CSS personnalisé
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css('style.css')

# Initialisation
lemmatizer = WordNetLemmatizer()

@st.cache_resource
def load_model_and_data():
    intents = data.data["intents"]

    # Création des listes
    words = []
    classes = []
    doc_X = []
    doc_y = []

    # Parcourir toutes les intentions
    for intent in intents:
        for pattern in intent["patterns"]:
            tokens = nltk.word_tokenize(pattern)
            words.extend(tokens)
            doc_X.append(pattern)
            doc_y.append(intent["tag"])

        if intent["tag"] not in classes:
            classes.append(intent["tag"])

    words = [lemmatizer.lemmatize(word.lower()) for word in words if word not in string.punctuation]
    words = sorted(set(words))
    classes = sorted(set(classes))

    training = []
    out_empty = [0] * len(classes)

    for idx, doc in enumerate(doc_X):
        bow = [1 if word in lemmatizer.lemmatize(doc.lower()) else 0 for word in words]
        output_row = list(out_empty)
        output_row[classes.index(doc_y[idx])] = 1
        training.append([bow, output_row])

    random.shuffle(training)
    training = np.array(training, dtype=object)
    train_X = np.array(list(training[:, 0]))
    train_y = np.array(list(training[:, 1]))

    # Modèle Deep Learning
    model = Sequential()
    model.add(Dense(128, input_shape=(len(train_X[0]),), activation="relu"))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation="relu"))
    model.add(Dropout(0.3))
    model.add(Dense(len(train_y[0]), activation="softmax"))

    adam = tf.keras.optimizers.Adam(learning_rate=0.01)
    model.compile(loss='categorical_crossentropy', optimizer=adam, metrics=["accuracy"])

    model.fit(train_X, train_y, epochs=200, verbose=0)
    model.save('gasy_gpt_model.keras')

    return model, words, classes, intents
 
# Charger le modèle et les données
model, words, classes, intents = load_model_and_data()

def clean_text(text):
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return tokens

def bag_of_words(text):
    tokens = clean_text(text)
    bow = [0] * len(words)
    for w in tokens:
        for idx, word in enumerate(words):
            if word == w:
                bow[idx] = 1
    return np.array(bow)

def pred_class(text):
    bow = bag_of_words(text)
    result = model.predict(np.array([bow]))[0]
    thresh = 0.2
    y_pred = [[idx, res] for idx, res in enumerate(result) if res > thresh]

    y_pred.sort(key=lambda x: x[1], reverse=True)
    return [classes[r[0]] for r in y_pred]

def get_response(intents_list):
    tag = intents_list[0]
    for intent in intents:
        if intent["tag"] == tag:
            fampidirana = random.choice(intent['fampidirana']).capitalize()  # Capitaliser seulement ici
            result = f"**{fampidirana}.** " + \
                     random.choice(intent["responses"]) + ". " + \
                     random.choice(intent["famaranana"]) + "."
            result = result.replace("\n", "</br>")
            return result  # Pas besoin de `capitalize()` ici
    return "Désolé, je n'ai pas compris."

# Interface utilisateur
st.title("Ahoana no ahafahako manampy anao ?")

if "messages" not in st.session_state:
    st.session_state.messages = []

message_containers = [st.empty() for _ in range(len(st.session_state.messages) + 1)]

for idx, message in enumerate(st.session_state.messages):
    if message["role"] == "user":
        message_containers[idx].chat_message("user").markdown(message["content"].replace("-", "</br>"), unsafe_allow_html=True)
    else:
        message_containers[idx].chat_message("assistant").markdown(message["content"].replace("-", "</br>"), unsafe_allow_html=True)

if prompt := st.chat_input("Ny hafatrao"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    message_containers[len(st.session_state.messages) - 1].chat_message("user").markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        ints = pred_class(prompt)
        res = get_response(ints)

        for chunk in res.split():
            full_response += chunk + " "
            time.sleep(0.05)
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})

st.sidebar.title("GasyGPT")
st.sidebar.subheader("Mombamomba")
st.sidebar.info("Ity chatbot ity dia natao hanomezana vaovao momba ny fahasalamana sy ny kolontsaina malagasy.")
