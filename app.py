import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction System',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
        icons=['activity','heart','person'],
        default_index=0
    )

st.title("Multiple Disease Prediction System")

# ================================
# DIABETES PREDICTION PAGE
# ================================
if selected == 'Diabetes Prediction':

    st.subheader('Diabetes Prediction')

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')

    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):
        try:
            input_data = [
                Pregnancies, Glucose, BloodPressure, SkinThickness,
                Insulin, BMI, DiabetesPedigreeFunction, Age
            ]
            input_data = [float(i) for i in input_data]

            diab_prediction = diabetes_model.predict([input_data])

            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'

        except:
            diab_diagnosis = "⚠ Please enter valid numeric values!"

    st.success(diab_diagnosis)

# ================================
# HEART DISEASE PREDICTION PAGE
# ================================
if selected == 'Heart Disease Prediction':

    st.subheader('Heart Disease Prediction')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal (0 = normal; 1 = fixed defect; 2 = reversible defect)')

    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        try:
            input_data = [
                age, sex, cp, trestbps, chol, fbs,
                restecg, thalach, exang, oldpeak,
                slope, ca, thal
            ]
            input_data = [float(i) for i in input_data]

            heart_prediction = heart_disease_model.predict([input_data])

            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'

        except:
            heart_diagnosis = "⚠ Please enter valid numeric values!"

    st.success(heart_diagnosis)

# ================================
# PARKINSONS PREDICTION PAGE
# ================================
# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    st.subheader('Heart Disease Prediction')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input('Age', min_value=1, max_value=120, value=25)

    with col2:
        sex = st.number_input('Sex (1=Male, 0=Female)', min_value=0, max_value=1, value=1)

    with col3:
        cp = st.number_input('Chest Pain types (0-3)', min_value=0, max_value=3, value=0)

    with col1:
        trestbps = st.number_input('Resting Blood Pressure', min_value=50, max_value=250, value=120)

    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl', min_value=100, max_value=600, value=200)

    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl (1=yes, 0=no)', min_value=0, max_value=1, value=0)

    with col1:
        restecg = st.number_input('Resting ECG (0–2)', min_value=0, max_value=2, value=1)

    with col2:
        thalach = st.number_input('Max Heart Rate Achieved', min_value=50, max_value=250, value=150)

    with col3:
        exang = st.number_input('Exercise Induced Angina (1=yes, 0=no)', min_value=0, max_value=1, value=0)

    with col1:
        oldpeak = st.number_input('ST Depression', min_value=0.0, max_value=10.0, value=1.0)

    with col2:
        slope = st.number_input('Slope (0–2)', min_value=0, max_value=2, value=1)

    with col3:
        ca = st.number_input('Major Vessels (0–4)', min_value=0, max_value=4, value=0)

    with col1:
        thal = st.number_input('Thal (1,2,3)', min_value=1, max_value=3, value=2)

    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        
        input_data = [
            age, sex, cp, trestbps, chol, fbs,
            restecg, thalach, exang, oldpeak, slope, ca, thal
        ]

        heart_prediction = heart_disease_model.predict([input_data])

        if (heart_prediction[0] == 1):
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# =========== DARK THEME BACKGROUND + FOOTER ============
# =========== FULL DARK THEME (NO FOOTER, NO CREDITS) ============
def set_dark_theme():

    # ---- Removed footer completely ----

    # Dark theme styling
    dark_theme_css = """
    <style>
        body {
            background-color: #0d0d0d !important;
            color: #e0e0e0 !important;
        }
        .stApp {
            background: linear-gradient(135deg, #0d0d0d 40%, #1a1a1a 100%) !important;
        }
        .stButton button {
            background-color: #222 !important;
            color: white !important;
            border-radius: 8px !important;
            padding: 0.6em 1.2em !important;
            border: 1px solid #444 !important;
        }
        .stTextInput > div > div input {
            background-color: #1a1a1a !important;
            color: white !important;
            border: 1px solid #444 !important;
        }
        .stNumberInput > div > div input {
            background-color: #1a1a1a !important;
            color: white !important;
            border: 1px solid #444 !important;
        }
        .stSelectbox > div > div {
            background-color: #1a1a1a !important;
            color: white !important;
        }
        header, footer {
            visibility: hidden;
        }
    </style>
    """

    st.markdown(dark_theme_css, unsafe_allow_html=True)


# Call dark theme
set_dark_theme()
