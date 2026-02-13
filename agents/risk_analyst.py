"""
Risk Analyst Agent
Analyzes climate risk and economic damage data
"""

import pandas as pd
from typing import Dict, List, Any, Optional
import autogen
from .config import AgentConfig, RISK_ANALYST_SYSTEM_MESSAGE


class RiskAnalystAgent:
    """Risk Analyst Agent for climate damage analysis"""
    
    def __init__(self):
        """Initialize Risk Analyst Agent"""
        AgentConfig.validate_config()
        
        self.llm_config = AgentConfig.get_llm_config()
        
        # Create AutoGen assistant agent
        self.agent = autogen.AssistantAgent(
            name="RiskAnalyst",
            system_message=RISK_ANALYST_SYSTEM_MESSAGE,
            llm_config=self.llm_config,
        )
    
    def analyze_climate_data(self, data: pd.DataFrame) -> Dict[str, Any]:
        """
        Analyze climate damage data
        
        Args:
            data: DataFrame containing climate damage information
            
        Returns:
            Dictionary containing risk analysis results
        """
        # Calculate basic statistics
        total_damages = data['damage_cost'].sum() if 'damage_cost' in data.columns else 0
        avg_damages = data['damage_cost'].mean() if 'damage_cost' in data.columns else 0
        
        # Country-level analysis
        country_damages = {}
        if 'country' in data.columns and 'damage_cost' in data.columns:
            country_damages = data.groupby('country')['damage_cost'].sum().to_dict()
        
        analysis_result = {
            "total_damages": float(total_damages),
            "average_damages": float(avg_damages),
            "country_damages": country_damages,
            "data_points": len(data),
            "risk_level": self._calculate_risk_level(total_damages, avg_damages)
        }
        
        return analysis_result
    
    def calculate_co2_correlation(self, data: pd.DataFrame) -> Dict[str, Any]:
        """
        Calculate correlation between CO2 emissions and damages
        
        Args:
            data: DataFrame with CO2 and damage data
            
        Returns:
            Correlation analysis results
        """
        correlations = {}
        
        if 'co2_emissions' in data.columns and 'damage_cost' in data.columns:
            correlation = data['co2_emissions'].corr(data['damage_cost'])
            correlations['co2_damage_correlation'] = float(correlation)
        
        if 'gdp' in data.columns and 'damage_cost' in data.columns:
            correlation = data['gdp'].corr(data['damage_cost'])
            correlations['gdp_damage_correlation'] = float(correlation)
        
        return correlations
    
    def identify_high_risk_countries(self, data: pd.DataFrame, top_n: int = 5) -> List[Dict[str, Any]]:
        """
        Identify countries with highest climate risk
        
        Args:
            data: Climate damage data
            top_n: Number of top countries to return
            
        Returns:
            List of high-risk countries with metrics
        """
        if 'country' not in data.columns or 'damage_cost' not in data.columns:
            return []
        
        # Group by country and calculate metrics
        country_stats = data.groupby('country').agg({
            'damage_cost': ['sum', 'mean', 'count']
        }).reset_index()
        
        country_stats.columns = ['country', 'total_damage', 'avg_damage', 'incident_count']
        
        # Sort by total damage and get top N
        top_countries = country_stats.nlargest(top_n, 'total_damage')
        
        return top_countries.to_dict('records')
    
    def generate_risk_report(self, data: pd.DataFrame) -> str:
        """
        Generate a comprehensive risk analysis report
        
        Args:
            data: Climate damage data
            
        Returns:
            Formatted risk report string
        """
        analysis = self.analyze_climate_data(data)
        correlations = self.calculate_co2_correlation(data)
        high_risk = self.identify_high_risk_countries(data)
        
        report = f"""
=== CLIMATE RISK ANALYSIS REPORT ===

OVERVIEW:
- Total Climate Damages: ${analysis['total_damages']:,.2f}
- Average Damage per Incident: ${analysis['average_damages']:,.2f}
- Total Data Points Analyzed: {analysis['data_points']}
- Overall Risk Level: {analysis['risk_level']}

CORRELATION ANALYSIS:
"""
        
        if correlations:
            for key, value in correlations.items():
                report += f"- {key.replace('_', ' ').title()}: {value:.3f}\n"
        
        report += "\nHIGH-RISK COUNTRIES:\n"
        for idx, country in enumerate(high_risk, 1):
            report += f"{idx}. {country['country']}: ${country['total_damage']:,.2f} (Incidents: {country['incident_count']})\n"
        
        return report
    
    def _calculate_risk_level(self, total_damages: float, avg_damages: float) -> str:
        """
        Calculate overall risk level based on damage metrics
        
        Args:
            total_damages: Total damages
            avg_damages: Average damages
            
        Returns:
            Risk level string
        """
        if avg_damages > 1_000_000_000:  # > $1B average
            return "CRITICAL"
        elif avg_damages > 500_000_000:  # > $500M average
            return "HIGH"
        elif avg_damages > 100_000_000:  # > $100M average
            return "MEDIUM"
        else:
            return "LOW"
    
    def get_agent(self) -> autogen.AssistantAgent:
        """Return the AutoGen agent instance"""
        return self.agent
