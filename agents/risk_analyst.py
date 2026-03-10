import pandas as pd
from typing import Dict, Any
from .llm_client import AzureOpenAIClient
from .config import RISK_ANALYST_SYSTEM_MESSAGE

class RiskAnalystAgent:
    """Risk Analyst Agent with Azure OpenAI integration"""
    
    def __init__(self):
        self.llm = AzureOpenAIClient()
        self.system_message = RISK_ANALYST_SYSTEM_MESSAGE
    
    def analyze_climate_data(self, df: pd.DataFrame) -> Dict[str, Any]:
        """
        Analyze climate damage data with AI-powered insights
        
        Returns:
            Dictionary with:
            - Statistical analysis (Python calculations)
            - AI-generated insights (Azure OpenAI)
            - Risk assessment
            - High-risk countries
        """
        # 1. STATISTICAL ANALYSIS (Python)
        total_damages = float(df['damage_cost'].sum())
        avg_damage = float(df['damage_cost'].mean())
        total_co2 = float(df['co2_emissions'].sum())
        avg_gdp = float(df['gdp'].mean())
        
        # Calculate correlations
        if len(df) > 1:
            co2_damage_corr = df['co2_emissions'].corr(df['damage_cost'])
            gdp_damage_corr = df['gdp'].corr(df['damage_cost'])
        else:
            co2_damage_corr = 0
            gdp_damage_corr = 0
        
        # Risk level (rule-based)
        if total_damages > 5000000:
            risk_level = "EXTREME"
        elif total_damages > 2000000:
            risk_level = "HIGH"
        elif total_damages > 1000000:
            risk_level = "MEDIUM"
        else:
            risk_level = "LOW"
        
        # High-risk countries
        country_damages = df.groupby('country').agg({
            'damage_cost': ['sum', 'mean', 'count']
        }).reset_index()
        country_damages.columns = ['country', 'total_damage', 'avg_damage', 'incident_count']
        country_damages = country_damages.sort_values('total_damage', ascending=False)
        
        high_risk_countries = country_damages.head(5).to_dict('records')
        
        # 2. AI-POWERED INSIGHTS (Azure OpenAI) 🤖
        data_summary = {
            "Total Climate Damages": f"${total_damages:,.0f}",
            "Average Damage per Event": f"${avg_damage:,.0f}",
            "Total CO2 Emissions": f"{total_co2:,.0f} tons",
            "Average GDP": f"${avg_gdp:,.0f}",
            "CO2-Damage Correlation": f"{co2_damage_corr:.3f}",
            "GDP-Damage Correlation": f"{gdp_damage_corr:.3f}",
            "Risk Level": risk_level,
            "Countries Analyzed": len(df['country'].unique()),
            "Top Risk Country": high_risk_countries[0]['country'] if high_risk_countries else "N/A"
        }
        
        # Generate AI insights
        ai_insights = self.llm.generate_structured_analysis(
            system_message=self.system_message,
            data_summary=data_summary,
            analysis_type="Climate Risk"
        )
        
        # 3. RETURN COMBINED RESULTS
        return {
            "total_damages": total_damages,
            "average_damage": avg_damage,
            "risk_level": risk_level,
            "high_risk_countries": high_risk_countries,
            "correlations": {
                "co2_damage_correlation": float(co2_damage_corr),
                "gdp_damage_correlation": float(gdp_damage_corr)
            },
            "statistics": {
                "total_co2": total_co2,
                "average_gdp": avg_gdp,
                "countries_analyzed": len(df['country'].unique()),
                "total_incidents": len(df)
            },
            # 🤖 AI-GENERATED INSIGHTS
            "ai_insights": ai_insights,
            "insights_generated_by": "Azure OpenAI (gpt-4o-mini)"
        }