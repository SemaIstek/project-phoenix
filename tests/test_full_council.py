# test_full_council.py
import sys
import os
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

import pandas as pd
from agents.council import AgentCouncil

print("=" * 70)
print("🏛️  PROJECT PHOENIX - FULL AGENT COUNCIL TEST")
print("=" * 70)

# Create comprehensive climate data
print("\n📊 Creating climate damage dataset...")
sample_data = pd.DataFrame({
    'country': ['USA', 'China', 'India', 'Brazil', 'Germany', 'Japan', 'Australia', 'Canada'],
    'damage_cost': [1000000, 2000000, 1500000, 800000, 600000, 700000, 500000, 400000],
    'co2_emissions': [5000, 10000, 3000, 2000, 800, 1200, 400, 600],
    'gdp': [21000000, 14000000, 2800000, 1800000, 3800000, 5000000, 1500000, 1700000]
})
print(f"✅ Dataset ready: {len(sample_data)} countries, ${sample_data['damage_cost'].sum():,.0f} total damages\n")

# Initialize council
print("🤖 Initializing Agent Council (Risk Analyst + Recovery Architect + Strategy Agent)...")
try:
    council = AgentCouncil()
    print("✅ All agents initialized!\n")
except Exception as e:
    print(f"❌ Failed to initialize: {e}")
    sys.exit(1)

# Run full analysis
print("🚀 Running full climate risk analysis pipeline...\n")
try:
    report = council.analyze_and_recommend(sample_data)
    
    print("\n" + "=" * 70)
    print("📋 EXECUTIVE SUMMARY")
    print("=" * 70)
    
    summary = report['summary']
    print(f"\n💰 Total Climate Damages: ${summary['total_damages']:,.2f}")
    print(f"⚠️  Overall Risk Level: {summary['risk_level']}")
    print(f"📊 Recovery Scenarios Generated: {summary['number_of_scenarios']}")
    print(f"📜 Policy Recommendations Created: {summary['number_of_policies']}")
    print(f"💵 Total Investment Required: ${summary['total_investment_required']:,.2f}")
    
    print("\n" + "=" * 70)
    print("🌍 TOP 3 HIGH RISK COUNTRIES")
    print("=" * 70)
    for i, country in enumerate(report['risk_analysis']['high_risk_countries'][:3], 1):
        print(f"\n#{i} 📍 {country['country']}")
        print(f"   💸 Total Damage: ${country['total_damage']:,.2f}")
        print(f"   📉 Average Damage: ${country['avg_damage']:,.2f}")
        print(f"   🔢 Incident Count: {country['incident_count']}")
    
    print("\n" + "=" * 70)
    print("🏗️  RECOVERY SCENARIOS")
    print("=" * 70)
    for scenario in report['recovery_scenarios']:
        print(f"\n🎯 {scenario['scenario_name']}")
        print(f"   ⏱️  Timeframe: {scenario['timeframe']}")
        print(f"   💰 Estimated Cost: ${scenario['estimated_cost']:,.2f}")
        print(f"   🎯 Focus: {scenario['focus']}")
        print(f"   📈 Expected Impact: {scenario['expected_impact']}")
        print(f"   🔧 Key Actions: {len(scenario['key_actions'])} planned")
    
    print("\n" + "=" * 70)
    print("📜 POLICY RECOMMENDATIONS")
    print("=" * 70)
    for policy in report['policy_recommendations']:
        print(f"\n🚨 {policy['priority']}: {policy['title']}")
        print(f"   💵 Budget: ${policy['estimated_budget']:,.2f}")
        print(f"   📝 {policy['description']}")
    
    print("\n" + "=" * 70)
    print("✅ FULL COUNCIL ANALYSIS COMPLETE!")
    print("=" * 70)
    
    print("\n📊 Correlations:")
    if 'correlations' in report['risk_analysis']:
        corr = report['risk_analysis']['correlations']
        if 'co2_damage_correlation' in corr:
            print(f"   🏭 CO2 ↔ Damage: {corr['co2_damage_correlation']:.3f}")
        if 'gdp_damage_correlation' in corr:
            print(f"   💰 GDP ↔ Damage: {corr['gdp_damage_correlation']:.3f}")
    
    print("\n🎉 Project Phoenix is operational with Ollama!")
    
except Exception as e:
    print(f"\n❌ Council analysis failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)