import streamlit as st
import random
import datetime

st.set_page_config(page_title="Amaravati Mitra - AI Citizen Assistant", page_icon="City", layout="centered")

try:
    st.image("logo.png.png", width=600)
except:
    pass

st.title("Amaravati Mitra")
st.subheader("AI Citizen Assistant | Telugu + English + Voice")
st.markdown("Ask in Telugu or English - Road, Water, Light, Drainage, Garbage")

# Departments
DEPTS = {
    "road": {"telugu": "Roads & Buildings Dept", "phone": "0863-2340101", "days": "3-5 Days"},
    "water": {"telugu": "Water Supply Dept", "phone": "0863-2340102", "days": "1-2 Days"},
    "light": {"telugu": "Electrical Dept", "phone": "0863-2340103", "days": "2-3 Days"},
    "drainage": {"telugu": "Drainage Dept", "phone": "0863-2340104", "days": "3-4 Days"},
    "garbage": {"telugu": "Sanitation Dept", "phone": "0863-2340105", "days": "1 Day"},
    "traffic": {"telugu": "Traffic Police", "phone": "0863-2340106", "days": "1 Day"},
}

ZONES = ["Seed Access Road", "Nekkallu", "Thullur", "Mangalagiri", "Vaddeswaram", "Uddandarayunipalem"]

def process_query(text):
    t = text.lower()
    if "road" in t or "pothole" in t or "gundam" in t:
        return "road", "Road complaint noted"
    if "water" in t or "neeru" in t or "tap" in t:
        return "water", "Water complaint noted"
    if "light" in t or "current" in t:
        return "light", "Light complaint noted"
    if "drain" in t or "muriki" in t:
        return "drainage", "Drainage complaint noted"
    if "garbage" in t or "chetta" in t or "dustbin" in t:
        return "garbage", "Garbage complaint noted"
    if "traffic" in t or "signal" in t:
        return "traffic", "Traffic complaint noted"
    return "general", "General complaint noted"

lang_choice = st.selectbox("Select Language", ["Telugu + English", "Telugu Only", "English Only"])
zone = st.selectbox("Select Zone / Area", ZONES)
user_input = st.text_area("Type your problem / Mee samasyanu ikkada type cheyandi", placeholder="e.g. Road lo pedda pothole undi...")

if st.button("Ask Mitra"):
    if user_input.strip() == "":
        st.warning("Please type your problem first")
    else:
        key, reply = process_query(user_input)
        if key in DEPTS:
            info = DEPTS[key]
        else:
            info = {"telugu": "CRDA Helpdesk", "phone": "0863-2340101", "days": "3-5 Days"}
        complaint_id = f"AMR{random.randint(1000, 9999)}"
        st.success(f"Complaint Registered! ID: {complaint_id}")
        st.markdown("### Mitra Reply:")
        if lang_choice == "Telugu Only":
            st.info(f"Namaste! Mee complaint {zone} lo {key} gurinchi nenu note chesukunnanu.")
        elif lang_choice == "English Only":
            st.info(f"Hello! Your complaint about {key} in {zone} is noted.")
        else:
            st.info(f"Namaste! Mee complaint {zone} lo {key} gurinchi ardham ayyindi.")
        st.write(f"Zone: {zone}")
        st.write(f"Department: {info['telugu']}")
        st.write(f"Phone: {info['phone']}")
        st.write(f"Expected Solution: {info['days']}")
        st.write(f"Complaint ID: {complaint_id}")
        st.write(f"Status: In Progress")
        wa_text = f"Mitra Complaint {complaint_id} - {key} in {zone}"
        st.link_button("Share on WhatsApp", f"https://wa.me/?text={wa_text}")

st.markdown("### How to use / Ela Vadali")
st.write("1. Choose language - Telugu / English / Both")
st.write("2. Type your problem in the box")
st.write("3. Click Ask Mitra")
st.write("4. Mitra will give Department, Phone & Days")