# FastAPI ML Service Template

A template for creating REST API services for machine learning models.

## Features

- RESTful API for model inference
- Request/response validation
- Async request handling
- API documentation (Swagger)
- Health checks and monitoring
- Docker containerization

## Setup

```bash
pip install fastapi uvicorn pydantic scikit-learn
```

## Usage

```bash
uvicorn main:app --reload
```

Visit `http://localhost:8000/docs` for API documentation.

## Structure

```
fastapi-ml-service/
├── main.py               # FastAPI application
├── models/               # Model artifacts
├── schemas/              # Request/response models
├── services/             # Business logic
├── tests/                # Unit tests
├── Dockerfile            # Container definition
├── requirements.txt      # Dependencies
└── README.md            # This file
```

## API Endpoints

- `POST /predict` - Model predictions
- `GET /health` - Health check
- `GET /model/info` - Model metadata

---
[← Back to Templates](../README.md)