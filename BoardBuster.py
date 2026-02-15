import streamlit as st
import streamlit.components.v1 as components

# Page Config
st.set_page_config(page_title="Board Stress Buster", page_icon="🔱", layout="centered")

# Custom Styling (FIXED: unsafe_allow_html=True)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    h1 { color: #00ffcc; text-align: center; font-family: 'Courier New', Courier, monospace; }
    .stAudio { margin-top: 20px; border-radius: 50px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔱 Board Exam Stress Buster")
st.write("<p style='text-align: center; color: #aaa;'> इयरफ़ोन लगा लो, आँखें बंद करो और बस महसूस करो...</p>", unsafe_allow_html=True)

# --- 1. HEXAGON ANIMATION ---
hex_code = """
<canvas id="canvas"></canvas>
<style>
    body { margin: 0; overflow: hidden; background: #0e1117; }
    canvas { display: block; width: 100vw; height: 350px; }
</style>
<script>
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = 350;

    let tick = 0;
    function drawHex(x, y, size, color) {
        ctx.beginPath();
        for (let i = 0; i < 6; i++) {
            ctx.lineTo(x + size * Math.cos(i * Math.PI / 3), y + size * Math.sin(i * Math.PI / 3));
        }
        ctx.closePath();
        ctx.strokeStyle = color;
        ctx.lineWidth = 2;
        ctx.stroke();
    }

    function animate() {
        ctx.fillStyle = 'rgba(14, 17, 23, 0.15)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        for (let x = 0; x < canvas.width + 60; x += 60) {
            for (let y = 0; y < canvas.height + 60; y += 60) {
                let size = 15 + Math.sin(tick * 0.03 + (x + y) * 0.01) * 12;
                let hue = (tick * 0.5 + x * 0.1) % 360;
                drawHex(x, y, size, `hsla(${hue}, 80%, 60%, 0.5)`);
            }
        }
        tick++;
        requestAnimationFrame(animate);
    }
    animate();
</script>
"""
components.html(hex_code, height=350)

# --- 2. AUDIO SECTION ---
audio_file_path = "2_5213430714921421985_20260210_163912.mp3"

try:
    with open(audio_file_path, "rb") as f:
        audio_bytes = f.read()
    st.audio(audio_bytes, format="audio/mp3")
except Exception as e:
    st.error("Audio file play nahi ho rahi. Check karein ki file GitHub par uploaded hai.")

# --- 3. MOTIVATIONAL QUOTES ---
st.divider()
st.markdown("""
> "कम पढ़कर भी जो बच्चा फोड़ के आए, उसे लेजेंड कहते हैं और तू एक लेजेंड है!"

**Important Reminders:**
* **120% Effort:** इस पेपर में अपना बेस्ट देकर आना है।
* **Never Give Up:** जब तक टीचर पेपर न छीन ले, तब तक लिखते रहना है।
* **The Why:** अच्छे मार्क्स इसलिए चाहिए ताकि कल कोई तुम्हें दबा न सके।
""")

st.success("Best of luck! Ja, Phod Ke Aa! 🚀")
