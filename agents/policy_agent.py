"""
Policy Agent
Specialized agent for policy recommendation and governance strategy
"""

import pandas as pd
from typing import Dict, List, Any, Optional
import autogen
from .config import AgentConfig


POLICY_AGENT_SYSTEM_MESSAGE = """
You are a Policy Strategy Agent specializing in climate governance and policy development.

Your responsibilities:
1. Generate evidence-based policy recommendations for climate adaptation
2. Prioritize interventions based on urgency, impact, and feasibility
3. Design implementation roadmaps with clear milestones
4. Assess policy feasibility considering political, social, and economic constraints
5. Provide governance frameworks for climate resilience

You work with policy frameworks, governance models, and stakeholder analysis.
Your recommendations help governments create effective climate action plans.
"""


class PolicyAgent:
    """Policy Agent for policy recommendation and strategy"""
    
    def __init__(self):
        """Initialize Policy Agent"""
        AgentConfig.validate_config()
        
        self.llm_config = AgentConfig.get_llm_config()
        
        # Create AutoGen assistant agent
        self.agent = autogen.AssistantAgent(
            name="PolicyStrategist",
            system_message=POLICY_AGENT_SYSTEM_MESSAGE,
            llm_config=self.llm_config,
        )
    
    def generate_policy_recommendations(self, risk_data: Dict[str, Any], economic_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Generate policy recommendations based on risk and economic analysis
        
        Args:
            risk_data: Risk analysis results
            economic_data: Economic impact data
            
        Returns:
            List of policy recommendations
        """
        policies = []
        
        risk_level = risk_data.get('risk_level', 'MEDIUM')
        total_damages = risk_data.get('total_damages', 0)
        
        # Policy 1: Emergency Response Framework
        policies.append({
            "policy_id": "POL-001",
            "title": "Climate Emergency Response Framework",
            "category": "Emergency Management",
            "priority": "CRITICAL" if risk_level in ["HIGH", "CRITICAL"] else "HIGH",
            "description": "Establish comprehensive emergency response protocols for climate disasters",
            "estimated_budget": total_damages * 0.15,
            "timeframe": "0-6 months",
            "implementation_steps": [
                "Create national climate emergency coordination center",
                "Deploy early warning systems",
                "Establish emergency relief funds",
                "Train first responders in climate disaster management"
            ],
            "expected_outcomes": [
                "Reduce emergency response time by 50%",
                "Save lives and minimize immediate damages",
                "Coordinate multi-agency responses effectively"
            ]
        })
        
        # Policy 2: Infrastructure Resilience
        policies.append({
            "policy_id": "POL-002",
            "title": "Climate-Resilient Infrastructure Development",
            "category": "Infrastructure",
            "priority": "HIGH",
            "description": "Modernize infrastructure to withstand climate impacts",
            "estimated_budget": total_damages * 0.35,
            "timeframe": "6-36 months",
            "implementation_steps": [
                "Conduct infrastructure vulnerability assessments",
                "Upgrade critical infrastructure (power, water, transport)",
                "Implement green infrastructure solutions",
                "Establish building codes for climate resilience"
            ],
            "expected_outcomes": [
                "Reduce infrastructure damage by 40%",
                "Improve service continuity during extreme events",
                "Create construction jobs"
            ]
        })
        
        # Policy 3: Climate Finance Mechanism
        policies.append({
            "policy_id": "POL-003",
            "title": "National Climate Finance Mechanism",
            "category": "Finance",
            "priority": "HIGH",
            "description": "Create dedicated funding mechanism for climate adaptation",
            "estimated_budget": total_damages * 0.20,
            "timeframe": "3-12 months",
            "implementation_steps": [
                "Establish climate adaptation fund",
                "Create green bonds program",
                "Implement carbon pricing mechanism",
                "Develop insurance schemes for climate risks"
            ],
            "expected_outcomes": [
                "Mobilize $X billion for climate action",
                "Incentivize private sector investment",
                "Provide financial protection for vulnerable populations"
            ]
        })
        
        # Policy 4: Renewable Energy Transition
        policies.append({
            "policy_id": "POL-004",
            "title": "Accelerated Renewable Energy Transition",
            "category": "Energy",
            "priority": "MEDIUM",
            "description": "Transition to 100% renewable energy by 2040",
            "estimated_budget": total_damages * 0.30,
            "timeframe": "1-10 years",
            "implementation_steps": [
                "Phase out fossil fuel subsidies",
                "Invest in solar, wind, and hydro infrastructure",
                "Modernize power grid for distributed generation",
                "Provide incentives for renewable energy adoption"
            ],
            "expected_outcomes": [
                "Reduce carbon emissions by 70% by 2035",
                "Create 500,000 green energy jobs",
                "Improve energy security and independence"
            ]
        })
        
        return policies
    
    def prioritize_interventions(self, policies: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Prioritize policy interventions based on multiple criteria
        
        Args:
            policies: List of policy recommendations
            
        Returns:
            Prioritized list of policies
        """
        priority_map = {"CRITICAL": 4, "HIGH": 3, "MEDIUM": 2, "LOW": 1}
        
        # Sort by priority
        prioritized = sorted(
            policies,
            key=lambda p: priority_map.get(p.get('priority', 'MEDIUM'), 2),
            reverse=True
        )
        
        # Add ranking
        for idx, policy in enumerate(prioritized, 1):
            policy['rank'] = idx
            policy['urgency_score'] = priority_map.get(policy.get('priority', 'MEDIUM'), 2) * 25
        
        return prioritized
    
    def assess_policy_feasibility(self, policy: Dict[str, Any]) -> Dict[str, Any]:
        """
        Assess the feasibility of a policy implementation
        
        Args:
            policy: Policy recommendation
            
        Returns:
            Feasibility assessment
        """
        feasibility = {
            "policy_id": policy.get('policy_id'),
            "policy_title": policy.get('title'),
            "feasibility_score": 0.0,
            "assessment": {
                "political_feasibility": "Medium",
                "technical_feasibility": "High",
                "financial_feasibility": "Medium",
                "social_acceptance": "High",
                "implementation_complexity": "Medium"
            },
            "barriers": [
                "Political resistance from fossil fuel interests",
                "Initial high capital costs",
                "Need for technical capacity building"
            ],
            "enablers": [
                "Growing public awareness of climate risks",
                "Declining renewable energy costs",
                "International climate commitments"
            ],
            "risk_factors": [
                "Budget constraints",
                "Coordination challenges across agencies",
                "Potential delays in procurement"
            ]
        }
        
        # Calculate overall feasibility score (0-100)
        feasibility["feasibility_score"] = 72.0  # Simplified calculation
        
        return feasibility
    
    def create_implementation_roadmap(self, policy: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create detailed implementation roadmap for a policy
        
        Args:
            policy: Policy recommendation
            
        Returns:
            Implementation roadmap
        """
        roadmap = {
            "policy_id": policy.get('policy_id'),
            "policy_title": policy.get('title'),
            "phases": [
                {
                    "phase": 1,
                    "name": "Planning and Design",
                    "duration": "Months 1-3",
                    "activities": [
                        "Conduct stakeholder consultations",
                        "Develop detailed policy framework",
                        "Secure budget approval",
                        "Establish implementation team"
                    ],
                    "deliverables": [
                        "Policy framework document",
                        "Budget allocation",
                        "Implementation team roster"
                    ],
                    "budget_allocation": "10%"
                },
                {
                    "phase": 2,
                    "name": "Pilot Implementation",
                    "duration": "Months 4-9",
                    "activities": [
                        "Launch pilot programs in selected regions",
                        "Monitor and evaluate pilot results",
                        "Gather stakeholder feedback",
                        "Refine implementation approach"
                    ],
                    "deliverables": [
                        "Pilot program reports",
                        "Lessons learned document",
                        "Revised implementation plan"
                    ],
                    "budget_allocation": "20%"
                },
                {
                    "phase": 3,
                    "name": "Full-Scale Rollout",
                    "duration": "Months 10-24",
                    "activities": [
                        "Scale up to national level",
                        "Provide training and capacity building",
                        "Establish monitoring systems",
                        "Coordinate with local governments"
                    ],
                    "deliverables": [
                        "National implementation",
                        "Training materials",
                        "M&E framework"
                    ],
                    "budget_allocation": "50%"
                },
                {
                    "phase": 4,
                    "name": "Monitoring and Optimization",
                    "duration": "Months 25+",
                    "activities": [
                        "Continuous performance monitoring",
                        "Impact evaluation",
                        "Policy adjustments based on data",
                        "Knowledge sharing and documentation"
                    ],
                    "deliverables": [
                        "Annual impact reports",
                        "Policy optimization recommendations",
                        "Best practices documentation"
                    ],
                    "budget_allocation": "20%"
                }
            ],
            "key_milestones": [
                {"month": 3, "milestone": "Policy framework approved"},
                {"month": 9, "milestone": "Pilot completed successfully"},
                {"month": 12, "milestone": "50% national coverage achieved"},
                {"month": 24, "milestone": "100% national coverage achieved"}
            ],
            "success_metrics": [
                "Number of beneficiaries reached",
                "Reduction in climate damages",
                "Stakeholder satisfaction score",
                "Budget utilization rate"
            ]
        }
        
        return roadmap
    
    def get_agent(self) -> autogen.AssistantAgent:
        """Return the AutoGen agent instance"""
        return self.agent
