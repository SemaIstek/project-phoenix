import pandas as pd
from typing import Dict, Any
from .risk_analyst import RiskAnalystAgent
from .recovery_architect import RecoveryArchitectAgent
from .strategy_agent import StrategyAgent

class AgentCouncil:
    """
    Orchestrates multiple AI agents for climate risk analysis
    Uses Azure OpenAI for AI-powered insights
    """
    
    def __init__(self):
        """Initialize all agents"""
        print("🤖 Initializing Agent Council with Azure OpenAI...")
        self.risk_analyst = RiskAnalystAgent()
        self.recovery_architect = RecoveryArchitectAgent()
        self.strategy_agent = StrategyAgent()
        print("✅ All agents ready!")
    
    def analyze_and_recommend(self, climate_data: pd.DataFrame) -> Dict[str, Any]:
        """
        Full analysis pipeline with AI-powered insights
        
        Args:
            climate_data: DataFrame with columns:
                - country: str
                - damage_cost: float
                - co2_emissions: float
                - gdp: float
                
        Returns:
            Complete analysis with AI insights
        """
        print("\n" + "="*50)
        print("🏛️  PROJECT PHOENIX - AI AGENT COUNCIL")
        print("="*50)
        
        # Step 1: Risk Analysis (with AI)
        print("\n🔍 Step 1: Running Risk Analysis with Azure OpenAI...")
        risk_analysis = self.risk_analyst.analyze_climate_data(climate_data)
        print(f"✅ Risk Level: {risk_analysis['risk_level']}")
        print(f"✅ Total Damages: ${risk_analysis['total_damages']:,.0f}")
        
        # Step 2: Recovery Scenarios (with AI)
        print("\n🏗️  Step 2: Generating Recovery Scenarios with AI...")
        recovery_scenarios = self.recovery_architect.generate_recovery_scenarios(risk_analysis)
        print(f"✅ Generated {len(recovery_scenarios)} recovery scenarios")
        
        # Step 3: Policy Recommendations (with AI)
        print("\n📋 Step 3: Creating Policy Recommendations with AI...")
        policy_recommendations = self.strategy_agent.create_policy_recommendations(
            risk_analysis, 
            recovery_scenarios
        )
        print(f"✅ Generated {len(policy_recommendations)} policy recommendations")
        
        # Step 4: Executive Summary
        print("\n📊 Step 4: Generating Executive Summary...")
        total_investment = sum(s['estimated_cost'] for s in recovery_scenarios)
        
        summary = {
            "total_damages": risk_analysis['total_damages'],
            "risk_level": risk_analysis['risk_level'],
            "countries_analyzed": risk_analysis['statistics']['countries_analyzed'],
            "total_investment_required": total_investment,
            "number_of_scenarios": len(recovery_scenarios),
            "number_of_policies": len(policy_recommendations),
            "ai_powered": True,
            "ai_model": "Azure OpenAI gpt-4o-mini"
        }
        
        print("\n" + "="*50)
        print("✅ ANALYSIS COMPLETE!")
        print("="*50)
        print(f"💰 Total Investment Required: ${total_investment:,.0f}")
        print(f"🤖 AI Model: Azure OpenAI gpt-4o-mini")
        print(f"📊 Scenarios: {len(recovery_scenarios)}")
        print(f"📜 Policies: {len(policy_recommendations)}")
        
        return {
            "risk_analysis": risk_analysis,
            "recovery_scenarios": recovery_scenarios,
            "policy_recommendations": policy_recommendations,
            "summary": summary
        }