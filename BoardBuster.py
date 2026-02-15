import streamlit as st
import streamlit.components.v1 as components

# Page config
st.set_page_config(page_title="Board Stress Buster", page_icon="🔱", layout="wide")

# CSS to make everything black and fit perfectly
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    [data-testid="stHeader"] { display: none; }
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    .audio-wrapper {
        position: fixed;
        top: 20px;
        left: 50%;
        transform: translateX(-50%);
        z-index: 999;
        width: 90%;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Audio Player at the Top
audio_file_path = "2_5213430714921421985_20260210_163912.mp3"
st.markdown('<div class="audio-wrapper">', unsafe_allow_html=True)
try:
    with open(audio_file_path, "rb") as f:
        st.audio(f.read(), format="audio/mp3")
except:
    st.error("Audio file missing on GitHub!")
st.markdown('</div>', unsafe_allow_html=True)

# --- HYPNOTIC FULL SCREEN VISUALS ---
hypnotic_js = """
<canvas id="c" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: black;"></canvas>
<script>
    var c = document.getElementById("c");
    var ctx = c.getContext("2d");
    var w, h;
    var stars = [];

    function init() {
        w = window.innerWidth;
        h = window.innerHeight;
        c.width = w;
        c.height = h;
        stars = [];
        for (var i = 0; i < 300; i++) {
            stars.push({
                x: Math.random() * w,
                y: Math.random() * h,
                r: Math.random() * 2 + 1,
                vx: Math.random() * 2 - 1,
                vy: Math.random() * 2 - 1,
                hue: Math.random() * 360
            });
        }
    }

    function draw() {
        ctx.fillStyle = "rgba(0, 0, 0, 0.1)";
        ctx.fillRect(0, 0, w, h);
        for (var i = 0; i < stars.length; i++) {
            var s = stars[i];
            ctx.beginPath();
            ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
            ctx.fillStyle = "hsla(" + s.hue + ", 100%, 70%, 0.8)";
            ctx.fill();
            s.x += s.vx;
            s.y += s.vy;
            s.hue += 0.5;
            if (s.x < 0 || s.x > w) s.vx *= -1;
            if (s.y < 0 || s.y > h) s.vy *= -1;
        }
        requestAnimationFrame(draw);
    }
    window.addEventListener("resize", init);
    init();
    draw();
</script>
"""
# Height 1000 taaki scroll ka jhanjhat hi na ho
components.html(hypnotic_js, height=1000)
