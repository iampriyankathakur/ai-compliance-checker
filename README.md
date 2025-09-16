# 🧠 AI-Powered Compliance Checker

This tool scans contracts, policies, or business documents and **flags potential compliance issues**.  
It combines **rule-based checks** with **NLP models** to highlight missing clauses, risky terms, or data protection gaps.


## 🚀 Features
- Named Entity Recognition (NER) for clauses, obligations, and parties
- Rule-based detection of risky/missing terms (e.g., GDPR, confidentiality, liability)
- JSON export of flagged issues
- Easy to extend with custom compliance rules

## ⚙️ Installation
```bash
git clone https://github.com/yourusername/ai-compliance-checker.git
cd ai-compliance-checker
pip install -r requirements.txt
```
▶️ Usage
python src/checker.py --file data/sample_contract.txt

Output:
{
  "missing": ["GDPR clause", "Data retention policy"],
  "risky": ["unlimited liability", "automatic renewal"]
}


📊 Tech Stack

Python

NLP: spaCy, regex

Export: JSON / Streamlit (optional UI)

Testing: pytest

📌 Roadmap

 Add GDPR-specific rules

 Expand to healthcare (HIPAA) compliance

 Build Streamlit dashboard for contract upload

 
---

## requirements
spacy
regex
pandas
pytest

