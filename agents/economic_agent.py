"""
Economic Agent
Specialized agent for economic impact analysis and financial modeling
"""

import pandas as pd
from typing import Dict, List, Any, Optional
import autogen
from .config import AgentConfig


ECONOMIC_AGENT_SYSTEM_MESSAGE = """
You are an Economic Impact Analyst Agent specializing in climate-related economic damage assessment.

Your responsibilities:
1. Analyze economic impacts of climate events on GDP, employment, and trade
2. Calculate cost-benefit ratios for climate adaptation investments
3. Model economic recovery pathways and timelines
4. Assess sector-specific vulnerabilities (agriculture, infrastructure, etc.)
5. Provide financial forecasts and investment recommendations

You work with economic data, financial models, and market indicators.
Your analysis helps governments and organizations make informed financial decisions.
"""


class EconomicAgent:
    """Economic Agent for economic impact analysis"""
    
    def __init__(self):
        """Initialize Economic Agent"""
        AgentConfig.validate_config()
        
        self.llm_config = AgentConfig.get_llm_config()
        
        # Create AutoGen assistant agent
        self.agent = autogen.AssistantAgent(
            name="EconomicAnalyst",
            system_message=ECONOMIC_AGENT_SYSTEM_MESSAGE,
            llm_config=self.llm_config,
        )
    
    def calculate_economic_impact(self, data: pd.DataFrame) -> Dict[str, Any]:
        """
        Calculate economic impact of climate damages
        
        Args:
            data: DataFrame with damage costs and GDP data
            
        Returns:
            Economic impact analysis
        """
        impact = {
            "total_economic_loss": 0.0,
            "gdp_impact_percentage": 0.0,
            "affected_countries": 0,
            "sector_impacts": {}
        }
        
        if 'damage_cost' in data.columns:
            impact["total_economic_loss"] = float(data['damage_cost'].sum())
            impact["affected_countries"] = data['country'].nunique() if 'country' in data.columns else 0
        
        # Calculate GDP impact
        if 'gdp' in data.columns and 'damage_cost' in data.columns:
            total_gdp = data['gdp'].sum()
            if total_gdp > 0:
                impact["gdp_impact_percentage"] = (impact["total_economic_loss"] / total_gdp) * 100
        
        # Sector-specific impacts
        if 'event_type' in data.columns and 'damage_cost' in data.columns:
            sector_damages = data['group by']('event_type')['damage_cost'].sum()
            impact["sector_impacts"] = sector_damages.to_dict()
        
        return impact
    
    def assess_investment_needs(self, damage_data: pd.DataFrame, recovery_multiplier: float = 1.5) -> Dict[str, Any]:
        """
        Assess investment needs for climate resilience
        
        Args:
            damage_data: Historical damage data
            recovery_multiplier: Multiplier for recovery investment
            
        Returns:
            Investment needs assessment
        """
        total_damages = damage_data['damage_cost'].sum() if 'damage_cost' in damage_data.columns else 0
        
        investment_needs = {
            "immediate_relief": total_damages * 0.15,
            "short_term_recovery": total_damages * 0.35,
            "long_term_resilience": total_damages * 0.50,
            "total_investment_required": total_damages * recovery_multiplier,
            "roi_projection": {
                "expected_damage_reduction": "40-60%",
                "payback_period_years": "5-10",
                "benefit_cost_ratio": 3.0
            }
        }
        
        return investment_needs
    
    def model_recovery_timeline(self, baseline_damage: float, country: str = "Generic") -> Dict[str, Any]:
        """
        Model economic recovery timeline
        
        Args:
            baseline_damage: Total damage cost
            country: Country name
            
        Returns:
            Recovery timeline model
        """
        recovery_timeline = {
            "country": country,
            "baseline_damage": baseline_damage,
            "recovery_phases": [
                {
                    "phase": "Emergency Response",
                    "duration": "0-6 months",
                    "gdp_impact": "-5% to -8%",
                    "employment_impact": "High unemployment",
                    "estimated_cost": baseline_damage * 0.15
                },
                {
                    "phase": "Reconstruction",
                    "duration": "6-24 months",
                    "gdp_impact": "-2% to -4%",
                    "employment_impact": "Gradual recovery",
                    "estimated_cost": baseline_damage * 0.35
                },
                {
                    "phase": "Long-term Recovery",
                    "duration": "2-5 years",
                    "gdp_impact": "0% to +2%",
                    "employment_impact": "Full recovery",
                    "estimated_cost": baseline_damage * 0.50
                }
            ]
        }
        
        return recovery_timeline
    
    def calculate_cost_benefit_ratio(self, investment: float, expected_damage_reduction: float) -> Dict[str, Any]:
        """
        Calculate cost-benefit ratio for climate investments
        
        Args:
            investment: Proposed investment amount
            expected_damage_reduction: Expected reduction in future damages
            
        Returns:
            Cost-benefit analysis
        """
        benefit_cost_ratio = expected_damage_reduction / investment if investment > 0 else 0
        
        analysis = {
            "investment": investment,
            "expected_benefits": expected_damage_reduction,
            "benefit_cost_ratio": benefit_cost_ratio,
            "net_present_value": expected_damage_reduction - investment,
            "recommendation": "Proceed" if benefit_cost_ratio > 1.0 else "Reconsider"
        }
        
        return analysis
    
    def assess_sector_vulnerability(self, data: pd.DataFrame) -> Dict[str, Any]:
        """
        Assess economic vulnerability by sector
        
        Args:
            data: Economic and damage data by sector
            
        Returns:
            Sector vulnerability assessment
        """
        vulnerability = {
            "high_risk_sectors": [],
            "medium_risk_sectors": [],
            "low_risk_sectors": []
        }
        
        if 'event_type' in data.columns and 'damage_cost' in data.columns:
            sector_damages = data.groupby('event_type')['damage_cost'].sum().sort_values(ascending=False)
            total_damage = sector_damages.sum()
            
            for sector, damage in sector_damages.items():
                percentage = (damage / total_damage * 100) if total_damage > 0 else 0
                
                sector_info = {
                    "sector": sector,
                    "total_damage": float(damage),
                    "percentage_of_total": float(percentage)
                }
                
                if percentage > 30:
                    vulnerability["high_risk_sectors"].append(sector_info)
                elif percentage > 15:
                    vulnerability["medium_risk_sectors"].append(sector_info)
                else:
                    vulnerability["low_risk_sectors"].append(sector_info)
        
        return vulnerability
    
    def get_agent(self) -> autogen.AssistantAgent:
        """Return the AutoGen agent instance"""
        return self.agent