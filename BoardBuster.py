import streamlit as st

# 1. Page Config
st.set_page_config(page_title="Board Stress Buster", page_icon="🔥", layout="centered")

# 2. Energetic CSS (Neon Red, Pulse, and TG Button)
st.markdown("""
    <style>
    .stApp {
        background-color: #000000;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    [data-testid="stHeader"], footer { display: none; }
    
    .main-text {
        font-family: 'Arial Black', sans-serif;
        color: #FF0000;
        font-size: 70px;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 5px;
        text-shadow: 0 0 10px #FF0000, 0 0 20px #FF0000, 0 0 40px #FF0000;
        animation: pulse 1.5s infinite;
    }

    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    .tg-container {
        margin-top: 40px;
        text-align: center;
    }

    .tg-button {
        display: inline-flex;
        align-items: center;
        background-color: #229ED9; /* Telegram Blue */
        color: white !important;
        padding: 12px 25px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: bold;
        font-family: sans-serif;
        box-shadow: 0 0 15px rgba(34, 158, 217, 0.6);
        transition: 0.3s;
    }

    .tg-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 0 25px rgba(34, 158, 217, 0.9);
    }

    .tg-logo {
        width: 25px;
        margin-right: 10px;
    }

    @media only screen and (max-width: 600px) {
        .main-text { font-size: 45px; }
    }
    </style>
    """, unsafe_allow_html=True)

# 3. High Energy Command
st.markdown('<h1 class="main-text">JA PHOD KE AA! 🔥</h1>', unsafe_allow_html=True)

# 4. Audio Section
audio_file_path = "2_5213430714921421985_20260210_163912.mp3"
try:
    with open(audio_file_path, "rb") as f:
        st.audio(f.read(), format="audio/mp3")
except:
    st.error("Audio file check karein!")

# 5. Telegram Channel Link
st.markdown(f"""
    <div class="tg-container">
        <p style="color: #666; margin-bottom: 10px; font-size: 14px;">Join for more Motivation & Updates</p>
        <a href="https://t.me/+DWoy0pgaw9VjOGM1" target="_blank" class="tg-button">
            <img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg" class="tg-logo">
            Join Telegram Channel
        </a>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<p style="color: #444; text-align: center; margin-top: 50px; font-size: 12px;">Made with ❤️ for Students</p>', unsafe_allow_html=True)
