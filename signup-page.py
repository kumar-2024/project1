import streamlit as st
from datetime import date

# --- Page Config ---
st.set_page_config(
    page_title="Marwari College Ranchi | SignUp",
    page_icon="🎓",
    layout="centered"
)

# --- Custom CSS Styling ---
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Poppins', sans-serif;
        }

        .main {
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            min-height: 100vh;
        }

        .block-container {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 20px;
            padding: 2.5rem 3rem !important;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.1);
            box-shadow: 0 8px 32px rgba(0,0,0,0.3);
            margin-top: 2rem;
        }

        h1, h2, h3 {
            color: #ffffff !important;
        }

        label {
            color: #c9d6df !important;
            font-weight: 600;
        }

        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea,
        .stSelectbox > div > div,
        .stDateInput > div > div > input {
            background-color: rgba(255,255,255,0.08) !important;
            color: white !important;
            border: 1px solid rgba(255,255,255,0.2) !important;
            border-radius: 10px !important;
        }

        .stButton > button {
            background: linear-gradient(90deg, #f7971e, #ffd200);
            color: #0f2027;
            font-weight: 700;
            font-size: 16px;
            padding: 0.6rem 2.5rem;
            border-radius: 12px;
            border: none;
            width: 100%;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(247,151,30,0.4);
        }

        .stCheckbox > label,
        .stRadio > label {
            color: #c9d6df !important;
        }

        .stSlider > div > div > div {
            color: #ffd200 !important;
        }

        .section-header {
            color: #ffd200;
            font-size: 15px;
            font-weight: 600;
            letter-spacing: 0.5px;
            margin: 1.2rem 0 0.4rem 0;
            border-left: 3px solid #ffd200;
            padding-left: 8px;
        }

        .success-box {
            background: rgba(40, 200, 120, 0.15);
            border: 1px solid #28c878;
            border-radius: 12px;
            padding: 1rem 1.5rem;
            color: #28c878;
            font-size: 15px;
            margin-top: 1rem;
        }

        .college-banner {
            text-align: center;
            padding: 1rem 0 0.5rem 0;
        }

        .college-banner h1 {
            font-size: 2rem;
            font-weight: 700;
            color: #ffd200 !important;
            letter-spacing: 1px;
        }

        .college-banner p {
            color: #c9d6df;
            font-size: 14px;
            margin-top: -0.5rem;
        }

        hr {
            border: none;
            border-top: 1px solid rgba(255,255,255,0.1);
            margin: 1.2rem 0;
        }
    </style>
""", unsafe_allow_html=True)

# --- College Banner ---
st.markdown("""
    <div class="college-banner">
        <h1>🎓 Marwari College, Ranchi</h1>
        <p>Affiliated to Ranchi University | Empowering Futures Since 1952</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")
st.subheader("📋 Student Registration Form")
st.caption("Fill in the details below to create your student account.")
st.markdown("---")

# --- Section: Account Details ---
st.markdown('<p class="section-header">🔐 Account Details</p>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    username = st.text_input("👨‍💼 Username", placeholder="e.g. john_doe")
with col2:
    password = st.text_input("🔑 Password", type="password", placeholder="Min. 8 characters")

mobile = st.text_input("📞 Mobile Number", placeholder="e.g. 98XXXXXXXX")

# --- Section: Personal Info ---
st.markdown('<p class="section-header">👤 Personal Information</p>', unsafe_allow_html=True)
col3, col4 = st.columns(2)
with col3:
    dob = st.date_input("🎂 Date of Birth", value=date(2003, 1, 1),
                         min_value=date(1990, 1, 1), max_value=date(2010, 12, 31))
with col4:
    age = st.slider("🔢 Age", min_value=16, max_value=28, value=18)

gender = st.radio("⚧️ Gender", options=["Male 👨", "Female 👩", "Other 🧑"], horizontal=True)

address = st.text_area("🏠 Address", placeholder="Enter your full residential address...", height=100)

# --- Section: Academic Details ---
st.markdown('<p class="section-header">🏫 Academic Details</p>', unsafe_allow_html=True)
course = st.selectbox("📚 Select Your Course", [
    "B.SC CA – Computer Applications",
    "B.SC IT – Information Technology",
    "B.SC CS – Computer Science",
    "B.COM – Commerce",
    "B.A – Arts",
    "BBA – Business Administration"
])

st.markdown('<p class="section-header">🌐 Languages Known</p>', unsafe_allow_html=True)
col5, col6, col7, col8 = st.columns(4)
with col5:
    hindi    = st.checkbox("🇮🇳 Hindi")
with col6:
    english  = st.checkbox("🇬🇧 English")
with col7:
    nagpuri  = st.checkbox("🗣️ Nagpuri")
with col8:
    bhojpuri = st.checkbox("📢 Bhojpuri")

# --- Section: Documents ---
st.markdown('<p class="section-header">📁 Upload Documents</p>', unsafe_allow_html=True)
col9, col10 = st.columns(2)
with col9:
    photo = st.file_uploader("🖼️ Profile Photo", type=["jpg", "jpeg", "png"],
                              help="Upload a recent passport-size photograph")
with col10:
    live_photo = st.camera_input("📸 Take Live Photo")

# --- Terms & Submit ---
st.markdown("---")
agree = st.checkbox("☑️ I agree to the **Terms & Conditions** and confirm the information is accurate.")

if st.button("✅ Register Now"):
    errors = []
    if not username.strip():
        errors.append("Username is required.")
    if not password.strip() or len(password) < 8:
        errors.append("Password must be at least 8 characters.")
    if not mobile.strip() or not mobile.isdigit() or len(mobile) != 10:
        errors.append("Enter a valid 10-digit mobile number.")
    if not address.strip():
        errors.append("Address is required.")
    if not agree:
        errors.append("You must agree to the Terms & Conditions.")

    if errors:
        for err in errors:
            st.error(f"⚠️ {err}")
    else:
        langs = []
        if hindi:    langs.append("Hindi")
        if english:  langs.append("English")
        if nagpuri:  langs.append("Nagpuri")
        if bhojpuri: langs.append("Bhojpuri")

        st.markdown(f"""
        <div class="success-box">
            ✅ <strong>Registration Successful!</strong><br><br>
            👨‍💼 <strong>Username:</strong> {username}<br>
            📞 <strong>Mobile:</strong> {mobile}<br>
            📚 <strong>Course:</strong> {course}<br>
            🎂 <strong>DOB:</strong> {dob}<br>
            🔢 <strong>Age:</strong> {age}<br>
            ⚧️ <strong>Gender:</strong> {gender}<br>
            🌐 <strong>Languages:</strong> {', '.join(langs) if langs else 'None selected'}<br>
            🏠 <strong>Address:</strong> {address}
        </div>
        """, unsafe_allow_html=True)
        st.balloons()

# --- Footer ---
st.markdown("---")
st.markdown("""
    <p style='text-align:center; color:#6c8ebf; font-size:13px;'>
        © 2025 Marwari College, Ranchi &nbsp;|&nbsp; Developed with ❤️ using Streamlit
    </p>
""", unsafe_allow_html=True)