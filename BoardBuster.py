import streamlit as st

# 1. Page Config
st.set_page_config(page_title="Board Stress Buster", page_icon="🔥", layout="centered")

# 2. Energetic CSS (Neon Red & Pulse Effect)
st.markdown("""
    <style>
    .stApp {
        background-color: #000000;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    [data-testid="stHeader"], footer { display: none; }
    
    .main-text {
        font-family: 'Arial Black', sans-serif;
        color: #FF0000; /* Pure Red */
        font-size: 70px;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 10px;
        /* Neon Glow Effect */
        text-shadow: 0 0 10px #FF0000, 0 0 20px #FF0000, 0 0 40px #FF0000;
        animation: pulse 1.5s infinite;
    }

    @keyframes pulse {
        0% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.05); opacity: 0.8; }
        100% { transform: scale(1); opacity: 1; }
    }
    
    .audio-container {
        display: flex;
        justify-content: center;
        margin-top: 10px;
    }

    /* Mobile Responsive */
    @media only screen and (max-width: 600px) {
        .main-text { font-size: 45px; }
    }
    </style>
    """, unsafe_allow_html=True)

# 3. High Energy Command
st.markdown('<h1 class="main-text">JA PHOD KE AA! 🔥</h1>', unsafe_allow_html=True)

# 4. Audio Section
audio_file_path = "2_5213430714921421985_20260210_163912.mp3"

st.markdown('<div class="audio-container">', unsafe_allow_html=True)
try:
    with open(audio_file_path, "rb") as f:
        st.audio(f.read(), format="audio/mp3")
except:
    st.error("Audio file missing on GitHub!")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<p style="color: #ffffff; font-weight: bold; text-align: center; margin-top: 30px; letter-spacing: 1px;">TUMSE BEHTAR KOI NAHI HAI. 🔱</p>', unsafe_allow_html=True)
