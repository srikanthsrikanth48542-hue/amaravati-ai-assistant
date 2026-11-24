import streamlit as st
st.set_page_config(page_title="Amaravati Mitra", page_icon="🤖", layout="wide")
try:
    st.image("logo.png.png", width=600)
except:
    pass
st.title("🤖 Amaravati Mitra")
st.subheader("AI Citizen Assistant | Telugu + English + Voice")
st.markdown("Ask in Telugu or English - Road, Water, Light, Drainage, Garbage")
import streamlit as st
import random
import datetime

st.set_page_config(page_title="Amaravati Mitra - AI Citizen Assistant", page_icon="🤖", layout="centered")
# Departments
DEPTS = {
    "road": {"telugu": "Roads & Buildings Dept", "phone": "0863-2340101", "days": "3-5 Days"},
    "water": {"telugu": "Water Supply Dept", "phone": "0863-2340102", "days": "1-2 Days"},
    "light": {"telugu": "Electrical Dept", "phone": "0863-2340103", "days": "2-3 Days"},
    "drainage": {"telugu": "Drainage Dept", "phone": "0863-2340104", "days": "3-4 Days"},
    "garbage": {"telugu": "Sanitation Dept", "phone": "0863-2340105", "days": "1 Day"},
    "traffic": {"telugu": "Traffic Police", "phone": "0863-2340106", "days": "Same Day"},
}

zones = ["Seed Access Road", "Nehru Nagar", "Mandadam", "Venkatapalem", "Thullur", "Ananthavaram"]

zone = st.selectbox("Select Your Zone / Mee Zone:", zones, key="zone2")
lang = st.radio("Language:", ["Telugu + English", "English Only", "Telugu Only"], key="lang2")

user_input = st.text_input("Type your problem here / Mee samasya...", key="input1")
if st.button("Ask Mitra 🚀", key="ask2"):
    if not user_input:
        st.warning("Please type your problem first!")
    else:
        text = user_input.lower()
        # Detect category
        category = "road"
        if any(w in text for w in ["water", "neeru", "neellu", "tap"]):
            category = "water"
        elif any(w in text for w in ["light", "current", "bulb", "street light"]):
            category = "light"
        elif any(w in text for w in ["drainage", "muriki", "nala"]):
            category = "drainage"
        elif any(w in text for w in ["garbage", "chetta", "dustbin"]):
            category = "garbage"
        elif any(w in text for w in ["traffic", "jam", "signal"]):
            category = "traffic"

        dept = DEPTS[category]
        comp_id = f"AMR{random.randint(1000,9999)}"
        today = datetime.date.today()

        st.success(f"✅ Complaint Registered! ID: {comp_id}")
               # WhatsApp Share - UPDATED
    import urllib.parse
    msg = f"Namaste! Amaravati Mitra Complaint ID: {comp_id}. Problem: {user_input}. Dept: {category}. Please solve fast."
    whatsapp_link = f"https://wa.me/?text={urllib.parse.quote(msg)}"
    st.link_button("Share on WhatsApp", whatsapp_link)

    st.markdown(f"""
    ### Mitra Reply:
    **Namaste! Mee complaint ardham ayyindi.**
    **Department: {dept['telugu']}**
    **Phone: {dept['phone']}**
    **Expected Solution: {dept['days']}**
    """)
    
   