import streamlit as st
import opengradient as og
import asyncio
from datetime import datetime

# --- 1. Page Configuration ---
st.set_page_config(
    page_title="VeriYield | 2026 DeFi Intelligence",
    page_icon="🛡️",
    layout="centered"
)

# --- 2. Advanced CSS (Deep Blue & Neon Green Theme) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Orbitron:wght@500&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', sans-serif;
        background-color: #001529; /* Deep Blue */
        color: #e4e6eb;
    }

    h1 { font-family: 'Orbitron', sans-serif; color: #00ff88 !important; text-align: center; }
    
    /* Metric Cards */
    div[data-testid="stMetric"] { 
        background-color: #002142;
        padding: 20px; 
        border-radius: 16px; 
        border: 1px solid rgba(0, 255, 136, 0.2);
    }

    /* Tabs Styling */
    .stTabs [data-baseweb="tab"] { 
        font-weight: 600; 
        color: #b0b3b8; 
        background-color: #002b5c;
        padding: 10px 20px;
        border-radius: 12px;
        margin-right: 8px;
    }

    .stTabs [data-baseweb="tab"][aria-selected="true"] { 
        color: #000000 !important;
        background-color: #00ff88 !important;
    }

    /* Primary Button */
    div.stButton > button:first-child {
        width: 100%;
        background: linear-gradient(90deg, #00ff88 0%, #00e6ff 100%);
        color: #000000;
        font-weight: 700;
        height: 55px;
        border-radius: 12px;
        border: none;
        box-shadow: 0 4px 15px rgba(0, 255, 136, 0.3);
    }

    /* Info Boxes */
    .edu-box {
        background-color: rgba(0, 43, 92, 0.5);
        border-radius: 12px;
        padding: 20px;
        border-left: 5px solid #00ff88;
        margin-bottom: 15px;
    }
    
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- 3. Header & Dynamic Date ---
st.markdown("<h1>🛡️ VeriYield</h1>", unsafe_allow_html=True)
# Dynamic date reflects the actual current date in 2026
current_date = datetime.now().strftime("%B %d, %Y")
st.markdown(f"<p style='text-align: center; color: #b0b3b8; letter-spacing: 2px;'>LIVE DEFI INTELLIGENCE • {current_date}</p>", unsafe_allow_html=True)
st.divider()

# --- 4. Main Tabs Navigation ---
tab_optimizer, tab_security, tab_edu = st.tabs(["🚀 Optimizer", "🔐 Security Proof", "📚 DeFi Education"])

with tab_optimizer:
    st.markdown("### 💰 Strategy Engine")
    
    # Empty input by default
    asset = st.text_input("Asset Symbol", value="", placeholder="Enter asset (e.g. BTC, SOL, ETH)")

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("GENERATE VERIFIABLE STRATEGY"):
        if not asset.strip():
            st.warning("Please provide an asset symbol to begin analysis.")
        else:
            with st.spinner(f"Analyzing {asset} Market Cycles for {current_date}..."):
                try:
                    if "OG_PRIVATE_KEY" in st.secrets:
                        PRIVATE_KEY = st.secrets["OG_PRIVATE_KEY"]
                    else:
                        st.error("System Error: OG_PRIVATE_KEY not found in Secrets.")
                        st.stop()
                    
                    llm = og.LLM(private_key=PRIVATE_KEY)
                    
                    # 2026 Context-Aware Query
                    query = f"""
                    Current Date: {current_date}. 
                    Task: Generate an institutional-grade yield strategy for {asset}.
                    
                    Specifics for 2026:
                    1. Focus on modern primitives: Liquid Restaking Tokens (LRTs), AI-optimized vaults, and Cross-chain yield aggregators.
                    2. Provide a 'Market Sentiment' summary for Q2 2026.
                    3. Output a 'Strategy Matrix' table: | Risk Level | Protocol | Mechanism | Est. APY |
                    4. Professional, clear, and direct tone. No filler text.
                    """
                    
                    result = asyncio.run(
                        llm.chat(
                            model=og.TEE_LLM.CLAUDE_SONNET_4_6,
                            messages=[
                                {"role": "system", "content": "You are VeriYield AI, an elite DeFi analyst operating in 2026. You provide verifiable, hardware-signed financial intelligence."},
                                {"role": "user", "content": query}
                            ],
                            max_tokens=600
                        )
                    )
                    
                    st.success(f"#### 🎯 Real-Time Strategy: {asset}")
                    content = result.chat_output.get('content') if hasattr(result, 'chat_output') else str(result)
                    st.markdown(content)
                    
                    # Cryptographic TEE Proof
                    tx_hash = getattr(result, 'proof_tx_hash', None)
                    if tx_hash:
                        with st.expander("🛡️ View Hardware Attestation"):
                            st.info("This response was computed in a Trusted Execution Environment (TEE).")
                            st.code(tx_hash, language="plaintext")
                            st.caption(f"Verified Proof Hash • Compiled on {current_date}")
                            
                except Exception as e:
                    st.error(f"Inference Error: {str(e)}")

with tab_security:
    st.markdown("### 🔒 2026 Security Standards")
    st.write("""
    VeriYield utilizes **OpenGradient TEE (Trusted Execution Environments)** to provide 
    non-custodial financial intelligence.
    """)
    st.info("**Integrity:** AI logic is executed in a hardware-locked enclave.")
    st.info("**Transparency:** Every strategy is cryptographically signed on the OpenGradient network.")
    st.image("https://img.icons8.com/nolan/128/security-shield.png", width=100)

with tab_edu:
    st.markdown("### 📚 2026 DeFi Intelligence")
    st.write("Stay ahead of the curve with current market primitives.")
    
    st.markdown(f"""
    <div class="edu-box">
        <h4 style='color:#00ff88; margin-top:0;'>The Restaking Standard</h4>
        <p>In 2026, <b>Liquid Restaking (LRT)</b> has become the base-layer for yield. Users no longer just stake; they secure multiple actively validated services (AVS) simultaneously to maximize capital efficiency.</p>
    </div>
    
    <div class="edu-box">
        <h4 style='color:#00ff88; margin-top:0;'>AI-Managed Liquidity</h4>
        <p>Dynamic ranges in DEXs are now managed by TEE-signed AI agents. VeriYield helps you identify which agents are performing optimally without human bias.</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()
st.markdown(f"<p style='text-align: center; color: #5c6370; font-size: 0.8rem;'>VeriYield v2.1 • Certified 2026 Intelligence • {current_date}</p>", unsafe_allow_html=True)
