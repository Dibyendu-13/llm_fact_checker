from extract_claim import extract_claim
from retrieve import retrieve_similar_fact
from compare_llm import get_verdict
import json

def fact_check(text):
    claim = extract_claim(text)
    retrieved = retrieve_similar_fact(claim)
    verdict = get_verdict(claim, retrieved)
    return verdict

if __name__ == "__main__":
    statement = input("Enter a statement to verify: ")
    result = fact_check(statement)
    print("\nRESULT:\n", result)

    with open("sample_output/result.json", "w") as f:
        json.dump(result, f)
