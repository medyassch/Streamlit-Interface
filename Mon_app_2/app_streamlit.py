import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("https://github.com/medyassch/Streamlit-Interface/blob/main/Mon_app_2/random_forest_model.pkl", "rb"))

st.title("Prédiction de Client")

st.header("Veuillez entrer les informations du client :")

age = st.number_input('Âge', min_value=0, step=1)
balance = st.number_input('Balance bancaire')
num_products = st.number_input('Nombre de produits', min_value=0, max_value=10, step=1)
is_active = st.selectbox('Client actif ?', ('Oui', 'Non'))

if is_active == 'Oui':
    is_active = 1 
else : is_active = 0

gender = st.selectbox('Sexe', ('Male', 'Female'))
geo = st.selectbox('Géographie', ('France', 'Germany', 'Spain'))

if st.button('Prédire'):
    # Gender
    if gender == 'Female' :
     gender_female = 1
    else : gender_female= 0

    if gender == 'Male':
        gender_male = 1 
    else : gender_male=0

    # Géographie
    if geo == 'France' :
       geo_france = 1 
    else: geo_france = 0
    if geo == 'Germany':
        geo_germany = 1 
    else: geo_germany = 0
    if geo == 'Spain':
        geo_spain = 1 
    else: geo_spain = 0

    features = np.array([[age, balance, num_products, is_active,
                          geo_france, geo_germany, geo_spain,
                          gender_female, gender_male]])

    prediction = model.predict(features)

    # Affichage du résultat
    st.success(f"Résultat de la prédiction : {int(prediction[0])}")
