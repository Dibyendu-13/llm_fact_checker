# 🔍 LLM Fact Checker

This project verifies user statements using embeddings + LLM reasoning using a local knowledge base and FAISS.

---

## 🚀 How to Run

### 1️⃣ Install Dependencies

```sh
pip install -r requirements.txt
```

### 2️⃣ Download Required SpaCy Model

```sh
python -m spacy download en_core_web_sm
```

### 3️⃣ Build the Embeddings (Run Once)

> Only required if running the project for the first time or after updating your dataset.

```sh
python src/build_embeddings.py
```

If successful, you'll see:

```
Vector DB Created Successfully!
```

### 4️⃣ Run the Fact Checker

```sh
python src/main.py
```

You’ll be prompted to enter a statement:

```
Enter a statement to verify:
```

Example:

```
Enter a statement to verify: The capital of France is Paris.
```

Output example:

```json
{
  "claim": "The capital of France is Paris.",
  "status": "True",
  "explanation": "The statement matches verified factual knowledge."
}
```

---

## 🧠 When Should You Rebuild Embeddings?

| Change                       | Rebuild Needed? |
| ---------------------------- | --------------- |
| You add/edit the dataset     | ✅ Yes           |
| You change embedding model   | ✅ Yes           |
| You restart program          | ❌ No            |
| You only test new statements | ❌ No            |

---

## 📁 Example Dataset Format (`data/facts.csv`)

```csv
id,fact
1,The Earth revolves around the Sun.
2,Water boils at 100 degrees Celsius at sea level.
3,The capital of France is Paris.
4,Humans need oxygen to survive.
5,Albert Einstein developed the theory of relativity.
6,The Great Wall of China is located in China.
7,Lightning is a natural electrical discharge.
8,Apple Inc was founded by Steve Jobs, Steve Wozniak and Ronald Wayne.
9,Mount Everest is the tallest mountain on Earth above sea level.
10,A day has 24 hours.
```
