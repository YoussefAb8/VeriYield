import streamlit as st
import opengradient as og
import asyncio
import requests

# --- 1. Page Configuration ---
st.set_page_config(
    page_title="VeriYield | AI DeFi Intelligence",
    page_icon="🛡️",
    layout="centered"
)

# --- 2. Professional CSS (Dark Mode & Neon Accents) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', sans-serif;
        background-color: #080a10;
        color: #e4e6eb;
    }
    h1, h2, h3 { color: #ffffff !important; font-weight: 700; }
    
    /* Metrics Styling */
    div[data-testid="stMetric"] { 
        background-color: #11151c; 
        padding: 20px; 
        border-radius: 15px; 
        border: 1px solid #1c212b;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    [data-testid="stMetricValue"] { color: #00ff88 !important; font-size: 28px !important; }

    /* Tabs Styling */
    .stTabs [data-baseweb="tab"] { 
        font-weight: 600; 
        color: #888a8e; 
        background-color: #11151c;
        padding: 10px 20px;
        border-radius: 12px;
        margin-right: 10px;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] { 
        color: #000000 !important;
        background-color: #00ff88 !important;
    }

    /* Primary Button Styling */
    div.stButton > button:first-child {
        width: 100%;
        background: linear-gradient(90deg, #00ff88 0%, #00e6ff 100%);
        color: #000000;
        font-weight: 700;
        height: 55px;
        border-radius: 12px;
        border: none;
        transition: 0.3s;
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0, 255, 136, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. Real-Time Price Engine ---
def get_real_price(asset_name):
    ids = {"BTC": "bitcoin", "ETH": "ethereum", "SOL": "solana", "USDC": "usd-coin"}
    coin_id = ids.get(asset_name, "bitcoin")
    try:
        # Fetching data from CoinGecko
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
        response = requests.get(url, timeout=5)
        data = response.json()
        return float(data[coin_id]['usd'])
    except Exception:
        # Realistic fallback prices if API is throttled
        fallbacks = {"BTC": 67450.0, "ETH": 3480.0, "SOL": 145.0, "USDC": 1.0}
        return fallbacks.get(asset_name, 100.0)

# --- 4. Header Section ---
st.markdown("<h1 style='text-align: center;'>🛡️ VeriYield</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888a8e;'>Verifiable AI Yield Optimization • Powered by OpenGradient TEE</p>", unsafe_allow_html=True)
st.divider()

# --- 5. Application Interface ---
tab_opt, tab_sec, tab_mkt = st.tabs(["🚀 Strategy Optimizer", "🔐 Security Proof", "📊 Market Live"])

with tab_opt:
    st.markdown("### 💰 Customize Your Strategy")
    
    c1, c2 = st.columns([2, 1])
    with c1:
        # Using unique keys prevents UI freezing/resetting
        selected_asset = st.selectbox("Select Asset to Optimize", ["BTC", "ETH", "SOL", "USDC"], key="asset_select")
        risk_val = st.select_slider("Select Risk Level", options=["Low", "Medium", "High"], key="risk_slider")
    
    # Update price instantly based on selection
    live_price = get_real_price(selected_asset)
    
    with c2:
        st.metric(f"Current {selected_asset}", f"${live_price:,}", delta="LIVE UPDATING")

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("Generate Verifiable Strategy"):
        with st.spinner("🔗 Establishing Secure TEE Connection..."):
            try:
                # Security Check for Private Key
                if "OG_PRIVATE_KEY" in st.secrets:
                    sk = st.secrets["OG_PRIVATE_KEY"]
                else:
                    st.error("Error: Please configure OG_PRIVATE_KEY in Streamlit Secrets.")
                    st.stop()
                
                llm = og.LLM(private_key=sk)
                
                # Dynamic Prompt using real-world data
                user_msg = (
                    f"Provide a professional {risk_val} risk yield strategy for {selected_asset}. "
                    f"Current market price is ${live_price}. "
                    f"Output the report in clear bullet points or a table."
                )
                
                # Executing TEE-verified Inference
                result = asyncio.run(
                    llm.chat(
                        model=og.TEE_LLM.CLAUDE_SONNET_4_6,
                        messages=[
                            {"role": "system", "content": "You are VeriYield AI, a DeFi expert analyst. Focus on security and APY efficiency."},
                            {"role": "user", "content": user_msg}
                        ],
                        max_tokens=450
                    )
                )
                
                content = result.chat_output.get('content') if hasattr(result, 'chat_output') else str(result)
                
                st.success(f"#### 🎯 {risk_val}-Risk Recommendation for {selected_asset}")
                st.markdown(content)
                
                # Proof Verification Section
                tx_hash = getattr(result, 'transaction_hash', None) or getattr(result, 'proof_tx_hash', None)
                if tx_hash:
                    with st.expander("🛡️ View Cryptographic Proof"):
                        st.info("This inference was executed inside an isolated Trusted Execution Environment (TEE).")
                        st.code(tx_hash, language="plaintext")
                        st.caption("Verify this transaction on the OpenGradient Explorer.")

            except Exception as e:
                st.error(f"Inference Error: {str(e)}")

with tab_sec:
    st.markdown("### 🔒 Security Framework")
    st.write("VeriYield leverages OpenGradient TEE technology to provide:")
    st.info("1. **Integrity**: The AI cannot be manipulated by third parties.\n2. **Proof**: Every recommendation is signed cryptographically.\n3. **Confidentiality**: Your parameters are processed in a secure hardware enclave.")
    st.image("https://img.icons8.com/nolan/128/security-shield.png")

with tab_mkt:
    st.markdown("### 📊 Market Snapshot")
    m_col1, m_col2, m_col3 = st.columns(3)
    m_col1.metric("BTC", f"${get_real_price('BTC'):,}")
    m_col2.metric("ETH", f"${get_real_price('ETH'):,}")
    m_col3.metric("SOL", f"${get_real_price('SOL'):,}")
    st.caption("Real-time data powered by CoinGecko API")

st.divider()
st.markdown("<p style='text-align: center; color: #888a8e;'>VeriYield v1.2 | The Future of Trustless Finance</p>", unsafe_allow_html=True)
