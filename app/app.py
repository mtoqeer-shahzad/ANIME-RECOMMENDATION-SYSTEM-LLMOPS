import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# =============================================
# PAGE CONFIG
# =============================================
st.set_page_config(
    page_title="AniMatch — AI Anime Recommender",
    page_icon="🎌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =============================================
# CUSTOM CSS
# =============================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Raleway:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300&display=swap');

/* ---- ROOT VARIABLES ---- */
:root {
    --bg-dark:        #07070f;
    --bg-card:        #0f0f1a;
    --bg-input:       #16162a;
    --accent-red:     #e94560;
    --accent-gold:    #f5a623;
    --accent-blue:    #4fc3f7;
    --text-primary:   #ffffff;
    --text-secondary: #8888aa;
    --text-muted:     #55556a;
}

/* ---- RESET & BASE ---- */
*, *::before, *::after { box-sizing: border-box; }

html, body,
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
.main {
    background: var(--bg-dark) !important;
    font-family: 'Raleway', sans-serif !important;
}

[data-testid="stAppViewContainer"] {
    background:
        radial-gradient(ellipse 80% 50% at 50% -10%, rgba(233,69,96,0.12) 0%, transparent 60%),
        radial-gradient(ellipse 60% 40% at 80% 80%, rgba(79,195,247,0.06) 0%, transparent 50%),
        var(--bg-dark) !important;
    min-height: 100vh;
}

[data-testid="stHeader"]      { background: transparent !important; }
[data-testid="stToolbar"]     { display: none !important; }
[data-testid="stDecoration"]  { display: none !important; }
#MainMenu, footer             { visibility: hidden !important; }

.block-container {
    max-width: 880px !important;
    margin: 0 auto !important;
    padding: 0 1.5rem 4rem !important;
}

/* ===================== HERO ===================== */
.hero {
    text-align: center;
    padding: 4rem 1rem 1.5rem;
}
.hero-eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: rgba(233,69,96,0.1);
    border: 1px solid rgba(233,69,96,0.35);
    color: var(--accent-red);
    padding: 0.35rem 1.2rem;
    border-radius: 100px;
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 1.6rem;
}
.hero-title {
    font-family: 'Cinzel', serif;
    font-size: clamp(2.8rem, 7vw, 5.5rem);
    font-weight: 900;
    line-height: 1;
    letter-spacing: -1px;
    background: linear-gradient(135deg, #ffffff 0%, #e94560 45%, #f5a623 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 1rem;
}
.hero-sub {
    font-size: 1rem;
    color: var(--text-secondary);
    font-weight: 300;
    letter-spacing: 0.5px;
    line-height: 1.7;
    max-width: 480px;
    margin: 0 auto;
}

/* ===================== ORNAMENT ===================== */
.ornament {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin: 2.5rem auto;
    max-width: 340px;
}
.ornament-line {
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(233,69,96,0.45), transparent);
}
.ornament-sym { color: var(--accent-gold); font-size: 1rem; }

/* ===================== STATS ===================== */
.stats {
    display: flex;
    justify-content: center;
    margin: 0 auto 2.5rem;
    max-width: 540px;
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 18px;
    overflow: hidden;
}
.stat {
    flex: 1;
    text-align: center;
    padding: 1.2rem 0.8rem;
    border-right: 1px solid rgba(255,255,255,0.06);
}
.stat:last-child { border-right: none; }
.stat-val {
    font-family: 'Cinzel', serif;
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--accent-red);
    line-height: 1;
}
.stat-lbl {
    font-size: 0.62rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--text-muted);
    margin-top: 0.4rem;
}

/* ===================== SEARCH CARD ===================== */
.search-card {
    background: var(--bg-card);
    border: 1px solid rgba(233,69,96,0.16);
    border-radius: 24px;
    padding: 2.5rem 2.5rem 2rem;
    position: relative;
    overflow: hidden;
    box-shadow: 0 20px 60px rgba(0,0,0,0.5), 0 0 80px rgba(233,69,96,0.03);
    margin-bottom: 0.5rem;
}
.search-card::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse 100% 50% at 50% 0%, rgba(233,69,96,0.06) 0%, transparent 70%);
    pointer-events: none;
}
.search-card::after {
    content: '';
    position: absolute;
    top: 0; left: 8%; right: 8%;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--accent-red), var(--accent-gold), transparent);
}

