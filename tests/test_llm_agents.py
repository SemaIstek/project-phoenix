from agents.council import AgentCouncil
import pandas as pd

# Sample data
data = pd.DataFrame({
    'country': ['Turkey', 'Greece', 'Italy'],
    'damage_cost': [2500000, 1800000, 2200000],
    'co2_emissions': [450000000, 85000000, 330000000],
    'gdp': [905000000000, 215000000000, 2100000000000]
})

# Run analysis with AI
council = AgentCouncil()
results = council.analyze_and_recommend(data)

# Check AI insights
print("🤖 AI Risk Insights:")
print(results['risk_analysis']['ai_insights'])

print("\n🤖 AI Recovery Scenarios:")
for scenario in results['recovery_scenarios']:
    print(f"\n{scenario['scenario_name']}:")
    print(scenario['ai_generated_details'])

print("\n🤖 AI Policy Recommendations:")
for policy in results['policy_recommendations']:
    print(f"\n{policy['title']}:")
    print(policy['ai_generated_details'])