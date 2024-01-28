import numpy as np
import pickle
import streamlit as st

loaded = pickle.load(open('C:\\Users\\abdul\\Downloads\\trained_model.sav', "rb"))

#funcation

def diabetes(input_data): 

    #input_data =(5 , 166 , 72 , 19, 175,25.8,0.587,51)
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded.predict(input_data_reshaped)
    return (prediction)

    if (prediction[0]== 0):
        return ('The person is not diabetic')
    else:
        return ('The person is  diabetic')

def main():
   # the name of the websit
    st.title('Diabetes Prediction Web App')

    Age = st.text_input('Enter the age: ', key='age_input')
    Gender = st.text_input('Enter the Gender: ', key='gender_input')
    Polyuria = st.text_input('Enter yes or no : ', key='Polyuria_input')
    Polydipsia = st.text_input('Enter yes or no : ', key='polydipsia_input')
    sudden_weight_loss = st.text_input('Enter yes or no: ', key='sudden_weight_loss_input')
    weakness = st.text_input('Enter yes or no: ', key='weakness_input')
    Polyphagia = st.text_input('Enter yes or no: ', key='Polyphagia_input')
    Genital_thrush = st.text_input('Enter yes or no: ', key='Genital_thrush_input')
    visual_blurring = st.text_input('Enter yes or no: ', key='visual_blurring_input')
    Itching = st.text_input('Enter yes or no: ', key='Itching_input')
    Irritability = st.text_input('Enter yes or no: ', key='Irritability_input')
    delayed_healing = st.text_input('Enter yes or no: ', key='delayed_healing_input')
    partial_paresis = st.text_input('Enter yes or no: ', key='partial_paresis_input')
    muscle_stiffness = st.text_input('Enter yes or no: ', key='muscle_stiffness_input')
    Alopecia = st.text_input('Enter yes or no: ', key='Alopecia_input')
    Obesity = st.text_input('Enter yes or no: ', key='Obesity_input')
    


    dignosis = ''
    # creating a button for perdiction
    if st.button('Diabetes test Result'):
        dignosis = diabetes(['Age', 'Gender', 'Polyuria', 'Polydipsia', 'sudden weight loss',
       'weakness', 'Polyphagia', 'Genital thrush', 'visual blurring',
       'Itching', 'Irritability', 'delayed healing', 'partial paresis',
       'muscle stiffness', 'Alopecia', 'Obesity'])

    st.success(dignosis)

if __name__ == '__main__':
    main()
