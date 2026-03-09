import sys
import os
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from agents.config import AgentConfig
from agents.risk_analyst import RiskAnalystAgent
import pandas as pd

print("=" * 60)
print("🧪 AZURE OPENAI TEST")
print("=" * 60)

# 1. Config test
print("\n📋 Step 1: Validating Azure OpenAI config...")
try:
    AgentConfig.validate_config()
    print(f"✅ Using: {AgentConfig.AZURE_OPENAI_DEPLOYMENT}")
    print(f"✅ Endpoint: {AgentConfig.AZURE_OPENAI_ENDPOINT}")
except Exception as e:
    print(f"❌ Config error: {e}")
    sys.exit(1)

# 2. Sample data
print("\n📊 Step 2: Creating sample data...")
sample_data = pd.DataFrame({
    'country': ['USA', 'China', 'India'],
    'damage_cost': [1000000, 2000000, 1500000],
    'co2_emissions': [5000, 10000, 3000],
    'gdp': [21000000, 14000000, 2800000]
})
print(f"✅ {len(sample_data)} countries ready")

# 3. Initialize agent
print("\n🤖 Step 3: Initializing Risk Analyst Agent with Azure OpenAI...")
try:
    agent = RiskAnalystAgent()
    print("✅ Agent created!")
except Exception as e:
    print(f"❌ Agent creation failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# 4. Run analysis
print("\n🔬 Step 4: Running analysis with Azure OpenAI...")
try:
    result = agent.analyze_climate_data(sample_data)
    print("✅ Analysis complete!")
    print(f"\n📈 Results:")
    print(f"   Total Damages: ${result['total_damages']:,.2f}")
    print(f"   Risk Level: {result['risk_level']}")
    print(f"   Data Points: {result['data_points']}")
except Exception as e:
    print(f"❌ Analysis failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\n" + "=" * 60)
print("🎉 AZURE OPENAI TEST SUCCESSFUL!")
print("=" * 60)

