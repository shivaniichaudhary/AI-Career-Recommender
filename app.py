import streamlit as st
from model import predict_career  # connect ML model

# Title
st.title("AI Career & Internship Recommendation Platform")

# User Input
skills = st.text_input("Enter your skills (comma separated)")
cgpa = st.number_input("Enter your CGPA", 0.0, 10.0, step=0.1)
interest = st.selectbox("Interest Area", ["AI", "Web", "Data", "Software"])
year = st.selectbox("Current Year", ["2nd", "3rd", "4th"])

# Button to get recommendation
if st.button("Get Recommendation"):
    career = predict_career(skills)  # call ML model
    
    st.subheader("Recommended Career:")
    st.success(career)

    st.subheader("Suggested Internships:")
    st.write(f"{career} Internship")

    st.subheader("Skills to Learn Next:")
    st.write("DSA, Git, Projects, Problem Solving")
