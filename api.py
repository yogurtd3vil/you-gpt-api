from flask import Flask, request, jsonify
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))
import you

app = Flask(__name__)

@app.route('/gpt4free', methods=['POST'])
def get_answer():
    question = request.json['question']
    try:
        result = you.Completion.create(
            prompt=question)
        answer = result['response']
        return jsonify({'answer': answer})
    except Exception as e:
        return jsonify({'error': f'Erro: {e}. Um erro ocorreu, tente com um novo user-agent '})

if __name__ == '__main__':
    app.run(debug=True)
