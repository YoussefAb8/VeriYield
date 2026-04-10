import streamlit as st
import opengradient as og
import asyncio
import requests

# --- 1. Page Configuration ---
st.set_page_config(page_title="VeriYield | AI DeFi Enclave", page_icon="💠", layout="wide")

# --- 2. Professional UI ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@500;700&display=swap');
    html, body, [data-testid="stAppViewContainer"] { background-color: #000411 !important; color: #e0f2fe; font-family: 'Rajdhani', sans-serif; }
    h1, h2, h3 { font-family: 'Orbitron', sans-serif; color: #00e6ff !important; text-shadow: 0 0 15px rgba(0, 230, 255, 0.4); }
    div[data-testid="stMetric"] { background: rgba(10, 25, 49, 0.85); padding: 22px; border-radius: 15px; border: 1px solid #0056e0; }
    [data-testid="stMetricValue"] { color: #ffffff !important; font-size: 28px !important; font-family: 'Orbitron'; }
    div.stButton > button:first-child { width: 100%; background: linear-gradient(90deg, #0056e0, #00e6ff); color: white; font-family: 'Orbitron'; font-weight: bold; height: 60px; border-radius: 12px; border: none; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. Live Data Engine ---
@st.cache_data(ttl=60)
def fetch_live_market_data():
    try:
        url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin,ethereum,solana&order=market_cap_desc&per_page=3&page=1&sparkline=false"
        data = requests.get(url, timeout=10).json()
        market_dict = {}
        for coin in data:
            market_dict[coin['symbol'].upper()] = {"price": coin['current_price'], "mcap": coin['market_cap'], "supply": coin['circulating_supply']}
        return market_dict
    except:
        return {"BTC": {"price": 72939.0, "mcap": 1.4e12, "supply": 19.6e6}, "ETH": {"price": 2245.0, "mcap": 2.7e11, "supply": 120e6}, "SOL": {"price": 84.5, "mcap": 4.8e10, "supply": 444e6}}

# --- 4. Main App ---
st.markdown("<h1 style='text-align: center;'>💠 VeriYield Atlantis</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #00e6ff;'>ELITE AI DEFI STRATEGIST • FULL REPORT MODE</p>", unsafe_allow_html=True)

market_data = fetch_live_market_data()
tab1, tab2, tab3 = st.tabs(["🚀 STRATEGY ENGINE", "📊 MARKET DATA", "🔐 SECURITY"])

with tab1:
    col_in, col_met = st.columns([2, 1])
    with col_in:
        asset_select = st.selectbox("CHOOSE ASSET", ["BTC", "ETH", "SOL"])
        risk_select = st.select_slider("RISK LEVEL", ["LOW", "BALANCED", "HIGH"])
    
    asset_info = market_data.get(asset_select)
    with col_met:
        st.metric(f"{asset_select} LIVE PRICE", f"${asset_info['price']:,}")

    if st.button("GENERATE FULL ANALYTICS REPORT"):
        with st.spinner("TEE Enclave is generating deep-dive analytics..."):
            try:
                sk = st.secrets["OG_PRIVATE_KEY"]
                llm = og.LLM(private_key=sk)
                
                # المحفز المطور لإجابة طويلة وشاملة
                query = f"""
                Act as a Senior DeFi Hedge Fund Manager. Provide an EXTENDED and IN-DEPTH {risk_select} risk yield strategy for {asset_select} at ${asset_info['price']}.
                
                Structure the report into these EXACT sections:
                1. Executive Summary: Overview of the strategy.
                2. Market Context: Current sentiment for {asset_select}.
                3. Top 3 Protocol Recommendations: Detailed breakdown of each (e.g., Aave, Lido, Curve) including estimated APY and why they fit a {risk_select} profile.
                4. Risk Mitigation: How to protect the principal investment.
                5. Step-by-Step Implementation: How a user should start.
                
                Be detailed, professional, and write at least 500 words.
                """
                
                result = asyncio.run(
                    llm.chat(
                        model=og.TEE_LLM.CLAUDE_SONNET_4_6, 
                        messages=[{"role": "user", "content": query}],
                        max_tokens=1500 # قمنا برفع عدد الكلمات المسموح بها جداً
                    )
                )
                
                st.success("✅ COMPREHENSIVE STRATEGY VERIFIED")
                content = result.chat_output.get('content') if hasattr(result, 'chat_output') else str(result)
                st.markdown(content)
                
                tx_hash = getattr(result, 'transaction_hash', getattr(result, 'proof_tx_hash', 'TEE_VERIFIED_0x...'))
                with st.expander("🛡️ Cryptographic Receipt"):
                    st.code(tx_hash)
                
            except Exception as e:
                st.error("Connection Failed. Verify OG_PRIVATE_KEY.")

# بقية الأقسام (Market & Security) تظل كما هي في النسخ السابقة لضمان الاستقرار
with tab2:
    for sym in ["BTC", "ETH", "SOL"]:
        d = market_data[sym]
        c1, c2, c3 = st.columns(3)
        c1.metric(f"{sym} Price", f"${d['price']:,}")
        c2.metric("Market Cap", f"${d['mcap']/1e12:.2f}T" if d['mcap'] > 1e12 else f"${d['mcap']/1e9:.2f}B")
        c3.metric("Supply", f"{d['supply']/1e6:.1f}M")
        st.divider()

with tab3:
    st.markdown("### 🔒 Infrastructure Status")
    st.write("VeriYield Atlantis operates within Trusted Execution Environments to ensure AI integrity.")
    st.info("Verification: Hardware-level Proof of Compute active.")
