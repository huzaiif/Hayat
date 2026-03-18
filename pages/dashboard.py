import streamlit as st
from database.db import get_reports, get_recommendations

def show_dashboard():
    st.title("Welcome to Hayat 🏥")
    st.markdown(f"Hello **{st.session_state['username']}**, welcome to your personal AI Health Assistant.")
    
    st.markdown("---")
    
    user_id = st.session_state['user_id']
    
    # Fetch stats
    reports = get_reports(user_id)
    recommendations = get_recommendations(user_id)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{len(reports)}</div>
            <div class="metric-label">Saved Reports</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{len(recommendations)}</div>
            <div class="metric-label">Assessments Taken</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">Active</div>
            <div class="metric-label">Status</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### Quick Actions")
    col1, col2 = st.columns(2)
    with col1:
        st.info("💡 Start a new chat with Hayat to get general medical advice.")
    with col2:
        st.success("📊 Take a disease prediction assessment in the Recommendations tab.")

if __name__ == "__main__":
    if 'logged_in' in st.session_state and st.session_state['logged_in']:
        show_dashboard()
    else:
        st.warning("Please log in to view this page.")
