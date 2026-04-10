import streamlit as st
import opengradient as og
import asyncio
import time

# --- 1. Page Configuration & Branding ---
st.set_page_config(
    page_title="VeriYield | Verifiable DeFi Intelligence",
    page_icon="🛡️",
    layout="centered"
)

# --- 2. Advanced Custom CSS (Professional UI) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', sans-serif;
        background-color: #080a10;
        color: #e4e6eb;
    }

    h1, h2, h3, h4 { color: #ffffff !important; font-weight: 700; }
    
    [data-testid="stMetricValue"] { 
        font-size: 32px !important; 
        font-weight: 700; 
        color: #00ff88 !important; 
    }
    
    div[data-testid="stMetric"] { 
        background-color: #11151c;
        padding: 20px; 
        border-radius: 16px; 
        border: 1px solid #1c212b;
    }

    .stTabs [data-baseweb="tab"] { 
        font-weight: 600; 
        color: #888a8e; 
        background-color: #11151c;
        padding: 10px 20px;
        border-radius: 20px;
        margin-right: 10px;
    }

    .stTabs [data-baseweb="tab"][aria-selected="true"] { 
        color: #000000 !important;
        background-color: #00ff88 !important;
    }

    div.stButton > button:first-child {
        width: 100%;
        background: linear-gradient(90deg, #00ff88 0%, #00e6ff 100%);
        color: #000000;
        font-weight: 700;
        height: 55px;
        border-radius: 12px;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. Header ---
st.markdown("<h1 style='text-align: center;'>🛡️ VeriYield</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888a8e;'>Verifiable AI Yield Optimization • Powered by OpenGradient TEE</p>", unsafe_allow_html=True)
st.divider()

# --- 4. Main Tabs ---
tab_optimizer, tab_security, tab_market = st.tabs(["🚀 Optimizer", "🔐 Security Proof", "📊 Market Info"])

with tab_optimizer:
    st.markdown("### 💰 Generate Yield Strategy")
    
    col_input, col_balance = st.columns([2, 1])
    with col_input:
        asset = st.text_input("Asset to Optimize", value="ETH", placeholder="e.g. BTC, USDC")
    with col_balance:
        st.metric("Estimated Balance", f"1,250.00 {asset}")

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("Generate Verifiable Strategy"):
        if not asset.strip():
            st.error("Please enter a valid asset symbol.")
        else:
            with st.spinner("Executing Secure Inference in TEE Enclave..."):
                try:
                    # --- SECURE KEY RETRIEVAL ---
                    if "OG_PRIVATE_KEY" in st.secrets:
                        PRIVATE_KEY = st.secrets["OG_PRIVATE_KEY"]
                    else:
                        st.error("System Error: Private Key not found in Secrets. Please configure OG_PRIVATE_KEY in Advanced Settings.")
                        st.stop()
                    
                    llm = og.LLM(private_key=PRIVATE_KEY)
                    llm.ensure_opg_approval(min_allowance=0.1)
                    
                    result = asyncio.run(
                        llm.chat(
                            model=og.TEE_LLM.CLAUDE_SONNET_4_6,
                            messages=[
                                {"role": "system", "content": "You are VeriYield AI, a DeFi intelligence agent. Provide a professional, table-based strategy report in English."},
                                {"role": "user", "content": f"Create a yield strategy for {asset} with a focus on risk management."}
                            ],
                            max_tokens=400
                        )
                    )
                    
                    text = result.chat_output.get('content') if hasattr(result, 'chat_output') else str(result)
                    
                    st.success("#### 🎯 AI-Driven Recommendation")
                    st.markdown(text)
                    
                    tx_hash = getattr(result, 'transaction_hash', None) or getattr(result, 'proof_tx_hash', None)
                    if tx_hash:
                        with st.expander("🛡️ View Cryptographic Proof (On-Chain Hash)"):
                            st.info("This response is signed by a Trusted Execution Environment (TEE). Verification ensures the AI model has not been tampered with.")
                            st.code(tx_hash, language="plaintext")
                            
                except Exception as e:
                    st.error(f"Inference Error: {str(e)}")

with tab_security:
    st.markdown("### 🔒 How VeriYield Protects You")
    st.write("""
    VeriYield leverages **Trusted Execution Environments (TEE)** to ensure that your financial advice is:
    
    1. **Tamper-Proof:** No one (including developers) can alter the AI output.
    2. **Verifiable:** Each response is cryptographically signed and recorded on the OpenGradient network.
    3. **Private:** Secure computation ensures your query parameters remain isolated.
    """)
    st.image("https://img.icons8.com/nolan/128/security-shield.png")

with tab_market:
    st.markdown("### 📊 Market Status")
    st.info("Live market data feeds and protocol TVL metrics coming in v1.1.")

st.divider()
st.markdown("<p style='text-align: center; color: #888a8e;'>VeriYield Alpha v1.0 • Built on OpenGradient Network</p>", unsafe_allow_html=True)
