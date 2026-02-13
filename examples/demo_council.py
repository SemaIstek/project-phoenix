# Demo Script for Agent Council Initialization and Execution

import pandas as pd
from agent_council import AgentCouncil

# Sample climate data
sample_data = {
    'temperature': [22, 21, 19, 20, 23],
    'humidity': [0.55, 0.57, 0.60, 0.52, 0.58],
    'wind_speed': [5, 7, 6, 5, 4]
}

# Create a DataFrame from the sample climate data
climate_df = pd.DataFrame(sample_data)

# Initialize the Agent Council
council = AgentCouncil(data=climate_df)

# Run the Agent Council
results = council.run() 

# Display results
print('Agent Council Results:')
print(results)