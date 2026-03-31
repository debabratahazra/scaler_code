# GitHub Copilot Instructions

## Overview
These instructions guide GitHub Copilot when implementing new features, exploring ideas, writing tests, and creating documentation in this Data Science & ML workspace.

---

## 📚 Detailed Instruction Files

Each aspect of the development lifecycle has a dedicated instruction file. Copilot must follow the relevant file for every task:

| Instruction File | When to Use |
|---|---|
| [`instructions/feature-planning.instructions.md`](instructions/feature-planning.instructions.md) | Before writing any code — plan the feature end-to-end |
| [`instructions/user-story-template.instructions.md`](instructions/user-story-template.instructions.md) | Writing or implementing a user story |
| [`instructions/architecture-diagram.instructions.md`](instructions/architecture-diagram.instructions.md) | Designing system/pipeline architecture |
| [`instructions/developer-guide.instructions.md`](instructions/developer-guide.instructions.md) | Creating module/feature developer documentation |
| [`instructions/user-guide.instructions.md`](instructions/user-guide.instructions.md) | Writing end-user documentation |
| [`instructions/unit-testing.instructions.md`](instructions/unit-testing.instructions.md) | Writing unit tests with `pytest` |
| [`instructions/integration-testing.instructions.md`](instructions/integration-testing.instructions.md) | Writing end-to-end integration tests |
| [`instructions/tester-template.instructions.md`](instructions/tester-template.instructions.md) | Creating test plans, test cases, and bug reports |
| [`instructions/swagger-doc.instructions.md`](instructions/swagger-doc.instructions.md) | Documenting REST API endpoints (OpenAPI/Swagger) |
| [`instructions/readme.instructions.md`](instructions/readme.instructions.md) | Writing project/module `README.md` files |

---

## 🔄 End-to-End User Story Workflow

For every user story, follow this sequence — Copilot must complete **all** steps:

```
1. 📋 Feature Planning      →  feature-planning.instructions.md
2. 📖 User Story            →  user-story-template.instructions.md
3. 📐 Architecture Diagram  →  architecture-diagram.instructions.md
4. 🚀 Implementation        →  (General Principles below)
5. 🧪 Unit Tests            →  unit-testing.instructions.md
6. 🔬 Integration Tests     →  integration-testing.instructions.md
7. 📡 Swagger Docs          →  swagger-doc.instructions.md  (if API)
8. 👩‍💻 Developer Guide       →  developer-guide.instructions.md
9. 👤 User Guide            →  user-guide.instructions.md
10. 🧑‍🔬 Tester Template      →  tester-template.instructions.md
11. 📄 README Update        →  readme.instructions.md
```

> A feature is **DONE** only when all 11 steps are complete.

---

## 🚀 Implementing New Features

### General Principles
- Follow **modular design**: each feature should be a self-contained function or class.
- Prefer **readable code over clever code** — use descriptive variable names.
- Add **type hints** to all function signatures.
- Use **docstrings** for every function and class (NumPy or Google style).
- Keep functions **small and focused** (single responsibility principle).

### Data Science / ML Features
- Always **validate inputs** (check for nulls, shape mismatches, correct dtypes).
- Use **`pandas`** for tabular data manipulation; prefer **`numpy`** for numerical ops.
- For ML models, wrap training logic in a function that accepts `X_train`, `y_train` and returns a fitted model.
- Save models using **`joblib`** or **`pickle`** with versioned filenames (e.g., `model_v1.pkl`).
- Log key metrics (accuracy, RMSE, etc.) using **`print`** or **`logging`** after training.

### Example Pattern — New Feature
```python
def train_model(X_train: pd.DataFrame, y_train: pd.Series, params: dict) -> Any:
    """
    Train a model with given parameters.

    Parameters
    ----------
    X_train : pd.DataFrame
        Training features.
    y_train : pd.Series
        Target variable.
    params : dict
        Hyperparameters for the model.

    Returns
    -------
    model : fitted model object
    """
    model = SomeModel(**params)
    model.fit(X_train, y_train)
    return model
```

---

## 💡 Exploring New Ideas

### Notebook Exploration Guidelines
- Create a **new `.ipynb` notebook** per idea/experiment — name it clearly:
  - `explore_<topic>_<date>.ipynb` (e.g., `explore_clustering_2026-03-25.ipynb`)
- Start every exploration notebook with a **Markdown cell** describing:
  - The idea or hypothesis being explored
  - Expected outcome
  - Dataset being used
- Use **`matplotlib`** or **`seaborn`** for quick plots; use **`plotly`** for interactive ones.
- At the end of the notebook, add a **"Findings & Next Steps"** Markdown cell.

