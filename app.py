import streamlit as st
import opengradient as og
import asyncio

# --- 1. Page Configuration ---
st.set_page_config(
    page_title="VeriYield | Trustless DeFi Intelligence",
    page_icon="💠",
    layout="wide"
)

# --- 2. THE ULTIMATE CYBER-BLUE UI (Custom CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@500;700&display=swap');
    
    /* Global Styles: Deep Blue Background */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #000411 !important;
        background-image: radial-gradient(#0a1931 1px, transparent 1px);
        background-size: 30px 30px;
        color: #e0f2fe;
        font-family: 'Rajdhani', sans-serif;
    }

    h1, h2, h3 { 
        font-family: 'Orbitron', sans-serif;
        color: #00e6ff !important;
        text-shadow: 0 0 10px rgba(0, 230, 255, 0.7);
    }
    
    /* Metrics / Data Cards styling */
    div[data-testid="stMetric"] { 
        background: rgba(10, 25, 49, 0.6);
        padding: 25px; 
        border-radius: 20px; 
        border: 2px solid #0056e0;
        box-shadow: 0 0 20px rgba(0, 86, 224, 0.5);
        transition: 0.3s;
    }
    div[data-testid="stMetric"]:hover {
        border-color: #00e6ff;
        box-shadow: 0 0 30px rgba(0, 230, 255, 0.6);
    }
    [data-testid="stMetricValue"] { color: #ffffff !important; font-size: 36px !important; font-weight: 700; }
    [data-testid="stMetricDelta"] { color: #00e6ff !important; }

    /* Neon Blue Tabs */
    .stTabs [data-baseweb="tab-list"] { gap: 15px; }
    .stTabs [data-baseweb="tab"] { 
        font-family: 'Orbitron', sans-serif;
        background-color: #0a1931;
        color: #00e6ff;
        border-radius: 15px 15px 0 0;
        padding: 15px 30px;
        border: 1px solid #0056e0;
    }
    .stTabs [data-baseweb="tab"]:hover { background-color: #112a52; }
    .stTabs [data-baseweb="tab"][aria-selected="true"] { 
        background-color: #00e6ff !important;
        color: #000411 !important;
        box-shadow: 0 0 20px rgba(0, 230, 255, 0.8);
    }

    /* Cyberpunk Action Button */
    div.stButton > button:first-child {
        width: 100%;
        background: linear-gradient(135deg, #0056e0 0%, #00e6ff 100%);
        color: #ffffff;
        font-family: 'Orbitron', sans-serif;
        font-weight: 700;
        font-size: 18px;
        height: 65px;
        border-radius: 15px;
        border: 2px solid #ffffff;
        text-transform: uppercase;
        letter-spacing: 2px;
        box-shadow: 0 0 15px rgba(0, 230, 255, 0.6);
    }
    div.stButton > button:first-child:hover {
        background: linear-gradient(135deg, #00e6ff 0%, #ffffff 100%);
        color: #000411;
        box-shadow: 0 0 30px rgba(255, 255, 255, 0.8);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. Header Section (With Cyber Logo) ---
st.markdown("<h1 style='text-align: center;'>💠 VeriYield Atlantis</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #88cbff; font-size: 1.2rem;'>Trusted AI-Driven DeFi Intelligence | Secured by TEE Enclave</p>", unsafe_allow_html=True)
st.divider()

# --- 4. Main Application Layout ---
tab_opt, tab_sec, tab_mkt = st.tabs(["🚀 STRATEGY ENGINE", "🔐 SECURITY PROTOCOL", "📊 MARKET OVERVIEW"])

with tab_opt:
    st.markdown("## 💰 DEFINE YOUR PARAMETERS")
    
    col_input, col_info = st.columns([2, 1])
    with col_input:
        asset = st.selectbox("SELECT TARGET ASSET", ["ETH", "SOL", "WBTC", "USDC"], key="asset_select")
        risk = st.select_slider("SET RISK TOLERANCE", options=["LOW", "BALANCED", "HIGH"], key="risk_slider")
    
    with col_info:
        st.metric("CURRENT ENCLAVE STATUS", "ACTIVE", delta="TEE SECURED", delta_color="normal")
        st.caption(f"Strategy will be generated for {asset} with {risk} risk profile.")

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("INITIALIZE SECURE INFERENCE"):
        with st.spinner("Establishng TEE Connection... Performing On-Chain Verification..."):
            try:
                # Security Check for Private Key in Secrets
                if "OG_PRIVATE_KEY" in st.secrets:
                    sk = st.secrets["OG_PRIVATE_KEY"]
                else:
                    st.error("SYSTEM ERROR: Private Key configuration missing.")
                    st.stop()
                
                llm = og.LLM(private_key=sk)
                
                # Professional Prompt (without live price dependency)
                user_msg = f"Act as a DeFi quant analyst. Provide a professional {risk}-risk yield strategy report for {asset}. Focus on protocol reputation and historical APY stability. Output in clean Markdown."
                
                result = asyncio.run(
                    llm.chat(
                        model=og.TEE_LLM.CLAUDE_SONNET_4_6,
                        messages=[
                            {"role": "system", "content": "You are VeriYield AI, a secure DeFi advisor."},
                            {"role": "user", "content": user_msg}
                        ],
                        max_tokens=500
                    )
                )
                
                content = result.chat_output.get('content') if hasattr(result, 'chat_output') else str(result)
                
                st.success(f"#### 🎯 {risk}-RISK RECOMMENDATION FOR {asset}")
                st.markdown(content)
                
                # Verification Hash
                tx_hash = getattr(result, 'transaction_hash', None) or getattr(result, 'proof_tx_hash', None)
                if tx_hash:
                    with st.expander("🛡️ VIEW CRYPTOGRAPHIC PROOF (HASH)"):
                        st.code(tx_hash, language="plaintext")
                        st.caption("This hash proves the inference was executed in an untampered TEE.")

            except Exception as e:
                st.error(f"Inference Error: {str(e)}")

with tab_sec:
    st.markdown("## 🔒 TRUSTLESS FRAMEWORK")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
        VeriYield is not a standard AI app. We use **OpenGradient's Trusted Execution Environments (TEE)**.
        - **Tamper-Proof Logic:** No human can change the AI's internal reasoning.
        - **On-Chain Verification:** Each result has a cryptographic 'receipt' you can check.
        - **Isolated Compute:** Your query details are processed in a secure hardware vault.
        """)
    with col2:
        st.image("https://img.icons8.com/nolan/256/1A6DFF/C82471/security-lock.png")

with tab_mkt:
    st.markdown("## 📊 MARKET REFERENCE DATA")
    st.warning("Note: Market data is currently static for this version.")
    c1, c2, c3 = st.columns(3)
    c1.metric("ETH REFERENCE PRICE", "$3,500")
    c2.metric("SOL REFERENCE PRICE", "$150")
    c3.metric("BTC REFERENCE PRICE", "$68,000")

st.divider()
st.markdown("<p style='text-align: center; color: #00aaff;'>VeriYield Atlantis v1.3 • Web3 Native Intelligence • Built on OpenGradient</p>", unsafe_allow_html=True)
