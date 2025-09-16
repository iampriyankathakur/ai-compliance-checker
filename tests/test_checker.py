from src.checker import check_compliance

def test_check_compliance():
    sample_text = "This contract includes confidentiality but allows automatic renewal."
    results = check_compliance(sample_text)
    assert "GDPR" in results["missing"]
    assert "automatic renewal" in results["risky"]
