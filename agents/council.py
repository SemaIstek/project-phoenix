"""
Agent Council
Orchestrates the collaboration between Risk Analyst, Recovery Architect, and Strategy Agent
"""

import pandas as pd
from typing import Dict, List, Any, Optional
import autogen
from .risk_analyst import RiskAnalystAgent
from .recovery_architect import RecoveryArchitectAgent
from .strategy_agent import StrategyAgent
from .config import AgentConfig


class AgentCouncil:
    """Council of Agents for Climate Risk Analysis and Policy Generation"""
    
    def __init__(self):
        """Initialize the Agent Council"""
        # Initialize all three agents
        self.risk_analyst = RiskAnalystAgent()
        self.recovery_architect = RecoveryArchitectAgent()
        self.strategy_agent = StrategyAgent()
        
        # Create user proxy for interaction
        self.user_proxy = autogen.UserProxyAgent(
            name="UserProxy",
            human_input_mode="NEVER",
            max_consecutive_auto_reply=10,
            code_execution_config=False,
        )
    
    def analyze_and_recommend(self, climate_data: pd.DataFrame) -> Dict[str, Any]:
        """
        Run full analysis pipeline: Risk Analysis -> Recovery Planning -> Strategy
        
        Args:
            climate_data: DataFrame containing climate damage information
            
        Returns:
            Complete analysis with risk assessment, recovery scenarios, and policy recommendations
        """
        # Step 1: Risk Analysis
        print("🔍 Step 1: Running Risk Analysis...")
        risk_analysis = self.risk_analyst.analyze_climate_data(climate_data)
        correlations = self.risk_analyst.calculate_co2_correlation(climate_data)
        high_risk_countries = self.risk_analyst.identify_high_risk_countries(climate_data)
        
        risk_analysis['correlations'] = correlations
        risk_analysis['high_risk_countries'] = high_risk_countries
        
        print(f"✅ Risk Analysis Complete - Risk Level: {risk_analysis['risk_level']}")
        
        # Step 2: Recovery Architecture
        print("\n🏗️  Step 2: Generating Recovery Scenarios...")
        recovery_scenarios = self.recovery_architect.generate_recovery_scenarios(risk_analysis)
        
        print(f"✅ Generated {len(recovery_scenarios)} recovery scenarios")
        
        # Step 3: Strategy Synthesis
        print("\n📋 Step 3: Creating Policy Recommendations...")
        synthesis = self.strategy_agent.synthesize_insights(risk_analysis, recovery_scenarios)
        policy_recommendations = self.strategy_agent.create_policy_recommendations(synthesis)
        
        print(f"✅ Created {len(policy_recommendations)} policy recommendations")
        
        # Compile final report
        final_report = {
            "risk_analysis": risk_analysis,
            "recovery_scenarios": recovery_scenarios,
            "synthesis": synthesis,
            "policy_recommendations": policy_recommendations,
            "summary": {
                "total_damages": risk_analysis['total_damages'],
                "risk_level": risk_analysis['risk_level'],
                "total_investment_required": synthesis['total_investment_required'],
                "number_of_scenarios": len(recovery_scenarios),
                "number_of_policies": len(policy_recommendations)
            }
        }
        
        print("\n✅ Council Analysis Complete!")
        return final_report
    
    def generate_executive_summary(self, report: Dict[str, Any]) -> str:
        """Generate executive summary from council report"""
        
        Args:
            report: Complete analysis report from analyze_and_recommend()
            
        Returns:
            Formatted executive summary string
        """
        summary = report.get('summary', {})
        
        exec_summary = f"""
╔══════════════════════════════════════════════════════════════╗
║           PROJECT PHOENIX - EXECUTIVE SUMMARY                ║
╚══════════════════════════════════════════════════════════════╝

📊 CLIMATE RISK ASSESSMENT
──────────────────────────────────────────────────────────────
Total Climate Damages:        ${summary.get('total_damages', 0):,.2f}
Overall Risk Level:           {summary.get('risk_level', 'UNKNOWN')}

🎯 RECOVERY PLANNING
──────────────────────────────────────────────────────────────
Recovery Scenarios Generated: {summary.get('number_of_scenarios', 0)}
Total Investment Required:    ${summary.get('total_investment_required', 0):,.2f}

📋 POLICY RECOMMENDATIONS
──────────────────────────────────────────────────────────────
Policy Recommendations:       {summary.get('number_of_policies', 0)}
"""
        
        return exec_summary
    
    def get_agent(self) -> autogen.AssistantAgent:
        """Return the AutoGen agent instance"""
        return self.strategy_agent.get_agent()