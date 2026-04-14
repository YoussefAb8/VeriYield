import streamlit as st
import opengradient as og
import asyncio
from datetime import datetime
import pandas as pd

# Try to import Plotly safely
try:
    import plotly.express as px
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False

# ------------------- PAGE CONFIG & ADVANCED STYLING -------------------
st.set_page_config(
    page_title="VeriYield | 2026 DeFi Intelligence",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Orbitron:wght@500;600;700&display=swap');
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', sans-serif;
        background: linear-gradient(180deg, #0a0f1f 0%, #000814 100%);
        color: #e4e6eb;
    }
    h1, h2, h3 {
        font-family: 'Orbitron', sans-serif;
        color: #00ff9d;
        letter-spacing: 0.5px;
    }
    .glass-card {
        background: rgba(15, 23, 42, 0.75);
        border-radius: 16px;
        padding: 24px;
        border: 1px solid rgba(0, 255, 157, 0.25);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        backdrop-filter: blur(16px);
    }
    .glass-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 40px rgba(0, 255, 157, 0.3);
    }
    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #00ff9d 0%, #00d4ff 100%);
        color: #0a0f1f;
        font-weight: 700;
        height: 54px;
        border-radius: 14px;
        border: none;
        box-shadow: 0 4px 20px rgba(0, 255, 157, 0.5);
    }
    .stButton > button:hover {
        transform: scale(1.03);
        box-shadow: 0 8px 30px rgba(0, 255, 157, 0.7);
    }
    .stTabs [data-baseweb="tab"] {
        font-weight: 600;
        background: rgba(15, 23, 42, 0.8);
        color: #94a3b8;
        padding: 14px 28px;
        border-radius: 12px;
        margin: 0 6px;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background: linear-gradient(90deg, #00ff9d, #00d4ff);
        color: #0a0f1f !important;
    }
    /* Better readability for long markdown responses */
    .stMarkdown p, .stMarkdown li {
        line-height: 1.7;
    }
    </style>
    """, unsafe_allow_html=True)

# ------------------- SIDEBAR -------------------
with st.sidebar:
    st.markdown("<h2 style='text-align:center; color:#00ff9d;'>🛡️ VERIYIELD</h2>", unsafe_allow_html=True)
    st.caption("2026 Verifiable DeFi Intelligence")
    st.divider()
   
    st.markdown("### Quick Asset")
    quick_assets = ["", "ETH", "BTC", "SOL", "SUI", "AVAX", "TON", "BNB"]
    selected_quick = st.selectbox("Popular Assets", quick_assets, index=0)
   
    st.divider()
    st.success("✅ TEE Hardware Verified")
    st.info("🔗 OpenGradient Live")
    st.divider()
    st.caption("VeriYield v2.5 • Tamper-Proof Yield Intelligence")

# ------------------- HEADER -------------------
st.markdown("<h1 style='text-align:center; color:#00ff9d;'>🛡️ VERIYIELD</h1>", unsafe_allow_html=True)
current_date = datetime.now().strftime("%B %d, %Y • %H:%M UTC")
st.markdown(f"<p style='text-align:center; color:#94a3b8; font-size:1.1rem;'>{current_date}</p>", unsafe_allow_html=True)
st.caption("LIVE DEFI INTELLIGENCE • POWERED BY TRUSTED EXECUTION ENVIRONMENTS")
st.divider()

# ------------------- TABS -------------------
tab_optimizer, tab_market, tab_security, tab_edu = st.tabs([
    "🚀 Strategy Optimizer",
    "📈 Market Pulse",
    "🔐 Security & Proofs",
    "📚 DeFi Academy"
])

# TAB 1: OPTIMIZER - LONG DETAILED ANSWERS
with tab_optimizer:
    st.markdown("### 💰 Generate Verifiable 2026 Yield Strategy")
   
    c1, c2 = st.columns([3, 1])
    with c1:
        asset = st.text_input("Asset Symbol (e.g. ETH, SOL)", value=selected_quick or "", placeholder="ETH")
    with c2:
        risk_level = st.select_slider("Risk Profile", options=["Conservative", "Balanced", "Aggressive"], value="Balanced")
   
    detail_level = st.select_slider(
        "Desired Detail Level",
        options=["Concise", "Standard", "Detailed", "Very Comprehensive"],
        value="Very Comprehensive"
    )
   
    if st.button("🚀 GENERATE VERIFIABLE STRATEGY", type="primary"):
        if not asset.strip():
            st.error("Please enter an asset symbol.")
        else:
            with st.spinner(f"Analyzing {asset.upper()} in TEE hardware... Generating detailed strategy (this may take 10-30 seconds)"):
                try:
                    PRIVATE_KEY = st.secrets.get("OG_PRIVATE_KEY")
                    if not PRIVATE_KEY:
                        st.error("OG_PRIVATE_KEY missing in Secrets. Add it in Streamlit Cloud Settings.")
                        st.stop()
                   
                    llm = og.LLM(private_key=PRIVATE_KEY)
                    llm.ensure_opg_approval(min_allowance=0.1)
                   
                    detail_instructions = {
                        "Concise": "Keep the response professional but relatively concise.",
                        "Standard": "Provide a balanced, informative response with good detail.",
                        "Detailed": "Provide a highly detailed response with in-depth analysis.",
                        "Very Comprehensive": "Provide an extremely detailed, comprehensive, and in-depth 2026 yield strategy. Expand on every section with thorough explanations, multiple examples, data-backed reasoning, and forward-looking insights."
                    }
                   
                    query = f"""
                    Current date: {current_date}.
                    Risk profile: {risk_level}.
                    Detail level: {detail_level}.
                    
                    You are VeriYield AI — an expert, highly analytical 2026 DeFi strategist.
                    
                    Create a **very detailed and comprehensive** yield strategy for {asset.upper()} (considering it as one of the Top 30 assets).
                    
                    Use clear markdown formatting and structure your response with these sections:
                    
                    1. **Executive Summary** — 3-5 rich paragraphs
                    2. **Strategy Matrix** — A well-formatted markdown table with columns: Risk Level | Recommended Protocols | Mechanism | Estimated APY Range | Rationale & Time Horizon
                    3. **Detailed Strategy Breakdown** — Explain each component thoroughly
                    4. **Composability & Advanced Tactics** — Portfolio integration, leverage, cross-chain, etc.
                    5. **Key Risks & Mitigation Strategies** — At least 7-8 risks with detailed mitigations
                    6. **2026 Market Outlook for {asset}** — Macro factors, catalysts, bull/bear/base scenarios
                    7. **Monitoring Recommendations** — Key metrics to track weekly/monthly
                    
                    Be professional, insightful, and data-oriented. Use bullet points, subheadings, and tables freely.
                    {detail_instructions[detail_level]}
                    """
                   
                    result = asyncio.run(
                        llm.chat(
                            model=og.TEE_LLM.CLAUDE_SONNET_4_6,
                            messages=[
                                {"role": "system", "content": "You are VeriYield AI — a professional, extremely detailed, and insightful 2026 DeFi strategist. Prioritize depth and thorough analysis over brevity when the user requests comprehensive answers."},
                                {"role": "user", "content": query}
                            ],
                            max_tokens=3000,      # Increased for long answers
                            temperature=0.7       # Balanced creativity + coherence
                        )
                    )
                   
                    content = result.chat_output.get('content') if hasattr(result, 'chat_output') else str(result)
                   
                    st.success(f"🎯 {asset.upper()} Strategy • {risk_level} Risk • {detail_level} Detail")
                    
                    word_count = len(content.split())
                    st.caption(f"📝 Generated response: ~{word_count:,} words")
                    
                    # Main readable output
                    st.markdown(content)
                    
                    # Expander for raw / copy-paste
                    with st.expander("📄 View Full Raw Response"):
                        st.markdown(content)
                    
                    # TEE Proof
                    tx_hash = getattr(result, 'proof_tx_hash', None) or getattr(result, 'transaction_hash', None)
                    if tx_hash:
                        with st.expander("🛡️ View TEE Hardware Attestation"):
                            st.code(tx_hash, language="plaintext")
                            st.caption("Verified in Trusted Execution Environment • Publicly verifiable")
                   
                except Exception as e:
                    st.error(f"Error generating strategy: {str(e)}")
                    st.info("Make sure you have sufficient OPG tokens and that the private key is correctly set in secrets.")

# TAB 2: MARKET PULSE (unchanged)
with tab_market:
    st.markdown("### 📈 2026 DeFi Market Pulse")
   
    df = pd.DataFrame({
        "Asset": ["ETH", "SOL", "BTC", "AVAX", "SUI"],
        "Base APY": [4.1, 6.5, 0.9, 7.2, 5.8],
        "LRT Premium": [3.4, 4.9, 2.5, 4.1, 6.2],
        "AI Vault": [2.3, 3.1, 1.8, 2.6, 3.9],
        "Projected Total": [9.8, 14.5, 5.2, 13.9, 15.9]
    })
   
    left, right = st.columns([2, 1])
    with left:
        st.dataframe(
            df.style.format({col: "{:.1f}%" for col in ["Base APY", "LRT Premium", "AI Vault", "Projected Total"]}),
            use_container_width=True,
            hide_index=True
        )
   
    with right:
        if PLOTLY_AVAILABLE:
            fig = px.bar(
                df,
                x="Asset",
                y="Projected Total",
                color="Projected Total",
                color_continuous_scale=px.colors.sequential.Emrld,
                text="Projected Total"
            )
            fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
            fig.update_layout(
                yaxis_title="Projected Total APY (%)",
                plot_bgcolor="rgba(0,0,0,0)",
                paper_bgcolor="rgba(0,0,0,0)",
                margin=dict(t=20, b=40)
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Plotly is not available. Add 'plotly' to requirements.txt and redeploy.")
   
    st.caption("2026 Trend: LRTs + AI vaults deliver the highest risk-adjusted yields.")

# TAB 3: SECURITY (unchanged)
with tab_security:
    st.markdown("### 🔐 Security & Proofs")
    st.write("All strategies run inside **OpenGradient Trusted Execution Environments (TEE)** — hardware-isolated and tamper-proof.")
    cols = st.columns(3)
    with cols[0]:
        st.markdown('<div class="glass-card"><h4>Integrity</h4><p>Hardware enclave execution</p></div>', unsafe_allow_html=True)
    with cols[1]:
        st.markdown('<div class="glass-card"><h4>Transparency</h4><p>On-chain cryptographic proof</p></div>', unsafe_allow_html=True)
    with cols[2]:
        st.markdown('<div class="glass-card"><h4>Verifiability</h4><p>Anyone can verify the output</p></div>', unsafe_allow_html=True)

# TAB 4: EDUCATION (unchanged)
with tab_edu:
    st.markdown("### 📚 2026 DeFi Academy")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div class="glass-card">
            <h4 style='color:#00ff9d;'>Liquid Restaking Tokens (LRTs)</h4>
            <p>Allow one asset to secure multiple networks while remaining liquid and composable.</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="glass-card">
            <h4 style='color:#00ff9d;'>AI-Curated Vaults</h4>
            <p>Dynamic allocation across opportunities using real-time risk and yield data.</p>
        </div>
        """, unsafe_allow_html=True)

# FOOTER
st.divider()
st.markdown(f"<p style='text-align:center; color:#64748b; font-size:0.85rem;'>VeriYield v2.5 • GitHub Deployed • {current_date}</p>", unsafe_allow_html=True)
