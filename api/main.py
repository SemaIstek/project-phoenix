from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/analysis")
async def analyze():
    # Replace with your analysis logic
    return {"message": "Analysis endpoint"}

@app.get("/strategy")
async def strategy():
    # Replace with your strategy logic
    return {"message": "Strategy endpoint"}