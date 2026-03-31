# Feature Planning Instructions

## Purpose
Structure and document every new feature before a single line of code is written. Feature planning ensures alignment between business goals, technical design, and testing strategy.

---

## 📋 Feature Planning Document Structure

### 1. Feature Summary

| Field | Details |
|---|---|
| **Feature Name** | Short, descriptive name |
| **Feature ID** | `FEAT-<number>` (e.g., `FEAT-012`) |
| **Author** | Name of the feature owner |
| **Date Created** | YYYY-MM-DD |
| **Status** | `Draft` / `In Review` / `Approved` / `In Progress` / `Done` |
| **Priority** | `P0 - Critical` / `P1 - High` / `P2 - Medium` / `P3 - Low` |
| **Target Release** | Sprint or date |

---

### 2. Problem Statement
- What problem does this feature solve?
- Who is affected by this problem?
- What is the current workaround (if any)?
- What is the cost of NOT solving this? (business impact)

---

### 3. Goals & Success Criteria

**Goals:**
- [ ] Goal 1: e.g., Reduce model retraining time by 30%
- [ ] Goal 2: e.g., Support automated daily predictions

**Success Criteria (measurable):**
- Model accuracy ≥ 85% on test set
- Pipeline runs in < 10 minutes end-to-end
- Zero data leakage confirmed by validation checks

---

### 4. Out of Scope
Explicitly list what this feature will NOT cover to prevent scope creep:
- e.g., "Real-time streaming data is out of scope for this release"
- e.g., "Hyperparameter auto-tuning will be addressed in FEAT-015"

---

### 5. User Stories
Link to or embed user stories that this feature fulfills:
- `US-001`: As a data analyst, I want to...
- `US-002`: As a business manager, I want to...

> See `user-story-template.instructions.md` for user story format.

---

### 6. Technical Design

#### 6.1 Architecture Overview
- Link to architecture diagram: `docs/diagrams/<feature>_architecture.md`
- Brief description of components involved

#### 6.2 Data Requirements
| Dataset | Source | Format | Volume | Refresh Frequency |
|---|---|---|---|---|
| Customer transactions | DB / S3 / CSV | CSV | ~500K rows | Daily |
| Product catalog | Internal API | JSON | ~10K records | Weekly |

#### 6.3 Algorithm / Approach
- What algorithm or technique will be used?
- Why was this approach chosen over alternatives?
- Known trade-offs

#### 6.4 New Modules / Files to Create
| File | Purpose |
|---|---|
| `src/feature_name.py` | Main feature logic |
| `tests/test_feature_name.py` | Unit tests |
| `docs/user-guides/guide_feature_name.md` | User guide |

#### 6.5 Dependencies
- New Python libraries required (add to `requirements.txt`)
- External APIs or services
- Other features/modules this depends on

---

### 7. Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Data quality issues | High | High | Add validation step before processing |
| Model underperformance | Medium | High | Baseline comparison, fallback to rule-based logic |
| Pipeline timeout | Low | Medium | Add chunked processing for large datasets |

---

### 8. Milestones & Timeline

| Milestone | Target Date | Owner | Status |
|---|---|---|---|
| Architecture diagram approved | YYYY-MM-DD | | ⬜ |
| Data pipeline implemented | YYYY-MM-DD | | ⬜ |
| Model trained and validated | YYYY-MM-DD | | ⬜ |
| Unit tests passing | YYYY-MM-DD | | ⬜ |
| Integration tests passing | YYYY-MM-DD | | ⬜ |
| User guide written | YYYY-MM-DD | | ⬜ |
| Swagger docs updated | YYYY-MM-DD | | ⬜ |
| Feature deployed | YYYY-MM-DD | | ⬜ |

---

### 9. Testing Strategy
- Link to unit test file: `tests/test_<feature>.py`
- Link to integration test plan: `docs/tests/integration_<feature>.md`
- Edge cases to cover (list them explicitly)

---

### 10. Definition of Done (DoD)
A feature is considered DONE only when ALL of the following are true:

- [ ] Code is reviewed and merged to `dev` branch
- [ ] All unit tests pass (`pytest` with 0 failures)
- [ ] Integration tests pass end-to-end
- [ ] Architecture diagram created/updated
- [ ] Developer guide updated
- [ ] User guide written
- [ ] Swagger/API docs updated (if applicable)
- [ ] README updated
- [ ] No critical linting errors (`flake8` / `pylint`)
- [ ] Model metrics meet success criteria

---

## 📁 File Storage Convention

```
docs/
└── feature-plans/
    ├── FEAT-001_churn_prediction.md
    ├── FEAT-002_sales_forecasting.md
    └── FEAT-003_customer_segmentation.md
```

---

## ✅ Copilot Behavior for Feature Planning

- **Always generate a feature planning document before writing implementation code**
- Populate the "Definition of Done" checklist at feature start
- Cross-reference user stories, architecture diagrams, and test files in the plan
- Flag risks in the planning phase rather than discovering them during implementation
- Update the milestone table as tasks are completed
