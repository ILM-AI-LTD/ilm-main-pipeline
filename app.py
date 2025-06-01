from scripts import generate_evaluation, generate_script
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/generate-script', methods=['POST'])
def script_endpoint():
    data = request.json
    topic = data.get('topic')
    context = data.get('context')
    level = data.get('level')

    if not topic or not context:
        return jsonify({"error": "Missing topic or context"}), 400

    script = generate_script(topic, context, level)
    return jsonify({"script": script})

@app.route('/evaluate-answer', methods=['POST'])
def evaluation_endpoint():
    data = request.json
    question = data.get('question')
    student_ans = data.get('student_answer')

    if not question or not student_ans:
        return jsonify({"error": "Missing question or student answer"}), 400

    evaluation = generate_evaluation(question, student_ans)
    return jsonify({"evaluation": evaluation})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)