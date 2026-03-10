# api/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
from agents.council import AgentCouncil
from typing import List, Dict, Any

app = FastAPI(
    title="Project Phoenix API",
    description="AI-powered climate risk analysis platform",
    version="1.0.0"
)

# CORS for Power BI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic Models
class ClimateDataPoint(BaseModel):
    country: str
    damage_cost: float
    co2_emissions: float
    gdp: float

class AnalysisRequest(BaseModel):
    data: List[ClimateDataPoint]

class AnalysisResponse(BaseModel):
    risk_analysis: Dict[str, Any]
    recovery_scenarios: List[Dict[str, Any]]
    policy_recommendations: List[Dict[str, Any]]
    summary: Dict[str, Any]

@app.get("/")
async def root():
    return {
        "service": "Project Phoenix API",
        "status": "operational",
        "version": "1.0.0"
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "azure_openai": "connected",
        "agents": "ready"
    }

@app.post("/api/v1/analyze", response_model=AnalysisResponse)
async def analyze_climate_risk(request: AnalysisRequest):
    """
    Analyze climate risk using AI Agent Council
    """
    try:
        # Convert to DataFrame
        df = pd.DataFrame([item.dict() for item in request.data])
        
        # Initialize Agent Council
        council = AgentCouncil()
        
        # Run analysis
        results = council.analyze_and_recommend(df)
        
        return AnalysisResponse(**results)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/agents")
async def list_agents():
    """List available AI agents"""
    return {
        "agents": [
            {"name": "Risk Analyst", "status": "active"},
            {"name": "Climate Specialist", "status": "active"},
            {"name": "Economic Analyst", "status": "active"},
            {"name": "Recovery Architect", "status": "active"},
            {"name": "Policy Strategist", "status": "active"},
            {"name": "Strategy Synthesis", "status": "active"}
        ]
    }