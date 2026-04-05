# -----------------------------
# 1. Base image
# -----------------------------
FROM python:3.12-slim AS base

# Prevent Python from writing pyc files & buffering logs
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies (only if needed)
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# -----------------------------
# 2. Dependencies stage
# -----------------------------
FROM base AS deps

# Install app dependencies (better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# -----------------------------
# 3. Runtime stage
# -----------------------------
FROM python:3.12-slim AS runner

WORKDIR /app

# Copy dependencies
COPY --from=deps /usr/local /usr/local

# Copy app code
COPY . .

# Create non-root user
RUN useradd -m appuser
USER appuser

# Expose port
EXPOSE 80

# Healthcheck (FastAPI health endpoint recommended)
HEALTHCHECK CMD curl -f http://localhost:80/health || exit 1

  # Entry point: production server
ENTRYPOINT ["uvicorn"]

# Run app
CMD ["api.main:app", "--host", "0.0.0.0", "--port", "80", "--workers", "2"]
