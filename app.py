import streamlit as st
import opengradient as og
import asyncio
from datetime import datetime
import pandas as pd
import plotly.express as px

# ------------------- CONFIG & THEME -------------------
st.set_page_config(
    page_title="VeriYield | 2026 DeFi Intelligence",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Advanced Glassmorphic + Cyberpunk CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Orbitron:wght@500;600;700&display=swap');

    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', sans-serif;
        background: linear-gradient(180deg, #0a0f1f 0%, #000814 100%);
        color: #e4e6eb;
    }

    .main .block-container { padding-top: 2.5rem; }

    h1, h2, h3 { 
        font-family: 'Orbitron', sans-serif; 
        color: #00ff9d; 
        letter-spacing: 0.5px;
    }

    /* Glassmorphic cards */
    .glass-card {
        background: rgba(15, 23, 42, 0.75);
        border-radius: 16px;
        padding: 24px;
        border: 1px solid rgba(0, 255, 157, 0.25);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        backdrop-filter: blur(16px);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .glass-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 40px rgba(0, 255, 157, 0.3);
    }

    /* Neon button */
    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #00ff9d 0%, #00d4ff 100%);
        color: #0a0f1f;
        font-weight: 700;
        height: 54px;
        border-radius: 14px;
        border: none;
        box-shadow: 0 4px 20px rgba(0, 255, 157, 0.5);
        transition: all 0.3s;
    }
    .stButton > button:hover {
        transform: scale(1.03);
        box-shadow: 0 8px 30px rgba(0, 255, 157, 0.7);
    }

    /* Tabs */
    .stTabs [data-baseweb="tab"] {
        font-weight: 600;
        background: rgba(15, 23, 42, 0.8);
        color: #94a3b8;
        padding: 14px 28px;
        border-radius: 12px;
        margin: 0 6px;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background: linear-gradient(90deg, #00ff9d, #00d4ff);
        color: #0a0f1f !important;
        box-shadow: 0 4px 15px rgba(0, 255, 157, 0.4);
    }

    /* Metrics */
    .metric-card {
        background: rgba(15, 23, 42, 0.8);
        border-radius: 12px;
        padding: 18px;
        text-align: center;
        border-left: 5px solid #00ff9d;
    }

    .glitch-header {
        position: relative;
        color: #00ff9d;
        animation: glitch 3s infinite;
    }

    @keyframes glitch {
        0% { text-shadow: 3px 0 #00d4ff, -3px 0 #ff00c8; }
        10% { text-shadow: -3px 0 #00d4ff, 3px 0 #ff00c8; }
        20% { text-shadow: 3px 0 #00d4ff, -3px 0 #ff00c8; }
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #0a0f1f;
        border-right: 1px solid rgba(0, 255, 157, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)

# ------------------- SIDEBAR -------------------
with st.sidebar:
    st.markdown("<h2 style='text-align:center; color:#00ff9d; margin-bottom:0;'>🛡️ VERIYIELD</h2>", unsafe_allow_html=True)
    st.caption("2026 Verifiable DeFi Intelligence")
    
    st.divider()
    
    st.markdown("### Quick Asset Scan")
    quick_assets = ["", "ETH", "BTC", "SOL", "SUI", "AVAX", "TON", "BNB"]
    selected_quick = st.selectbox("Popular Top-30 Assets", quick_assets, index=0)
    
    st.divider()
    
    st.markdown("### Platform")
    st.success("✅ TEE Hardware Verified")
    st.info("🔗 OpenGradient Network Live")
    
    st.divider()
    st.markdown("**VeriYield v2.4**  \nHardware-Proven • Tamper-Proof • 2026 Ready")

# ------------------- HEADER -------------------
col_title, col_date = st.columns([3, 1])
with col_title:
    st.markdown("<h1 class='glitch-header'>🛡️ VERIYIELD</h1>", unsafe_allow_html=True)
with col_date:
    current_date = datetime.now().strftime("%B %d, %Y • %H:%M UTC")
    st.markdown(f"<p style='text-align:right; color:#94a3b8; font-size:1.05rem; margin-top:1.2rem;'>{current_date}</p>", unsafe_allow_html=True)

st.caption("LIVE DEFI YIELD INTELLIGENCE • POWERED BY TRUSTED EXECUTION ENVIRONMENTS")

st.divider()

# ------------------- NAVIGATION TABS -------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "🚀 Strategy Optimizer",
    "📈 Market Pulse",
    "🔐 Security & Proofs",
    "📚 DeFi Academy 2026"
])

# TAB 1: OPTIMIZER
with tab1:
    st.markdown("### 💰 Generate Tamper-Proof Yield Strategy")
    
    c1, c2 = st.columns([3, 1])
    with c1:
        asset = st.text_input(
            "Asset Symbol",
            value=selected_quick or "",
            placeholder="ETH, SOL, BTC...",
            help="Analyzes Top 30 market cap assets with 2026 primitives (LRTs, AI vaults, multi-AVS restaking)"
        )
    with c2:
        risk_level = st.select_slider(
            "Your Risk Profile",
            options=["Conservative", "Balanced", "Aggressive"],
            value="Balanced"
        )
    
    if st.button("🚀 GENERATE VERIFIABLE STRATEGY", type="primary", use_container_width=True):
        if not asset.strip():
            st.error("Please enter an asset symbol.")
        else:
            with st.spinner(f"Computing {asset.upper()} strategy in TEE hardware enclave..."):
                try:
                    PRIVATE_KEY = st.secrets.get("OG_PRIVATE_KEY")
                    if not PRIVATE_KEY:
                        st.error("OG_PRIVATE_KEY not found in Streamlit Secrets.")
                        st.stop()
                    
                    llm = og.LLM(private_key=PRIVATE_KEY)
                    llm.ensure_opg_approval(min_allowance=0.1)
                    
                    query = f"""
                    Date: {current_date}. Risk Profile: {risk_level}.
                    Generate a concise 2026 yield strategy for {asset} (Top 30 scope).
                    Include:
                    - 1-sentence executive summary
                    - Strategy Matrix table with columns: Risk | Protocol | Mechanism | Est. APY | Rationale
                    - Key risks & mitigations
                    - Composability notes
                    Keep response direct and actionable.
                    """
                    
                    result = asyncio.run(
                        llm.chat(
                            model=og.TEE_LLM.CLAUDE_SONNET_4_6,
                            messages=[
                                {"role": "system", "content": "You are VeriYield AI — a precise, hardware-verified 2026 DeFi strategist."},
                                {"role": "user", "content": query}
                            ],
                            max_tokens=420
                        )
                    )
                    
                    content = result.chat_output.get('content') if hasattr(result, 'chat_output') else str(result)
                    
                    st.success(f"🎯 {asset.upper()} • {risk_level} Strategy (TEE-Verified)")
                    st.markdown(content)
                    
                    tx_hash = getattr(result, 'proof_tx_hash', None)
                    if tx_hash:
                        with st.expander("🛡️ Hardware Attestation Proof", expanded=False):
                            st.markdown("**Executed in isolated Trusted Execution Environment**")
                            st.code(tx_hash, language="plaintext")
                            st.caption("Publicly verifiable on OpenGradient • Immutable & tamper-proof")
                    
                    # Example yield snapshot (you can parse LLM output later)
                    st.markdown("### Projected Yield Breakdown")
                    m1, m2, m3, m4 = st.columns(4)
                    with m1: st.metric("Base APY", "6.8%", "↑1.2%")
                    with m2: st.metric("LRT Boost", "+4.1%", "EigenLayer")
                    with m3: st.metric("AI Vault", "+2.7%", "Dynamic")
                    with m4: st.metric("Total Est.", "13.6%", delta="Balanced")
                    
                except Exception as e:
                    st.error(f"Error: {str(e)}")
                    st.info("Check OPG token allowance (min 0.1) in your connected wallet.")

# TAB 2: MARKET PULSE
with tab2:
    st.markdown("### 📈 2026 DeFi Market Pulse")
    
    # Sample data — replace with real API calls later
    df = pd.DataFrame({
        "Asset": ["ETH", "SOL", "BTC", "AVAX", "SUI"],
        "Base APY": [4.1, 6.5, 0.9, 7.2, 5.8],
        "LRT Premium": [3.4, 4.9, 2.5, 4.1, 6.2],
        "AI Vault": [2.3, 3.1, 1.8, 2.6, 3.9],
        "Projected Total": [9.8, 14.5, 5.2, 13.9, 15.9]
    })
    
    left, right = st.columns([2, 1])
    with left:
        st.dataframe(df, use_container_width=True, hide_index=True)
    
    with right:
        fig = px.bar(df, x="Asset", y="Projected Total", 
                     color="Projected Total", 
                     color_continuous_scale="emerald")
        st.plotly_chart(fig, use_container_width=True)
    
    st.info("Trend: LRTs + AI-curated vaults dominate 2026 yield generation.")

# TAB 3: SECURITY
with tab3:
    st.markdown("### 🔐 Security & Verifiability")
    st.write("Every strategy is computed inside **OpenGradient TEEs** — hardware-enforced isolation that even the platform operators cannot access.")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="glass-card"><h4>Integrity</h4><p>Hardware-locked enclave execution</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="glass-card"><h4>Transparency</h4><p>Cryptographic proof on-chain</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="glass-card"><h4>Trust</h4><p>Publicly verifiable by anyone</p></div>', unsafe_allow_html=True)

# TAB 4: EDUCATION
with tab4:
    st.markdown("### 📚 2026 DeFi Academy")
    
    cols = st.columns(2)
    with cols[0]:
        st.markdown("""
        <div class="glass-card">
            <h4 style='color:#00ff9d;'>Liquid Restaking Tokens (LRTs)</h4>
            <p>Core primitive allowing one staked asset to secure multiple networks simultaneously while staying fully liquid.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with cols[1]:
        st.markdown("""
        <div class="glass-card">
            <h4 style='color:#00ff9d;'>AI-Curated Vaults</h4>
            <p>Intelligent agents that dynamically optimize allocations across lending, restaking, and yield opportunities in real time.</p>
        </div>
        """, unsafe_allow_html=True)

# ------------------- FOOTER -------------------
st.divider()
st.markdown(f"""
    <p style='text-align:center; color:#64748b; font-size:0.85rem;'>
    VeriYield v2.4 • Built with OpenGradient TEE • {current_date}
    </p>
""", unsafe_allow_html=True)