/* ===================== INPUT ===================== */
[data-testid="stTextInput"] label {
    color: var(--accent-red) !important;
    font-family: 'Raleway', sans-serif !important;
    font-size: 0.67rem !important;
    font-weight: 700 !important;
    letter-spacing: 3px !important;
    text-transform: uppercase !important;
}
[data-testid="stTextInput"] input {
    background: var(--bg-input) !important;
    border: 1px solid rgba(233,69,96,0.22) !important;
    border-radius: 14px !important;
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
    font-family: 'Raleway', sans-serif !important;
    font-size: 0.97rem !important;
    font-weight: 400 !important;
    padding: 0.9rem 1.2rem !important;
    transition: all 0.25s !important;
    caret-color: var(--accent-red) !important;
}
[data-testid="stTextInput"] input:focus {
    border-color: var(--accent-red) !important;
    box-shadow: 0 0 0 3px rgba(233,69,96,0.12) !important;
    background: #1a1a2e !important;
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
    outline: none !important;
}
[data-testid="stTextInput"] input:hover {
    border-color: rgba(233,69,96,0.4) !important;
}
[data-testid="stTextInput"] input::placeholder {
    color: #404060 !important;
    -webkit-text-fill-color: #404060 !important;
    font-style: italic !important;
    font-weight: 300 !important;
}

/* ===================== CHIPS ===================== */
.chips-section { margin-top: 1.4rem; }
.chips-title {
    font-size: 0.6rem;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: var(--text-muted);
    margin-bottom: 0.65rem;
    font-weight: 600;
}
.chips { display: flex; flex-wrap: wrap; gap: 0.45rem; }
.chip {
    background: rgba(79,195,247,0.05);
    border: 1px solid rgba(79,195,247,0.18);
    color: #6ab8d4;
    padding: 0.28rem 0.8rem;
    border-radius: 100px;
    font-size: 0.7rem;
    font-family: 'Raleway', sans-serif;
    font-weight: 500;
    cursor: default;
    transition: all 0.2s;
}
.chip:hover {
    background: rgba(79,195,247,0.1);
    border-color: rgba(79,195,247,0.35);
    color: var(--accent-blue);
}

