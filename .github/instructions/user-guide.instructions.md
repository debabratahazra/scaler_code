# User Guide Instructions

## Purpose
Generate clear, non-technical user documentation for every feature or tool built in this DS/ML workspace. The user guide is written for end-users (analysts, business stakeholders, or data scientists using the output), not developers.

---

## 📋 User Guide Structure

Every user guide must contain the following sections:

### 1. Introduction
- What does this tool/feature do?
- Who is it for? (target audience)
- What problem does it solve?
- What does the user get as output?

### 2. Getting Started
- Step-by-step setup instructions (non-technical language)
- What the user needs before they start (data format, access, etc.)
- Screenshots or notebook cell references where applicable

### 3. How to Use
- Numbered, step-by-step walkthrough
- Include example inputs and expected outputs
- Use plain language — avoid jargon

### 4. Input Requirements

| Field | Type | Required | Description | Example |
|---|---|---|---|---|
| `customer_id` | Integer | Yes | Unique customer identifier | `10023` |
| `purchase_date` | Date (YYYY-MM-DD) | Yes | Date of transaction | `2026-03-25` |
| `amount` | Float | Yes | Purchase amount in USD | `149.99` |
| `category` | String | No | Product category | `Electronics` |

### 5. Output Description
- What does the output look like?
- What does each output column/field mean?
- Example output table or screenshot

### 6. Interpreting Results
- How to read the output (e.g., what does a score of 0.87 mean?)
- What actions to take based on the output
- Threshold explanations (e.g., "score > 0.7 means high churn risk")

### 7. Limitations
- What the tool cannot do
- Data quality requirements (e.g., "requires at least 6 months of history")
- Known edge cases that may affect results

### 8. FAQs

**Q: What if my data has missing values?**
A: The tool will automatically handle missing values using median imputation for numeric fields and "Unknown" for categorical fields. Rows with more than 50% missing data will be dropped.

**Q: How often should I re-run the model?**
A: It is recommended to re-run monthly or whenever the underlying data distribution changes significantly.

**Q: Can I use this with a different dataset format?**
A: Currently only `.csv` files with UTF-8 encoding are supported. Excel files must be exported to CSV first.

### 9. Glossary
| Term | Definition |
|---|---|
| **Prediction Score** | A probability between 0 and 1 indicating the likelihood of an event |
| **Feature** | An input variable used by the model to make a prediction |
| **Churn** | When a customer stops using a product or service |
| **RMSE** | Root Mean Square Error — a measure of prediction accuracy (lower is better) |

### 10. Support & Feedback
- Who to contact for issues or feature requests
- How to report incorrect predictions
- Link to the issue tracker or team channel

---

## 📝 User Guide Writing Style Rules

- Use **second person** ("You can...", "Click on...", "Enter your...")
- Use **active voice** ("The model predicts..." not "Predictions are made by...")
- Use **short sentences** — max 20 words per sentence
- Use **numbered lists** for steps, **bullet points** for options
- Include a **screenshot or example** for every major step
- Avoid acronyms without first spelling them out
- Use **bold** for UI elements, field names, and important terms

---

## 📁 File Storage Convention

```
docs/
└── user-guides/
    ├── guide_churn_prediction.md
    ├── guide_sales_forecasting.md
    └── guide_customer_segmentation.md
```

---

## ✅ Copilot Behavior for User Guide

- When a feature is complete, **auto-generate the user guide skeleton** above
- Write in plain, non-technical English
- Always include an "Input Requirements" table and "Interpreting Results" section
- Link the user guide from the project `README.md`
- Update the user guide when the feature's inputs, outputs, or behavior changes
