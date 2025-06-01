from openai import OpenAI
from Prompts import Explanation_prompt, Evaluation_Prompt
from dotenv import load_dotenv
# import webbrowser

load_dotenv()

def generate_script(topic, script, level):
    """
    Generates a teacher-style script for students given a topic and prompt.
    """
    client = OpenAI()   
    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {
                "role": "system",
                "content": Explanation_prompt
            },
            {
                "role": "user",
                "content": f"Describe about \"{topic}\" with the help of following context: \n {script}. \nThe level of the student is {level}"
            }
        ],
        temperature= 0.5    
    )
    return response.output_text.strip()

def generate_evaluation(question, student_ans):
    """
    Generates evaluation of students' answer of the given question.
    """
    client = OpenAI()   
    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {
                "role": "system",
                "content": Evaluation_Prompt
            },
            {
                "role": "user",
                "content": f"Question: \n{question}, Students' answer: \n{student_ans} "
            }
        ],
        temperature= 0.5    
    )
    return response.output_text.strip()
