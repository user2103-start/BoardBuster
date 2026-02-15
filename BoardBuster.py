import streamlit as st

# 1. Page Config
st.set_page_config(page_title="Board Stress Buster", page_icon="🔱", layout="centered")

# 2. CSS for Styling (Black Background, Bold Gold Text)
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
        font-family: 'Arial Black', Gadget, sans-serif;
        color: #FFD700; /* Golden Color */
        font-size: 60px;
        text-align: center;
        line-height: 1.2;
        margin-bottom: 5px; /* .5 cm gap approx */
        text-shadow: 2px 2px 10px rgba(255, 215, 0, 0.5);
    }
    
    .audio-container {
        display: flex;
        justify-content: center;
        width: 100%;
    }
    
    /* Mobile Responsive Fix */
    @media only screen and (max-width: 600px) {
        .main-text { font-size: 40px; }
    }
    </style>
    """, unsafe_allow_html=True)

# 3. The Bold Text
st.markdown('<h1 class="main-text">JA PHOD KE AA! 🚀</h1>', unsafe_allow_html=True)

# 4. Audio Section (Just below the text)
audio_file_path = "2_5213430714921421985_20260210_163912.mp3"

try:
    with open(audio_file_path, "rb") as f:
        audio_bytes = f.read()
    st.audio(audio_bytes, format="audio/mp3")
except Exception as e:
    st.error("Audio file check karein!")

st.markdown('<p style="color: #666; text-align: center; margin-top: 20px;">Listen. Breathe. Conquer.</p>', unsafe_allow_html=True)
