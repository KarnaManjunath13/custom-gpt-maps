from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the Custom GPT Maps API!'})

@app.route('/api/some_endpoint', methods=['GET', 'POST'])
def some_endpoint():
    if request.method == 'POST':
        data = request.json
        return jsonify({'received_data': data}), 201
    return jsonify({'message': 'This endpoint accepts POST requests.'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)