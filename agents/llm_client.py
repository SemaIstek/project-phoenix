from openai import AzureOpenAI
from typing import Dict, Any, List
import os

class AzureOpenAIClient:
    """Azure OpenAI client for AI agents"""
    
    def __init__(self):
        self.client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-06-01"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
        )
        self.deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4o-mini")
    
    def generate_completion(
        self, 
        system_message: str, 
        user_message: str,
        temperature: float = 0.7,
        max_tokens: int = 1500
    ) -> str:
        """
        Generate completion using Azure OpenAI
        
        Args:
            system_message: Agent role/instructions
            user_message: User query with data
            temperature: Creativity (0-1)
            max_tokens: Response length
            
        Returns:
            Generated text
        """
        try:
            response = self.client.chat.completions.create(
                model=self.deployment,
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": user_message}
                ],
                temperature=temperature,
                max_tokens=max_tokens
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            print(f"❌ Azure OpenAI Error: {e}")
            return f"Error generating AI response: {str(e)}"
    
    def generate_structured_analysis(
        self,
        system_message: str,
        data_summary: Dict[str, Any],
        analysis_type: str
    ) -> str:
        """
        Generate structured analysis with data context
        
        Args:
            system_message: Agent instructions
            data_summary: Dict with key statistics
            analysis_type: Type of analysis (risk, recovery, policy)
            
        Returns:
            AI-generated analysis
        """
        # Format data as text for LLM
        data_text = "\n".join([f"- {k}: {v}" for k, v in data_summary.items()])
        
        user_message = f"""
{analysis_type.upper()} ANALYSIS REQUEST

Data Summary:
{data_text}

Please provide a detailed {analysis_type} analysis based on this data.
"""
        
        return self.generate_completion(system_message, user_message)