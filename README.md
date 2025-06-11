### POST `http://127.0.0.1:5000/generate-script`

**Example Input:**  
```json
{
  "goals": "Introduce the key formulas for calculating energy in these stores",
  "context": ".......",
  "level": 7
}
```

### POST http://127.0.0.1:5000/evaluate-answer
**Example Input:**
```json
{
  "question": "A byte (b) comprises 8 bits.How many bits are there in 1 terabyte (1Tb)? A 1 × 109 B 8 × 109 C 1 × 1012 D 8 × 1012 ",
  "student_answer": "D"
}
```
