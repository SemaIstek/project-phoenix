"""
Agent Configuration Module
Centralized configuration for all AI agents with Ollama support
"""

import os
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()


class AgentConfig:
    """Configuration class for AI agents"""
    
    # Ollama Configuration
    USE_OLLAMA = os.getenv("USE_OLLAMA", "true").lower() == "true"
    OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:7b")
    
    # Azure OpenAI Configuration (fallback)
    AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT", "")
    AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY", "")
    AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4")
    AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")
    
    # Agent Settings
    MAX_ITERATIONS = int(os.getenv("MAX_AGENT_ITERATIONS", "10"))
    TIMEOUT = int(os.getenv("AGENT_TIMEOUT", "300"))
    TEMPERATURE = 0.7
    
    @classmethod
    def get_llm_config(cls) -> Dict[str, Any]:
        """Get LLM configuration for AutoGen agents"""
        if cls.USE_OLLAMA:
            # Ollama configuration
            return {
                "config_list": [
                    {
                        "model": cls.OLLAMA_MODEL,
                        "base_url": cls.OLLAMA_BASE_URL,
                        "api_key": "ollama",  # Dummy key for Ollama
                    }
                ],
                "temperature": cls.TEMPERATURE,
                "timeout": cls.TIMEOUT,
            }
        else:
            # Azure OpenAI configuration
            return {
                "config_list": [
                    {
                        "model": cls.AZURE_OPENAI_DEPLOYMENT,
                        "api_type": "azure",
                        "api_key": cls.AZURE_OPENAI_API_KEY,
                        "base_url": cls.AZURE_OPENAI_ENDPOINT,
                        "api_version": cls.AZURE_OPENAI_API_VERSION,
                    }
                ],
                "temperature": cls.TEMPERATURE,
                "timeout": cls.TIMEOUT,
            }
    
    @classmethod
    def validate_config(cls) -> bool:
        """Validate that required configuration is present"""
        if cls.USE_OLLAMA:
            # Check if Ollama is running
            import httpx
            try:
                response = httpx.get(cls.OLLAMA_BASE_URL.replace("/v1", ""), timeout=5)
                if response.status_code != 200:
                    raise ValueError("Ollama is not responding properly")
                print(f"✅ Ollama is running! Using model: {cls.OLLAMA_MODEL}")
                return True
            except Exception as e:
                raise ValueError(f"❌ Ollama is not running! Start it with: ollama serve\nError: {e}")
        else:
            # Validate Azure OpenAI
            if not cls.AZURE_OPENAI_API_KEY:
                raise ValueError("AZURE_OPENAI_API_KEY is not set")
            if not cls.AZURE_OPENAI_ENDPOINT:
                raise ValueError("AZURE_OPENAI_ENDPOINT is not set")
            return True


# Agent System Messages
RISK_ANALYST_SYSTEM_MESSAGE = """
You are a Risk Analyst Agent specializing in climate risk and economic damage analysis.

Your responsibilities:
1. Analyze historical climate damage data
2. Identify correlations between CO2 emissions, GDP, and climate damages
3. Calculate risk scores for countries and regions
4. Identify high-risk sectors and vulnerabilities
5. Provide data-driven insights on climate financial risks

You work with structured data and produce quantitative risk assessments.
Always base your analysis on concrete data and statistical evidence.
"""

RECOVERY_ARCHITECT_SYSTEM_MESSAGE = """
You are a Recovery Architect Agent specializing in climate resilience and economic recovery planning.

Your responsibilities:
1. Generate climate resilience scenarios based on risk analysis
2. Model economic recovery pathways for climate-impacted regions
3. Simulate intervention outcomes and their financial implications
4. Design adaptive strategies for different risk levels
5. Create actionable recovery frameworks

You transform risk data into concrete recovery scenarios and pathways.
Think creatively but remain grounded in economic and environmental realities.
"""

STRATEGY_AGENT_SYSTEM_MESSAGE = """
You are a Strategy Agent specializing in policy recommendations and financial allocation.

Your responsibilities:
1. Synthesize insights from Risk Analyst and Recovery Architect
2. Create actionable policy recommendations for governments and institutions
3. Generate financial allocation strategies and investment priorities
4. Develop implementation roadmaps with clear milestones
5. Provide executive summaries for decision-makers

You are the final decision-making layer that produces clear, actionable strategies.
Your recommendations should be practical, evidence-based, and ready for implementation.
"""