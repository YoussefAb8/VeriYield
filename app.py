import streamlit as st
import opengradient as og
import asyncio
from datetime import datetime

# --- 1. Page Configuration & Professional Styling ---
st.set_page_config(
    page_title="VeriYield | 2026 DeFi Intelligence",
    page_icon="🛡️",
    layout="centered"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Orbitron:wght@500&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', sans-serif;
        background-color: #001529; 
        color: #e4e6eb;
    }

    h1 { font-family: 'Orbitron', sans-serif; color: #00ff88 !important; text-align: center; }
    
    div.stButton > button:first-child {
        width: 100%;
        background: linear-gradient(90deg, #00ff88 0%, #00e6ff 100%);
        color: #000000; font-weight: 700; height: 55px;
        border-radius: 12px; border: none;
        box-shadow: 0 4px 15px rgba(0, 255, 136, 0.3);
    }

    .stTabs [data-baseweb="tab"] { 
        font-weight: 600; color: #b0b3b8; background-color: #002b5c;
        padding: 10px 20px; border-radius: 12px; margin-right: 8px;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] { 
        color: #000000 !important; background-color: #00ff88 !important;
    }
    
    .edu-box {
        background-color: rgba(0, 43, 92, 0.5);
        border-radius: 12px; padding: 20px;
        border-left: 5px solid #00ff88; margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. Header & Date ---
st.markdown("<h1>🛡️ VeriYield</h1>", unsafe_allow_html=True)
current_date = datetime.now().strftime("%B %d, %Y")
st.markdown(f"<p style='text-align: center; color: #b0b3b8;'>LIVE DEFI INTELLIGENCE • {current_date}</p>", unsafe_allow_html=True)
st.divider()

# --- 3. Main Tabs ---
tab_optimizer, tab_security, tab_edu = st.tabs(["🚀 Optimizer", "🔐 Security Proof", "📚 DeFi Education"])

with tab_optimizer:
    st.markdown("### 💰 Strategy Engine")
    asset = st.text_input("Asset Symbol", value="", placeholder="Enter asset (e.g. BTC, ETH, SOL)")

    if st.button("GENERATE VERIFIABLE STRATEGY"):
        if not asset.strip():
            st.warning("Please provide an asset symbol to begin analysis.")
        else:
            with st.spinner(f"Analyzing {asset} (Top 30 Market Cap) for 2026..."):
                try:
                    if "OG_PRIVATE_KEY" in st.secrets:
                        PRIVATE_KEY = st.secrets["OG_PRIVATE_KEY"]
                    else:
                        st.error("System Error: OG_PRIVATE_KEY not found in Secrets.")
                        st.stop()
                    
                    llm = og.LLM(private_key=PRIVATE_KEY)
                    
                    # --- CRITICAL FIX: Setting min_allowance to 0.1 to avoid Error 402 ---
                    llm.ensure_opg_approval(min_allowance=0.1)
                    
                    # Optimized 2026 Context-Aware Query
                    query = f"""
                    Current Date: {current_date}. 
                    Task: Generate a professional yield strategy for {asset} within the Top 30 Market Cap scope.
                    
                    Requirements:
                    1. Focus on 2026 primitives: LRTs and AI-vaults.
                    2. Output a 'Strategy Matrix' table: | Risk Level | Protocol | Mechanism | Est. APY |
                    3. Keep the response highly concise and direct.
                    """
                    
                    result = asyncio.run(
                        llm.chat(
                            model=og.TEE_LLM.CLAUDE_SONNET_4_6,
                            messages=[
                                {"role": "system", "content": "You are VeriYield AI, a concise 2026 DeFi analyst providing verifiable financial intelligence."},
                                {"role": "user", "content": query}
                            ],
                            max_tokens=300 # Reduced from 600 to optimize Gas and avoid payment errors
                        )
                    )
                    
                    st.success(f"#### 🎯 Real-Time Strategy: {asset}")
                    content = result.chat_output.get('content') if hasattr(result, 'chat_output') else str(result)
                    st.markdown(content)
                    
                    tx_hash = getattr(result, 'proof_tx_hash', None)
                    if tx_hash:
                        with st.expander("🛡️ View Hardware Attestation"):
                            st.info("Verified by TEE (Trusted Execution Environment).")
                            st.code(tx_hash, language="plaintext")
                            
                except Exception as e:
                    st.error(f"Inference Error: {str(e)}")
                    st.info("Check if your wallet has OPG tokens for the 0.1 allowance.")

with tab_security:
    st.markdown("### 🔒 2026 Security Standards")
    st.write("VeriYield utilizes OpenGradient TEE to provide tamper-proof financial intelligence.")
    st.info("Integrity: AI logic is executed in a hardware-locked enclave.")
    st.info("Transparency: Every strategy is cryptographically signed.")

with tab_edu:
    st.markdown("### 📚 2026 DeFi Intelligence")
    st.markdown(f"""
    <div class="edu-box">
        <h4 style='color:#00ff88; margin-top:0;'>Liquid Restaking (LRT)</h4>
        <p>In 2026, LRTs are the foundation of yield, allowing capital to secure multiple networks simultaneously.</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()
st.markdown(f"<p style='text-align: center; color: #5c6370; font-size: 0.8rem;'>VeriYield v2.2 • Certified 2026 Intelligence • {current_date}</p>", unsafe_allow_html=True)
