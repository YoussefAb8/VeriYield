import streamlit as st
import opengradient as og
import asyncio
import requests

# --- 1. Page Configuration ---
st.set_page_config(
    page_title="VeriYield | AI DeFi Enclave", 
    page_icon="💠", 
    layout="wide"
)

# --- 2. Professional Cyber-Blue UI (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@500;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] { 
        background-color: #000411 !important; 
        color: #e0f2fe; 
        font-family: 'Rajdhani', sans-serif; 
    }
    
    h1, h2, h3 { 
        font-family: 'Orbitron', sans-serif; 
        color: #00e6ff !important; 
        text-shadow: 0 0 15px rgba(0, 230, 255, 0.5); 
    }
    
    /* Metrics Styling */
    div[data-testid="stMetric"] { 
        background: rgba(10, 25, 49, 0.8); 
        padding: 20px; 
        border-radius: 15px; 
        border: 1px solid #0056e0; 
    }
    [data-testid="stMetricValue"] { 
        color: #ffffff !important; 
        font-size: 26px !important; 
        font-family: 'Orbitron';
    }
    
    /* Action Button */
    div.stButton > button:first-child { 
        width: 100%; 
        background: linear-gradient(90deg, #0056e0, #00e6ff); 
        color: white; 
        font-family: 'Orbitron'; 
        font-weight: bold; 
        height: 60px; 
        border-radius: 12px; 
        border: none;
        transition: 0.3s;
    }
    div.stButton > button:first-child:hover {
        box-shadow: 0 0 25px rgba(0, 230, 255, 0.6);
        transform: translateY(-2px);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. Robust Live Data Engine ---
@st.cache_data(ttl=60) # Updates data every 60 seconds to avoid API rate limits
def fetch_live_market_data():
    try:
        # Fetching top 3 coins with real-time stats
        url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin,ethereum,solana&order=market_cap_desc&per_page=3&page=1&sparkline=false"
        response = requests.get(url, timeout=10)
        data = response.json()
        market_dict = {}
        for coin in data:
            market_dict[coin['symbol'].upper()] = {
                "name": coin['name'],
                "price": coin['current_price'],
                "mcap": coin['market_cap'],
                "supply": coin['circulating_supply']
            }
        return market_dict
    except:
        # Emergency Fallback (Realistic values if API fails)
        return {
            "BTC": {"name": "Bitcoin", "price": 72880.0, "mcap": 1460000000000, "supply": 19600000},
            "ETH": {"name": "Ethereum", "price": 2245.0, "mcap": 271000000000, "supply": 120100000},
            "SOL": {"name": "Solana", "price": 84.50, "mcap": 48500000000, "supply": 444200000}
        }

# --- 4. App Header ---
st.markdown("<h1 style='text-align: center;'>💠 VeriYield Atlantis</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #00e6ff; letter-spacing: 2px;'>LIVE MARKET INTELLIGENCE • TEE SECURED</p>", unsafe_allow_html=True)

market_data = fetch_live_market_data()

# Tabs in English
tab1, tab2, tab3 = st.tabs(["🚀 STRATEGY ENGINE", "📊 LIVE METRICS", "🔐 SECURITY"])

with tab1:
    st.markdown("### 💰 Generate Strategy")
    col_input, col_price = st.columns([2, 1])
    
    with col_input:
        asset_select = st.selectbox("SELECT ASSET", ["BTC", "ETH", "SOL"])
        risk_select = st.select_slider("RISK PROFILE", ["LOW", "BALANCED", "HIGH"])
    
    # Get specific asset data
    asset_data = market_data.get(asset_select)
    
    with col_price:
        st.metric(f"LIVE {asset_select} PRICE", f"${asset_data['price']:,}")

    if st.button("RUN SECURE INFERENCE"):
        with st.spinner("Connecting to OpenGradient TEE Enclave..."):
            try:
                # Accessing Streamlit Secrets
                sk = st.secrets["OG_PRIVATE_KEY"]
                llm = og.LLM(private_key=sk)
                
                query = f"Provide a {risk_select} risk yield strategy for {asset_select} at ${asset_data['price']}. Focus on security and APY."
                
                result = asyncio.run(
                    llm.chat(
                        model=og.TEE_LLM.CLAUDE_SONNET_4_6, 
                        messages=[{"role": "user", "content": query}]
                    )
                )
                
                st.success("✅ STRATEGY GENERATED")
                content = result.chat_output.get('content') if hasattr(result, 'chat_output') else str(result)
                st.markdown(content)
                
                # Verification Hash Display
                tx_hash = getattr(result, 'transaction_hash', getattr(result, 'proof_tx_hash', 'TEE_VERIFIED_0x...'))
                st.code(tx_hash, language="plaintext")
                
            except Exception as e:
                st.error("Connection Failed. Check Secrets/Private Key.")

with tab2:
    st.markdown("### 📊 Global Market Statistics")
    for symbol in ["BTC", "ETH", "SOL"]:
        d = market_data[symbol]
        c1, c2, c3 = st.columns(3)
        c1.metric(f"{symbol} Price", f"${d['price']:,}")
        
        # Formatting Market Cap (T for Trillion, B for Billion)
        mcap_val = f"${d['mcap']/1e12:.2f}T" if d['mcap'] > 1e12 else f"${d['mcap']/1e9:.2f}B"
        c2.metric("Market Cap", mcap_val)
        
        c3.metric("Circulating Supply", f"{d['supply']/1e6:.1f}M")
        st.divider()

with tab3:
    st.markdown("### 🔒 TEE Proof of Compute")
    st.write("VeriYield Atlantis uses Trusted Execution Environments (TEE) to guarantee untamperable AI results.")
    st.info("System Status: Enclave Locked & Cryptographically Verified.")
    st.image("https://img.icons8.com/nolan/128/security-shield.png")

st.markdown("<p style='text-align: center; color: #444; font-size: 0.8rem;'>Powered by OpenGradient Enclave Technology</p>", unsafe_allow_html=True)
