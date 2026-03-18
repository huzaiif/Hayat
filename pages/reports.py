import streamlit as st
from database.db import get_reports, delete_report

def show_reports():
    st.title("Saved Reports 📑")
    st.markdown("View all your saved health assessments and reports.")
    
    user_id = st.session_state['user_id']
    
    reports = get_reports(user_id)
    
    if not reports:
        st.info("No saved reports found. Run a disease prediction assessment to save one!")
        return
        
    for report in reports:
        with st.expander(f"{report['title']} - {report['created_at'][:10]}"):
            st.markdown(f"**Date:** {report['created_at']}")
            st.markdown(report['content'])
            
            if st.button("Delete Report", key=f"del_report_{report['id']}"):
                delete_report(report['id'], user_id)
                st.success("Report deleted.")
                st.rerun()

if __name__ == "__main__":
    if 'logged_in' in st.session_state and st.session_state['logged_in']:
        show_reports()
    else:
        st.warning("Please log in to view this page.")