/* ===================== BUTTON ===================== */
[data-testid="stButton"] > button {
    background: linear-gradient(135deg, #e94560 0%, #c0303f 100%) !important;
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
    border: none !important;
    border-radius: 14px !important;
    font-family: 'Raleway', sans-serif !important;
    font-size: 0.83rem !important;
    font-weight: 700 !important;
    letter-spacing: 2.5px !important;
    text-transform: uppercase !important;
    padding: 0.85rem 2rem !important;
    width: 100% !important;
    margin-top: 1.4rem !important;
    transition: all 0.25s !important;
    box-shadow: 0 4px 24px rgba(233,69,96,0.35) !important;
}
[data-testid="stButton"] > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 32px rgba(233,69,96,0.5) !important;
    background: linear-gradient(135deg, #f05070 0%, #d04050 100%) !important;
}
[data-testid="stButton"] > button:active {
    transform: translateY(0px) !important;
}

/* ===================== ALERTS ===================== */
.alert {
    border-radius: 14px;
    padding: 1rem 1.3rem;
    font-family: 'Raleway', sans-serif;
    font-size: 0.87rem;
    margin-top: 1.2rem;
    display: flex;
    align-items: flex-start;
    gap: 0.6rem;
    line-height: 1.5;
}
.alert-warn {
    background: rgba(245,166,35,0.07);
    border: 1px solid rgba(245,166,35,0.25);
    color: #c8a04a;
}
.alert-err {
    background: rgba(233,69,96,0.07);
    border: 1px solid rgba(233,69,96,0.25);
    color: #c05060;
}

/* ===================== RESULT ===================== */
.result-section { margin-top: 2rem; }
.result-hdr {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 1.2rem;
}
.rhl { flex:1; height:1px; background: linear-gradient(90deg, transparent, rgba(245,166,35,0.55)); }
.rhr { flex:1; height:1px; background: linear-gradient(90deg, rgba(245,166,35,0.55), transparent); }
.result-hdr-txt {
    font-family: 'Cinzel', serif;
    font-size: 0.7rem;
    color: var(--accent-gold);
    letter-spacing: 3px;
    text-transform: uppercase;
    white-space: nowrap;
}
.result-card {
    background: var(--bg-card);
    border: 1px solid rgba(245,166,35,0.16);
    border-radius: 20px;
    padding: 2rem 2.2rem;
    position: relative;
    overflow: hidden;
    box-shadow: 0 20px 60px rgba(0,0,0,0.4), 0 0 50px rgba(245,166,35,0.02);
}
.result-card::after {
    content: '';
    position: absolute;
    top: 0; left: 8%; right: 8%;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--accent-gold), transparent);
}
.result-card p,
.result-card li,
.result-card span,
.result-card div {
    color: #d8d8f0 !important;
    font-family: 'Raleway', sans-serif !important;
    line-height: 1.85 !important;
}
.result-card strong {
    color: var(--accent-gold) !important;
    font-weight: 700 !important;
}
.result-card h1,.result-card h2,.result-card h3 {
    color: #ffffff !important;
    font-family: 'Cinzel', serif !important;
    margin-bottom: 0.5rem !important;
}

/* ===================== FOOTER ===================== */
.site-footer {
    text-align: center;
    margin-top: 4rem;
    padding: 2rem 1rem;
    border-top: 1px solid rgba(255,255,255,0.04);
}
.footer-stack {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 0.4rem 0.8rem;
    margin-bottom: 1rem;
}
.footer-tag {
    font-size: 0.65rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: var(--text-muted);
    padding: 0.2rem 0.65rem;
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 100px;
}
.footer-copy {
    font-size: 0.7rem;
    color: var(--text-muted);
    letter-spacing: 0.5px;
}
.footer-copy span { color: var(--accent-red); }

/* ===================== SCROLLBAR ===================== */
::-webkit-scrollbar       { width: 5px; }
::-webkit-scrollbar-track { background: var(--bg-dark); }
::-webkit-scrollbar-thumb { background: rgba(233,69,96,0.4); border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: var(--accent-red); }

/* ===================== RESPONSIVE ===================== */
@media (max-width: 768px) {
    .block-container { padding: 0 1rem 3rem !important; }
    .hero { padding: 2.5rem 0.5rem 1rem; }
    .search-card { padding: 1.8rem 1.4rem 1.5rem; }
    .result-card { padding: 1.4rem 1.2rem; }
    .stats { max-width: 100%; }
}
@media (max-width: 480px) {
    .hero-title { font-size: 2.2rem !important; }
    .stats { flex-direction: column; }
    .stat { border-right: none; border-bottom: 1px solid rgba(255,255,255,0.06); }
    .stat:last-child { border-bottom: none; }
    .search-card { padding: 1.3rem 1rem; }
    .result-card { padding: 1.2rem 1rem; }
}
</style>
""", unsafe_allow_html=True)


# =============================================
# PIPELINE LOAD
# =============================================
@st.cache_resource(show_spinner=False)
def init_pipeline():
    try:
        from pipeline.pipeline import AnimeRecommendationPipeline
        return AnimeRecommendationPipeline()
    except Exception:
        return None


# =============================================
# HERO
# =============================================
st.markdown("""
<div class="hero">
    <div class="hero-eyebrow">🎌 &nbsp; AI — Powered Recommender</div>
    <h1 class="hero-title">AniMatch</h1>
    <p class="hero-sub">
        Describe your mood, a favourite anime, or a genre —<br>
        and let AI find your next obsession.
    </p>
</div>

