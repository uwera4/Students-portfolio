import streamlit as st
import json
from PIL import Image
import os

# Load or initialize profile data
def load_profile_data():
    if os.path.exists("profile_data.json"):
        with open("profile_data.json", "r") as file:
            return json.load(file)
    else:
        return {
            "name": "UWERA Gloriose",
            "location": "INES-Ruhengeri, Rwanda",
            "field_of_study": "BSc Software Engineering, Year 3",
            "about_me": "I'm a passionate software engineering student eager to build innovative solutions that solve real-world problems.",
            "skills": {"Python": 80, "JavaScript": 70, "PHP & MySQL": 90}
        }

# Save profile data
def save_profile_data(data):
    with open("profile_data.json", "w") as file:
        json.dump(data, file)

profile_data = load_profile_data()

# ---- Home Section ----
st.set_page_config(page_title="My Digital Footprint", layout="wide")

st.sidebar.image("image.jpg", caption="Profile Picture", width=150)

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", [
    "Home", "Projects", "Skills & Achievements", "Customize Profile", "Timeline", "Contact"
])

if page == "Home":
    st.title("My Digital Footprint – Showcasing My Journey")
    st.header("Personal Profile")
    
    st.image("image.jpg", width=200)
    st.write(f"Full Name: {profile_data['name']}")
    st.write(f"Location & University: {profile_data['location']}")
    st.write(f"Field of Study: {profile_data['field_of_study']}")
    
    st.subheader("Introduction")
    st.write(profile_data['about_me'])
    
    st.subheader("Download Resume")
    with open("my_cv.pdf", "rb") as file:
        st.download_button("Download CV", file, file_name="my_cv.pdf")

# ---- Projects Section ----
if page == "Projects":
    st.header("Projects")
    st.subheader("1. Inventory Management System")
    st.write("Type: Individual Project")
    st.write("A system to manage inventory using PHP, HTML, and CSS, featuring user authentication and database integration.")

    st.subheader("2. Employee Leave Management System")
    st.write("Type: Final Year Project")
    st.write("A web app to handle employee leave requests, approvals, and reports, built with PHP and MySQL.")

# ---- Skills & Achievements Section ----
if page == "Skills & Achievements":
    st.header("Skills & Achievements")
    st.subheader("Technical Skills")
    
    for skill, level in profile_data['skills'].items():
        st.progress(level, text=skill)
    
    st.subheader("Certifications & Achievements")
    st.write("- A2 in Software Development")
    st.write("- Web Design and Development certificate by FreeCodeCamp")

# ---- Customize Profile Section ----
if page == "Customize Profile":
    st.header("Customize Your Profile")
    
    with st.form(key='profile_form'):
        profile_data['name'] = st.text_input("Full Name", profile_data['name'])
        profile_data['location'] = st.text_input("Location & University", profile_data['location'])
        profile_data['field_of_study'] = st.text_input("Field of Study", profile_data['field_of_study'])
        profile_data['about_me'] = st.text_area("About Me", profile_data['about_me'])
        
        st.subheader("Skills")
        for skill in list(profile_data['skills'].keys()):
            profile_data['skills'][skill] = st.slider(skill, 0, 100, profile_data['skills'][skill])
        
        new_skill = st.text_input("Add New Skill")
        new_skill_level = st.slider("Skill Level", 0, 100, 50)
        
        if new_skill:
            profile_data['skills'][new_skill] = new_skill_level
        
        submit_button = st.form_submit_button("Save Changes")
        
        if submit_button:
            save_profile_data(profile_data)
            st.success("Profile updated successfully!")

# ---- Timeline Section ----
if page == "Timeline":
    st.header("Timeline of Projects & Achievements")
    
    st.subheader("Year 1")
    st.write("- Introduction to Programming (Python Basics) – Individual Project")
    
    st.subheader("Year 2")
    st.write("- Library Management System – Group Project")
    st.write("- Web-based To-Do List – Individual Project")
    
    st.subheader("Year 3")
    st.write("- Inventory Management System – Individual Project")
    st.write("- Employee Leave Management System – Final Year Project")

# ---- Contact Section ----
if page == "Contact":
    st.header("Contact Information")
    
    with st.form(key='contact_form'):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button("Send Message")

    st.write("LinkedIn: [www.linkedin.com/in/uwera-gloriose-2771742a3](#)")
    st.write("GitHub: [https://github.com/uwera4/](#)")
    st.write("Email: ug2320525@ines.ac.rw")