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
        """Generate recovery scenarios based on risk analysis
        
        Args:
            risk_analysis: Risk analysis results from RiskAnalystAgent
            
        Returns:
            List of recovery scenarios
        """
        risk_level = risk_analysis.get('risk_level', 'MEDIUM')
        total_damages = risk_analysis.get('total_damages', 0)
        
        scenarios = []
        
        # Scenario 1: Immediate Response
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
        
        # Scenario 2: Short-term Recovery
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
        
        # Scenario 3: Long-term Resilience
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
    
    def model_economic_recovery(self, country: str, baseline_damage: float) -> Dict[str, Any]:
        """Model economic recovery pathway for a specific country
        
        Args:
            country: Country name
            baseline_damage: Total climate damage cost
            
        Returns:
            Economic recovery model
        """
        recovery_model = {
            "country": country,
            "baseline_damage": baseline_damage,
            "recovery_pathway": {
                "year_1": {
                    "gdp_impact": "-5% to -8%",
                    "recovery_investment": baseline_damage * 0.15,
                    "expected_recovery": "20-25%"
                },
                "year_2": {
                    "gdp_impact": "-2% to -4%",
                    "recovery_investment": baseline_damage * 0.25,
                    "expected_recovery": "50-60%"
                },
                "year_3_5": {
                    "gdp_impact": "0% to +2%",
                    "recovery_investment": baseline_damage * 0.40,
                    "expected_recovery": "85-95%"
                },
                "year_6_10": {
                    "gdp_impact": "+2% to +5%",
                    "recovery_investment": baseline_damage * 0.30,
                    "expected_recovery": "100%+ (with resilience dividend)"
                }
            },
            "total_investment_needed": baseline_damage * 1.10,
            "roi_estimate": "Every $1 invested yields $4-6 in prevented future damages"
        }
        
        return recovery_model
    
    def simulate_intervention_outcomes(self, scenario: Dict[str, Any]) -> Dict[str, Any]:
        """Simulate outcomes of different intervention strategies
        
        Args:
            scenario: Recovery scenario to simulate
            
        Returns:
            Simulation results
        """
        scenario_name = scenario.get('scenario_name', 'Unknown')
        estimated_cost = scenario.get('estimated_cost', 0)
        
        simulation = {
            "scenario": scenario_name,
            "investment": estimated_cost,
            "outcomes": {
                "best_case": {
                    "damage_reduction": "60-70%",
                    "economic_growth": "+3% to +5%",
                    "jobs_created": int(estimated_cost / 100000),  # 1 job per $100k invested
                    "roi": 6.0
                },
                "expected_case": {
                    "damage_reduction": "40-50%",
                    "economic_growth": "+2% to +3%",
                    "jobs_created": int(estimated_cost / 150000),
                    "roi": 4.0
                },
                "worst_case": {
                    "damage_reduction": "20-30%",
                    "economic_growth": "0% to +1%",
                    "jobs_created": int(estimated_cost / 250000),
                    "roi": 2.0
                }
            },
            "risk_factors": [
                "Political stability and policy continuity",
                "International cooperation and funding",
                "Technology adoption rates",
                "Public acceptance and behavioral change"
            ]
        }
        
        return simulation
    
    def get_agent(self) -> autogen.AssistantAgent:
        """Return the AutoGen agent instance"""
        return self.agent
