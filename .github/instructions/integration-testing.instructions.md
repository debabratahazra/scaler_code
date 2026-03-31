# Integration Testing Instructions

## Purpose
Define standards for integration tests that verify multiple components work correctly together as a full pipeline. Integration tests sit above unit tests in the testing pyramid and validate end-to-end data flow.

---

## 🎯 Integration Testing Principles

- Test **interactions between components**, not individual functions
- Use **real (sample) data** — not mocks — wherever feasible
- Integration tests may be **slower** than unit tests (acceptable: < 60 seconds)
- Tests must be **idempotent** — running them multiple times produces the same result
- **Clean up** any files, DB entries, or artifacts created during the test

---

## 📁 File & Folder Structure

```
project/
├── src/
│   ├── ingest.py
│   ├── preprocess.py
│   ├── features.py
│   ├── train.py
│   └── evaluate.py
└── tests/
    ├── integration/
    │   ├── conftest.py              # Integration fixtures and setup
    │   ├── test_pipeline_e2e.py     # Full end-to-end pipeline test
    │   ├── test_data_flow.py        # Data format passing between stages
    │   └── test_model_serving.py    # Prediction API integration
    └── data/
        └── sample_integration.csv   # Small sample dataset for tests
```

---

## 📋 Integration Test File Template

```python
"""
Integration tests for the full ML pipeline.

Tests verify that:
- Data flows correctly from ingestion → preprocessing → features → training → evaluation
- Each stage produces output in the format expected by the next stage
- The complete pipeline runs without errors on sample data
"""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path

from src.ingest import load_data
from src.preprocess import preprocess
from src.features import build_features
from src.train import train_model
from src.evaluate import evaluate_model

# ─────────────────────────────────────────────
# Fixtures
# ─────────────────────────────────────────────

SAMPLE_DATA_PATH = Path("tests/data/sample_integration.csv")

@pytest.fixture(scope="module")
def raw_data() -> pd.DataFrame:
    """Load the sample dataset once for all integration tests."""
    return load_data(str(SAMPLE_DATA_PATH))

@pytest.fixture(scope="module")
def processed_data(raw_data) -> pd.DataFrame:
    """Preprocess the raw sample data."""
    return preprocess(raw_data)

@pytest.fixture(scope="module")
def feature_data(processed_data) -> pd.DataFrame:
    """Apply feature engineering to processed data."""
    return build_features(processed_data)

@pytest.fixture(scope="module")
def trained_model(feature_data):
    """Train a model on the feature data."""
    X = feature_data.drop(columns=["target"])
    y = feature_data["target"]
    X_train, y_train = X.iloc[:80], y.iloc[:80]
    return train_model(X_train, y_train, params={"n_estimators": 10, "random_state": 42})


# ─────────────────────────────────────────────
# Stage Handoff Tests
# ─────────────────────────────────────────────

def test_ingest_output_is_dataframe(raw_data):
    """Verify ingestion returns a non-empty DataFrame."""
    assert isinstance(raw_data, pd.DataFrame)
    assert len(raw_data) > 0

def test_preprocess_output_has_no_nulls(processed_data):
    """Verify preprocessing eliminates all null values."""
    assert processed_data.isnull().sum().sum() == 0

def test_preprocess_preserves_row_count(raw_data, processed_data):
    """Verify row count is preserved (no accidental drops)."""
    assert len(processed_data) == len(raw_data)

def test_features_output_contains_engineered_columns(feature_data):
    """Verify that expected engineered features are present."""
    assert "target" in feature_data.columns
    assert feature_data.shape[1] >= 5  # at least 5 feature columns

def test_features_output_has_correct_dtypes(feature_data):
    """Verify all feature columns are numeric after engineering."""
    non_numeric = feature_data.select_dtypes(exclude=[np.number]).columns.tolist()
    assert len(non_numeric) == 0, f"Non-numeric columns found: {non_numeric}"

def test_trained_model_has_predict_method(trained_model):
    """Verify the trained model exposes a predict interface."""
    assert hasattr(trained_model, "predict")
    assert callable(trained_model.predict)


# ─────────────────────────────────────────────
# End-to-End Pipeline Test
# ─────────────────────────────────────────────

def test_full_pipeline_runs_without_error():
    """
    Smoke test: run the complete pipeline from raw data to evaluation
    and verify it completes without raising an exception.
    """
    raw = load_data(str(SAMPLE_DATA_PATH))
    processed = preprocess(raw)
    features = build_features(processed)

    X = features.drop(columns=["target"])
    y = features["target"]
    split = int(len(X) * 0.8)
    X_train, X_test = X.iloc[:split], X.iloc[split:]
    y_train, y_test = y.iloc[:split], y.iloc[split:]

    model = train_model(X_train, y_train, params={"n_estimators": 10, "random_state": 42})
    metrics = evaluate_model(model, X_test, y_test)

    assert "accuracy" in metrics
    assert 0.0 <= metrics["accuracy"] <= 1.0

def test_full_pipeline_output_shape(feature_data, trained_model):
    """Verify prediction output has correct shape."""
    X_test = feature_data.drop(columns=["target"]).iloc[:20]
    predictions = trained_model.predict(X_test)
    assert len(predictions) == 20

def test_predictions_are_valid_classes(feature_data, trained_model):
    """Verify predictions only contain known class labels."""
    X_test = feature_data.drop(columns=["target"])
    y_true = feature_data["target"]
    predictions = trained_model.predict(X_test)
    valid_classes = set(y_true.unique())
    assert set(predictions).issubset(valid_classes)
```