<div class="ornament">
    <div class="ornament-line"></div>
    <span class="ornament-sym">⛩</span>
    <div class="ornament-line"></div>
</div>
""", unsafe_allow_html=True)


# =============================================
# STATS
# =============================================
st.markdown("""
<div class="stats">
    <div class="stat">
        <div class="stat-val">1200+</div>
        <div class="stat-lbl">Anime in DB</div>
    </div>
    <div class="stat">
        <div class="stat-val">LLaMA&nbsp;3</div>
        <div class="stat-lbl">AI Model</div>
    </div>
    <div class="stat">
        <div class="stat-val">3</div>
        <div class="stat-lbl">Picks for You</div>
    </div>
    <div class="stat">
        <div class="stat-val">RAG</div>
        <div class="stat-lbl">Technology</div>
    </div>
</div>
""", unsafe_allow_html=True)


# =============================================
# SEARCH CARD
# =============================================
st.markdown('<div class="search-card">', unsafe_allow_html=True)

query = st.text_input(
    "✦  WHAT ARE YOU IN THE MOOD FOR?",
    placeholder="e.g.  dark psychological thriller like Death Note…",
    key="anime_query"
)

st.markdown("""
<div class="chips-section">
    <div class="chips-title">✦ &nbsp; Try searching for</div>
    <div class="chips">
        <span class="chip">⚔️ Action &amp; Fighting</span>
        <span class="chip">💕 Romance &amp; School</span>
        <span class="chip">🧠 Dark Psychological</span>
        <span class="chip">🌟 Isekai Adventure</span>
        <span class="chip">😂 Comedy &amp; Slice of Life</span>
        <span class="chip">👻 Horror &amp; Mystery</span>
        <span class="chip">🤖 Sci-Fi &amp; Mecha</span>
        <span class="chip">🏆 Sports &amp; Competition</span>
    </div>
</div>
""", unsafe_allow_html=True)

search_btn = st.button("🎯  FIND MY ANIME", key="search_btn")

st.markdown("</div>", unsafe_allow_html=True)


# =============================================
# RESULTS
# =============================================
if search_btn:
    if not query.strip():
        st.markdown("""
        <div class="alert alert-warn">
            ⚠️ &nbsp; Please describe what kind of anime you're looking for!
        </div>
        """, unsafe_allow_html=True)
    else:
        with st.spinner("🔍  Scanning the anime universe…"):
            pipeline = init_pipeline()

        if pipeline is None:
            st.markdown("""
            <div class="alert alert-err">
                ❌ &nbsp; Pipeline could not be loaded.
                Please run <strong>build_pipeline.py</strong> first
                so the ChromaDB vector store exists.
            </div>
            """, unsafe_allow_html=True)
        else:
            with st.spinner("✨  Generating your recommendations…"):
                try:
                    response = pipeline.recommend(query)

                    st.markdown("""
                    <div class="result-section">
                        <div class="result-hdr">
                            <div class="rhl"></div>
                            <div class="result-hdr-txt">✦ &nbsp; Your Recommendations</div>
                            <div class="rhr"></div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                    st.markdown('<div class="result-card">', unsafe_allow_html=True)
                    st.markdown(response)
                    st.markdown("</div>", unsafe_allow_html=True)

                except Exception as e:
                    st.markdown(f"""
                    <div class="alert alert-err">
                        ❌ &nbsp; Something went wrong: {str(e)}
                    </div>
                    """, unsafe_allow_html=True)


# =============================================
# FOOTER
# =============================================
st.markdown("""
<div class="site-footer">
    <div class="footer-stack">
        <span class="footer-tag">LangChain</span>
        <span class="footer-tag">Groq · LLaMA 3</span>
        <span class="footer-tag">ChromaDB</span>
        <span class="footer-tag">HuggingFace</span>
        <span class="footer-tag">Streamlit</span>
    </div>
    <div class="footer-copy">
        Built with <span>♥</span> &nbsp;·&nbsp; AniMatch v1.0 &nbsp;·&nbsp; 🎌
    </div>
</div>
""", unsafe_allow_html=True)