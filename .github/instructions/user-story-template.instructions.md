# User Story Template Instructions

## Purpose
Standardize the format for writing user stories so every story captures the full context needed for implementation, testing, and acceptance — from a single source of truth.

---

## 📋 User Story Format

### Core Structure (Connextra Format)

```
As a [type of user],
I want to [perform some action],
So that [I achieve some goal/value].
```

---

## 📄 Full User Story Template

```markdown
---
# User Story: [US-XXX] Short Title

## Metadata
| Field | Value |
|---|---|
| **Story ID** | US-XXX |
| **Feature** | FEAT-XXX (link to feature planning doc) |
| **Author** | Name |
| **Created** | YYYY-MM-DD |
| **Status** | `Draft` / `Ready` / `In Progress` / `In Review` / `Done` |
| **Priority** | `P0` / `P1` / `P2` / `P3` |
| **Story Points** | (1 / 2 / 3 / 5 / 8 / 13) |
| **Sprint** | Sprint N |

---

## 📝 Story Statement

**As a** [data analyst / business manager / data scientist / ML engineer],
**I want to** [specific action or capability],
**So that** [business value or outcome].

---

## 🎯 Business Context

Explain the business motivation in 2–3 sentences:
- Why does this matter to the business?
- What decision or action does this enable?
- What is the cost of not having this?

---

## ✅ Acceptance Criteria

Acceptance criteria must be written in **Given / When / Then** format and be testable:

### AC-1: [Short Description]
- **Given** [a specific precondition or state]
- **When** [the user performs an action]
- **Then** [the expected observable outcome]

### AC-2: [Short Description]
- **Given** [precondition]
- **When** [action]
- **Then** [outcome]

### AC-3: Error Handling
- **Given** [invalid or missing input]
- **When** [the user submits the request]
- **Then** [a clear, meaningful error message is displayed]

### AC-4: Performance
- **Given** [a dataset of N records]
- **When** [the pipeline/feature is executed]
- **Then** [it completes within X seconds/minutes]

---

## 📐 Technical Notes

Provide implementation hints for the developer:
- Suggested algorithm or approach
- Known constraints or limitations
- Dependencies on other stories or modules
- Data schema assumptions
- Link to architecture diagram: `docs/diagrams/<feature>_architecture.md`

---

## 🔗 Dependencies

| Dependency | Type | Status |
|---|---|---|
| US-00X: Load raw dataset | Predecessor | ✅ Done |
| US-00Y: Feature engineering | Predecessor | 🔄 In Progress |
| FEAT-00Z: Model registry | Shared component | ✅ Available |

---

## 🧪 Testing Requirements

### Unit Tests Required
- [ ] Test: [function_name] handles empty input
- [ ] Test: [function_name] returns correct output for known input
- [ ] Test: [function_name] raises error for invalid input

### Integration Tests Required
- [ ] Test: End-to-end pipeline runs without error
- [ ] Test: Output schema matches downstream expectations

### Manual / UAT Tests Required
- [ ] Tester verifies output in notebook / dashboard
- [ ] Business stakeholder validates result interpretation

> See `tester-template.instructions.md` for the full test case format.

---

## 📎 Attachments & References

- [ ] Wireframe / mockup (if UI involved)
- [ ] Sample data file: `tests/data/sample_US_XXX.csv`
- [ ] Reference notebook: `notebooks/explore_<topic>.ipynb`
- [ ] Related Slack/Teams discussion (link)

---

## 📊 Definition of Done

This story is DONE when:
- [ ] Code is implemented and reviewed
- [ ] All acceptance criteria are verified
- [ ] Unit tests pass (0 failures)
- [ ] Integration test passes
- [ ] Developer guide updated
- [ ] User guide updated (if user-facing)
- [ ] Swagger docs updated (if API change)
- [ ] README updated (if applicable)
- [ ] Story demoed to stakeholder
- [ ] Status updated to `Done`
```

---

## 📋 Acceptance Criteria Writing Rules

- Each AC must be **independently testable**
- Use **concrete, measurable outcomes** ("returns a DataFrame with 5 columns", not "works correctly")
- Always include at least one **error/edge case AC**
- Always include at least one **performance AC** for pipeline-heavy stories
- Avoid implementation details in ACs — test *what*, not *how*

---

## 📏 Story Sizing Guide (Story Points)

| Points | Effort | Description |
|---|---|---|
| 1 | Trivial | Config change, minor fix, text update |
| 2 | Small | Simple function, existing pattern to follow |
| 3 | Medium | New module with tests and docs |
| 5 | Large | New pipeline stage, multiple components |
| 8 | Very Large | Complex feature, research needed |
| 13 | Extra Large | Too big — must be split into smaller stories |

---

## 📁 File Storage Convention

```
docs/
└── user-stories/
    ├── US-001_load_raw_data.md
    ├── US-002_preprocess_features.md
    ├── US-003_train_churn_model.md
    └── US-004_serve_predictions_api.md
```

---

## ✅ Copilot Behavior for User Stories

- When asked to implement a feature, **always generate or reference the user story first**
- Acceptance Criteria are the contract between product and engineering — implement to them exactly
- Map every AC to at least one unit test or integration test
- Use the story ID (e.g., `US-003`) as a comment reference in implementation code:
  ```python
  # US-003: Train churn prediction model
  def train_churn_model(X_train, y_train, params):
      ...
  ```
- Update story status in the metadata table as work progresses
