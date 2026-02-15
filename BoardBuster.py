import streamlit as st
import streamlit.components.v1 as components

# 1. Page Config (Mobile friendly & Full Width)
st.set_page_config(page_title="Board Stress Buster", page_icon="🔱", layout="wide")

# 2. CSS for Full Screen & Dark UI
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp { background-color: #000000; }
    .audio-container {
        position: fixed;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        z-index: 100;
        background: rgba(255, 255, 255, 0.1);
        padding: 10px;
        border-radius: 50px;
        backdrop-filter: blur(10px);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. HIGH-END VISUALS (Full Screen Starfield/Tunnel)
visuals_code = """
<canvas id="canvas" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 1;"></canvas>
<script>
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    let w, h, stars = [];

    function init() {
        w = window.innerWidth;
        h = window.innerHeight;
        canvas.width = w;
        canvas.height = h;
        stars = [];
        for(let i=0; i<400; i++) {
            stars.push({
                x: Math.random() * w - w/2,
                y: Math.random() * h - h/2,
                z: Math.random() * w,
                o: Math.random()
            });
        }
    }

    function draw() {
        ctx.fillStyle = 'rgba(0, 0, 0, 0.2)';
        ctx.fillRect(0, 0, w, h);
        ctx.save();
        ctx.translate(w/2, h/2);
        
        stars.forEach(s => {
            s.z -= 4; // Speed
            if(s.z <= 0) s.z = w;
            
            let x = s.x * (w/s.z);
            let y = s.y * (w/s.z);
            let size = (1 - s.z/w) * 5;
            
            ctx.beginPath();
            ctx.arc(x, y, size, 0, Math.PI*2);
            ctx.fillStyle = `hsla(${s.z % 360}, 70%, 70%, ${1 - s.z/w})`;
            ctx.fill();
        });
        ctx.restore();
        requestAnimationFrame(draw);
    }

    window.addEventListener('resize', init);
    init();
    draw();
</script>
"""
components.html(visuals_code, height=0) # Hidden trigger for JS

# 4. AUDIO OVERLAY
audio_file_path = "2_5213430714921421985_20260210_163912.mp3"
st.markdown('<div class="audio-container">', unsafe_allow_html=True)
try:
    with open(audio_file_path, "rb") as f:
        st.audio(f.read(), format="audio/mp3")
except:
    st.error("Audio Load Nahi Hui!")
st.markdown('</div>', unsafe_allow_html=True)
