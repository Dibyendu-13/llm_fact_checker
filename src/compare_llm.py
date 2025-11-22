from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment variables
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def get_verdict(claim, retrieved):
    system_prompt = """
    Task: Compare the claim with the retrieved factual statements.
    Output must be strictly in JSON format:
    {
        "claim": "...",
        "status": "True/False/Uncertain",
        "explanation": "Short reasoning."
    }
    """

    facts_text = "\n".join([f"- {item['fact']}" for item in retrieved])

    user_prompt = f"""
    Claim: "{claim}"

    Relevant Verified Facts:
    {facts_text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    print(get_verdict("The capital of France is Madrid.", [{"fact":"The capital of France is Paris."}]))
