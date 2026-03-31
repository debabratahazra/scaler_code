# Tester Template Instructions

## Purpose
Provide a standardized test case template for QA/testers to document, execute, and track manual and automated test cases for every user story and feature.

---

## 📄 Test Plan Template

Save as `docs/tests/test_plan_<feature>.md`:

```markdown
---
# Test Plan: [Feature / Story Name]

## Metadata
| Field | Value |
|---|---|
| **Test Plan ID** | TP-XXX |
| **Feature** | FEAT-XXX |
| **User Story** | US-XXX |
| **Author** | Tester Name |
| **Created** | YYYY-MM-DD |
| **Last Updated** | YYYY-MM-DD |
| **Status** | `Draft` / `Active` / `Complete` |
| **Environment** | Local / Dev / Staging / Production |

---

## 🎯 Test Objectives
- Verify that [feature] behaves according to acceptance criteria in US-XXX
- Validate data quality and model output correctness
- Ensure error handling is robust for invalid inputs

---

## 📋 Test Scope

### In Scope
- [ ] Happy path: normal inputs produce expected outputs
- [ ] Edge cases: empty data, nulls, boundary values
- [ ] Error cases: invalid types, missing required fields
- [ ] Performance: pipeline completes within defined SLAs
- [ ] Integration: components work together end-to-end

### Out of Scope
- [ ] Load/stress testing (addressed in TP-XXX)
- [ ] UI testing (no UI in this story)

---

## 🔧 Test Environment Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/ -v

# Check coverage
pytest tests/ --cov=src --cov-report=term-missing
```

---

## 📋 Test Cases

### TC-001: [Happy Path — Standard Input]

| Field | Details |
|---|---|
| **Test Case ID** | TC-001 |
| **Story Reference** | US-XXX, AC-1 |
| **Test Type** | Unit / Integration / Manual |
| **Priority** | High |

**Preconditions:**
- Dataset `tests/data/sample_integration.csv` is present
- Dependencies installed via `requirements.txt`

**Test Steps:**
1. Load the sample dataset using `load_data("tests/data/sample_integration.csv")`
2. Run the preprocessing function: `preprocess(df)`
3. Verify the output DataFrame has no null values
4. Verify the output has the same number of rows as the input

**Expected Result:**
- Output is a `pd.DataFrame`
- `output.isnull().sum().sum() == 0`
- `len(output) == len(input)`

**Actual Result:** *(Fill in after test execution)*

**Status:** ⬜ Not Run / ✅ Pass / ❌ Fail / ⚠️ Blocked

**Notes:**

---

### TC-002: [Edge Case — Empty DataFrame]

| Field | Details |
|---|---|
| **Test Case ID** | TC-002 |
| **Story Reference** | US-XXX, AC-3 |
| **Test Type** | Unit |
| **Priority** | Medium |

**Preconditions:**
- An empty DataFrame with the correct schema is available

**Test Steps:**
1. Create empty DataFrame: `pd.DataFrame(columns=["age", "income", "target"])`
2. Call `preprocess(empty_df)`
3. Observe the return value

**Expected Result:**
- Function returns an empty DataFrame (does not raise an exception)
- `result.empty == True`

**Actual Result:**

**Status:** ⬜ Not Run / ✅ Pass / ❌ Fail / ⚠️ Blocked

**Notes:**

---

### TC-003: [Error Case — Missing Required Column]

| Field | Details |
|---|---|
| **Test Case ID** | TC-003 |
| **Story Reference** | US-XXX, AC-3 |
| **Test Type** | Unit |
| **Priority** | High |

**Preconditions:**
- DataFrame is missing a required column

**Test Steps:**
1. Create DataFrame with missing column: `pd.DataFrame({"wrong_col": [1, 2, 3]})`
2. Call `preprocess(df)` with this malformed input
3. Observe the exception raised

**Expected Result:**
- `ValueError` or `KeyError` is raised
- Error message clearly indicates which column is missing

**Actual Result:**

**Status:** ⬜ Not Run / ✅ Pass / ❌ Fail / ⚠️ Blocked

**Notes:**

---

### TC-004: [Performance — Pipeline Runtime]

