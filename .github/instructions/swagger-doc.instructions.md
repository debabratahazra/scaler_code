# Swagger / API Documentation Instructions

## Purpose
Generate consistent, complete OpenAPI/Swagger documentation for every REST API endpoint exposed by DS/ML models or data pipelines.

---

## 🎯 When to Write Swagger Docs

- When a model is served via a REST API (FastAPI, Flask, etc.)
- When a data pipeline exposes an HTTP endpoint
- When building any microservice in the ML system
- For every new or modified API endpoint

---

## 📋 OpenAPI Specification Template

Save as `docs/swagger/swagger.yaml`:

```yaml
openapi: 3.0.3
info:
  title: ML Model Prediction API
  description: |
    REST API for serving machine learning model predictions.
    Supports single and batch prediction requests.
  version: "1.0.0"
  contact:
    name: DS/ML Team
    email: team@example.com

servers:
  - url: http://localhost:8000
    description: Local development server
  - url: https://api.example.com/v1
    description: Production server

tags:
  - name: Health
    description: Service health and status endpoints
  - name: Predictions
    description: Model prediction endpoints
  - name: Data
    description: Data ingestion and management endpoints

paths:

  /health:
    get:
      tags: [Health]
      summary: Health check
      description: Returns the current health status of the API service.
      operationId: healthCheck
      responses:
        "200":
          description: Service is healthy
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/HealthResponse"
              example:
                status: "healthy"
                version: "1.0.0"
                timestamp: "2026-03-27T10:00:00Z"

  /predict:
    post:
      tags: [Predictions]
      summary: Single prediction
      description: |
        Submit a single record and receive a model prediction with confidence score.
        Input features must match the training schema exactly.
      operationId: predictSingle
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/PredictionRequest"
            example:
              customer_id: 10023
              age: 35
              income: 75000
              tenure_months: 24
              category: "Electronics"
      responses:
        "200":
          description: Prediction successful
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/PredictionResponse"
              example:
                customer_id: 10023
                prediction: 1
                label: "high_risk"
                confidence: 0.87
                model_version: "v2.1"
        "422":
          description: Validation error — missing or invalid input fields
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ValidationError"
        "500":
          description: Internal server error
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorResponse"

  /predict/batch:
    post:
      tags: [Predictions]
      summary: Batch predictions
      description: Submit multiple records in a single request. Maximum batch size is 1000 records.
      operationId: predictBatch
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required: [records]
              properties:
                records:
                  type: array
                  items:
                    $ref: "#/components/schemas/PredictionRequest"
                  minItems: 1
                  maxItems: 1000
      responses:
        "200":
          description: Batch predictions successful
          content:
            application/json:
              schema:
                type: object
                properties:
                  results:
                    type: array
                    items:
                      $ref: "#/components/schemas/PredictionResponse"
                  total_records: { type: integer }
                  processing_time_ms: { type: number }
        "413":
          description: Batch size exceeds maximum limit
        "422":
          description: Validation error

components:
  schemas:

    PredictionRequest:
      type: object
      required:
        - customer_id
        - age
        - income
        - tenure_months
      properties:
        customer_id:
          type: integer
          description: Unique customer identifier
          example: 10023
        age:
          type: integer
          description: Customer age in years
          minimum: 18
          maximum: 120
          example: 35
        income:
          type: number
          format: float
          description: Annual income in USD
          minimum: 0
          example: 75000.0
        tenure_months:
          type: integer
          description: Number of months as a customer
          minimum: 0
          example: 24
        category:
          type: string
          description: Product category (optional)
          enum: ["Electronics", "Apparel", "Food", "Other"]
          example: "Electronics"

    PredictionResponse:
      type: object
      properties:
        customer_id:
          type: integer
          example: 10023
        prediction:
          type: integer
          description: Raw class label (0 or 1)
          example: 1
        label:
          type: string
          description: Human-readable class label
          example: "high_risk"
        confidence:
          type: number
          format: float
          description: Model confidence score between 0 and 1
          minimum: 0.0
          maximum: 1.0
          example: 0.87
        model_version:
          type: string
          description: Version of the model used for prediction
          example: "v2.1"

    HealthResponse:
      type: object
      properties:
        status:
          type: string
          enum: ["healthy", "degraded", "unhealthy"]
        version:
          type: string
        timestamp:
          type: string
          format: date-time

    ValidationError:
      type: object
      properties:
        error:
          type: string
          example: "Validation failed"
        details:
          type: array
          items:
            type: object
            properties:
              field: { type: string }
              message: { type: string }

    ErrorResponse:
      type: object
      properties:
        error:
          type: string
          example: "Internal server error"
        message:
          type: string
        trace_id:
          type: string

  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
    BearerAuth:
      type: http
      scheme: bearer

security:
  - ApiKeyAuth: []
```

---

## 🐍 FastAPI Auto-Documentation Pattern

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, validator
from typing import Optional

app = FastAPI(
    title="ML Prediction API",
    description="Serves predictions from trained ML models",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

class PredictionRequest(BaseModel):
    customer_id: int = Field(..., description="Unique customer identifier", example=10023)
    age: int = Field(..., ge=18, le=120, description="Customer age", example=35)
    income: float = Field(..., ge=0, description="Annual income in USD", example=75000.0)
    tenure_months: int = Field(..., ge=0, description="Months as customer", example=24)
    category: Optional[str] = Field(None, description="Product category", example="Electronics")

    @validator("income")
    def income_must_be_positive(cls, v):
        if v < 0:
            raise ValueError("Income must be non-negative")
        return v

class PredictionResponse(BaseModel):
    customer_id: int
    prediction: int
    label: str
    confidence: float
    model_version: str

@app.post("/predict", response_model=PredictionResponse, tags=["Predictions"])
def predict(request: PredictionRequest):
    """
    Submit a single record for prediction.

    Returns the predicted class label and confidence score.
    """
    # ... model inference logic
    pass
```

---

## 📋 API Documentation Checklist (per endpoint)

- [ ] Endpoint path, method, and summary defined
- [ ] All request parameters documented with types and constraints
- [ ] All required fields marked as `required`
- [ ] Request body has a concrete `example`
- [ ] All response codes documented (200, 4xx, 500)
- [ ] Response schema defined with field descriptions
- [ ] Error response schemas are consistent
- [ ] Authentication method specified
- [ ] Rate limits documented in description (if applicable)

---

## 📁 File Storage Convention

```
docs/
└── swagger/
    ├── swagger.yaml            # Main OpenAPI spec
    ├── schemas/
    │   ├── request_models.yaml
    │   └── response_models.yaml
    └── examples/
        ├── predict_request.json
        └── predict_response.json
```

---

## ✅ Copilot Behavior for Swagger Docs

- When creating any API endpoint, **generate the OpenAPI spec entry immediately**
- Use Pydantic models in FastAPI to auto-generate docs — always add `Field` descriptions
- Include at least one `example` per request/response schema
- Document all possible error codes — never leave only 200 responses
- Validate the YAML spec using `swagger-cli validate docs/swagger/swagger.yaml`
- Link to Swagger UI from the project `README.md`
