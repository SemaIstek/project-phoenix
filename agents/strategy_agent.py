"""
Strategy Agent
Synthesizes insights and creates actionable policy recommendations
"""

import autogen
from typing import Dict, List, Any
from .config import AgentConfig, STRATEGY_AGENT_SYSTEM_MESSAGE


class StrategyAgent:
    """Strategy Agent for policy recommendations and financial allocation"""
    
    def __init__(self):
        """Initialize Strategy Agent"""
        AgentConfig.validate_config()
        
        self.llm_config = AgentConfig.get_llm_config()
        
        # Create AutoGen assistant agent
        self.agent = autogen.AssistantAgent(
            name="StrategyAgent",
            system_message=STRATEGY_AGENT_SYSTEM_MESSAGE,
            llm_config=self.llm_config,
        )
    
    def synthesize_insights(self, 
                           risk_analysis: Dict[str, Any],
                           recovery_scenarios: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Synthesize insights from risk analysis and recovery scenarios"""
        synthesis = {
            "executive_summary": f"Climate damages: ${risk_analysis.get('total_damages', 0):,.2f}",
            "key_findings": [
                f"Risk level: {risk_analysis.get('risk_level', 'UNKNOWN')}"
                f"{len(recovery_scenarios)} recovery scenarios identified"
            ],
            "priority_level": risk_analysis.get('risk_level', 'MEDIUM'),
            "total_investment_required": sum(s.get('estimated_cost', 0) for s in recovery_scenarios)
        }
        
        return synthesis
    
    def create_policy_recommendations(self, synthesis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Create actionable policy recommendations"""
        recommendations = []
        
        recommendations.append({
            "policy_id": "POL-001",
            "title": "Emergency Climate Damage Response Fund",
            "priority": "CRITICAL",
            "description": "Establish dedicated emergency fund for immediate climate disaster response",
            "estimated_budget": synthesis.get('total_investment_required', 0) * 0.15,
        })
        
        recommendations.append({
            "policy_id": "POL-002",
            "title": "National Climate-Resilient Infrastructure Program",
            "priority": "HIGH",
            "description": "Comprehensive program to upgrade infrastructure with climate resilience",
            "estimated_budget": synthesis.get('total_investment_required', 0) * 0.40,
        })
        
        return recommendations
    
    def get_agent(self) -> autogen.AssistantAgent:
        """Return the AutoGen agent instance"""
        return self.agent