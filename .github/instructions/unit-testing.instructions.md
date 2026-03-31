# Unit Testing Instructions

## Purpose
Define standards and patterns for writing thorough unit tests across all DS/ML modules. Unit tests verify individual functions in isolation and form the first safety net of the testing pyramid.

---

## 🎯 Unit Testing Principles

- Test **one thing** per test function — no multi-assertion sprawl
- Tests must be **fast** (< 1 second per test, no real I/O)
- Tests must be **isolated** — mock all external dependencies (DB, files, APIs)
- Tests must be **deterministic** — same input always produces same result
- Use **meaningful names**: `test_<function>_<scenario>_<expected_outcome>`

---

## 📁 File & Folder Structure

```
project/
├── src/
│   ├── preprocess.py
│   ├── features.py
│   ├── train.py
│   └── evaluate.py
└── tests/
    ├── conftest.py          # Shared fixtures
    ├── test_preprocess.py
    ├── test_features.py
    ├── test_train.py
    └── test_evaluate.py
```

---

## 📋 Test File Template

```python
"""
Unit tests for src/module_name.py

Tests cover:
- Happy path (normal inputs)
- Edge cases (empty data, nulls, single row)
- Error handling (invalid inputs, wrong dtypes)
"""

import pytest
import pandas as pd
import numpy as np
from src.module_name import function_to_test


# ─────────────────────────────────────────────
# Fixtures
# ─────────────────────────────────────────────

@pytest.fixture
def sample_df() -> pd.DataFrame:
    """Standard sample DataFrame for testing."""
    return pd.DataFrame({
        "age":      [25, 30, None, 45],
        "income":   [50000, 80000, 60000, None],
        "category": ["A", "B", "A", "C"],
        "target":   [1, 0, 1, 0]
    })

@pytest.fixture
def empty_df() -> pd.DataFrame:
    """Empty DataFrame with correct schema."""
    return pd.DataFrame(columns=["age", "income", "category", "target"])


# ─────────────────────────────────────────────
# Happy Path Tests
# ─────────────────────────────────────────────

def test_function_returns_dataframe(sample_df):
    """Test that function returns a DataFrame."""
    result = function_to_test(sample_df)
    assert isinstance(result, pd.DataFrame)

def test_function_expected_columns(sample_df):
    """Test that output contains expected columns."""
    result = function_to_test(sample_df)
    assert "age" in result.columns
    assert "income" in result.columns

def test_function_output_row_count(sample_df):
    """Test that output row count matches after processing."""
    result = function_to_test(sample_df)
    assert len(result) == len(sample_df)


# ─────────────────────────────────────────────
# Edge Case Tests
# ─────────────────────────────────────────────

def test_function_handles_empty_dataframe(empty_df):
    """Test that function handles an empty DataFrame gracefully."""
    result = function_to_test(empty_df)
    assert result.empty

def test_function_handles_all_nulls():
    """Test behavior when all values are NaN."""
    df = pd.DataFrame({"age": [None, None], "income": [None, None], "target": [1, 0]})
    result = function_to_test(df)
    assert result is not None

def test_function_single_row(sample_df):
    """Test function with only one row of data."""
    result = function_to_test(sample_df.iloc[:1])
    assert len(result) == 1


# ─────────────────────────────────────────────
# Error Handling Tests
# ─────────────────────────────────────────────

def test_function_raises_on_wrong_type():
    """Test that TypeError is raised for non-DataFrame input."""
    with pytest.raises(TypeError):
        function_to_test("not_a_dataframe")

def test_function_raises_on_missing_column():
    """Test that KeyError/ValueError is raised when required column is missing."""
    df = pd.DataFrame({"wrong_col": [1, 2, 3]})
    with pytest.raises((KeyError, ValueError)):
        function_to_test(df)


# ─────────────────────────────────────────────
# Parametrized Tests
# ─────────────────────────────────────────────

@pytest.mark.parametrize("input_val, expected", [
    (0.0,  "low"),
    (0.5,  "medium"),
    (0.9,  "high"),
    (1.0,  "high"),
])
def test_score_to_label(input_val, expected):
    """Test score-to-label mapping for various threshold values."""
    from src.evaluate import score_to_label
    assert score_to_label(input_val) == expected
```

---

## 🧪 What to Test for Each Module Type

### Preprocessing (`preprocess.py`)
- [ ] Null values are removed or imputed correctly
- [ ] Dtypes are cast correctly after processing
- [ ] No data leakage (train-set statistics not applied to test set)
- [ ] Output shape is consistent with input

### Feature Engineering (`features.py`)
- [ ] New features have correct values for known inputs
- [ ] No infinite or NaN values in engineered features
- [ ] Encoding produces expected number of columns
- [ ] Scaling produces values in expected range [0, 1] or [-1, 1]

### Model Training (`train.py`)
- [ ] Model is fitted without errors (smoke test)
- [ ] Fitted model has `predict` and `predict_proba` methods
- [ ] Model is saved to disk correctly (check file exists)
- [ ] Reproducibility: same seed produces same model

### Model Evaluation (`evaluate.py`)
- [ ] Metrics are within [0, 1] range for classification
- [ ] RMSE is non-negative for regression
- [ ] Confusion matrix dimensions match number of classes
- [ ] Perfect predictions return metric score of 1.0

### Data Ingestion (`ingest.py`)
- [ ] Correct number of rows loaded
- [ ] Schema matches expected columns
- [ ] FileNotFoundError is raised for missing files
- [ ] Encoding errors are handled

---

## 🔧 Mocking External Dependencies

```python
from unittest.mock import patch, MagicMock

def test_load_data_calls_read_csv():
    """Test that load_data calls pd.read_csv with correct path."""
    with patch("src.ingest.pd.read_csv") as mock_csv:
        mock_csv.return_value = pd.DataFrame({"a": [1, 2]})
        from src.ingest import load_data
        result = load_data("fake_path.csv")
        mock_csv.assert_called_once_with("fake_path.csv")
        assert len(result) == 2
```

---

## 🚀 Running Tests

```bash
# Run all tests
pytest tests/

# Run with verbose output
pytest tests/ -v

# Run a specific file
pytest tests/test_preprocess.py -v

# Run with coverage report
pytest tests/ --cov=src --cov-report=term-missing

# Run only tests matching a keyword
pytest tests/ -k "preprocess"
```

---

## 📊 Coverage Requirements

| Module | Minimum Coverage |
|---|---|
| `preprocess.py` | 90% |
| `features.py` | 85% |
| `train.py` | 80% |
| `evaluate.py` | 85% |
| `ingest.py` | 90% |

---

## ✅ Copilot Behavior for Unit Tests

- When implementing any function, **generate corresponding unit tests immediately**
- Always include happy path, edge case, and error handling tests
- Use `conftest.py` fixtures for shared test data — never repeat fixture code
- Name tests descriptively: `test_<function>_<scenario>_<expected>`
- Mock all file I/O, database calls, and external APIs
- Run `pytest` after every implementation to confirm green tests
