import argparse
import json
from compliance_rules import COMPLIANCE_RULES
from nlp_pipeline import extract_entities

def check_compliance(text: str):
    results = {"missing": [], "risky": []}
    
    # Check missing clauses
    for rule in COMPLIANCE_RULES["missing"]:
        if rule.lower() not in text.lower():
            results["missing"].append(rule)
    
    # Check risky terms
    for rule in COMPLIANCE_RULES["risky"]:
        if rule.lower() in text.lower():
            results["risky"].append(rule)
    
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, help="Path to contract/policy file")
    args = parser.parse_args()

    with open(args.file, "r") as f:
        text = f.read()
    
    entities = extract_entities(text)
    print(f"🔍 Detected entities: {entities}")

    results = check_compliance(text)
    print(json.dumps(results, indent=2))

    with open("data/flagged_output.json", "w") as out:
        json.dump(results, out, indent=2)
