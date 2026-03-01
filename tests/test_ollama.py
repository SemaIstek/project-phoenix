import sys
import os

# Proje dizinini Python path'e ekle
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

import pandas as pd

# Test 1: Config validation
print("🔍 Step 1: Testing Ollama connection...")
try:
    from agents.config import AgentConfig
    AgentConfig.validate_config()
    print(f"✅ Ollama is running! Model: {AgentConfig.OLLAMA_MODEL}\n")
except Exception as e:
    print(f"❌ Error: {e}")
    print("\n💡 Fix: Make sure Ollama is running:")
    print("   ollama serve")
    sys.exit(1)

# Test 2: Create sample climate data
print("📊 Step 2: Creating sample climate data...")
sample_data = pd.DataFrame({
    'country': ['USA', 'China', 'India', 'Brazil', 'Germany'],
    'damage_cost': [1000000, 2000000, 1500000, 800000, 600000],
    'co2_emissions': [5000, 10000, 3000, 2000, 800],
    'gdp': [21000000, 14000000, 2800000, 1800000, 3800000]
})
print(f"✅ Created data with {len(sample_data)} countries\n")

# Test 3: Initialize Risk Analyst
print("🤖 Step 3: Initializing Risk Analyst Agent...")
try:
    from agents.risk_analyst import RiskAnalystAgent
    risk_agent = RiskAnalystAgent()
    print("✅ Risk Analyst Agent created!\n")
except Exception as e:
    print(f"❌ Error creating agent: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Test 4: Run analysis
print("🔬 Step 4: Running climate risk analysis...")
try:
    analysis = risk_agent.analyze_climate_data(sample_data)
    print("✅ Analysis complete!")
    print(f"\n📈 Results:")
    print(f"   Total Damages: ${analysis['total_damages']:,.2f}")
    print(f"   Average Damages: ${analysis['average_damages']:,.2f}")
    print(f"   Risk Level: {analysis['risk_level']}")
    print(f"   Data Points: {analysis['data_points']}")
except Exception as e:
    print(f"❌ Error during analysis: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\n🎉 Basic tests passed!")