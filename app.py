import streamlit as st
import opengradient as og
import asyncio
import requests

# --- 1. Page Config ---
st.set_page_config(page_title="VeriYield", page_icon="💠", layout="wide")

# --- 2. Clean Cyber-Blue UI ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@500;700&display=swap');
    html, body, [data-testid="stAppViewContainer"] { background-color: #000411 !important; color: #e0f2fe; font-family: 'Rajdhani', sans-serif; }
    h1 { font-family: 'Orbitron', sans-serif; color: #00e6ff !important; text-align: center; margin-bottom: 0px; }
    p.subtitle { text-align: center; color: #00e6ff; font-size: 0.8rem; letter-spacing: 2px; margin-bottom: 30px; }
    
    /* Hide specific Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Table Styling */
    table { width: 100%; border-collapse: collapse; background: rgba(0, 230, 255, 0.02); color: white; }
    th { background-color: #0056e0 !important; font-family: 'Orbitron'; padding: 15px; text-align: left; }
    td { border-bottom: 1px solid #0056e0; padding: 12px; }

    /* Button Styling */
    div.stButton > button:first-child { 
        width: 100%; background: linear-gradient(90deg, #0056e0, #00e6ff); 
        color: white; font-family: 'Orbitron'; height: 55px; border-radius: 8px; border: none; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. Simple Data Engine ---
@st.cache_data(ttl=60)
def get_market():
    try:
        url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin,ethereum,solana"
        data = requests.get(url, timeout=5).json()
        return {c['symbol'].upper(): c['current_price'] for c in data}
    except:
        return {"BTC": 72939, "ETH": 2247, "SOL": 84}

# --- 4. Content ---
st.markdown("<h1>VeriYield Atlantis</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>SECURE DEFI MATRIX</p>", unsafe_allow_html=True)

prices = get_market()
t1, t2 = st.tabs(["ENGINE", "MARKET"])

with t1:
    # Minimalist Inputs
    col1, col2 = st.columns(2)
    with col1:
        asset = st.selectbox("Asset", ["BTC", "ETH", "SOL"])
    with col2:
        risk = st.select_slider("Risk", ["Low", "Mid", "High"])
    
    if st.button("GENERATE MATRIX"):
        with st.spinner("Processing..."):
            try:
                sk = st.secrets["OG_PRIVATE_KEY"]
                llm = og.LLM(private_key=sk)
                
                # Direct prompt for a clean table
                query = f"""
                Generate a DeFi yield table for {asset} (Price: ${prices[asset]}).
                Risk Profile requested: {risk}.
                
                Show a table with these 4 columns:
                | Risk Level | Protocol | Strategy | Est. APY |
                
                Provide 3 clear rows (Low, Balanced, Aggressive).
                Below the table, add a 1-sentence security note.
                Keep it clean, English only, no conversational filler.
                """
                
                result = asyncio.run(llm.chat(
                    model=og.TEE_LLM.CLAUDE_SONNET_4_6, 
                    messages=[{"role": "user", "content": query}]
                ))
                
                st.markdown("### Result Matrix")
                content = result.chat_output.get('content') if hasattr(result, 'chat_output') else str(result)
                st.markdown(content)
                
            except:
                st.error("Connection Error.")

with t2:
    # Simplified Market View
    for s, p in prices.items():
        st.markdown(f"**{s}**: ${p:,}")
        st.divider()
