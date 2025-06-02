### POST `http://127.0.0.1:5000/generate-script`

**Example Input:**  
```json
{
  "topic": "Photosynthesis",
  "context": "Plants use sunlight to make food.",
  "level": 7
}
```

### POST http://127.0.0.1:5000/evaluate-answer
**Example Input:**
```json
{
  "question": "What is photosynthesis?",
  "student_answer": "It’s how plants eat sunlight."
}
```
