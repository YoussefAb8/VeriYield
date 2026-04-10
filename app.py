import streamlit as st
import opengradient as og
import asyncio

# --- 1. Page Config ---
st.set_page_config(page_title="VeriYield", page_icon="💠", layout="wide")

# --- 2. Original Design (The Clean Blue Style) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@500;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] { 
        background-color: #000411 !important; 
        color: #e0f2fe; 
        font-family: 'Rajdhani', sans-serif; 
    }
    
    h1 { 
        font-family: 'Orbitron', sans-serif; 
        color: #00e6ff !important; 
        text-align: center; 
    }

    div[data-testid="stMetric"] {
        background: rgba(10, 25, 49, 0.8);
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #0056e0;
    }

    div.stButton > button:first-child { 
        width: 100%; 
        background: linear-gradient(90deg, #0056e0, #00e6ff); 
        color: white; 
        font-family: 'Orbitron';
        height: 50px;
        border-radius: 8px;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. Header ---
st.markdown("<h1>VeriYield Atlantis</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Trustless DeFi Intelligence</p>", unsafe_allow_html=True)

# --- 4. Main Interface ---
col1, col2 = st.columns([2, 1])

with col1:
    asset = st.selectbox("Select Asset", ["ETH", "SOL", "BTC"])
    risk = st.select_slider("Risk Level", options=["Low", "Balanced", "High"])

with col2:
    st.metric("System Status", "Encrypted", delta="Verified")

if st.button("Run TEE Inference"):
    with st.spinner("Executing Secure Strategy..."):
        try:
            # Getting key from Secrets
            sk = st.secrets["OG_PRIVATE_KEY"]
            llm = og.LLM(private_key=sk)
            
            # The Original Direct Prompt
            prompt = f"Provide a {risk} risk yield strategy for {asset}. Focus on APY and Safety."
            
            result = asyncio.run(llm.chat(
                model=og.TEE_LLM.CLAUDE_SONNET_4_6, 
                messages=[{"role": "user", "content": prompt}]
            ))
            
            st.success("Strategy Generated Successfully")
            
            # Display Result
            if hasattr(result, 'chat_output'):
                st.markdown(result.chat_output.get('content'))
            else:
                st.markdown(str(result))
                
            # Proof Hash
            if hasattr(result, 'proof_tx_hash'):
                st.code(result.proof_tx_hash, language="plaintext")
                
        except Exception as e:
            st.error(f"Error: {e}")

st.divider()
st.caption("Powered by OpenGradient TEE Technology")