---

## 🔬 Integration Test Categories

### 1. Pipeline Stage Handoff Tests
Verify the output of stage N is compatible with the input of stage N+1:
- Ingest → Preprocess: schema match
- Preprocess → Features: no nulls, correct dtypes
- Features → Train: numeric-only matrix, no infinity values
- Train → Evaluate: model has `predict` / `predict_proba`

### 2. End-to-End (E2E) Smoke Tests
Run the entire pipeline on a small representative dataset:
- Completes without unhandled exceptions
- Produces output artifacts (model file, metrics dict)
- Metrics are within a sane range

### 3. Data Contract Tests
Verify that data schemas are honored across module boundaries:
- Expected columns are present at each stage
- Dtypes are as expected
- Value ranges are within bounds (no negative ages, etc.)

### 4. Model Serving Tests (if applicable)
If a REST API serves predictions:
- `POST /predict` returns HTTP 200 with correct payload
- Invalid input returns HTTP 422 with meaningful error
- Response time < 2 seconds for single predictions

---

## 🧹 Setup & Teardown

```python
@pytest.fixture(scope="module", autouse=True)
def cleanup_artifacts():
    """Remove any model artifacts created during integration tests."""
    yield
    # Teardown: remove test outputs
    import shutil
    test_model_path = Path("models/test_model.pkl")
    if test_model_path.exists():
        test_model_path.unlink()
```

---

## 🚀 Running Integration Tests

```bash
# Run only integration tests
pytest tests/integration/ -v

# Run with timeout per test (60 seconds)
pytest tests/integration/ --timeout=60

# Run integration tests with coverage
pytest tests/integration/ --cov=src --cov-report=term-missing

# Run and generate HTML report
pytest tests/integration/ --html=reports/integration_report.html
```

---

## ✅ Integration Test Checklist (per feature)

- [ ] Sample data file created in `tests/data/`
- [ ] All pipeline stage handoff tests written
- [ ] Full E2E smoke test written
- [ ] Cleanup fixtures added for all test artifacts
- [ ] Tests pass on a fresh environment
- [ ] Test runtime < 60 seconds
- [ ] All tests are idempotent (re-runnable)

---

## ✅ Copilot Behavior for Integration Tests

- Generate integration tests **after** unit tests are passing
- Always include a full E2E smoke test that covers the entire pipeline
- Use `scope="module"` fixtures for expensive setup (e.g., training a model)
- Never hardcode file paths — use `pathlib.Path` relative to the project root
- Ensure cleanup fixtures remove all test artifacts after the test suite runs
