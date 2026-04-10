import streamlit as st
import opengradient as og
import asyncio
import requests

# --- 1. Page Configuration ---
st.set_page_config(page_title="VeriYield | Trustless DeFi Intelligence", page_icon="💠", layout="wide")

# --- 2. THE ULTIMATE CYBER-BLUE UI ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@500;700&display=swap');
    html, body, [data-testid="stAppViewContainer"] { background-color: #000411 !important; color: #e0f2fe; font-family: 'Rajdhani', sans-serif; }
    h1, h2, h3 { font-family: 'Orbitron', sans-serif; color: #00e6ff !important; text-shadow: 0 0 10px rgba(0, 230, 255, 0.7); }
    div[data-testid="stMetric"] { background: rgba(10, 25, 49, 0.8); padding: 20px; border-radius: 15px; border: 1px solid #0056e0; box-shadow: 0 0 15px rgba(0, 86, 224, 0.3); }
    [data-testid="stMetricValue"] { color: #ffffff !important; font-size: 24px !important; }
    div.stButton > button:first-child { width: 100%; background: linear-gradient(135deg, #0056e0 0%, #00e6ff 100%); color: white; font-family: 'Orbitron', sans-serif; height: 55px; border-radius: 12px; border: none; font-weight: bold; }
    .stTabs [data-baseweb="tab"][aria-selected="true"] { background-color: #00e6ff !important; color: #000411 !important; font-family: 'Orbitron', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. Live Data Engine ---
def get_market_data(coin_id):
    try:
        url = f"https://api.coingecko.com/api/v3/coins/{coin_id}?localization=false&tickers=false&market_data=true&community_data=false&developer_data=false&sparkline=false"
        data = requests.get(url, timeout=10).json()
        m_data = data['market_data']
        return {
            "price": m_data['current_price']['usd'],
            "mcap": m_data['market_cap']['usd'],
            "supply": m_data['circulating_supply']
        }
    except:
        return {"price": 0.0, "mcap": 0.0, "supply": 0.0}

# --- 4. Header ---
st.markdown("<h1 style='text-align: center;'>💠 VeriYield Atlantis</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #00e6ff;'>Live Market Intelligence | Verified by TEE Enclave</p>", unsafe_allow_html=True)

tab_opt, tab_sec, tab_mkt = st.tabs(["🚀 STRATEGY ENGINE", "🔐 SECURITY PROTOCOL", "📊 LIVE MARKET DATA"])

with tab_opt:
    st.markdown("### 💰 Strategy Parameters")
    c1, c2 = st.columns([2, 1])
    with c1:
        asset = st.selectbox("SELECT ASSET", ["ETH", "SOL", "BTC", "USDC"], key="asset_select")
        risk = st.select_slider("RISK LEVEL", options=["LOW", "BALANCED", "HIGH"])
    
    with c2:
        # Quick price view for selected asset
        coin_map = {"ETH": "ethereum", "SOL": "solana", "BTC": "bitcoin", "USDC": "usd-coin"}
        quick_data = get_market_data(coin_map[asset])
        st.metric(f"LIVE {asset} PRICE", f"${quick_data['price']:,}")

    if st.button("RUN TEE INFERENCE"):
        with st.spinner("Executing Secure Enclave Strategy..."):
            try:
                sk = st.secrets["OG_PRIVATE_KEY"]
                llm = og.LLM(private_key=sk)
                prompt = f"Professional {risk}-risk yield strategy for {asset} at price ${quick_data['price']}. Focus on APY and Safety."
                result = asyncio.run(llm.chat(model=og.TEE_LLM.CLAUDE_SONNET_4_6, messages=[{"role": "user", "content": prompt}]))
                st.success("🎯 Recommendation Generated")
                st.markdown(result.chat_output.get('content') if hasattr(result, 'chat_output') else str(result))
                if hasattr(result, 'transaction_hash') or hasattr(result, 'proof_tx_hash'):
                    st.code(getattr(result, 'transaction_hash', getattr(result, 'proof_tx_hash', '')), language="plaintext")
            except Exception as e:
                st.error(f"Error: {e}")

with tab_mkt:
    st.markdown("### 📊 Real-Time Crypto Metrics")
    assets_to_show = [("ethereum", "ETH"), ("solana", "SOL"), ("bitcoin", "BTC")]
    
    for cid, symbol in assets_to_show:
        data = get_market_data(cid)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(f"{symbol} Price", f"${data['price']:,}")
        with col2:
            st.metric(f"{symbol} Market Cap", f"${data['mcap']/1e9:,.2f}B")
        with col3:
            st.metric(f"{symbol} Supply", f"{data['supply']/1e6:,.1f}M")
        st.divider()

with tab_sec:
    st.markdown("### 🔐 Security Framework")
    st.info("VeriYield utilizes OpenGradient TEEs to ensure untamperable AI computation.")
    st.image("https://img.icons8.com/nolan/128/security-shield.png")

st.markdown("<p style='text-align: center; color: #88cbff;'>VeriYield v1.4 • Live Data Edition</p>", unsafe_allow_html=True)
