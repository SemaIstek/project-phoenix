"""
Climate Agent
Specialized agent for climate data analysis and pattern detection
"""

import pandas as pd
from typing import Dict, List, Any, Optional
import autogen
from .config import AgentConfig


CLIMATE_AGENT_SYSTEM_MESSAGE = """
You are a Climate Data Specialist Agent with expertise in climate science and environmental data analysis.

Your responsibilities:
1. Analyze climate patterns and trends over time
2. Identify correlations between climate events and geographic regions
3. Detect anomalies and extreme weather patterns
4. Assess climate change indicators (temperature, precipitation, sea level)
5. Provide insights on climate vulnerability by region

You work with meteorological data, satellite observations, and climate models.
Your analysis helps predict future climate risks and inform adaptation strategies.
"""


class ClimateAgent:
    """Climate Agent for climate data analysis"""
    
    def __init__(self):
        """Initialize Climate Agent"""
        AgentConfig.validate_config()
        
        self.llm_config = AgentConfig.get_llm_config()
        
        # Create AutoGen assistant agent
        self.agent = autogen.AssistantAgent(
            name="ClimateSpecialist",
            system_message=CLIMATE_AGENT_SYSTEM_MESSAGE,
            llm_config=self.llm_config,
        )
    
    def analyze_climate_trends(self, data: pd.DataFrame) -> Dict[str, Any]:
        """
        Analyze climate trends over time
        
        Args:
            data: DataFrame with climate data (temperature, precipitation, etc.)
            
        Returns:
            Climate trend analysis
        """
        results = {
            "trend_analysis": {},
            "anomalies": [],
            "risk_indicators": {}
        }
        
        # Temperature trend analysis
        if 'temperature' in data.columns and 'year' in data.columns:
            temp_trend = data.groupby('year')['temperature'].mean()
            results["trend_analysis"]["temperature"] = {
                "mean": float(temp_trend.mean()),
                "std": float(temp_trend.std()),
                "trend": "increasing" if temp_trend.iloc[-1] > temp_trend.iloc[0] else "decreasing"
            }
        
        # Precipitation analysis
        if 'precipitation' in data.columns:
            results["trend_analysis"]["precipitation"] = {
                "mean": float(data['precipitation'].mean()),
                "variability": float(data['precipitation'].std())
            }
        
        return results
    
    def detect_extreme_events(self, data: pd.DataFrame, threshold_percentile: float = 95) -> List[Dict[str, Any]]:
        """
        Detect extreme climate events
        
        Args:
            data: Climate data
            threshold_percentile: Percentile threshold for extreme events
            
        Returns:
            List of extreme events
        """
        extreme_events = []
        
        if 'damage_cost' in data.columns:
            threshold = data['damage_cost'].quantile(threshold_percentile / 100)
            extreme_data = data[data['damage_cost'] > threshold]
            
            for _, row in extreme_data.iterrows():
                event = {
                    "year": row.get('year', 'Unknown'),
                    "country": row.get('country', 'Unknown'),
                    "damage_cost": float(row['damage_cost']),
                    "event_type": row.get('event_type', 'Unknown')
                }
                extreme_events.append(event)
        
        return extreme_events
    
    def assess_regional_vulnerability(self, data: pd.DataFrame) -> Dict[str, Any]:
        """
        Assess climate vulnerability by region
        
        Args:
            data: Climate damage data with geographic information
            
        Returns:
            Regional vulnerability assessment
        """
        vulnerability = {}
        
        if 'country' in data.columns:
            # Calculate vulnerability metrics per country
            country_stats = data.groupby('country').agg({
                'damage_cost': ['sum', 'mean', 'count']
            }).reset_index()
            
            country_stats.columns = ['country', 'total_damage', 'avg_damage', 'event_count']
            
            # Calculate vulnerability score (normalized)
            max_damage = country_stats['total_damage'].max()
            if max_damage > 0:
                country_stats['vulnerability_score'] = (
                    country_stats['total_damage'] / max_damage * 100
                )
            
            vulnerability['countries'] = country_stats.to_dict('records')
        
        return vulnerability
    
    def predict_climate_risk(self, historical_data: pd.DataFrame, projection_years: int = 10) -> Dict[str, Any]:
        """
        Predict future climate risks based on historical trends
        
        Args:
            historical_data: Historical climate data
            projection_years: Number of years to project
            
        Returns:
            Climate risk projections
        """
        projections = {
            "projection_period": projection_years,
            "risk_trend": "increasing",
            "confidence_level": "medium",
            "key_risks": [
                "Increased frequency of extreme weather events",
                "Rising temperatures",
                "Changes in precipitation patterns"
            ]
        }
        
        # Calculate average annual increase in damages
        if 'year' in historical_data.columns and 'damage_cost' in historical_data.columns:
            yearly_damages = historical_data.groupby('year')['damage_cost'].sum()
            if len(yearly_damages) > 1:
                avg_increase = yearly_damages.pct_change().mean() * 100
                projections["avg_annual_increase"] = f"{avg_increase:.2f}%"
        
        return projections
    
    def get_agent(self) -> autogen.AssistantAgent:
        """Return the AutoGen agent instance"""
        return self.agent
