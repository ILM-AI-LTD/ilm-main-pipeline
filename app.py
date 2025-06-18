from scripts import generate_evaluation, generate_script, generate_chat
from flask import Flask, request, jsonify, render_template

from flask_cors import CORS
import os
import json

app = Flask(__name__, template_folder='view')
CORS(app, origins="*")

@app.route('/')
def index():
    return render_template('interface.html')

@app.route('/generate-script', methods=['POST'])
def script_endpoint():
    data = request.json
    # topic = data.get('topic')
    context = data.get('context')
    level = data.get('level')
    goals = data.get('goals')

    if not goals or not context:
        return jsonify({"error": "Missing topic or context"}), 400

    script = generate_script(context, level, goals)
    script = script.replace('\n', '')
    return jsonify({"script": script})

@app.route('/evaluate-answer', methods=['POST'])
def evaluation_endpoint():
    data = request.json
    question = data.get('question')
    student_ans = data.get('student_answer')

    if not question or not student_ans:
        return jsonify({"error": "Missing question or student answer"}), 400

    evaluation = generate_evaluation(question, student_ans)
    evaluation = evaluation.replace('json\n','').replace('\n', '').replace('\\','').replace('html','').replace("```","")
    print(evaluation)
    try:
        # Parse the JSON string into a Python dictionary
        parsed_evaluation = json.loads(evaluation)
        return jsonify(parsed_evaluation)
    except: 
        return jsonify({"error": "Failed to parse evaluation response from model"})
    
    # return jsonify({"evaluation": evaluation})

@app.route('/ilm-chatbot', methods=['POST'])
def chatbox():
    data = request.json
    question = data.get('question')
    content = data.get('content')
    sub_topic = data.get('sub_topic')

    if not question:
        return jsonify({"error": "Missing question"}), 400

    answer = generate_chat(content, sub_topic, question)
    # print("Answer: \n", answer)
    return jsonify({"answer": answer})

@app.route('/chatbot-interface')
def chatbot_interface():
    return render_template('interface_chatbot.html')



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)