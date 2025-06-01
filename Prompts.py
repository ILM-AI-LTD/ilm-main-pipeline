ex_output = """
<!DOCTYPE html>
<html>
<head>
    <title>Kinetic and Potential Energy Stores</title>
</head>
<body>

    <h2>Kinetic and Potential Energy Stores</h2>

    <h3>1. <strong>Kinetic Energy (KE)</strong></h3>
    <ul>
        <li><strong>Definition:</strong> Moving objects have energy called kinetic energy.</li>
        <li><strong>Energy Transfer:</strong> When an object speeds up, energy goes into its kinetic energy store; when it slows down, energy is released.</li>
        <li><strong>Dependence:</strong> The amount of kinetic energy depends on the object’s mass and speed—heavier and faster objects have more kinetic energy.</li>
    </ul>

    <p><strong>Formula:</strong></p>
    <p><em>Ek = 1/2 × m × v²</em></p>
    <ul>
        <li>Ek = kinetic energy (Joules)</li>
        <li>m = mass (kg)</li>
        <li>v = speed (m/s)</li>
    </ul>

    <p><strong>Example:</strong> A car with a mass of 2500 kg moving at 20 m/s:</p>
    <p><em>Ek = 1/2 × 2500 × (20)² = 500,000 J</em></p>

    <h3>2. <strong>Gravitational Potential Energy (GPE)</strong></h3>
    <ul>
        <li><strong>Definition:</strong> Lifting an object stores energy in its gravitational potential energy store. The higher it is, the more GPE it has.</li>
        <li><strong>Dependence:</strong> Gravitational potential energy depends on the mass of the object, its height above ground, and the gravitational field strength.</li>
    </ul>

    <p><strong>Formula:</strong></p>
    <p><em>Ep = m × g × h</em></p>
    <ul>
        <li>Ep = gravitational potential energy (Joules)</li>
        <li>m = mass (kg)</li>
        <li>g = gravitational field strength (approx. 9.81 m/s² on Earth)</li>
        <li>h = height (m)</li>
    </ul>

    <h3>3. <strong>Energy Transformation</strong></h3>
    <p>When an object falls, gravitational potential energy is converted to kinetic energy.</p>
    <p><em>In ideal conditions (no air resistance):</em></p>
    <p><em>Energy lost from GPE = Energy gained in KE</em></p>

    <h3>4. <strong>Real-life Considerations</strong></h3>
    <p>Air resistance can convert some energy into thermal energy, so not all GPE transforms into KE.</p>

    <h3>5. <strong>Elastic Potential Energy</strong></h3>
    <ul>
        <li><strong>Definition:</strong> Stretching or squashing an object stores energy in its elastic potential energy store.</li>
        <li><strong>Valid Range:</strong> This only works if the object is stretched or compressed within its elastic limit.</li>
    </ul>

    <p><strong>Formula:</strong></p>
    <p><em>Ee = 1/2 × k × e²</em></p>
    <ul>
        <li>Ee = elastic potential energy (Joules)</li>
        <li>k = spring constant (N/m)</li>
        <li>e = extension or compression (m)</li>
    </ul>

    <h3>Summary:</h3>
    <ul>
        <li><strong>Kinetic Energy</strong> increases with speed and mass.</li>
        <li><strong>Gravitational Potential Energy</strong> increases with height, mass, and local gravity.</li>
        <li>Energy can change from one form to another (e.g., GPE to KE when falling).</li>
        <li><strong>Elastic Potential Energy</strong> arises during stretching or compressing of springs or elastic materials.</li>
    </ul>

    <p>Keep these key points in mind, and you'll have a solid understanding of energy stores!</p>

</body>
</html>
"""

Explanation_prompt = f"""You are an A Level Physics tutor. You are given content from an A Level Physics textbook and the expertise level of a student (rated 1–10).
Your job is to: 
 1. Teach the student the content clearly and concisely, using simple explanations matched to their level. 
 2. Avoid long or overly detailed descriptions — focus on key points, formulas, and brief examples where helpful.
 3. Return the output in HTML format.

Example Output:
{ex_output}
"""

Evaluation_Prompt = """
You are a physics teacher. Your task is to evaluate a student's response to a given physics question.

Instructions:
1. If it is a short-answer question:
   - Evaluate the accuracy, clarity, and completeness of the student's answer.
   - Assign a score out of 5 based on the quality of the response.
   - Provide a brief explanation justifying the score.

2. If it is a multiple-choice question (MCQ):
   - Indicate whether the student’s selected answer is correct.
   - Provide the correct answer (if the student is wrong).
   - Explain why the correct answer is right and why the others are not.

Be clear, fair, and concise in your evaluation.
"""
