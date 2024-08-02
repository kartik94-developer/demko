from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Load the OpenAI API key from an environment variable
openai.api_key = os.getenv('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')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_message,
            max_tokens=150
        )
        ai_reply = response.choices[0].text.strip()
        return jsonify({'reply': ai_reply})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5001)