### Idea Prototyping Checklist
- [ ] Define the problem or idea clearly
- [ ] Load and inspect the data (`df.head()`, `df.info()`, `df.describe()`)
- [ ] Build a minimal proof-of-concept
- [ ] Visualize results
- [ ] Note limitations and improvements

---

## 🧪 Writing Tests

### Testing Standards
- Use **`pytest`** for all unit tests.
- Place test files in a `tests/` folder alongside the module being tested.
- Name test files as `test_<module_name>.py`.
- Each test function must start with `test_`.

### What to Test in DS/ML Code
- Data loading and preprocessing functions
- Feature engineering transformations
- Model training pipeline (smoke test with small dummy data)
- Prediction output shape and dtype
- Edge cases: empty DataFrames, single-row inputs, NaN-heavy data

### Example Test Pattern
```python
import pytest
import pandas as pd
from your_module import preprocess_data

def test_preprocess_removes_nulls():
    """Test that preprocessing drops rows with null values."""
    df = pd.DataFrame({"feature": [1, None, 3], "target": [0, 1, 0]})
    result = preprocess_data(df)
    assert result.isnull().sum().sum() == 0

def test_preprocess_output_shape():
    """Test that output has expected number of columns."""
    df = pd.DataFrame({"feature": [1, 2, 3], "target": [0, 1, 0]})
    result = preprocess_data(df)
    assert result.shape[1] == 2
```

### Test Conventions
- Use **fixtures** for repeated setup (e.g., sample DataFrames).
- Keep tests **independent** — no test should depend on another.
- Use `pytest.mark.parametrize` for testing multiple input/output pairs.

---

## 📄 Writing Documentation

### Code Documentation
- Every **module** should have a top-level docstring explaining its purpose.
- Every **function/method** should have a docstring with:
  - Short description
  - `Parameters` section
  - `Returns` section
  - `Raises` section (if applicable)
  - `Examples` section (optional but preferred)
- Use **NumPy docstring format** (consistent with `pandas`, `sklearn` style).

### Notebook Documentation
- Each notebook should have:
  - A **title cell** (H1 Markdown) with the topic
  - A **context/objective cell** explaining the goal
  - **Section headers** (H2/H3) between logical steps
  - **Inline comments** in code cells for non-obvious logic
  - A **Conclusion / Summary** cell at the end

### README Guidelines
- Every project folder should have a `README.md` with:
  - **Project title and description**
  - **Folder structure** overview
  - **How to run** instructions
  - **Dependencies** (or link to `requirements.txt`)
  - **Key results / findings**

### Example Docstring (NumPy Style)
```python
def evaluate_model(model, X_test: pd.DataFrame, y_test: pd.Series) -> dict:
    """
    Evaluate a trained model on test data.

    Parameters
    ----------
    model : estimator object
        A fitted sklearn-compatible model.
    X_test : pd.DataFrame
        Test features.
    y_test : pd.Series
        True target values.

    Returns
    -------
    metrics : dict
        Dictionary containing 'accuracy', 'precision', 'recall', 'f1'.

    Examples
    --------
    >>> metrics = evaluate_model(clf, X_test, y_test)
    >>> print(metrics['f1'])
    0.87
    """
```

---

## 🗂️ File & Folder Conventions

| Type | Naming Convention | Example |
|------|-------------------|---------|
| Notebook | `<topic>_<number>.ipynb` | `linear_regression_03.ipynb` |
| Script | `<action>_<topic>.py` | `train_classifier.py` |
| Dataset | `<name>_<version>.csv` | `sales_data_v2.csv` |
| Model file | `<model>_v<n>.pkl` | `rf_model_v1.pkl` |
| Test file | `test_<module>.py` | `test_preprocessing.py` |
| Config | `config.yaml` or `config.json` | `config.yaml` |

---

## 🔧 Environment & Dependencies

- Use **Python 3.9+**
- Preferred libraries:
  - Data: `pandas`, `numpy`
  - Viz: `matplotlib`, `seaborn`, `plotly`
  - ML: `scikit-learn`, `xgboost`, `lightgbm`
  - DL: `tensorflow` or `pytorch`
  - NLP: `nltk`, `spacy`, `transformers`
  - Testing: `pytest`
- Always **pin versions** in `requirements.txt` for reproducibility.

---

## ✅ Copilot Behavior Reminders

- **Do not hardcode file paths** — use `os.path` or `pathlib.Path`.
- **Do not store credentials** in code — use environment variables or `.env` files.
- **Always handle exceptions** gracefully with meaningful error messages.
- **Prefer vectorized operations** over loops for DataFrame manipulation.
- When generating plots, always include **axis labels, title, and legend**.
- When unsure about data types, **assert or validate** before proceeding.
