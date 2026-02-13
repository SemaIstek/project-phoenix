"""
Recovery Architect Agent
Generates climate resilience scenarios and recovery pathways
"""

import autogen
from typing import Dict, List, Any
from .config import AgentConfig, RECOVERY_ARCHITECT_SYSTEM_MESSAGE


class RecoveryArchitectAgent:
    """Recovery Architect Agent for climate resilience planning"""
    
    def __init__(self):
        """Initialize Recovery Architect Agent"""
        AgentConfig.validate_config()
        
        self.llm_config = AgentConfig.get_llm_config()
        
        # Create AutoGen assistant agent
        self.agent = autogen.AssistantAgent(
            name="RecoveryArchitect",
            system_message=RECOVERY_ARCHITECT_SYSTEM_MESSAGE,
            llm_config=self.llm_config,
        )
    
    def generate_recovery_scenarios(self, risk_analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate recovery scenarios based on risk analysis""" 
        risk_level = risk_analysis.get('risk_level', 'MEDIUM')
        total_damages = risk_analysis.get('total_damages', 0)
        
        scenarios = []
        
        scenarios.append({
            "scenario_name": "Immediate Emergency Response",
            "timeframe": "0-6 months",
            "focus": "Emergency relief and immediate damage mitigation",
            "estimated_cost": total_damages * 0.15,
            "expected_impact": "Prevent further immediate losses, stabilize affected regions",
            "key_actions": [
                "Deploy emergency relief funds",
                "Establish disaster response coordination",
                "Provide immediate financial aid to affected populations",
                "Assess and secure critical infrastructure"
            ]
        })
        
        scenarios.append({
            "scenario_name": "Short-term Recovery & Rebuilding",
            "timeframe": "6-24 months",
            "focus": "Infrastructure rebuilding and economic stabilization",
            "estimated_cost": total_damages * 0.35,
            "expected_impact": "Restore 60-70% of economic activity, rebuild critical infrastructure",
            "key_actions": [
                "Rebuild damaged infrastructure with climate-resilient designs",
                "Provide business recovery loans and grants",
                "Implement temporary economic stimulus programs",
                "Establish early warning systems"
            ]
        })
        
        scenarios.append({
            "scenario_name": "Long-term Climate Resilience",
            "timeframe": "2-10 years",
            "focus": "Systemic resilience building and prevention",
            "estimated_cost": total_damages * 0.50,
            "expected_impact": "Reduce future climate damages by 40-60%, build sustainable economy",
            "key_actions": [
                "Invest in renewable energy infrastructure",
                "Implement comprehensive climate adaptation strategies",
                "Develop climate-smart agriculture and industry",
                "Create green jobs and sustainable economic sectors",
                "Establish climate risk insurance mechanisms"
            ]
        })
        
        return scenarios
    
    def get_agent(self) -> autogen.AssistantAgent:
        """Return the AutoGen agent instance""" 
        return self.agent
