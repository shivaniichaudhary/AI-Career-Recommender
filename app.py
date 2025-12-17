import streamlit as st
from model import predict_career

# Page config
st.set_page_config(page_title="AI Career Recommender", page_icon="🎯", layout="wide")

# Sidebar
st.sidebar.title("Student Info")
skills = st.sidebar.text_input("Enter your skills (comma separated)")
cgpa = st.sidebar.number_input("Enter your CGPA", 0.0, 10.0, step=0.1)
interest = st.sidebar.selectbox("Interest Area", ["AI", "Web", "Data", "Software"])
year = st.sidebar.selectbox("Current Year", ["2nd", "3rd", "4th"])

# Main Title
st.title("🎯 AI Career & Internship Recommendation Platform")

st.markdown(
    """
    This app recommends career paths and internship types based on your skills, CGPA, academic year, and interests.
    """
)

if st.button("Get Recommendation"):
   career = predict_career(skills, cgpa, year)

    
   st.subheader("Recommended Career:")
   st.success(career)

   st.subheader("Suggested Internships:")
   st.write(f"{career} Internship")

   st.subheader("Skills to Learn Next:")
   st.write("DSA, Git, Projects, Problem Solving")
st.markdown("---")
st.markdown("Made with ❤️ by Shivani Chaudhary")
