import streamlit as st
import opengradient as og
import asyncio

# --- 1. Page Configuration ---
st.set_page_config(
    page_title="VeriYield | Verifiable DeFi Intelligence",
    page_icon="🛡️",
    layout="centered"
)

# --- 2. Professional UI Styling (Royal Blue Theme) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Orbitron:wght@500&display=swap');
    
    /* Deep Royal Blue Background */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', sans-serif;
        background-color: #001529; 
        color: #e4e6eb;
    }

    h1 { font-family: 'Orbitron', sans-serif; color: #00ff88 !important; text-align: center; }
    
    /* Metrics & Cards */
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

    /* Generator Button */
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

    /* Education Box Styling */
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

# --- 3. Header Section ---
st.markdown("<h1>🛡️ VeriYield</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #b0b3b8; letter-spacing: 2px;'>VERIFIABLE AI YIELD OPTIMIZATION</p>", unsafe_allow_html=True)
st.divider()

# --- 4. Main Tabs Navigation ---
tab_optimizer, tab_security, tab_edu = st.tabs(["🚀 Optimizer", "🔐 Security Proof", "📚 DeFi Education"])

with tab_optimizer:
    st.markdown("### 💰 Strategy Engine")
    
    # Input is empty by default, no ETH pre-filled
    asset = st.text_input("Asset Symbol", value="", placeholder="Enter asset (e.g. BTC, SOL, USDC)")

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("GENERATE SECURE STRATEGY"):
        if not asset.strip():
            st.warning("Please enter an asset symbol to proceed.")
        else:
            with st.spinner("Executing Secure Inference in TEE Enclave..."):
                try:
                    if "OG_PRIVATE_KEY" in st.secrets:
                        PRIVATE_KEY = st.secrets["OG_PRIVATE_KEY"]
                    else:
                        st.error("Missing OG_PRIVATE_KEY in Secrets.")
                        st.stop()
                    
                    llm = og.LLM(private_key=PRIVATE_KEY)
                    
                    result = asyncio.run(
                        llm.chat(
                            model=og.TEE_LLM.CLAUDE_SONNET_4_6,
                            messages=[
                                {"role": "system", "content": "You are VeriYield AI. Provide a professional yield strategy in a markdown table format."},
                                {"role": "user", "content": f"Create a structured yield strategy for {asset}."}
                            ],
                            max_tokens=400
                        )
                    )
                    
                    text = result.chat_output.get('content') if hasattr(result, 'chat_output') else str(result)
                    
                    st.success("#### 🎯 AI Strategy Analysis")
                    st.markdown(text)
                    
                    # Cryptographic Proof Expansion
                    tx_hash = getattr(result, 'proof_tx_hash', None)
                    if tx_hash:
                        with st.expander("🛡️ View TEE Proof"):
                            st.code(tx_hash, language="plaintext")
                            
                except Exception as e:
                    st.error(f"Inference Error: {str(e)}")

with tab_security:
    st.markdown("### 🔒 Infrastructure Security")
    st.write("""
    VeriYield uses **Trusted Execution Environments (TEE)** to ensure your strategy is 
    calculated in a private hardware vault.
    """)
    st.info("**Integrity:** The AI logic cannot be modified by anyone.")
    st.info("**Privacy:** Your inputs are shielded from the cloud provider.")
    st.image("https://img.icons8.com/nolan/128/security-shield.png", width=100)

with tab_edu:
    st.markdown("### 📚 DeFi Intelligence Center")
    st.write("Essential knowledge for every decentralized investor.")
    
    st.markdown("""
    <div class="edu-box">
        <h4 style='color:#00ff88; margin-top:0;'>1. Liquidity Provision</h4>
        <p>Earning fees by providing tokens to decentralized exchanges. Be aware of <b>Impermanent Loss</b> during high volatility.</p>
    </div>
    
    <div class="edu-box">
        <h4 style='color:#00ff88; margin-top:0;'>2. Staking & Restaking</h4>
        <p>Securing networks by locking assets to earn rewards. Restaking allows you to earn multiple layers of yield on the same capital.</p>
    </div>

    <div class="edu-box">
        <h4 style='color:#00ff88; margin-top:0;'>3. TEE Verification</h4>
        <p>In a world of deepfakes, TEE (Trusted Execution Environment) provides a digital fingerprint proving that this advice came directly from the AI model, untampered.</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()
st.markdown("<p style='text-align: center; color: #5c6370; font-size: 0.8rem;'>VeriYield Alpha v1.1 • Built on OpenGradient Network</p>", unsafe_allow_html=True)
