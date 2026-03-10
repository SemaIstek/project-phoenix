from typing import Dict, Any, List
from .llm_client import AzureOpenAIClient
from .config import STRATEGY_AGENT_SYSTEM_MESSAGE

class StrategyAgent:
    """Strategy Agent with Azure OpenAI for policy generation"""
    
    def __init__(self):
        self.llm = AzureOpenAIClient()
        self.system_message = STRATEGY_AGENT_SYSTEM_MESSAGE
    
    def create_policy_recommendations(
        self, 
        risk_analysis: Dict[str, Any],
        recovery_scenarios: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """
        Generate AI-powered policy recommendations
        
        Returns:
            List of actionable policies with AI-generated details
        """
        total_investment = sum(s['estimated_cost'] for s in recovery_scenarios)
        
        # 🤖 Generate AI-powered policy recommendations
        context = f"""
COMPREHENSIVE ANALYSIS:

Risk Assessment:
- Total Damages: ${risk_analysis['total_damages']:,.0f}
- Risk Level: {risk_analysis['risk_level']}
- Countries Affected: {risk_analysis['statistics']['countries_analyzed']}

Recovery Investment Required: ${total_investment:,.0f}

Generate 3-5 ACTIONABLE POLICY RECOMMENDATIONS that:
1. Address immediate risks
2. Allocate budget effectively
3. Provide clear implementation steps
4. Consider political and economic feasibility

Format each policy as:
- Title
- Priority Level (CRITICAL/HIGH/MEDIUM)
- Budget Allocation
- Implementation Steps
- Expected Outcomes
"""
        
        ai_policies = self.llm.generate_completion(
            system_message=self.system_message,
            user_message=context,
            temperature=0.7,
            max_tokens=2000
        )
        
        # Structure policies
        policies = [
            {
                "policy_id": "POL-001",
                "title": "Emergency Climate Response Fund",
                "priority": "CRITICAL",
                "estimated_budget": total_investment * 0.30,
                "description": "Establish immediate emergency fund for climate disasters",
                "ai_generated_details": ai_policies,
                "implementation_timeline": "0-3 months",
                "expected_impact": "Rapid response capability for future climate events"
            }
        ]
        
        return policies