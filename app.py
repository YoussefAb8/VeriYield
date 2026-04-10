import streamlit as st
import opengradient as og
import asyncio

# --- 1. إعدادات الصفحة والهوية ---
st.set_page_config(
    page_title="VeriYield | Verifiable DeFi Intelligence",
    page_icon="🛡️",
    layout="centered"
)

# --- 2. تصميم CSS متطور (ألوان جذابة وتأثيرات بصرية) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Orbitron:wght@500&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', sans-serif;
        background-color: #05070a;
        color: #e4e6eb;
    }

    /* تصميم العناوين */
    h1 { font-family: 'Orbitron', sans-serif; color: #00ff88 !important; text-shadow: 0 0 15px rgba(0, 255, 136, 0.3); }
    
    /* تصميم البطاقات والمقاييس (Metrics) */
    div[data-testid="stMetric"] { 
        background: linear-gradient(145deg, #0f131a, #161b22);
        padding: 25px; 
        border-radius: 20px; 
        border: 1px solid rgba(0, 255, 136, 0.2);
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    
    [data-testid="stMetricValue"] { 
        color: #00e6ff !important; 
        font-family: 'Orbitron', sans-serif;
    }

    /* تصميم التبويبات (Tabs) */
    .stTabs [data-baseweb="tab"] { 
        font-weight: 600; 
        color: #888a8e; 
        border-radius: 10px;
        transition: 0.3s;
    }

    .stTabs [data-baseweb="tab"][aria-selected="true"] { 
        color: #ffffff !important;
        background-color: rgba(0, 255, 136, 0.1) !important;
        border-bottom: 2px solid #00ff88 !important;
    }

    /* الزر الرئيسي بتأثير متوهج */
    div.stButton > button:first-child {
        width: 100%;
        background: linear-gradient(90deg, #00ff88 0%, #00e6ff 100%);
        color: #000000;
        font-weight: 700;
        font-family: 'Orbitron', sans-serif;
        height: 55px;
        border-radius: 15px;
        border: none;
        box-shadow: 0 4px 20px rgba(0, 255, 136, 0.2);
        transition: 0.4s ease;
    }
    
    div.stButton > button:first-child:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0, 255, 136, 0.4);
    }

    /* تنسيق صندوق النتائج */
    .stSuccess {
        background-color: rgba(0, 255, 136, 0.05) !important;
        border: 1px solid #00ff88 !important;
        color: #e4e6eb !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. الهيدر (Header) ---
st.markdown("<h1 style='text-align: center;'>🛡️ VERIYIELD</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888a8e; letter-spacing: 2px;'>VERIFIABLE AI YIELD OPTIMIZATION</p>", unsafe_allow_html=True)
st.divider()

# --- 4. التبويبات الرئيسية (Main Tabs) ---
tab_optimizer, tab_security, tab_market = st.tabs(["🚀 Optimizer", "🔐 Security Proof", "📊 Market Info"])

with tab_optimizer:
    st.markdown("### 💰 Strategy Engine")
    
    # بطاقة إدخال أنيقة
    col_input, col_balance = st.columns([2, 1])
    with col_input:
        asset = st.text_input("Asset Symbol", value="ETH", placeholder="e.g. BTC, SOL, USDC")
    with col_balance:
        st.metric("Estimated Balance", f"1,250.00 {asset}")

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("GENERATE SECURE STRATEGY"):
        if not asset.strip():
            st.error("Please enter a valid asset symbol.")
        else:
            with st.spinner("Synchronizing with TEE Enclave..."):
                try:
                    # جلب المفتاح السري
                    if "OG_PRIVATE_KEY" in st.secrets:
                        PRIVATE_KEY = st.secrets["OG_PRIVATE_KEY"]
                    else:
                        st.error("System Error: Private Key missing.")
                        st.stop()
                    
                    llm = og.LLM(private_key=PRIVATE_KEY)
                    
                    result = asyncio.run(
                        llm.chat(
                            model=og.TEE_LLM.CLAUDE_SONNET_4_6,
                            messages=[
                                {"role": "system", "content": "You are VeriYield AI. Provide a professional yield strategy in a table format."},
                                {"role": "user", "content": f"Create a yield strategy for {asset} with focused risk tiers."}
                            ],
                            max_tokens=500
                        )
                    )
                    
                    text = result.chat_output.get('content') if hasattr(result, 'chat_output') else str(result)
                    
                    st.success("#### 🎯 AI-Driven Strategy Analysis")
                    st.markdown(text)
                    
                    # عرض برهان الحماية (Proof)
                    tx_hash = getattr(result, 'proof_tx_hash', None)
                    if tx_hash:
                        with st.expander("🛡️ View Cryptographic Proof"):
                            st.info("Verified by Trusted Execution Environment (TEE).")
                            st.code(tx_hash, language="plaintext")
                            
                except Exception as e:
                    st.error(f"Inference Error: {str(e)}")

with tab_security:
    st.markdown("### 🔒 Infrastructure Security")
    st.write("""
    VeriYield ensures that AI-driven financial insights are generated within a **Hardware-Secured Enclave**.
    """)
    
    c1, c2, c3 = st.columns(3)
    c1.info("**Tamper-Proof**\nAI logic cannot be modified.")
    c2.info("**Verifiable**\nOn-chain cryptographic signatures.")
    c3.info("**Private**\nInputs are isolated from the host.")

with tab_market:
    st.markdown("### 📊 Market Intelligence")
    st.info("Live data streams for TVL and APY will be active in the next update.")

st.divider()
st.markdown("<p style='text-align: center; color: #4a4a4a; font-size: 0.8rem;'>VeriYield Alpha v1.0 • Powered by OpenGradient Network</p>", unsafe_allow_html=True)
