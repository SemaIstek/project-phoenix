FROM python:3.11-slim

LABEL project="Project Phoenix"
LABEL description="AI-powered climate risk analysis with Azure OpenAI"

WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY agents/ ./agents/
COPY api/ ./api/
COPY frontend/ ./frontend/
COPY examples/ ./examples/

# Copy config files
COPY .env.example .env.example
COPY pyproject.toml pyproject.toml

# Create non-root user
RUN useradd -m -u 1000 phoenix && \
    chown -R phoenix:phoenix /app

USER phoenix

# Expose ports
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Run FastAPI
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
