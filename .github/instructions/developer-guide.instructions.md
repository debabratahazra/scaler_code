# Developer Guide Instructions

## Purpose
Provide a comprehensive developer guide for every feature or module. This ensures any developer (or future-you) can understand, set up, extend, and debug the codebase without prior context.

---

## 📋 Developer Guide Structure

Every developer guide must contain the following sections in order:

### 1. Overview
- What the module/feature does
- Why it exists (business/technical motivation)
- Where it fits in the overall system architecture

### 2. Prerequisites
- Python version required
- Required libraries and versions
- Environment variables needed
- External service access (APIs, databases, cloud)

### 3. Project Structure
```
feature_name/
├── data/               # Raw and processed datasets
├── notebooks/          # Exploration and prototyping notebooks
├── src/                # Source code modules
│   ├── __init__.py
│   ├── ingest.py       # Data loading logic
│   ├── preprocess.py   # Cleaning and transformation
│   ├── features.py     # Feature engineering
│   ├── train.py        # Model training
│   └── evaluate.py     # Model evaluation
├── tests/              # Unit and integration tests
├── models/             # Saved model artifacts
├── docs/               # Documentation and diagrams
├── config.yaml         # Configuration file
├── requirements.txt    # Pinned dependencies
└── README.md
```

### 4. Setup & Installation
```bash
# Clone the repo or navigate to the folder
cd feature_name/

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 5. Configuration
- Describe every key in `config.yaml` or `.env`
- Example:
```yaml
data:
  raw_path: data/raw/dataset_v1.csv
  processed_path: data/processed/

model:
  algorithm: random_forest
  n_estimators: 100
  max_depth: 10
  random_state: 42

evaluation:
  metric: f1_score
  threshold: 0.80
```

### 6. Running the Pipeline
```bash
# Step 1: Ingest data
python src/ingest.py

# Step 2: Preprocess
python src/preprocess.py

# Step 3: Train model
python src/train.py --config config.yaml

# Step 4: Evaluate
python src/evaluate.py
```

### 7. Module Reference

For every module (`src/*.py`), document:
- **Purpose** — one-line description
- **Key Functions** — name, inputs, outputs, side effects
- **Dependencies** — what it imports and why

### 8. Coding Standards
- Follow **PEP 8** style guide
- Max line length: **100 characters**
- Use **type hints** on all public functions
- Write **NumPy-style docstrings**
- No magic numbers — define constants at module level
- No hardcoded paths — use `pathlib.Path` or `config.yaml`

### 9. Error Handling Pattern
```python
import logging

logger = logging.getLogger(__name__)

def load_data(path: str) -> pd.DataFrame:
    """Load dataset from given path."""
    try:
        df = pd.read_csv(path)
        logger.info(f"Loaded {len(df)} rows from {path}")
        return df
    except FileNotFoundError:
        logger.error(f"File not found: {path}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error loading data: {e}")
        raise
```

### 10. Logging Standards
- Use Python's built-in `logging` module (not `print` in production code)
- Log levels: `DEBUG` for dev, `INFO` for pipeline steps, `WARNING` for recoverable issues, `ERROR` for failures
- Log format: `[LEVEL] [module_name] message`

### 11. Branching & Version Control
- `main` — stable, production-ready code
- `dev` — integration branch
- `feature/<feature-name>` — individual feature branches
- Commit message format: `[TYPE] short description`
  - Types: `feat`, `fix`, `docs`, `test`, `refactor`, `chore`

### 12. Known Issues & Limitations
- List any known bugs, edge cases, or technical debt
- Include workarounds where applicable

### 13. Troubleshooting
| Problem | Likely Cause | Solution |
|---|---|---|
| `ModuleNotFoundError` | Env not activated or package not installed | Activate venv, run `pip install -r requirements.txt` |
| `FileNotFoundError` | Wrong path in config | Check `config.yaml` paths |
| Model accuracy too low | Data leakage or wrong features | Review feature engineering step |
| `KeyError` on DataFrame | Column name mismatch | Run `df.columns` to verify |

---

## ✅ Copilot Behavior for Developer Guide

- When creating a new module or feature, **auto-generate the developer guide skeleton** above
- Always link to the architecture diagram from the developer guide
- Keep the developer guide updated whenever a function signature or config key changes
- Reference the developer guide in PR descriptions
