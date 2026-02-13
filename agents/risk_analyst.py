    def _calculate_risk_level(self, total_damages: float, avg_damages: float) -> str:
        """Calculate risk level based on damage metrics
        
        Args:
            total_damages: Total damage cost
            avg_damages: Average damage cost
            
        Returns:
            Risk level string (LOW, MEDIUM, HIGH, CRITICAL)
        """
        if total_damages == 0:
            return "LOW"
        elif total_damages < 1_000_000_000:  # < 1 billion
            return "MEDIUM"
        elif total_damages < 5_000_000_000:  # < 5 billion
            return "HIGH"
        else:
            return "CRITICAL"

    def get_agent(self) -> autogen.AssistantAgent:
        """Return the AutoGen agent instance"""
        return self.agent
