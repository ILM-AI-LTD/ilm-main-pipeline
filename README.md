# ILM AI - Intelligent Learning Management System

An AI-powered Flask application designed for A-Level Physics education, providing automated script generation, answer evaluation, and interactive chatbot functionality using OpenAI's GPT-4o model.

## 🚀 Features

- **Educational Script Generation**: Creates customized learning content based on context and goals
- **Automated Answer Evaluation**: Evaluates student responses with detailed feedback
- **Interactive Physics Chatbot**: Provides real-time assistance for physics questions
- **Modern Web Interface**: Responsive HTML interfaces for easy interaction
- **RESTful API**: Clean API endpoints for integration with other systems

## 📋 Prerequisites

- Python 3.7 or higher
- OpenAI API key
- Flask and dependencies (see requirements.txt)

## 🛠️ Installation & Setup

1. **Clone the repository**
```bash
git clone <repository-url>
cd ilm-main-pipeline
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Environment Setup**
Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

4. **Run the application**
```bash
python app.py
```

The server will start on `http://localhost:5000`

## 📚 API Documentation

### Base URL
```
http://localhost:5000
```

---

## 1. Root Endpoint

### `GET /`
**Description**: Serves the main interface HTML page for script generation and evaluation.

**Response**: HTML page (interface.html)

**Usage**: Navigate to `http://localhost:5000` in your browser

---

## 2. Generate Educational Script

### `POST /generate-script`
**Description**: Generates educational content based on provided context, student level, and learning goals using AI.

**Request Headers**:
```
Content-Type: application/json
```

**Request Body**:
```json
{
    "context": "string (required)",
    "level": "string (required)", 
    "goals": "string (required)"
}
```

**Sample Request**:
```bash
curl -X POST http://localhost:5000/generate-script \
-H "Content-Type: application/json" \
-d '{
    "context": "Energy conservation is a fundamental principle in physics. When energy appears to be lost in one form, it is actually converted to another form. In mechanical systems, kinetic energy can be converted to potential energy and vice versa. Heat, light, and sound are also forms of energy that can be produced from mechanical energy.",
    "level": "7",
    "goals": "Introduce the key formulas for calculating kinetic and potential energy"
}'
```

**Successful Response (200)**:
```json
{
    "script": "<p><strong>Energy cannot be created or destroyed.</strong><br>It can only be <strong>transferred</strong> from one store to another or between objects or systems.</p><ul><li>The total amount of energy in a <em>closed system</em> stays the same.</li><li>Energy may move or change form, but it is never lost or used up.</li></ul><p><strong>Key Energy Formulas:</strong></p><ul><li><strong>Kinetic Energy:</strong> KE = ½mv² <em>(where m = mass, v = velocity)</em></li><li><strong>Gravitational Potential Energy:</strong> PE = mgh <em>(where m = mass, g = gravity, h = height)</em></li></ul><p>Example: A ball thrown upward converts kinetic energy to potential energy as it rises, then back to kinetic energy as it falls.</p>"
}
```

**Error Response (400)**:
```json
{
    "error": "Missing topic or context"
}
```

---

## 3. Evaluate Student Answer

### `POST /evaluate-answer`
**Description**: Evaluates a student's answer against a given question, providing detailed feedback and scoring.

**Request Headers**:
```
Content-Type: application/json
```

**Request Body**:
```json
{
    "question": "string (required)",
    "student_answer": "string (required)"
}
```

**Sample Request (Multiple Choice)**:
```bash
curl -X POST http://localhost:5000/evaluate-answer \
-H "Content-Type: application/json" \
-d '{
    "question": "A byte (b) comprises 8 bits. How many bits are there in 1 terabyte (1Tb)? A) 1 × 10^9 B) 8 × 10^9 C) 1 × 10^12 D) 8 × 10^12",
    "student_answer": "D"
}'
```

**Sample Response (Multiple Choice)**:
```json
{
    "is_correct": true,
    "question_type": "Multiple-choice",
    "explanation": "<p>The student's answer is correct.</p><p><strong>Correct answer: D) 8 × 10<sup>12</sup></strong></p><p>Explanation:</p><ul><li>1 terabyte (1 Tb) = 10<sup>12</sup> bytes</li><li>Since 1 byte = 8 bits</li><li>1 terabyte = 10<sup>12</sup> × 8 = 8 × 10<sup>12</sup> bits</li></ul>"
}
```

