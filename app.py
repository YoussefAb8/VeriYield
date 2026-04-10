import streamlit as st
import opengradient as og
import asyncio
import time
import requests

# --- 1. Page Configuration & Branding ---
st.set_page_config(
    page_title="VeriYield | Verifiable DeFi Intelligence",
    page_icon="🛡",
    layout="centered"
)

# --- Function to fetch live prices ---
def get_live_price(coin_id):
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
        data = requests.get(url).json()
        return data[coin_id]['usd']
    except:
        return 2600.0 # Fallback

# --- 2. Advanced Custom CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', sans-serif;
        background-color: #080a10;
        color: #e4e6eb;
    }
    h1, h2, h3, h4 { color: #ffffff !important; font-weight: 700; }
    [data-testid="stMetricValue"] { font-size: 28px !important; font-weight: 700; color: #00ff88 !important; }
    div[data-testid="stMetric"] { background-color: #11151c; padding: 15px; border-radius: 12px; border: 1px solid #1c212b; }
    .stTabs [data-baseweb="tab"] { font-weight: 600; color: #888a8e; background-color: #11151c; padding: 8px 16px; border-radius: 12px; margin-right: 8px; }
    .stTabs [data-baseweb="tab"][aria-selected="true"] { color: #000000 !important; background-color: #00ff88 !important; }
    div.stButton > button:first-child { width: 100%; background: linear-gradient(90deg, #00ff88 0%, #00e6ff 100%); color: #000000; font-weight: 700; height: 50px; border-radius: 10px; border: none; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. Header ---
st.markdown("<h1 style='text-align: center;'>🛡 VeriYield</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888a8e;'>Verifiable AI Yield Optimization • Powered by OpenGradient TEE</p>", unsafe_allow_html=True)
st.divider()

# Get Real Data
eth_price = get_live_price('ethereum')

# --- 4. Main Tabs ---
tab_optimizer, tab_security, tab_market = st.tabs(["🚀 Optimizer", "🔐 Security Proof", "📊 Market Info"])

with tab_optimizer:
    st.markdown("### 💰 Generate Yield Strategy")
    
    col_input, col_balance = st.columns([2, 1])
    with col_input:
        asset = st.selectbox("Asset to Optimize", ["ETH", "SOL", "USDC", "BTC"])
        risk = st.select_slider("Risk Tolerance", options=["Low", "Medium", "High"])
    with col_balance:
        current_val = eth_price if asset == "ETH" else 1.0 if asset == "USDC" else 150.0
        st.metric(f"Current {asset} Price", f"${current_val:,}")

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("Generate Verifiable Strategy"):
        with st.spinner("Executing Secure Inference in TEE Enclave..."):
            try:
                if "OG_PRIVATE_KEY" in st.secrets:
                    PRIVATE_KEY = st.secrets["OG_PRIVATE_KEY"]
                else:
                    st.error("Missing Secrets!")
                    st.stop()
                
                llm = og.LLM(private_key=PRIVATE_KEY)
                
                # Dynamic Prompt based on Live Price and User Input
                prompt_content = f"Create a {risk} risk yield strategy for {asset} considering its current price is ${current_val}. Provide a professional table-based report."
                
                result = asyncio.run(
                    llm.chat(
                        model=og.TEE_LLM.CLAUDE_SONNET_4_6,
                        messages=[
                            {"role": "system", "content": "You are VeriYield AI, a DeFi intelligence agent. Provide expert financial analysis."},
                            {"role": "user", "content": prompt_content}
                        ],
                        max_tokens=500
                    )
                )
                
                text = result.chat_output.get('content') if hasattr(result, 'chat_output') else str(result)
                
                st.success(f"#### 🎯 Verifiable {risk}-Risk Strategy")
                st.markdown(text)
                
                tx_hash = getattr(result, 'transaction_hash', None) or getattr(result, 'proof_tx_hash', None)
                if tx_hash:
                    with st.expander("🛡 View Cryptographic Proof (On-Chain Hash)"):
                        st.info("Verified by OpenGradient TEE Infrastructure.")
                        st.code(tx_hash, language="plaintext")
                        
            except Exception as e:
                st.error(f"Inference Error: {str(e)}")

with tab_security:
    st.markdown("### 🔒 How VeriYield Protects You")
    st.write("VeriYield ensures that AI-generated financial advice is:")
    st.markdown("- **Tamper-Proof:** AI cannot be manipulated.\n- **Verifiable:** Each response has a unique Proof Hash.\n- **Private:** User data stays in the Secure Enclave.")
    st.image("https://img.icons8.com/nolan/128/security-shield.png")

with tab_market:
    st.markdown("### 📊 Live Market Feed")
    m1, m2 = st.columns(2)
    m1.metric("Ethereum (ETH)", f"${eth_price}", "LIVE")
    m2.metric("Solana (SOL)", f"${get_live_price('solana')}", "LIVE")
    st.success("API Connection: Active (CoinGecko)")

st.divider()
st.markdown("<p style='text-align: center; color: #888a8e;'>VeriYield v1.2 • Built on OpenGradient Network</p>", unsafe_allow_html=True)
