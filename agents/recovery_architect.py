import pandas as pd
from typing import Dict, Any, List
from .llm_client import AzureOpenAIClient
from .config import RECOVERY_ARCHITECT_SYSTEM_MESSAGE

class RecoveryArchitectAgent:
    """Recovery Architect Agent with Azure OpenAI"""
    
    def __init__(self):
        self.llm = AzureOpenAIClient()
        self.system_message = RECOVERY_ARCHITECT_SYSTEM_MESSAGE
    
    def generate_recovery_scenarios(self, risk_analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Generate AI-powered recovery scenarios
        
        Args:
            risk_analysis: Output from Risk Analyst Agent
            
        Returns:
            List of recovery scenarios with AI-generated details
        """
        total_damages = risk_analysis['total_damages']
        risk_level = risk_analysis['risk_level']
        
        # Base scenario calculations (Python)
        immediate_cost = total_damages * 0.15
        short_term_cost = total_damages * 0.35
        long_term_cost = total_damages * 0.5
        
        # 🤖 Generate AI-powered scenario details
        context = f"""
Risk Analysis Summary:
- Total Damages: ${total_damages:,.0f}
- Risk Level: {risk_level}
- High-Risk Countries: {', '.join([c['country'] for c in risk_analysis['high_risk_countries'][:3]])}

Generate THREE detailed recovery scenarios:
1. IMMEDIATE (0-6 months): ${immediate_cost:,.0f} budget
2. SHORT-TERM (6-24 months): ${short_term_cost:,.0f} budget  
3. LONG-TERM (2-10 years): ${long_term_cost:,.0f} budget

For each scenario, provide:
- Specific focus areas
- Key actions (3-5 concrete steps)
- Expected impact
- Implementation timeline
"""
        
        ai_scenarios = self.llm.generate_completion(
            system_message=self.system_message,
            user_message=context,
            temperature=0.8,  # More creative
            max_tokens=2000
        )
        
        # Structure scenarios with AI content
        scenarios = [
            {
                "scenario_name": "Immediate Response",
                "timeframe": "0-6 months",
                "estimated_cost": immediate_cost,
                "focus": "Emergency relief and rapid stabilization",
                "ai_generated_details": ai_scenarios.split("\n\n")[0] if ai_scenarios else "N/A",
                "priority": "CRITICAL"
            },
            {
                "scenario_name": "Short-term Recovery",
                "timeframe": "6-24 months",
                "estimated_cost": short_term_cost,
                "focus": "Infrastructure repair and economic recovery",
                "ai_generated_details": ai_scenarios.split("\n\n")[1] if len(ai_scenarios.split("\n\n")) > 1 else "N/A",
                "priority": "HIGH"
            },
            {
                "scenario_name": "Long-term Resilience",
                "timeframe": "2-10 years",
                "estimated_cost": long_term_cost,
                "focus": "Climate adaptation and sustainable development",
                "ai_generated_details": ai_scenarios.split("\n\n")[2] if len(ai_scenarios.split("\n\n")) > 2 else "N/A",
                "priority": "MEDIUM"
            }
        ]
        
        return scenarios