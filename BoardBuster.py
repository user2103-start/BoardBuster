import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Board Stress Buster", page_icon="🔱", layout="wide")

# CSS for a clean, immersive look
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    [data-testid="stHeader"], footer, #MainMenu { display: none; }
    .audio-wrapper {
        position: fixed;
        bottom: 30px;
        left: 50%;
        transform: translateX(-50%);
        z-index: 999;
        background: rgba(255, 255, 255, 0.05);
        padding: 15px;
        border-radius: 30px;
        backdrop-filter: blur(8px);
    }
    </style>
    """, unsafe_allow_html=True)

# Audio at the bottom for better reach
audio_file_path = "2_5213430714921421985_20260210_163912.mp3"
st.markdown('<div class="audio-wrapper">', unsafe_allow_html=True)
try:
    with open(audio_file_path, "rb") as f:
        st.audio(f.read(), format="audio/mp3")
except:
    st.error("Audio file missing!")
st.markdown('</div>', unsafe_allow_html=True)

# --- ADVANCED SPIROGRAPH / FLUID VISUALS ---
hypnotic_js = """
<canvas id="canvas" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: #000;"></canvas>
<script>
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    let w, h, particles = [];

    function init() {
        w = window.innerWidth;
        h = window.innerHeight;
        canvas.width = w;
        canvas.height = h;
    }

    let hue = 0;
    function draw() {
        ctx.fillStyle = 'rgba(0, 0, 0, 0.05)'; // Trail effect
        ctx.fillRect(0, 0, w, h);
        
        let time = Date.now() * 0.001;
        ctx.translate(w/2, h/2);
        
        for (let i = 0; i < 100; i++) {
            let angle = i * 0.2 + time;
            let radius = Math.sin(i * 0.02 + time) * (w * 0.35);
            let x = Math.cos(angle) * radius;
            let y = Math.sin(angle) * radius;
            
            ctx.beginPath();
            ctx.arc(x, y, 2, 0, Math.PI * 2);
            ctx.fillStyle = `hsla(${hue + i}, 80%, 60%, 0.8)`;
            ctx.fill();
        }
        
        ctx.translate(-w/2, -h/2);
        hue += 0.5;
        requestAnimationFrame(draw);
    }

    window.addEventListener('resize', init);
    init();
    draw();
</script>
"""
components.html(hypnotic_js, height=2000)
