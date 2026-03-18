import streamlit as st
from features.recommendation import predict_diabetes, predict_heart_disease, predict_parkinsons
from features.chatbot import generate_health_tips
from database.db import save_recommendation, save_report

def show_recommendations():
    st.title("Disease Risk Assessment 🩺")
    st.markdown("Use our ML models to assess your risk for specific conditions.")
    
    user_id = st.session_state['user_id']
    
    tab1, tab2, tab3 = st.tabs(["Diabetes", "Heart Disease", "Parkinson's"])
    
    with tab1:
        st.subheader("Diabetes Prediction")
        col1, col2, col3 = st.columns(3)
        with col1:
            Pregnancies = st.number_input('Number of Pregnancies', min_value=0, step=1)
            SkinThickness = st.number_input('Skin Thickness value', min_value=0.0)
            DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value', min_value=0.0)
        with col2:
            Glucose = st.number_input('Glucose Level', min_value=0.0)
            Insulin = st.number_input('Insulin Level', min_value=0.0)
            Age = st.number_input('Age of the Person', min_value=1, step=1)
        with col3:
            BloodPressure = st.number_input('Blood Pressure value', min_value=0.0)
            BMI = st.number_input('BMI value', min_value=0.0)
            
        if st.button('Diabetes Test Result', use_container_width=True):
            user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                          BMI, DiabetesPedigreeFunction, Age]
            
            prediction = predict_diabetes(user_input)
            
            if prediction == 1:
                diagnosis = 'The person is diabetic'
                st.error(diagnosis)
            else:
                diagnosis = 'The person is not diabetic'
                st.success(diagnosis)
                
            save_recommendation(user_id, diagnosis, "Diabetes")
            
            st.subheader("Health Advice & Tips")
            with st.spinner("Generating personalized health tips..."):
                tips = generate_health_tips(diagnosis, "Diabetes")
                st.write(tips)
                
                # Save as report
                report_content = f"**Diagnosis:** {diagnosis}\n\n**Health Tips:**\n{tips}\n\n**Inputs:**\nPregnancies: {Pregnancies}, Glucose: {Glucose}, BP: {BloodPressure}, BMI: {BMI}"
                save_report(user_id, "Diabetes Risk Assessment", report_content)
                st.info("Report saved to your account automatically.")
                
    with tab2:
        st.subheader("Heart Disease Prediction")
        col1, col2, col3 = st.columns(3)
        with col1:
            age = st.number_input('Age', min_value=1, step=1, key="hd_age")
            trestbps = st.number_input('Resting Blood Pressure', min_value=0.0)
            restecg = st.number_input('Resting Electrocardiographic results', min_value=0.0)
            oldpeak = st.number_input('ST depression induced by exercise', min_value=0.0)
            thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect', min_value=0, max_value=2, step=1)
        with col2:
            sex = st.number_input('Sex (1=Male, 0=Female)', min_value=0, max_value=1, step=1)
            chol = st.number_input('Serum Cholestoral in mg/dl', min_value=0.0)
            thalach = st.number_input('Maximum Heart Rate achieved', min_value=0.0)
            slope = st.number_input('Slope of the peak exercise ST segment', min_value=0.0)
        with col3:
            cp = st.number_input('Chest Pain types', min_value=0, step=1)
            fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl (1=true, 0=false)', min_value=0, max_value=1, step=1)
            exang = st.number_input('Exercise Induced Angina (1=yes, 0=no)', min_value=0, max_value=1, step=1)
            ca = st.number_input('Major vessels colored by flourosopy', min_value=0, step=1)

        if st.button('Heart Disease Test Result', use_container_width=True):
            user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            
            prediction = predict_heart_disease(user_input)
            
            if prediction == 1:
                diagnosis = 'The person is having heart disease'
                st.error(diagnosis)
            else:
                diagnosis = 'The person does not have any heart disease'
                st.success(diagnosis)
                
            save_recommendation(user_id, diagnosis, "Heart Disease")

            st.subheader("Health Advice & Tips")
            with st.spinner("Generating personalized health tips..."):
                tips = generate_health_tips(diagnosis, "Heart Disease")
                st.write(tips)
                
                report_content = f"**Diagnosis:** {diagnosis}\n\n**Health Tips:**\n{tips}\n\n**Inputs:**\nAge: {age}, Sex: {'Male' if sex==1 else 'Female'}, Cholestoral: {chol}, Max Heart Rate: {thalach}"
                save_report(user_id, "Heart Disease Risk Assessment", report_content)
                st.info("Report saved to your account automatically.")

    with tab3:
        st.subheader("Parkinson's Disease Prediction")
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            fo = st.number_input('MDVP:Fo(Hz)', min_value=0.0)
            RAP = st.number_input('MDVP:RAP', min_value=0.0)
            APQ3 = st.number_input('Shimmer:APQ3', min_value=0.0)
            HNR = st.number_input('HNR', min_value=0.0)
            D2 = st.number_input('D2', min_value=0.0)
        with col2:
            fhi = st.number_input('MDVP:Fhi(Hz)', min_value=0.0)
            PPQ = st.number_input('MDVP:PPQ', min_value=0.0)
            APQ5 = st.number_input('Shimmer:APQ5', min_value=0.0)
            RPDE = st.number_input('RPDE', min_value=0.0)
            PPE = st.number_input('PPE', min_value=0.0)
        with col3:
            flo = st.number_input('MDVP:Flo(Hz)', min_value=0.0)
            DDP = st.number_input('Jitter:DDP', min_value=0.0)
            APQ = st.number_input('MDVP:APQ', min_value=0.0)
            DFA = st.number_input('DFA', min_value=0.0)
        with col4:
            Jitter_percent = st.number_input('MDVP:Jitter(%)', min_value=0.0)
            Shimmer = st.number_input('MDVP:Shimmer', min_value=0.0)
            DDA = st.number_input('Shimmer:DDA', min_value=0.0)
            spread1 = st.number_input('spread1', value=0.0)
        with col5:
            Jitter_Abs = st.number_input('MDVP:Jitter(Abs)', min_value=0.0)
            Shimmer_dB = st.number_input('MDVP:Shimmer(dB)', min_value=0.0)
            NHR = st.number_input('NHR', min_value=0.0)
            spread2 = st.number_input('spread2', value=0.0)

        if st.button("Parkinson's Test Result", use_container_width=True):
            user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                          RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5,
                          APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
            
            prediction = predict_parkinsons(user_input)
            
            if prediction == 1:
                diagnosis = "The person has Parkinson's disease"
                st.error(diagnosis)
            else:
                diagnosis = "The person does not have Parkinson's disease"
                st.success(diagnosis)
                
            save_recommendation(user_id, diagnosis, "Parkinson's Disease")

            st.subheader("Health Advice & Tips")
            with st.spinner("Generating personalized health tips..."):
                tips = generate_health_tips(diagnosis, "Parkinson's Disease")
                st.write(tips)
                
                report_content = f"**Diagnosis:** {diagnosis}\n\n**Health Tips:**\n{tips}\n\n**Inputs:**\nFo(Hz): {fo}, Fhi: {fhi}, Flo: {flo}"
                save_report(user_id, "Parkinson's Risk Assessment", report_content)
                st.info("Report saved to your account automatically.")

if __name__ == "__main__":
    if 'logged_in' in st.session_state and st.session_state['logged_in']:
        show_recommendations()
    else:
        st.warning("Please log in to view this page.")
