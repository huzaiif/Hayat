import streamlit as st
from database.db import save_health_record, get_health_record

def show_profile():
    st.title("Health Profile 👤")
    st.markdown("Keep your health records up to date for better recommendations.")
    
    user_id = st.session_state['user_id']
    record = get_health_record(user_id)
    
    # Set default values if record doesn't exist
    default_age = record['age'] if record and record['age'] else 25
    default_weight = record['weight'] if record and record['weight'] else 70.0
    default_height = record['height'] if record and record['height'] else 170.0
    default_medical = record['medical_conditions'] if record and record['medical_conditions'] else ""
    default_allergies = record['allergies'] if record and record['allergies'] else ""
    
    with st.form("health_profile_form"):
        st.subheader("Personal Information")
        col1, col2, col3 = st.columns(3)
        with col1:
            age = st.number_input("Age (Years)", min_value=1, max_value=120, value=int(default_age))
        with col2:
            weight = st.number_input("Weight (kg)", min_value=1.0, max_value=300.0, value=float(default_weight))
        with col3:
            height = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, value=float(default_height))
            
        st.subheader("Medical History")
        medical_conditions = st.text_area("Existing Medical Conditions", value=default_medical, 
                                          placeholder="E.g., Hypertension, Asthma (Leave empty if none)")
        allergies = st.text_area("Allergies", value=default_allergies, 
                                 placeholder="E.g., Peanuts, Penicillin (Leave empty if none)")
                                 
        submit_button = st.form_submit_button("Save Profile", use_container_width=True)
        
        if submit_button:
            save_health_record(user_id, age, weight, height, medical_conditions, allergies)
            st.success("Health profile updated successfully!")

if __name__ == "__main__":
    if 'logged_in' in st.session_state and st.session_state['logged_in']:
        show_profile()
    else:
        st.warning("Please log in to view this page.")
