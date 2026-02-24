"""
Project Phoenix - Streamlit Frontend
Climate Risk Analysis Dashboard
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import sys
import os

# Add parent directory to path to import agents
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.council import AgentCouncil
from agents.climate_agent import ClimateAgent
from agents.economic_agent import EconomicAgent
from agents.policy_agent import PolicyAgent

# Page configuration
st.set_page_config(
    page_title="Project Phoenix - Climate Risk Analysis",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #FF6B35;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #004E89;
        margin-top: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
    }
    .agent-card {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #FF6B35;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Title and description
st.markdown('<h1 class="main-header">🔥 Project Phoenix</h1>', unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; font-size: 1.2rem; color: #666; margin-bottom: 2rem;">
    <em>Transforming climate data into living intelligence</em><br>
    AI-Powered Climate Risk Analysis & Economic Strategy Platform
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/clouds/200/phoenix.png", width=150)
    st.title("🌍 Navigation")
    
    page = st.radio(
        "Select Page",
        ["🏠 Home", "📊 Data Upload", "🤖 AI Analysis", "📈 Results", "ℹ️ About"]
    )
    
    st.markdown("---")
    st.markdown("### ⚙️ Settings")
    show_debug = st.checkbox("Show Debug Info", value=False)
    
    st.markdown("---")
    st.markdown("""
    ### 📌 Quick Stats
    - **Agents**: 6 AI Specialists
    - **Framework**: Azure AutoGen
    - **Status**: ✅ Online
    """
)

# Initialize session state
if 'data' not in st.session_state:
    st.session_state.data = None
if 'analysis_results' not in st.session_state:
    st.session_state.analysis_results = None

# Page routing
if page == "🏠 Home":
    st.markdown('<h2 class="sub-header">Welcome to Project Phoenix</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="agent-card">
            <h3>🎯 The Problem</h3>
            <p>Climate data trapped in spreadsheets. No roadmap for the future. 
            Trillions in damages invisible to decision-makers.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="agent-card">
            <h3>💡 Our Solution</h3>
            <p>Council of 6 AI Agents analyzing climate risk, economic impact, 
            and generating actionable strategies.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="agent-card">
            <h3>🚀 The Result</h3>
            <p>Transform historical data into predictive intelligence. 
            Build a financial shield for governments.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown('<h3 class="sub-header">🤖 Meet the Agent Council</h3>', unsafe_allow_html=True)
    
    agents_info = [
        {"name": "Risk Analyst", "icon": "🔍", "role": "Analyzes climate damage data & identifies high-risk regions"},
        {"name": "Climate Specialist", "icon": "🌡️", "role": "Tracks climate trends & predicts extreme events"},
        {"name": "Economic Analyst", "icon": "💰", "role": "Calculates economic impact & investment needs"},
        {"name": "Recovery Architect", "icon": "🏗️", "role": "Designs climate resilience scenarios"},
        {"name": "Policy Strategist", "icon": "📋", "role": "Creates actionable policy recommendations"},
        {"name": "Strategy Synthesizer", "icon": "🎯", "role": "Synthesizes insights into executive strategies"}
    ]
    
    col1, col2, col3 = st.columns(3)
    
    for idx, agent in enumerate(agents_info):
        col = [col1, col2, col3][idx % 3]
        with col:
            st.markdown(f"""
            <div class="agent-card">
                <h4>{agent['icon']} {agent['name']}</h4>
                <p style="font-size: 0.9rem;">{agent['role']}</p>
            </div>
            """, unsafe_allow_html=True)

elif page == "📊 Data Upload":
    st.markdown('<h2 class="sub-header">📊 Upload Climate Data</h2>', unsafe_allow_html=True)
    
    st.info("Upload a CSV file with climate damage data. Required columns: country, damage_cost, year")
    
    uploaded_file = st.file_uploader("Choose a CSV file", type=['csv'])
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.session_state.data = df
            
            st.success(f"✅ Data loaded successfully! {len(df)} rows")
            
            st.markdown("### 📋 Data Preview")
            st.dataframe(df.head(10), use_container_width=True)
            
            st.markdown("### 📈 Quick Statistics")
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Total Rows", len(df))
            with col2:
                st.metric("Columns", len(df.columns))
            with col3:
                if 'damage_cost' in df.columns:
                    st.metric("Total Damages", f"${df['damage_cost'].sum():,.0f}")
            with col4:
                if 'country' in df.columns:
                    st.metric("Countries", df['country'].nunique())
            
            # Visualizations
            if 'damage_cost' in df.columns and 'country' in df.columns:
                st.markdown("### 🌍 Damage Distribution by Country")
                top_countries = df.groupby('country')['damage_cost'].sum().sort_values(ascending=False).head(10)
                fig = px.bar(
                    x=top_countries.values,
                    y=top_countries.index,
                    orientation='h',
                    labels={'x': 'Total Damage ($)', 'y': 'Country'},
                    title='Top 10 Countries by Climate Damage'
                )
                st.plotly_chart(fig, use_container_width=True)
            
        except Exception as e:
            st.error(f"❌ Error loading data: {str(e)}")
    else:
        st.warning("👆 Please upload a CSV file to continue")
        
        # Sample data generator
        if st.button("🎲 Generate Sample Data"):
            sample_data = pd.DataFrame({
                'country': ['USA', 'China', 'India', 'Brazil', 'Germany'] * 4,
                'damage_cost': [1000000, 800000, 600000, 500000, 400000] * 4,
                'year': [2020, 2021, 2022, 2023] * 5,
                'event_type': ['Flood', 'Hurricane', 'Drought', 'Wildfire', 'Heatwave'] * 4
            })
            st.session_state.data = sample_data
            st.success("✅ Sample data generated!")
            st.rerun()

elif page == "🤖 AI Analysis":
    st.markdown('<h2 class="sub-header">🤖 AI Agent Analysis</h2>', unsafe_allow_html=True)
    
    if st.session_state.data is None:
        st.warning("⚠️ Please upload data first!")
        st.info("Go to 📊 Data Upload page to load your climate data.")
    else:
        st.success(f"✅ Data loaded: {len(st.session_state.data)} rows")
        
        st.markdown("### 🚀 Start Analysis")
        st.info("Click the button below to run the AI Agent Council analysis. This may take a few minutes.")
        
        if st.button("🔥 Run Council Analysis", type="primary"):
            with st.spinner("🤖 AI Agents are analyzing the data..."):
                try:
                    # Initialize council
                    council = AgentCouncil()
                    
                    # Progress tracking
                    progress_bar = st.progress(0)
                    status_text = st.empty()
                    
                    status_text.text("🔍 Risk Analyst working...")
                    progress_bar.progress(20)
                    
                    # Run analysis
                    results = council.analyze_and_recommend(st.session_state.data)
                    
                    status_text.text("✅ Analysis complete!")
                    progress_bar.progress(100)
                    
                    st.session_state.analysis_results = results
                    
                    st.success("🎉 Analysis complete! View results in the 📈 Results page.")
                    
                except Exception as e:
                    st.error(f"❌ Analysis failed: {str(e)}")
                    if show_debug:
                        st.exception(e)

elif page == "📈 Results":
    st.markdown('<h2 class="sub-header">📈 Analysis Results</h2>', unsafe_allow_html=True)
    
    if st.session_state.analysis_results is None:
        st.warning("⚠️ No analysis results yet!")
        st.info("Go to 🤖 AI Analysis page to run the analysis first.")
    else:
        results = st.session_state.analysis_results
        
        # Executive Summary
        st.markdown("### 📊 Executive Summary")
        summary = results.get('summary', {})
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Damages", f"${summary.get('total_damages', 0):,.0f}")
        with col2:
            st.metric("Risk Level", summary.get('risk_level', 'N/A'))
        with col3:
            st.metric("Investment Required", f"${summary.get('total_investment_required', 0):,.0f}")
        with col4:
            st.metric("Policy Recommendations", summary.get('number_of_policies', 0))
        
        # Risk Analysis
        st.markdown("### 🔍 Risk Analysis")
        risk_analysis = results.get('risk_analysis', {})
        
        col1, col2 = st.columns(2)
        with col1:
            st.json(risk_analysis)
        
        # Recovery Scenarios
        st.markdown("### 🏗️ Recovery Scenarios")
        scenarios = results.get('recovery_scenarios', [])
        
        for scenario in scenarios:
            with st.expander(f"📋 {scenario.get('scenario_name', 'Scenario')}"):
                st.markdown(f"**Timeframe:** {scenario.get('timeframe', 'N/A')}")
                st.markdown(f"**Focus:** {scenario.get('focus', 'N/A')}")
                st.markdown(f"**Estimated Cost:** ${scenario.get('estimated_cost', 0):,.0f}")
                st.markdown(f"**Expected Impact:** {scenario.get('expected_impact', 'N/A')}")
        
        # Policy Recommendations
        st.markdown("### 📋 Policy Recommendations")
        policies = results.get('policy_recommendations', [])
        
        for policy in policies:
            with st.expander(f"🎯 {policy.get('title', 'Policy')}"):
                st.markdown(f"**Priority:** {policy.get('priority', 'N/A')}")
                st.markdown(f"**Description:** {policy.get('description', 'N/A')}")
                st.markdown(f"**Budget:** ${policy.get('estimated_budget', 0):,.0f}")
        
        # Download results
        st.markdown("### 💾 Download Results")
        if st.button("📥 Download Full Report (JSON)"):
            import json
            json_str = json.dumps(results, indent=2)
            st.download_button(
                label="Download JSON",
                data=json_str,
                file_name=f"phoenix_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json"
            )

elif page == "ℹ️ About":
    st.markdown('<h2 class="sub-header">ℹ️ About Project Phoenix</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    ### 🔥 Project Phoenix
    
    **Transforming climate data into living intelligence**
    
    Built for AI Dev Days Hackathon 2026
    
    #### 🎯 Mission
    Transform static climate data into actionable intelligence that helps governments and organizations
    build resilience against climate change.
    
    #### 🏗️ Architecture
    - **Frontend**: Streamlit (Python)
    - **Backend**: FastAPI
    - **AI Framework**: Microsoft Azure AutoGen
    - **Agents**: 6 specialized AI agents
    - **Cloud**: Microsoft Azure
    
    #### 🤖 Agent Council
    1. **Risk Analyst** - Climate damage analysis
    2. **Climate Specialist** - Climate trend analysis
    3. **Economic Analyst** - Economic impact assessment
    4. **Recovery Architect** - Resilience scenario planning
    5. **Policy Strategist** - Policy recommendations
    6. **Strategy Synthesizer** - Executive decision support
    
    #### 📊 Data Sources
    - Climate damage data (Loss & Damage Database)
    - CO2 emissions (Global Carbon Project)
    - GDP & economic indicators (World Bank)
    
    #### 🔗 Links
    - [GitHub Repository](https://github.com/SemaIstek/project-phoenix)
    - [Microsoft Agent Framework](https://microsoft.github.io/autogen/)
    - [Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-services/openai-service)
    
    ---
    
    **From the ashes, we rise. 🔥**
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p>🔥 Project Phoenix | Built with ❤️ for AI Dev Days Hackathon 2026</p>
    <p><em>Powered by Microsoft Azure AutoGen & GitHub Copilot</em></p>
</div>
""", unsafe_allow_html=True)