| Field | Details |
|---|---|
| **Test Case ID** | TC-004 |
| **Story Reference** | US-XXX, AC-4 |
| **Test Type** | Performance |
| **Priority** | Medium |

**Preconditions:**
- Full dataset (50,000 rows) is available at `data/raw/dataset_v1.csv`

**Test Steps:**
1. Record start time
2. Run the full pipeline end-to-end on the full dataset
3. Record end time
4. Calculate total runtime

**Expected Result:**
- Pipeline completes in < 10 minutes
- No memory errors (peak RAM usage < 4GB)

**Actual Result:**

**Status:** ⬜ Not Run / ✅ Pass / ❌ Fail / ⚠️ Blocked

**Notes:**

---

### TC-005: [End-to-End Integration — Full Pipeline]

| Field | Details |
|---|---|
| **Test Case ID** | TC-005 |
| **Story Reference** | US-XXX, AC-1, AC-2 |
| **Test Type** | Integration / E2E |
| **Priority** | High |

**Preconditions:**
- All pipeline modules (`ingest`, `preprocess`, `features`, `train`, `evaluate`) are implemented
- Sample data is available

**Test Steps:**
1. Run `pytest tests/integration/test_pipeline_e2e.py -v`
2. Verify all test cases pass
3. Check model artifact saved to `models/` folder
4. Check metrics output is a dict with keys `accuracy`, `f1`, `roc_auc`

**Expected Result:**
- All integration tests pass (0 failures)
- Model file created at `models/model_v1.pkl`
- Metrics: `accuracy ≥ 0.80`, `f1 ≥ 0.78`

**Actual Result:**

**Status:** ⬜ Not Run / ✅ Pass / ❌ Fail / ⚠️ Blocked

**Notes:**
```

---

## 📊 Test Summary Report Template

```markdown
## Test Execution Summary

| Metric | Value |
|---|---|
| **Total Test Cases** | 15 |
| **Passed** | 13 ✅ |
| **Failed** | 1 ❌ |
| **Blocked** | 1 ⚠️ |
| **Not Run** | 0 |
| **Pass Rate** | 86.7% |
| **Test Run Date** | YYYY-MM-DD |
| **Tester** | Name |

## Failed Test Cases
| TC ID | Description | Defect ID | Severity |
|---|---|---|---|
| TC-003 | Missing column not raising error | BUG-042 | High |

## Blocked Test Cases
| TC ID | Description | Blocking Reason |
|---|---|---|
| TC-004 | Performance test | Full dataset not yet available |

## Recommendations
- BUG-042 must be resolved before release
- TC-004 to be re-run after dataset provisioning
- Story US-XXX is **NOT ready for release**
```

---

## 🐛 Bug Report Template

```markdown
## Bug Report: [BUG-XXX] Short Description

| Field | Value |
|---|---|
| **Bug ID** | BUG-XXX |
| **Test Case** | TC-XXX |
| **Severity** | Critical / High / Medium / Low |
| **Status** | Open / In Progress / Fixed / Closed |
| **Reporter** | Name |
| **Date Found** | YYYY-MM-DD |

### Description
Clear, concise description of the bug.

### Steps to Reproduce
1. Step 1
2. Step 2
3. Step 3

### Expected Behavior
What should have happened.

### Actual Behavior
What actually happened.

### Environment
- Python version: 3.x.x
- OS: Windows / Linux / macOS
- Relevant package versions

### Logs / Error Output
```
Paste stack trace or error output here
```

### Possible Fix
(Optional) Developer's suggested fix or root cause.
```

---

## 📁 File Storage Convention

```
docs/
└── tests/
    ├── test_plan_FEAT-001_churn.md
    ├── test_plan_FEAT-002_forecasting.md
    └── bug_reports/
        ├── BUG-001.md
        └── BUG-002.md
```

---

## ✅ Copilot Behavior for Tester Template

- When a user story is marked "In Progress", **generate the test plan automatically**
- Map every Acceptance Criterion to at least one test case (TC)
- Always include happy path, edge case, error case, and performance test cases
- After running `pytest`, populate the "Actual Result" and "Status" fields automatically
- Generate the Test Summary Report after all test cases have been executed