**Sample Request (Short Answer)**:
```bash
curl -X POST http://localhost:5000/evaluate-answer \
-H "Content-Type: application/json" \
-d '{
    "question": "(i) State what is meant by a line of force in a gravitational field. [1 mark] (ii) Explain why the acceleration of free fall near Earth'\''s surface is approximately constant. [3 marks]",
    "student_answer": "(i) A line of force shows the direction a mass would move in the field. (ii) Near Earth'\''s surface, gravitational field lines are parallel and evenly spaced, indicating uniform field strength, so acceleration is constant."
}'
```

**Sample Response (Short Answer)**:
```json
{
    "is_correct": true,
    "question_type": "Short-answer",
    "score": 4,
    "explanation": "<ul><li><strong>Part (i):</strong> The student correctly defined a gravitational line of force as indicating the direction a mass would move. This is accurate and clear for 1 mark.</li><li><strong>Part (ii):</strong> The explanation is accurate and well-reasoned. The student correctly mentions that the lines are parallel and evenly spaced near Earth's surface, indicating uniform field strength and constant acceleration. Complete answer for 3 marks.</li></ul>"
}
```

**Error Responses**:
- **400 Bad Request**:
```json
{
    "error": "Missing question or student answer"
}
```

- **500 Internal Server Error**:
```json
{
    "error": "Failed to parse evaluation response from model"
}
```

---

## 4. ILM Chatbot

### `POST /ilm-chatbot`
**Description**: Provides interactive Q&A functionality for physics-related questions with contextual understanding.

**Request Headers**:
```
Content-Type: application/json
```

**Request Body**:
```json
{
    "question": "string (required)",
    "content": "string (optional)",
    "sub_topic": "string (optional)"
}
```

**Sample Request**:
```bash
curl -X POST http://localhost:5000/ilm-chatbot \
-H "Content-Type: application/json" \
-d '{
    "question": "Does a higher specific heat capacity mean it heats up faster or slower?",
    "content": "Specific heat capacity is the amount of energy required to raise the temperature of 1 kg of a substance by 1°C. Different materials have different specific heat capacities. Water has a high specific heat capacity compared to metals.",
    "sub_topic": "Specific Heat Capacity"
}'
```

**Sample Response**:
```json
{
    "answer": "<p>A higher specific heat capacity means it heats up <strong>slower</strong>.</p><p>Here's why:</p><ul><li>Specific heat capacity tells us how much energy is needed to raise 1 kg of material by 1°C</li><li>If a material has a <strong>high</strong> specific heat capacity, it needs <strong>more energy</strong> to increase its temperature</li><li>This means it takes longer to heat up (heats up slower)</li><li>If a material has a <strong>low</strong> specific heat capacity, it needs <strong>less energy</strong> to increase its temperature</li><li>This means it heats up faster</li></ul><p><strong>Example:</strong> Water (high specific heat capacity) takes longer to heat up than aluminum (low specific heat capacity) when the same amount of energy is applied.</p>"
}
```

**Sample Request (General Physics Question)**:
```bash
curl -X POST http://localhost:5000/ilm-chatbot \
-H "Content-Type: application/json" \
-d '{
    "question": "What is the difference between mass and weight?",
    "content": "",
    "sub_topic": "Forces and Motion"
}'
```

**Sample Response**:
```json
{
    "answer": "<p><strong>Mass</strong> and <strong>weight</strong> are different:</p><ul><li><strong>Mass:</strong><br/>• Measured in kilograms (kg)<br/>• The amount of matter in an object<br/>• Stays the same everywhere (on Earth, Moon, space)</li><li><strong>Weight:</strong><br/>• Measured in newtons (N)<br/>• The gravitational force acting on an object<br/>• Changes depending on gravitational field strength</li></ul><p><strong>Key formula:</strong> Weight = mass × gravitational field strength (W = mg)</p><p><strong>Example:</strong> An astronaut has the same mass on Earth and Moon, but weighs less on the Moon due to weaker gravity.</p>"
}
```

**Error Response (400)**:
```json
{
    "error": "Missing question"
}
```

---

## 5. Chatbot Interface

### `GET /chatbot-interface`
**Description**: Serves the interactive chatbot HTML interface.

**Response**: HTML page (interface_chatbot.html)

**Usage**: Navigate to `http://localhost:5000/chatbot-interface` in your browser

---

## 🌐 Web Interfaces

