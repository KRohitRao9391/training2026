from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def generate_code(prompt):
    if "python" in prompt.lower():
        return "print('Hello from AI Code Generator')"
    elif "html" in prompt.lower():
        return "<h1>Hello from AI Code Generator</h1>"
    else:
        return "Code generation not supported for this prompt."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get('prompt', '')
    code = generate_code(prompt)
    return jsonify({'code': code})

if __name__ == "__main__":
    app.run(debug=True)