### Main Interface (`/`)
- **Script Generation**: Input context, goals, and student level to generate educational content
- **Answer Evaluation**: Submit questions and student answers for automated grading
- **Real-time Processing**: Loading indicators and formatted results display

### Chatbot Interface (`/chatbot-interface`)
- **Interactive Chat**: Real-time conversation with the AI physics tutor
- **Context Setup**: Optional content and sub-topic specification
- **Message History**: Maintains conversation flow with proper formatting

## 🔧 Technical Details

### Technology Stack
- **Backend**: Flask 3.1.1 with CORS support
- **AI Model**: OpenAI GPT-4o
- **Frontend**: Vanilla HTML/CSS/JavaScript
- **Response Format**: JSON for API, HTML for content rendering

### Project Architecture
```
├── app.py                 # Main Flask application with API routes
├── scripts.py             # Core AI generation functions
├── Prompts.py            # AI prompt templates and examples
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (not in repo)
├── .gitignore           # Git ignore rules
└── view/                # HTML templates
    ├── interface.html           # Main interface
    └── interface_chatbot.html   # Chatbot interface
```

### Key Functions in scripts.py
- `generate_script(context, level, goals)`: Creates educational content
- `generate_evaluation(question, student_ans)`: Evaluates answers
- `generate_chat(content, sub_topic, question)`: Powers chatbot responses

### AI Configuration
- **Model**: GPT-4o
- **Temperature**: 0.1 (script/chat), 0 (evaluation) for consistency
- **Response Format**: HTML for web display
- **Prompt Engineering**: Structured prompts in Prompts.py

## 🛡️ Security & Configuration

### Environment Variables
```env
OPENAI_API_KEY=your_api_key_here
PORT=5000  # Optional, defaults to 5000
```

### CORS Configuration
- Enabled for all origins (`origins="*"`)
- Suitable for development; restrict for production

### Input Validation
- Required field validation
- JSON parsing error handling
- API response sanitization

## 🚨 Error Handling

The API implements comprehensive error handling:

### Common Error Responses
- **400 Bad Request**: Missing required fields
- **500 Internal Server Error**: AI model response parsing errors
- **Network Errors**: Connection issues with OpenAI API

### Client-Side Error Handling
- Network connectivity issues
- Invalid JSON responses
- API timeout handling
- User-friendly error messages

## 📝 Usage Examples

### Testing with curl
```bash
# Test script generation
curl -X POST http://localhost:5000/generate-script \
-H "Content-Type: application/json" \
-d '{"context":"Newton'\''s laws","level":"7","goals":"Explain F=ma"}'

# Test answer evaluation
curl -X POST http://localhost:5000/evaluate-answer \
-H "Content-Type: application/json" \
-d '{"question":"What is acceleration?","student_answer":"Rate of change of velocity"}'

# Test chatbot
curl -X POST http://localhost:5000/ilm-chatbot \
-H "Content-Type: application/json" \
-d '{"question":"What is momentum?","content":"","sub_topic":"Forces"}'
```

### Integration Example (JavaScript)
```javascript
// Example: Generate educational script
async function generateScript(context, level, goals) {
    try {
        const response = await fetch('http://localhost:5000/generate-script', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                context: context,
                level: level,
                goals: goals
            })
        });
        
        const data = await response.json();
        if (response.ok) {
            return data.script;
        } else {
            throw new Error(data.error);
        }
    } catch (error) {
        console.error('Error generating script:', error);
        throw error;
    }
}
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Important Notes

- **API Key Security**: Never commit your OpenAI API key to version control
- **Rate Limits**: Be aware of OpenAI API rate limits and costs
- **Production Use**: Update CORS settings and add authentication for production deployment
- **Model Updates**: Monitor OpenAI API changes and update accordingly

## 🆘 Troubleshooting

### Common Issues

1. **"Missing OpenAI API key"**
   - Ensure `.env` file exists with `OPENAI_API_KEY=your_key`
   - Check that python-dotenv is installed

2. **"Failed to parse evaluation response"**
   - This may occur if the AI model returns unexpected format
   - Check the Prompts.py for proper prompt formatting

3. **CORS errors in browser**
   - Ensure Flask-CORS is installed and configured
   - Check that the API is running on the expected port

4. **Import errors**
   - Verify all dependencies are installed: `pip install -r requirements.txt`
   - Check Python version compatibility

## 📞 Support

For issues and questions:
1. Check the troubleshooting section above
2. Review the API documentation
3. Create an issue in the repository with detailed error information

---

